import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Carregar a planilha do Excel
def process_fft_from_excel(file_path, sheet_name, time_column, voltage_column, freq_min=None, freq_max=None, amplitude_scale=1.0):
    # Ler os dados do Excel
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Extrair colunas de tempo e voltagem
    time = df[time_column].values
    voltage = df[voltage_column].values * amplitude_scale  # Ajustar a amplitude
    
    # Garantir que os dados estejam igualmente espaçados
    delta_t = time[1] - time[0]  # Intervalo de tempo
    sampling_freq = 1 / delta_t  # Frequência de amostragem
    n = len(voltage)  # Número de pontos

    # Realizar a FFT
    fft_values = fft(voltage)
    fft_magnitude = np.abs(fft_values)[:n // 2]  # Magnitude positiva
    fft_magnitude_db = 20 * np.log10(fft_magnitude)  # Converter para dB

    # Gerar o eixo de frequência
    freqs = np.fft.fftfreq(n, delta_t)[:n // 2]

    # Filtrar intervalo de frequência
    if freq_min is not None and freq_max is not None:
        mask = (freqs >= freq_min) & (freqs <= freq_max)
        freqs = freqs[mask]
        fft_magnitude_db = fft_magnitude_db[mask]

    # Plotar os resultados
    plt.figure(figsize=(10, 6))
    plt.plot(freqs, fft_magnitude_db)
    plt.title("Espectro de Amplitude em dB")
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.grid()
    plt.show()

# Exemplo de uso
file_path = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\varreduda da onda3.xlsx"
sheet_name = "Sheet1"  # Substitua pelo nome da aba se necessário
time_column = "Tempo"  # Nome da coluna de tempo
e_voltage_column = "Voltagem"  # Nome da coluna de voltagem

# Parâmetros de frequência
freq_min = 10  # Frequência mínima (Hz)
freq_max = 20000  # Frequência máxima (Hz)
amplitude_scale = 2.0  # Fator de escala para a amplitude

process_fft_from_excel(file_path, sheet_name, time_column, e_voltage_column, freq_min, freq_max, amplitude_scale)
