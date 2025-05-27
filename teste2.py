
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid as trapz
from scipy.integrate import cumulative_trapezoid as cumtrapz
from scipy.special import ellipe
from scipy.optimize import fsolve
from scipy.optimize import minimize
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit

#==========================================================================
#
#   Compute Frenet-Serret frame from three arrays of data, (x,y and z)
#   Method to compute the curvature

def TNB_Flat(x, y, t):
    # dr is the differential of the curve
    dr = np.matrix([np.gradient(x), np.gradient(y)])
    ds = np.power(np.sum(np.square(dr), 0), 0.5)  # Arc length associated with each point. ||dr||.
    T = np.divide(dr, ds)  # Unit tangent vector. e aponta na direção da curva

    # s is the arc of the length, it grows with T
    T0 = np.zeros(len(x))
    T1 = np.zeros(len(x))
    
    # Separating in x and y
    for i in range(0, len(x), 1):
        T0[i] = T[0, i]
        T1[i] = T[1, i]

    # dT is the differential of the tangent vector
    dT = np.c_[np.gradient(T0), np.gradient(T1)]  # T'(t).
    dT = np.transpose(dT)
    dTds = np.divide(dT, ds)

    # Calculate first derivatives
    dx_dt = np.gradient(x, t)
    dy_dt = np.gradient(y, t)

    # Calculate second derivatives
    d2x_dt2 = np.gradient(dx_dt, t)
    d2y_dt2 = np.gradient(dy_dt, t)

    # Form the first and second derivative vectors
    drdt = np.vstack((dx_dt, dy_dt)).T
    d2rdt2 = np.vstack((d2x_dt2, d2y_dt2)).T

    # Expand the 2D vectors to 3D by adding a third dimension of zeros
    drdt_3d = np.hstack((drdt, np.zeros((drdt.shape[0], 1))))
    d2rdt2_3d = np.hstack((d2rdt2, np.zeros((d2rdt2.shape[0], 1))))

    # Compute the cross product in 3D
    cross_product = np.cross(drdt_3d, d2rdt2_3d)

    # Ensure cross_product is a 2D array
    if cross_product.ndim == 1:
        cross_product = cross_product.reshape(-1, 1)

    # Compute the numerator of the curvature formula (norm of the cross product)
    numerator = np.linalg.norm(cross_product, axis=1)

    # Compute the denominator of the curvature formula (norm of the first derivative to the power of 3)
    denominator = np.linalg.norm(drdt, axis=1) ** 3

    # Compute the curvature (t)
    kappa_t = numerator / denominator
    kappa = np.power(sum(np.square(dTds), 0), 0.5)

    # Normal vector
    N = np.divide(dTds, kappa)  # Unit normal vector.

    return T, N, kappa, kappa_t, ds


# Method to define ellipse
def ellipse(a, b, t):
    x = a * np.cos(t + np.pi/2)
    y = b * np.sin(t + np.pi/2)
    return x, y

# Method to compute the distributed macrobend loss as a function of the curvature radius (1/k)
def curvature_loss_exp(curvature):
    a1 = 1525.965951223269
    b1 = -869.0646471499498
    a2 = 1525.9295489081296
    b2 = -869.0650046536391

    return a1 * np.exp(b1 * (1 / curvature)) + a2 * np.exp(b2 * (1 / curvature))

# Used to find the eccentricity that satisfies the equation for the ellipse.
def error_function (e, E):
    return ellipe(e**2) - E

# Used to calculate the Mean Squared Error between the y value (sum of losses) and a straight line
def mse_loss(x, y):
    model = LinearRegression()
    model.fit(x.reshape(-1, 1), y)  
    y_pred = model.predict(x.reshape(-1, 1))  
    mse = np.mean((y - y_pred) ** 2)  
    return mse

# Defining delta
deltas = np.linspace(0.05, 0.1, 100)

# Defining the initial radius of the ellipse
initial_radius = (38.1/2) * 1e-03

# Defining radius
Length = 2 * np.pi * initial_radius

# Defining the angle for the elliptic integral
theta = np.linspace(0, np.pi/2, 10000)
print(theta)

# Computing the sine of theta
sin_theta = np.sin(theta)

