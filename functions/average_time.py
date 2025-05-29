import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Função para processar dados da onda e calcular a média
def process_fft(pasta, num_arquivos, titulo_grafico):
    lista_tempo = []
    lista_voltagem = []

    # Ler os arquivos e agregar os dados
    for i in range(1, num_arquivos + 1):
        arquivo = os.path.join(pasta, f"ONDA{i}.xlsx")
        data = pd.read_excel(arquivo)
        lista_tempo.append(data['Tempo'])
        lista_voltagem.append(data['Voltagem'])

    # Calcular a média
    media_tempo = pd.concat(lista_tempo, axis=1).mean(axis=1)
    media_voltagem = pd.concat(lista_voltagem, axis=1).mean(axis=1)

    # Criar DataFrame com as médias
    ONDA_media = pd.DataFrame({
        'Tempo': media_tempo,
        'Voltagem': media_voltagem
    })

    # Salvar o resultado
    ONDA_media.to_excel(os.path.join(pasta, "ONDA_media.xlsx"), index=False)

    # Gerar o gráfico
    plt.figure(figsize=(14, 5))
    plt.plot(ONDA_media['Tempo'], ONDA_media['Voltagem'])
    plt.title(titulo_grafico)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Voltagem (V)")
    plt.grid()
    plt.show()

# Lista de configurações para processar múltiplas pastas
configuracoes = [
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(1)Média das medidas das FFTs de 100 Hz próximo com 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\5mm de distância",
        "num_arquivos": 10,
        "titulo_grafico": f"(2)Média da onda de 100 Hz a 5 mm de distância com 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\7mm de distância",
        "num_arquivos": 10,
        "titulo_grafico": f"(3)Média da onda de 100 Hz a 7 mm de distância com 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\Próximo\80% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(4)Média da onda de 100 Hz próximo com 80% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\Próximo\93,75% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(5)Média da onda de 510 Hz próximo com 93,75% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(6)Média da onda de 510 Hz próximo com 50% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\93,75% do volume\90 graus",
        "num_arquivos": 9,
        "titulo_grafico": f"(7)Média da onda de 510 Hz a 4.5 cm de distância com 93,75% do volume sem angulação"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\68,75% do volume\90 graus",
        "num_arquivos": 9,
        "titulo_grafico": f"(8)Média da onda de 510 Hz a 4.5 cm de distância com 68,75% do volume sem angulação"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\93,75% do volume\140 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(9)Média da onda de 510 Hz a 4.5 cm de distância com 93,75% do volume com angulação de 140 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\68,75% do volume\120 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(10)Média da onda de 510 Hz a 4.5 cm de distância com 68,75% do volume com angulação de 120 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(11)Média da onda de 300 Hz e 320 Hz próximo com 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(12)Média da onda de 300 Hz e 320 Hz próximo com 50% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\100% do volume\90 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(13)Média da onda de 300 Hz e 320 Hz a 2 cm de distância com 100% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\100% do volume\170 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(14)Média da onda de 300 Hz e 320 Hz a 2 cm de distância com 100% do volume e 170 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\68,75% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(15)Média da onda de 300 Hz e 320 Hz a 2 cm de distância com 68,75% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(16)Média da onda de 100 Hz próximo com 100% do volume e 25 mm de diâmetro"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\75% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(17)Média da onda de 100 Hz próximo com 75% do volume e 25 mm de diâmetro"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(18)Média da onda de 100 Hz próximo com 50% do volume e 25 mm de diâmetro"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\90 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(19)Média da onda de 100 Hz a 1 cm de distância com 100% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\90 graus\80% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(20)Média da onda de 100 Hz a 1 cm de distância com 80% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\120 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(21)Média da onda de 100 Hz a 1 cm de distância com 100% do volume e 120 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\120 graus\90% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(22)Média da onda de 100 Hz a 1 cm de distância com 90% do volume e 120 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(23)Média da onda de 510 Hz próximo com 100% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(24)Média da onda de 510 Hz próximo com 50% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\20% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(25)Média da onda de 510 Hz próximo com 20% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(26)Média da onda de 510 Hz a 5 cm de distância com 100% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(27)Média da onda de 510 Hz a 5 cm de distância com 50% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\25% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(28)Média da onda de 510 Hz a 5 cm de distância com 25% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\100% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(29)Média da onda de 510 Hz a 5 cm de distância com 100% do volume e 165 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(30)Média da onda de 510 Hz a 5 cm de distância com 50% do volume e 165 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\25% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(31)Média da onda de 510 Hz a 5 cm de distância com 25% do volume e 165 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\50% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(32)Média da onda de 300 Hz e 320 Hz próximo com 50% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\25% do volume",
        "num_arquivos": 10,
        "titulo_grafico": f"(33)Média da onda de 300 Hz e 320 Hz próximo com 25% do volume"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\50% do volume\90 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(34)Média da onda de 300 Hz e 320 Hz a 5 cm de distância com 50% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\50% do volume\180 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(35)Média da onda de 300 Hz e 320 Hz a 5 cm de distância com 50% do volume e 180 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\25% do volume\90 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(36)Média da onda de 300 Hz e 320 Hz a 5 cm de distância com 25% do volume e 90 graus"
    },
    {
        "pasta": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\25% do volume\180 graus",
        "num_arquivos": 10,
        "titulo_grafico": f"(37)Média da onda de 300 Hz e 320 Hz a 5 cm de distância com 25% do volume e 180 graus"
    }

        
]

# Processar todas as configurações
for config in configuracoes:
    process_fft(
        pasta=config["pasta"],
        num_arquivos=config["num_arquivos"],
        titulo_grafico=config["titulo_grafico"]
    )
