import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

############### 100 Hz 5mm de distancia ################
pasta1 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\5mm de distância"

lista_Tempo1 = []
lista_Voltagem1 = []

for i in range (1, 11):
    arquivo_entrada1 = os.path.join(pasta1, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada1)

    lista_Tempo1.append(data['Tempo'])
    lista_Voltagem1.append(data['Voltagem'])

media_Tempo1 = pd.concat(lista_Tempo1, axis = 1).mean(axis = 1)
media_Voltagem1 = pd.concat(lista_Voltagem1, axis = 1).mean(axis = 1)

ONDA_media1 = pd.DataFrame({
    'Tempo': media_Tempo1,
    'Voltagem': media_Voltagem1
})
arquivo_saida1 = os.path.join(pasta1, "ONDA_media.xlsx")

ONDA_media1.to_excel(arquivo_saida1, index = False)

Tempo1 = np.asarray(ONDA_media1["Tempo"])
Voltagem1 = np.asanyarray(ONDA_media1["Voltagem"])

fig1, ax1 = plt.subplots(figsize=(15, 6))
ax1.plot(Tempo1, Voltagem1)
ax1.set_title('Média ONDA de 100 Hz a 5 mm de distância')
ax1.set_xlabel("Tempo (s)")
ax1.set_ylabel('Tensão (Volts)')
#plt.show()






############### 100 Hz 7mm de distancia ################
pasta2 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\7mm de distância"

lista_Tempo2 = []
lista_Voltagem2 = []

for i in range(1, 11):  
    arquivo_entrada2 = os.path.join(pasta2, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada2)

    lista_Tempo2.append(data['Tempo'])
    lista_Voltagem2.append(data['Voltagem'])

media_Tempo2 = pd.concat(lista_Tempo2, axis=1).mean(axis=1)
media_Voltagem2 = pd.concat(lista_Voltagem2, axis=1).mean(axis=1)

ONDA_media2 = pd.DataFrame({
    'Tempo': media_Tempo2,
    'Voltagem': media_Voltagem2
})
arquivo_saida2 = os.path.join(pasta2, "ONDA_media.xlsx")

ONDA_media2.to_excel(arquivo_saida2, index=False)

Tempo2 = np.asarray(ONDA_media2["Tempo"])
Voltagem2 = np.asanyarray(ONDA_media2["Voltagem"])

fig2, ax2 = plt.subplots(figsize=(15, 6))
ax2.plot(Tempo2, Voltagem2)
ax2.set_title('Média ONDA de 100 Hz a 7 mm de distância')
ax2.set_xlabel("Tempo (s)")
ax2.set_ylabel('Tensão (Volts)')
#plt.show()







############### 100 Hz Próximo 100% do volume ################
pasta3 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\Próximo\100% do volume"

lista_Tempo3 = []
lista_Voltagem3 = []

for i in range(1, 11):
    arquivo_entrada3 = os.path.join(pasta3, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada3)

    lista_Tempo3.append(data['Tempo'])
    lista_Voltagem3.append(data['Voltagem'])

media_Tempo3 = pd.concat(lista_Tempo3, axis=1).mean(axis=1)
media_Voltagem3 = pd.concat(lista_Voltagem3, axis=1).mean(axis=1)

ONDA_media3 = pd.DataFrame({
    'Tempo': media_Tempo3,
    'Voltagem': media_Voltagem3
})
arquivo_saida3 = os.path.join(pasta3, "ONDA_media.xlsx")

ONDA_media3.to_excel(arquivo_saida3, index=False)

Tempo3 = np.asarray(ONDA_media3["Tempo"])
Voltagem3 = np.asanyarray(ONDA_media3["Voltagem"])

fig3, ax3 = plt.subplots(figsize=(15, 6))
ax3.plot(Tempo3, Voltagem3)
ax3.set_title(f'Média ONDA de 100 Hz próximo com 100% do volume')
ax3.set_xlabel("Tempo (s)")
ax3.set_ylabel('Tensão (Volts)')
#plt.show()




