import pandas as pd
import matplotlib.pyplot as plt
import os

def transformar_fft(pasta_entrada, pasta_saida, num_arquivos):
    for i in range(1, num_arquivos + 1):

        arquivo_entrada = os.path.join(pasta_entrada, f"FFT{i}.csv")
        arquivo_saida = os.path.join(pasta_saida, f"FFT{i}.xlsx")

        data = pd.read_csv(
        arquivo_entrada,
        skiprows = 3,
        delimiter = ',',
        engine = 'python',
        header = None,
        on_bad_lines = 'skip'
        )

        data.columns = ['Index', 'Tempo', 'Unidade', 'Frequencia', 'Amplitude', 'Extra']
        data.to_excel(arquivo_saida, index = False)
        print(f"planilha FFT{i} salva!")

configuracoes = [
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\1 frequência\100 Hz\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\Próximo\100% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\1 frequência\100 Hz\Próximo\80% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\Próximo\80% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\1 frequência\100 Hz\5mm de distância",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\5mm de distância",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\1 frequência\100 Hz\7mm de distância",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz\7mm de distância",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\1 frequência\510 Hz\Próximo\93,75% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\Próximo\93,75% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\1 frequência\510 Hz\Próximo\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\Próximo\50% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\93,75% do volume\90 graus",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\93,75% do volume\90 graus",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\93,75% do volume\140 graus",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\93,75% do volume\140 graus",
        "num_arquivos": 10
    },
    {
       "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\68,75% do volume\90 graus",
       "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\68,75% do volume\90 graus",
       "num_arquivos": 9 
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\68,75% do volume\120 graus",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\510 Hz\4.5 cm de distância\68,75% do volume\120 graus",
        "num_arquivos": 10 
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\100% do volume",
        "num_arquivos": 10 
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\50% do volume",
        "num_arquivos": 10 
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\100% do volume\90 graus",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\100% do volume\90 graus",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\100% do volume\170 graus",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\100% do volume\170 graus",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\68,75% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\2 frequências\300 Hz e 320 Hz\2cm de distância\68,75% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\100% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\75% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\75% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\Próximo\50% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\90 graus\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\90 graus\100% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\90 graus\80% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\90 graus\80% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\120 graus\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\120 graus\100% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\120 graus\90% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\100 Hz\1 cm de distância\120 graus\90% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\100% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\50% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\20% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\20% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\100% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\50% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\25% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\90 graus\25% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\100% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\50% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\25% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\5 cm de distância\165 graus\25% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\50% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\25% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\Próximo\25% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\50% do volume\90 graus",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\50% do volume\90 graus",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\50% do volume\180 graus",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\50% do volume\180 graus",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\25% do volume\90 graus",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\25% do volume\90 graus",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\25% do volume\180 graus",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\2 frequências\300 Hz e 320 Hz\5 cm de distância\25% do volume\180 graus",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\20mm de diâmetro\1 frequência\100 Hz novo\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\20mm de diâmetro\1 frequência\100 Hz novo\Próximo\100% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo novo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo novo\100% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo novo\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo novo\50% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo novo\40% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo novo\40% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\teste março 2025\1 frequência\510 Hz\Próximo\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\teste março 2025\1 frequência\510 Hz\Próximo\50% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\teste março 2025\1 frequência\510 Hz\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\teste março 2025\1 frequência\510 Hz\Próximo\100% do volume",
        "num_arquivos": 10
    },
    {
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\100 Hz\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\100 Hz\Próximo\100% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\Próximo\100% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\Próximo\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\Próximo\50% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\2 cm\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\2 cm\100% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\2 cm\75% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\200 Hz\2 cm\75% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\440 Hz\Próximo\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\440 Hz\Próximo\50% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\440 Hz\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\440 Hz\Próximo\100% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\50% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\100% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\25% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\25% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\50% do computador",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\Próximo\50% do computador",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\3 cm\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\510 Hz\3 cm\100% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\440 Hz\Próximo\50% do computador",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\440 Hz\Próximo\50% do computador",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\550 Hz\Próximo\50% do computador",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\550 Hz\Próximo\50% do computador",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\550 Hz\Próximo\50% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\550 Hz\Próximo\50% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\20 mm\1 frequência\550 Hz\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\20 mm\1 frequência\550 Hz\Próximo\100% do volume",
        "num_arquivos": 10
    },{
        "pasta_entrada": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Emanuele\de novo\2 voltas e meia\25 mm\1 frequência\200 Hz\Próximo\100% do volume",
        "pasta_saida": r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\de novo\2 voltas e meia\25 mm\1 frequência\200 Hz\Próximo\100% do volume",
        "num_arquivos": 10
    }

    
]

for configuracao in configuracoes:
    transformar_fft(
        pasta_entrada = configuracao["pasta_entrada"],
        pasta_saida = configuracao["pasta_saida"],
        num_arquivos = configuracao["num_arquivos"]
    )




# for i in range (1, 10):

#     pasta = r"C:\Users\emanu\OneDrive\Área de Trabalho\IC\IC Milena\Manus\3 voltas\25 mm de diâmetro\1 frequência\510 Hz\Próximo\50% do volume"
#     arquivo = os.path.join(pasta, f"FFT{i}.xlsx")
#     data = pd.read_excel(arquivo)
#     lista_frequencia = data["Frequencia"]
#     lista_amplitude = data["Amplitude"]

#     indice_pico = data['Amplitude'].idxmax()

#     # Frequência e amplitude do pico
#     frequencia_pico = data['Frequencia'][indice_pico]
#     amplitude_pico = data['Amplitude'][indice_pico]

#     plt.figure(figsize = (10,7))
#     plt.plot(lista_frequencia, lista_amplitude)
#     plt.xlabel("Frequência (Hz)")
#     plt.ylabel("Amplitude (dB)")
#     plt.annotate(f'Pico: {frequencia_pico:.2f} Hz, {amplitude_pico:.2f} dB', 
#                  xy=(frequencia_pico, amplitude_pico), 
#                  xytext=(frequencia_pico + 50, amplitude_pico - 3),
#                  arrowprops=dict(facecolor='blue', shrink=0.005))
#     plt.grid()
#     plt.show()


