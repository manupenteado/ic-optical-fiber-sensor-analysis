import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para processar dados FFT e calcular a média
def process_fft(pasta, num_arquivos, titulo_grafico):
    lista_frequencias = []
    lista_amplitudes = []

    # Ler os arquivos e agregar os dados
    if (num_arquivos == 10 or num_arquivos == 9 or num_arquivos == 8):
        for i in range(1, num_arquivos + 1):
            arquivo = os.path.join(pasta, f"FFT{i}.xlsx")
            data = pd.read_excel(arquivo)
            lista_frequencias.append(data['Frequencia'])
            lista_amplitudes.append(data['Amplitude'])

        # Calcular a média
        media_frequencia = pd.concat(lista_frequencias, axis=1).mean(axis=1)
        media_amplitude = pd.concat(lista_amplitudes, axis=1).mean(axis=1)

        # Criar DataFrame com as médias
        FFT_media = pd.DataFrame({
            'Frequencia': media_frequencia,
            'Amplitude': media_amplitude
        })

        # Encontrar o índice do pico mais alto
        indice_pico = FFT_media['Amplitude'].idxmax()

        # Frequência e amplitude do pico
        frequencia_pico = FFT_media['Frequencia'][indice_pico]
        amplitude_pico = FFT_media['Amplitude'][indice_pico]

        # Salvar o resultado
        FFT_media.to_excel(os.path.join(pasta, "FFT_media.xlsx"), index=False)

        # Gerar o gráfico
        plt.figure(figsize=(11, 7))
        plt.plot(FFT_media['Frequencia'], FFT_media['Amplitude'])
        plt.title(titulo_grafico)
        plt.xlabel("Frequência (Hz)")
        plt.ylabel("Amplitude (dB)")
        # Adicionar anotação para o pico
        plt.annotate(f'Pico: {frequencia_pico:.2f} Hz, {amplitude_pico:.2f} dB', 
                    xy=(frequencia_pico, amplitude_pico), 
                    xytext=(frequencia_pico + 50, amplitude_pico - 3),
                    arrowprops=dict(facecolor='blue', shrink=0.005))
        plt.xlim(0, 1000)  # <-- aqui você limita o eixo X de 0 a 1000
        plt.grid()
        plt.show()

        print("Média FFT calculada e salva com sucesso.")