############### 100 Hz Próximo 80% do volume ################
pasta4 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\Próximo\80% do volume"

lista_Tempo4 = []
lista_Voltagem4 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada4 = os.path.join(pasta4, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada4)

    lista_Tempo4.append(data['Tempo'])
    lista_Voltagem4.append(data['Voltagem'])

media_Tempo4 = pd.concat(lista_Tempo4, axis=1).mean(axis=1)
media_Voltagem4 = pd.concat(lista_Voltagem4, axis=1).mean(axis=1)

ONDA_media4 = pd.DataFrame({
    'Tempo': media_Tempo4,
    'Voltagem': media_Voltagem4
})
arquivo_saida4 = os.path.join(pasta4, "ONDA_media.xlsx")

ONDA_media4.to_excel(arquivo_saida4, index=False)

Tempo4 = np.asarray(ONDA_media4["Tempo"])
Voltagem4 = np.asanyarray(ONDA_media4["Voltagem"])

fig4, ax4 = plt.subplots(figsize=(15, 6))
ax4.plot(Tempo4, Voltagem4)
ax4.set_title(f'Média ONDA de 100 Hz próximo com 80% do volume')
ax4.set_xlabel("Tempo (s)")
ax4.set_ylabel('Tensão (Volts)')
#plt.show()



############### 510 Hz 4.5cm de distancia com 68,75% do volume com 90 graus ################

pasta5 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5cm de distância\68,75% do volume\90 graus"

lista_Tempo5 = []
lista_Voltagem5 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada5 = os.path.join(pasta5, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada5)

    lista_Tempo5.append(data['Tempo'])
    lista_Voltagem5.append(data['Voltagem'])

media_Tempo5 = pd.concat(lista_Tempo5, axis=1).mean(axis=1)
media_Voltagem5 = pd.concat(lista_Voltagem5, axis=1).mean(axis=1)

ONDA_media5 = pd.DataFrame({
    'Tempo': media_Tempo5,
    'Voltagem': media_Voltagem5
})
arquivo_saida5 = os.path.join(pasta5, "ONDA_media.xlsx")

ONDA_media5.to_excel(arquivo_saida5, index=False)

Tempo5 = np.asarray(ONDA_media5["Tempo"])
Voltagem5 = np.asanyarray(ONDA_media5["Voltagem"])

fig5, ax5 = plt.subplots(figsize=(15, 6))
ax5.plot(Tempo5, Voltagem5)
ax5.set_title(f'Média ONDA de 510 Hz com 4.5cm de distancia com 68,75% do volume com 90 graus')
ax5.set_xlabel("Tempo (s)")
ax5.set_ylabel('Tensão (Volts)')
#plt.show()



############### 510 Hz 4.5cm de distancia com 68,75% do volume com 120 graus ################
pasta6 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5cm de distância\68,75% do volume\120 graus"

lista_Tempo6 = []
lista_Voltagem6 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada6 = os.path.join(pasta6, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada6)

    lista_Tempo6.append(data['Tempo'])
    lista_Voltagem6.append(data['Voltagem'])

media_Tempo6 = pd.concat(lista_Tempo6, axis=1).mean(axis=1)
media_Voltagem6 = pd.concat(lista_Voltagem6, axis=1).mean(axis=1)

ONDA_media6 = pd.DataFrame({
    'Tempo': media_Tempo6,
    'Voltagem': media_Voltagem6
})
arquivo_saida6 = os.path.join(pasta6, "ONDA_media.xlsx")

ONDA_media6.to_excel(arquivo_saida6, index=False)

Tempo6 = np.asarray(ONDA_media6["Tempo"])
Voltagem6 = np.asanyarray(ONDA_media6["Voltagem"])

fig6, ax6 = plt.subplots(figsize=(15, 6))
ax6.plot(Tempo6, Voltagem6)
ax6.set_title(f'Média ONDA de 510 Hz com 4.5cm de distancia com 68,75% do volume com 120 graus')
ax6.set_xlabel("Tempo (s)")
ax6.set_ylabel('Tensão (Volts)')
#plt.show()