# Optimizing delta
def optimize_delta(deltas, Length, theta, sin_theta, curvature_loss_exp, TNB_Flat, error_function, desired_slope):
    best_delta = None
    min_combined_metric = float('inf')
    for delta in deltas:
        totalLoss1 = []
        totalLoss2 = []
        two_a_value = []
        a1_value = []
        a2_value = []
        e2_value = []
        
        for eccentricity in np.linspace(0, 0.9555, 300):
            elliptic_integral = trapz(np.sqrt(1 - eccentricity**2 * sin_theta**2), theta)

            b1  = (1/4) * Length * np.sqrt(1 - eccentricity**2) / elliptic_integral

            a1 = b1 / np.sqrt(1 - eccentricity**2)
            a1_value.append(a1)

            a2 = ((2 * b1) + delta) / 2
            a2_value.append(a2)

            two_a2 = 2 * a2
            function_Ee = Length / (4 * a2)
            
            initial_e_guess = 0.09
            e2 = fsolve(error_function, initial_e_guess, args=(function_Ee), xtol=1e-03)[0]

            b2 = a2 * (np.sqrt(1 - (e2 ** 2)))

          

            t = np.linspace(0, 2 * np.pi, 500)

            x1, y1 = ellipse(a1, b1, t)
            x2, y2 = ellipse(a2, b2, t)

            T, N, kappa_TNB, _, ds = TNB_Flat(x1, y1, t)
            T2, N2, kappa_TNB2, _, ds2 = TNB_Flat(x2, y2, t)

            # Verify the value of the radius
            if any([(1/np.max(kappa_TNB)) < 0.00237, (1/np.max(kappa_TNB2)) < 0.00237]):
                continue 

            s = cumtrapz(ds, initial=0)
            s2 = cumtrapz(ds2, initial=0)

            curvatureLoss = curvature_loss_exp(kappa_TNB)
            curvatureLoss2 = curvature_loss_exp(kappa_TNB2)

            totalLoss1.append(trapz(curvatureLoss, s))
            totalLoss2.append(trapz(curvatureLoss2, s2))

            two_a_value.append(two_a2)
            e2_value.append(e2)

            if a2 <= b2 + 1e-5:
                break
        
        # Calculate the sum of the curvature losses
        totalLoss_sum = np.array(totalLoss1) + np.array(totalLoss2)
        two_a_value = np.array(two_a_value)

        x = two_a_value.reshape(-1, 1)
        y = totalLoss_sum

        # Compute the MSE between the sum of curvature losses and a straight line fit
        mse = mse_loss(x, y)

        # Calculating slope
        model = LinearRegression()
        model.fit(x, y)
        calculated_slope = model.coef_[0]  
        calculated_intercept = model.intercept_
        slope_difference = abs(calculated_slope - desired_slope)

        # Check if the current delta gives a better fit
        combined_metric = mse + 10 * slope_difference 
        if combined_metric < min_combined_metric:
            min_combined_metric = combined_metric
            best_delta = delta
            
    return best_delta, two_a_value, totalLoss_sum, calculated_slope, calculated_intercept

desired_slope = -20
best_delta, two_a_value, totalLoss_sum, calculated_slope, calculated_intercept  = optimize_delta(deltas, Length, theta, sin_theta, curvature_loss_exp, TNB_Flat, error_function, desired_slope)

print(two_a_value.size)
print(totalLoss_sum.size)

calculated_slope = float(calculated_slope)  
calculated_intercept = float(calculated_intercept)  

line_values = calculated_slope * two_a_value + calculated_intercept

# Plot the optimized result:
fig1, ax1 = plt.subplots(figsize=(13, 8))
ax1.plot(two_a_value, totalLoss_sum, label=f'Sum of Curvature Losses [dB] (optimized delta = {best_delta})', color='blue', linewidth=2)
ax1.plot(
    two_a_value,
    line_values,
    label=f'Fitted Line (slope={calculated_slope:.2f}, intercept={calculated_intercept:.2f})',
    color='red',
    linestyle='--',
    linewidth=2
)
ax1.set_title('Sum of Curvature Losses vs 2a (Optimized)')
ax1.set_xlabel('2a [m]')
ax1.set_ylabel('Sum Loss [dB]')
ax1.grid(True)
ax1.tick_params(axis='both', which='major')
plt.tight_layout()
plt.show()

print(f"The best delta is {best_delta}")









# Choosing range: 0.120 to 0.125
mask = (two_a_value >= 0.120) & (two_a_value <= 0.125)
two_a_filtered = two_a_value[mask]
totalLoss_sum_filtered = totalLoss_sum[mask]

# Plot the filtered results
fig2, ax2 = plt.subplots(figsize=(13, 8))
ax2.plot(two_a_filtered, totalLoss_sum_filtered, label='Sum of Curvature Losses [dB] (filtered)')
ax2.set_title('Sum of Curvature Losses vs 2a (Filtered: 2a from 0.120 to 0.125)')
ax2.set_xlabel('2a [m]')
ax2.set_ylabel('Sum Loss [dB]')
ax2.grid(True)
ax2.tick_params(axis='both', which='major')
plt.tight_layout()
plt.show()