# Lista de configurações para processar múltiplas pastas
configuracoes = [
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz novo\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(0) 100 hz próximo novo"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(1)Média das medidas das FFTs de 100 Hz próximo com 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\5mm de distância",
        "num_arquivos": 10,
        "titulo_grafico": f"(2)Média FFT de 100 Hz a 5 mm de distância com 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\7mm de distância",
        "num_arquivos": 10,
        "titulo_grafico": f"(3)Média FFT de 100 Hz a 7 mm de distância com 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\Próximo\80% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(4)Média FFT de 100 Hz próximo com 80% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\Próximo\93,75% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(5)Média FFT de 510 Hz próximo com 93,75% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(6)Média FFT de 510 Hz próximo com 50% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\93,75% do volume\90 graus",
        "num_arquivos": 8,
        "titulo_grafico": f"(7)Média FFT de 510 Hz a 4.5 cm de distância com 93,75% do volume sem angulação"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\68,75% do volume\90 graus",
        "num_arquivos": 9,
        "titulo_grafico": f"(8)Média FFT de 510 Hz a 4.5 cm de distância com 68,75% do volume sem angulação"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\93,75% do volume\140 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(9)Média FFT de 510 Hz a 4.5 cm de distância com 93,75% do volume com angulação de 140 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\68,75% do volume\120 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(10)Média FFT de 510 Hz a 4.5 cm de distância com 68,75% do volume com angulação de 120 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(11)Média FFT de 300 Hz e 320 Hz próximo com 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(12)Média FFT de 300 Hz e 320 Hz próximo com 50% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\100% do volume\90 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(13)Média FFT de 300 Hz e 320 Hz a 2 cm de distância com 100% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\100% do volume\170 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(14)Média FFT de 300 Hz e 320 Hz a 2 cm de distância com 100% do volume e 170 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\68,75% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(15)Média FFT de 300 Hz e 320 Hz a 2 cm de distância com 68,75% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(16)Média FFT de 100 Hz próximo com 100% do volume e 25 mm de diâmetro"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\75% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(17)Média FFT de 100 Hz próximo com 75% do volume e 25 mm de diâmetro"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(18)Média FFT de 100 Hz próximo com 50% do volume e 25 mm de diâmetro"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\90 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(19)Média FFT de 100 Hz a 1 cm de distância com 100% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\90 graus\80% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(20)Média FFT de 100 Hz a 1 cm de distância com 80% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\120 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(21)Média FFT de 100 Hz a 1 cm de distância com 100% do volume e 120 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\120 graus\90% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(22)Média FFT de 100 Hz a 1 cm de distância com 90% do volume e 120 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(23)Média FFT de 510 Hz próximo com 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(24)Média FFT de 510 Hz próximo com 50% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\20% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(25)Média FFT de 510 Hz próximo com 20% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(26)Média FFT de 510 Hz a 5 cm de distância com 100% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(27)Média FFT de 510 Hz a 5 cm de distância com 50% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\25% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(28)Média FFT de 510 Hz a 5 cm de distância com 25% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(29)Média FFT de 510 Hz a 5 cm de distância com 100% do volume e 165 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(30)Média FFT de 510 Hz a 5 cm de distância com 50% do volume e 165 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\25% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(31)Média FFT de 510 Hz a 5 cm de distância com 25% do volume e 165 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(32)Média FFT de 300 Hz e 320 Hz próximo com 50% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\25% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(33)Média FFT de 300 Hz e 320 Hz próximo com 25% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\50% do volume\90 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(34)Média FFT de 300 Hz e 320 Hz a 5 cm de distância com 50% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\50% do volume\180 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(35)Média FFT de 300 Hz e 320 Hz a 5 cm de distância com 50% do volume e 180 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\25% do volume\90 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(36)Média FFT de 300 Hz e 320 Hz a 5 cm de distância com 25% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\25% do volume\180 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(37)Média FFT de 300 Hz e 320 Hz a 5 cm de distância com 25% do volume e 180 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz novo\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(38)"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo novo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(39) 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo novo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(40) 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\20% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(41) 20% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo novo\40% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(42) 40% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\teste março 2025\1 frequência\510 Hz\Próximo\50% do volume",
        "num_arquivos": 9,
        "titulo_grafico": f"(43) 510 hz 50% do volume"

    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\teste março 2025\1 frequência\510 Hz\Próximo\100% do volume",
        "num_arquivos": 9,
        "titulo_grafico": f"(44) 510 hz 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\100 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(45) 100 Hz 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(46) 200 hz 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(47) 200 hz 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\2 cm\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(48) 200 hz 100% do volume 2 cm"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\2 cm\75% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(49) 200 hz 75% do volume 2 cm"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\440 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(50) 440 hz 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\440 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(51) 440 hz 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(52) 510 hz 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(53) 510 hz 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\25% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(54) 510 hz 25% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\50% do computador",
        "num_arquivos": 10,
        "titulo_grafico": f"(55) 510 hz 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\3 cm\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(56) 510 hz 100% do volume 3 cm"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\440 Hz\Próximo\50% do computador",
        "num_arquivos": 10,
        "titulo_grafico": f"(57) 440 hz 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\550 Hz\Próximo\50% do computador",
        "num_arquivos": 10,
        "titulo_grafico": f"(58) 550 hz 50% do computador"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\550 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(59) 550 hz 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\550 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(60) 550 hz 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\200 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(61) 200 hz próximo 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\200 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(62) 200 hz próximo 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\200 Hz\1.5 cm de distância\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(63) 200 hz 1.5 cm de distância 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\200 Hz\1.5 cm de distância\70% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(64) 200 hz 1.5 cm de distância 70% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\440 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(65) 440 hz próximo 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\440 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(66) 440 hz próximo 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\440 Hz\1.5 cm de distância\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(67) 440 hz 1.5 cm de distância 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\440 Hz\1.5 cm de distância\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(68) 440 hz 1.5 cm de distância 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\510 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(69) 510 hz próximo 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\510 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(70) 510 hz próximo 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\550 Hz\Próximo\90 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(71) 550 hz próximo 90 graus 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\550 Hz\Próximo\90 graus\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(72) 550 hz próximo 90 graus 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\550 Hz\Próximo\120 graus\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(73) 550 hz próximo 120 graus 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\550 Hz\Próximo\120 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(74) 550 hz próximo 120 graus 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\550 Hz\2.5 cm de distância\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(75) 550 hz 2.5 cm de distância 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\550 Hz\2.5 cm de distância\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(76) 550 hz 2.5 cm de distância 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\2 frequências\300 e 305 Hz\1.5 cm de distância\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(77) 300 e 305 hz 1.5 cm de distância 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\2 frequências\300 e 305 Hz\1.5 cm de distância\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(78) 300 e 305 hz 1.5 cm de distância 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\2 frequências\300 e 305 Hz\Próximo\90 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(79) 300 e 305 hz próximo 90 graus 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\2 frequências\300 e 305 Hz\Próximo\90 graus\75% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(80) 300 e 305 hz próximo 90 graus 75% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\2 frequências\300 e 305 Hz\Próximo\90 graus\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(81) 300 e 305 hz próximo 90 graus 50% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\2 frequências\300 e 305 Hz\Próximo\115 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(82) 300 e 305 hz próximo 115 graus 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\2 frequências\320 e 325 Hz\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(83) 320 e 325 hz 100% do volume"
    },{
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\2 frequências\320 e 325 Hz\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(84) 320 e 325 hz 50% do volume"
    }


]

# Processar todas as configurações
for config in configuracoes:
    process_fft(
        pasta=config["pasta"],
        num_arquivos=config["num_arquivos"],
        titulo_grafico=config["titulo_grafico"]
    )