############### 510 Hz 4.5cm de distancia com 93,75% do volume com 90 graus ################
pasta7 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5cm de distância\93,75% do volume\90 graus"

lista_Tempo7 = []
lista_Voltagem7 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada7 = os.path.join(pasta7, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada7)

    lista_Tempo7.append(data['Tempo'])
    lista_Voltagem7.append(data['Voltagem'])

media_Tempo7 = pd.concat(lista_Tempo7, axis=1).mean(axis=1)
media_Voltagem7 = pd.concat(lista_Voltagem7, axis=1).mean(axis=1)

ONDA_media7 = pd.DataFrame({
    'Tempo': media_Tempo7,
    'Voltagem': media_Voltagem7
})
arquivo_saida7 = os.path.join(pasta7, "ONDA_media.xlsx")

ONDA_media7.to_excel(arquivo_saida7, index=False)

Tempo7 = np.asarray(ONDA_media7["Tempo"])
Voltagem7 = np.asanyarray(ONDA_media7["Voltagem"])

fig7, ax7 = plt.subplots(figsize=(15, 6))
ax7.plot(Tempo7, Voltagem7)
ax7.set_title(f'Média ONDA de 510 Hz com 4.5cm de distancia com 93,75% do volume com 90 graus')
ax7.set_xlabel("Tempo (s)")
ax7.set_ylabel('Tensão (Volts)')
#plt.show()




############### 510 Hz 4.5cm de distancia com 93,75% do volume com 140 graus ################
pasta8 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5cm de distância\93,75% do volume\140 graus"

lista_Tempo8 = []
lista_Voltagem8 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada8 = os.path.join(pasta8, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada8)

    lista_Tempo8.append(data['Tempo'])
    lista_Voltagem8.append(data['Voltagem'])

media_Tempo8 = pd.concat(lista_Tempo8, axis=1).mean(axis=1)
media_Voltagem8 = pd.concat(lista_Voltagem8, axis=1).mean(axis=1)

ONDA_media8 = pd.DataFrame({
    'Tempo': media_Tempo8,
    'Voltagem': media_Voltagem8
})
arquivo_saida8 = os.path.join(pasta8, "ONDA_media.xlsx")

ONDA_media8.to_excel(arquivo_saida8, index=False)

Tempo8 = np.asarray(ONDA_media8["Tempo"])
Voltagem8 = np.asanyarray(ONDA_media8["Voltagem"])

fig8, ax8 = plt.subplots(figsize=(15, 6))
ax8.plot(Tempo8, Voltagem8)
ax8.set_title(f'Média ONDA de 510 Hz com 4.5cm de distancia com 93,75% do volume com 140 graus')
ax8.set_xlabel("Tempo (s)")
ax8.set_ylabel('Tensão (Volts)')
#plt.show()



############### 510 Hz proximo com 50% do volume ################

pasta9 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\Próximo\50% do volume"

lista_Tempo9 = []
lista_Voltagem9 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada9 = os.path.join(pasta9, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada9)

    lista_Tempo9.append(data['Tempo'])
    lista_Voltagem9.append(data['Voltagem'])

media_Tempo9 = pd.concat(lista_Tempo9, axis=1).mean(axis=1)
media_Voltagem9 = pd.concat(lista_Voltagem9, axis=1).mean(axis=1)

ONDA_media9 = pd.DataFrame({
    'Tempo': media_Tempo9,
    'Voltagem': media_Voltagem9
})
arquivo_saida9 = os.path.join(pasta9, "ONDA_media.xlsx")

ONDA_media9.to_excel(arquivo_saida9, index=False)

Tempo9 = np.asarray(ONDA_media9["Tempo"])
Voltagem9 = np.asanyarray(ONDA_media9["Voltagem"])

fig9, ax9 = plt.subplots(figsize=(15, 6))
ax9.plot(Tempo9, Voltagem9)
ax9.set_title(f'Média ONDA de 510 Hz próximo com 50% do volume')
ax9.set_xlabel("Tempo (s)")
ax9.set_ylabel('Tensão (Volts)')
#plt.show()