# Linearity metric: R-squared (R²) / Coefficient of Determination
def calculate_r2(x, y):
    model = LinearRegression()
    model.fit(x.reshape(-1, 1), y)
    y_pred = model.predict(x.reshape(-1, 1))
    r2 = r2_score(y, y_pred)
    return r2

# Applying the function to the filtered values
r2_filtered = calculate_r2(two_a_filtered, totalLoss_sum_filtered)
print(f"R²: {r2_filtered}")

# Function to fit a line (linear regression) and plot
def plot_best_fit_line(x, y):
    x = x.reshape(-1, 1)
    
    model = LinearRegression()
    model.fit(x, y)
    
    y_pred = model.predict(x)
    
    # Plot the filtered data
    fig3, ax3 = plt.subplots(figsize=(13, 8))
    ax3.plot(x, y, label='Sum of Curvature Losses [dB] (filtered)', color='green', linewidth=2)
    
    # Plotar the fitted line
    ax3.plot(x, y_pred, label='Fitted line', color='red', linestyle='--', linewidth=2)
    ax3.set_title('Sum of Curvature Losses vs 2a (With Fitted Line)')
    ax3.set_xlabel('2a [m]')
    ax3.set_ylabel('Sum Loss [dB]')
    ax3.grid(True)
    ax3.tick_params(axis='both', which='major')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # Slope and intercept
    print(f"Slope: {model.coef_}")
    print(f"Intercept: {model.intercept_}")
    print(f"calculated_slope: {calculated_slope}")

plot_best_fit_line(two_a_filtered, totalLoss_sum_filtered)











"""



    # Plot for One Turn Curvature Loss vs b
    fig1, ax1 = plt.subplots(figsize=(13, 8))
    ax1.plot(two_a_value, totalLoss1, label="One Turn Curvature Loss [dB]", color='red', linewidth=2)
    ax1.set_title(f'First Turn Curvature Loss vs 2a (delta = {delta})', fontsize=20)
    ax1.set_xlabel('2a [m]', fontsize=35)
    ax1.set_ylabel('Loss [dB]', fontsize=35)
    ax1.grid(True)
    ax1.tick_params(axis='both', which='major', labelsize=20)
    plt.tight_layout()
    plt.show()

    # Plot for One Turn Curvature Loss 2 vs b2
    fig2, ax2 = plt.subplots(figsize=(13, 8))
    ax2.plot(two_a_value, totalLoss2, label="One Turn Curvature Loss 2 [dB]", color='red', linewidth=2)
    ax2.set_title(f'Second Turn Curvature Loss vs 2a (delta = {delta})', fontsize=20)
    ax2.set_xlabel('2a [m]', fontsize=35)
    ax2.set_ylabel('Loss 2[dB]', fontsize=35)
    ax2.grid(True)
    ax2.tick_params(axis='both', which='major', labelsize=20)
    plt.tight_layout()
    plt.show()

    # Plotting the sum of the two curvature losses
    totalLoss_sum = np.array(totalLoss1) + np.array(totalLoss2)

    fig3, ax3 = plt.subplots(figsize=(13, 8))
    ax3.plot(two_a_value, totalLoss_sum, label="Sum of Curvature Losses [dB]", color='blue', linewidth=2)
    ax3.set_title(f'Sum of Curvature Losses vs 2a (delta = {delta})', fontsize=20)
    ax3.set_xlabel('b [m]', fontsize=35)
    ax3.set_ylabel('Sum Loss [dB]', fontsize=35)
    ax3.grid(True)
    ax3.tick_params(axis='both', which='major', labelsize=20)
    plt.tight_layout()
    plt.show()

    fig5, ax5 = plt.subplots(figsize=(13, 8))
    ax5.plot(e2_value, label="e2", color='red', linewidth=2)
    ax5.set_title(f'Second eccentricity (delta = {delta})', fontsize=20)
    plt.show()


fig4, ax4 = plt.subplots(figsize=(13, 8))
ax4.plot(a1_value, label="a1", color='red', linewidth=2)
ax4.plot(a2_value, label="a2", color='yellow', linewidth=2)
ax4.plot(b_value1, label="b1", color='pink', linewidth=2)
ax4.plot(b_value2, label="b2", color='blue', linewidth=2)
plt.legend()
plt.show()
"""

#2.37 mm é o menor raio que pode ser usado, tem que ser maior, então cuidaod com o delta
#Rmin= 1/kappa max >= Rmin exp (que é 2.37mm)
#mse ja esta minimizando, com a slope - slope desejado (quando for igual, vai dar 0) quer minimizar essa diferença do slope desejado ao mesmo tempo do mse