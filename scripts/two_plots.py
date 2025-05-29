import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arquivo = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\Próximo\100% do volume\FFT_media.xlsx"
data = pd.read_excel(arquivo)
arquivo2 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\200 Hz\Próximo\100% do volume\FFT_media.xlsx"
data2 = pd.read_excel(arquivo2)

indice_pico = data['Amplitude'].idxmax()
frequencia_pico = data['Frequencia'][indice_pico]
amplitude_pico = data['Amplitude'][indice_pico]

indice_pico2 = data2['Amplitude'].idxmax()
frequencia_pico2 = data2['Frequencia'][indice_pico2]
amplitude_pico2 = data2['Amplitude'][indice_pico2]

plt.figure(figsize=(10, 6))
plt.plot(data['Frequencia'], data['Amplitude'], color = "lightblue", label = "20 mm") 
plt.plot(data2['Frequencia'], data2['Amplitude'], color = "pink", label = "25 mm")  
plt.title("Média da FFT de 440 Hz com 20 mm de diâmetro próximo variando o volume do som")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Amplitude (dB)")

# Seta azul para 100%
plt.annotate(f'Pico: {frequencia_pico:.2f} Hz, {amplitude_pico:.2f} dB', 
                 xy=(frequencia_pico, amplitude_pico), 
                 xytext=(frequencia_pico + 50, amplitude_pico - 3),
                 arrowprops=dict(facecolor='lightblue', shrink=0.005))

# Seta rosa para 50%
plt.annotate(f'Pico: {frequencia_pico2:.2f} Hz, {amplitude_pico2:.2f} dB', 
                 xy=(frequencia_pico2, amplitude_pico2), 
                 xytext=(frequencia_pico2 + 50, amplitude_pico2 - 0.7),
                 arrowprops=dict(facecolor='pink', shrink=0.005))

plt.legend()
plt.xlim(0, 1000)  # <-- aqui você limita o eixo X de 0 a 1000
plt.grid()
plt.show()