############### 510 Hz proximo com 93,75% do volume ################
pasta10 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\Próximo\93,75% do volume"

lista_Tempo10 = []
lista_Voltagem10 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada10 = os.path.join(pasta10, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada10)

    lista_Tempo10.append(data['Tempo'])
    lista_Voltagem10.append(data['Voltagem'])

media_Tempo10 = pd.concat(lista_Tempo10, axis=1).mean(axis=1)
media_Voltagem10 = pd.concat(lista_Voltagem10, axis=1).mean(axis=1)

ONDA_media10 = pd.DataFrame({
    'Tempo': media_Tempo10,
    'Voltagem': media_Voltagem10
})
arquivo_saida10 = os.path.join(pasta10, "ONDA_media.xlsx")

ONDA_media10.to_excel(arquivo_saida10, index=False)

Tempo10 = np.asarray(ONDA_media10["Tempo"])
Voltagem10 = np.asanyarray(ONDA_media10["Voltagem"])

fig10, ax10 = plt.subplots(figsize=(15, 6))
ax10.plot(Tempo10, Voltagem10)
ax10.set_title(f'Média ONDA de 510 Hz próximo com 93,75% do volume')
ax10.set_xlabel("Tempo (s)")
ax10.set_ylabel('Tensão (Volts)')
#plt.show()




########### 300 e 320 Hz próximo com 100% do volume ##########

pasta11 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\100% do volume"

lista_Tempo11 = []
lista_Voltagem11 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada11 = os.path.join(pasta11, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada11)

    lista_Tempo11.append(data['Tempo'])
    lista_Voltagem11.append(data['Voltagem'])

media_Tempo11 = pd.concat(lista_Tempo11, axis=1).mean(axis=1)
media_Voltagem11 = pd.concat(lista_Voltagem11, axis=1).mean(axis=1)

ONDA_media11 = pd.DataFrame({
    'Tempo': media_Tempo11,
    'Voltagem': media_Voltagem11
})
arquivo_saida11 = os.path.join(pasta11, "ONDA_media.xlsx")

ONDA_media11.to_excel(arquivo_saida11, index=False)

Tempo11 = np.asarray(ONDA_media11["Tempo"])
Voltagem11 = np.asanyarray(ONDA_media11["Voltagem"])

fig11, ax11 = plt.subplots(figsize=(15, 6))
ax11.plot(Tempo11, Voltagem11)
ax11.set_title(f'Média ONDA 300 Hz e 320 Hz próximo com 100% do volume')
ax11.set_xlabel("Tempo (s)")
ax11.set_ylabel('Tensão (Volts)')
#plt.show()



########### 300 e 320 Hz próximo com 50% do volume ##########
pasta12 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\50% do volume"

lista_Tempo12 = []
lista_Voltagem12 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada12 = os.path.join(pasta12, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada12)

    lista_Tempo12.append(data['Tempo'])
    lista_Voltagem12.append(data['Voltagem'])

media_Tempo12 = pd.concat(lista_Tempo12, axis=1).mean(axis=1)
media_Voltagem12 = pd.concat(lista_Voltagem12, axis=1).mean(axis=1)

ONDA_media12 = pd.DataFrame({
    'Tempo': media_Tempo12,
    'Voltagem': media_Voltagem12
})
arquivo_saida12 = os.path.join(pasta12, "ONDA_media.xlsx")

ONDA_media12.to_excel(arquivo_saida12, index=False)

Tempo12 = np.asarray(ONDA_media12["Tempo"])
Voltagem12 = np.asanyarray(ONDA_media12["Voltagem"])

fig12, ax12 = plt.subplots(figsize=(15, 6))
ax12.plot(Tempo12, Voltagem12)
ax12.set_title(f'Média ONDA de 300 e 320 Hz próximo com 50% do volume')
ax12.set_xlabel("Tempo (s)")
ax12.set_ylabel('Tensão (Volts)')
#plt.show()



######### 300 e 320 Hz 2 cm 100 % do volume e 90 graus ###########
pasta13 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\100% do volume\90 graus"

