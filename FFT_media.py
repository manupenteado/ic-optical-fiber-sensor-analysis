import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


############### 510 Hz 4.5cm de distancia com 93,75% do volume com 90 graus ################
pasta7 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\440 Hz\Próximo\50% do volume"
lista_frequencia7 = []
lista_amplitude7 = []

for i in range(1, 3):  # O número 1 no range não foi alterado
    arquivo_entrada7 = os.path.join(pasta7, f"FFT{i}.xlsx")
    data = pd.read_excel(arquivo_entrada7)

    lista_frequencia7.append(data['Frequencia'])
    lista_amplitude7.append(data['Amplitude'])

media_frequencia7 = pd.concat(lista_frequencia7, axis=1).mean(axis=1)
media_amplitude7 = pd.concat(lista_amplitude7, axis=1).mean(axis=1)

FFT_media7 = pd.DataFrame({
    'Frequencia': media_frequencia7,
    'Amplitude': media_amplitude7
})
arquivo_saida7 = os.path.join(pasta7, "FFT_media.xlsx")

FFT_media7.to_excel(arquivo_saida7, index=False)

frequencia7 = np.asarray(FFT_media7["Frequencia"])
amplitude7 = np.asanyarray(FFT_media7["Amplitude"])

fig7, ax7 = plt.subplots(figsize=(15, 8))
ax7.plot(frequencia7, amplitude7)
ax7.set_title(f'Média FFT de 510 Hz com 4.5cm de distancia com 93,75% do volume com 90 graus')
ax7.set_xlabel("Frequência (Hz)")
ax7.set_ylabel('Amplitude (dB)')
#plt.show()


plt.show()