lista_Tempo13 = []
lista_Voltagem13 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada13 = os.path.join(pasta13, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada13)

    lista_Tempo13.append(data['Tempo'])
    lista_Voltagem13.append(data['Voltagem'])

media_Tempo13 = pd.concat(lista_Tempo13, axis=1).mean(axis=1)
media_Voltagem13 = pd.concat(lista_Voltagem13, axis=1).mean(axis=1)

ONDA_media13 = pd.DataFrame({
    'Tempo': media_Tempo13,
    'Voltagem': media_Voltagem13
})
arquivo_saida13 = os.path.join(pasta13, "ONDA_media.xlsx")

ONDA_media13.to_excel(arquivo_saida13, index=False)

Tempo13 = np.asarray(ONDA_media13["Tempo"])
Voltagem13 = np.asanyarray(ONDA_media13["Voltagem"])

fig13, ax13 = plt.subplots(figsize=(15, 6))
ax13.plot(Tempo13, Voltagem13)
ax13.set_title(f'Média ONDA de 300 e 320 Hz 2 cm 100 % do volume e 90 graus')
ax13.set_xlabel("Tempo (s)")
ax13.set_ylabel('Tensão (Volts)')
#plt.show()



####### 300 e 320 Hz 2 cm 100 % do volume e 170 graus ########
pasta14 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\100% do volume\170 graus"

lista_Tempo14 = []
lista_Voltagem14 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada14 = os.path.join(pasta14, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada14)

    lista_Tempo14.append(data['Tempo'])
    lista_Voltagem14.append(data['Voltagem'])

media_Tempo14 = pd.concat(lista_Tempo14, axis=1).mean(axis=1)
media_Voltagem14 = pd.concat(lista_Voltagem14, axis=1).mean(axis=1)

ONDA_media14 = pd.DataFrame({
    'Tempo': media_Tempo14,
    'Voltagem': media_Voltagem14
})
arquivo_saida14 = os.path.join(pasta14, "ONDA_media.xlsx")

ONDA_media14.to_excel(arquivo_saida14, index=False)

Tempo14 = np.asarray(ONDA_media14["Tempo"])
Voltagem14 = np.asanyarray(ONDA_media14["Voltagem"])

fig14, ax14 = plt.subplots(figsize=(15, 6))
ax14.plot(Tempo14, Voltagem14)
ax14.set_title(f'Média ONDA de 300 e 320 Hz 2 cm 100 % do volume e 170 graus')
ax14.set_xlabel("Tempo (s)")
ax14.set_ylabel('Tensão (Volts)')
#plt.show()




####### 300 e 320 Hz 2 cm 68,75% do volume ########
pasta15 = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\68,75% do volume"

lista_Tempo15 = []
lista_Voltagem15 = []

for i in range(1, 11):  # O número 1 no range não foi alterado
    arquivo_entrada15 = os.path.join(pasta15, f"ONDA{i}.xlsx")
    data = pd.read_excel(arquivo_entrada15)

    lista_Tempo15.append(data['Tempo'])
    lista_Voltagem15.append(data['Voltagem'])

media_Tempo15 = pd.concat(lista_Tempo15, axis=1).mean(axis=1)
media_Voltagem15 = pd.concat(lista_Voltagem15, axis=1).mean(axis=1)

ONDA_media15 = pd.DataFrame({
    'Tempo': media_Tempo15,
    'Voltagem': media_Voltagem15
})
arquivo_saida15 = os.path.join(pasta15, "ONDA_media.xlsx")

ONDA_media15.to_excel(arquivo_saida15, index=False)

Tempo15 = np.asarray(ONDA_media15["Tempo"])
Voltagem15 = np.asanyarray(ONDA_media15["Voltagem"])

fig15, ax15 = plt.subplots(figsize=(15, 6))
ax15.plot(Tempo15, Voltagem15)
ax15.set_title(f'Média ONDA de 300 e 320 Hz 2 cm 68,75% do volume')
ax15.set_xlabel("Tempo (s)")
ax15.set_ylabel('Tensão (Volts)')
plt.show()
