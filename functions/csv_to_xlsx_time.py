import pandas as pd
import os

def transformar_onda(pasta_entrada, pasta_saida, num_arquivos):
    for i in range(1, num_arquivos + 1):

        arquivo_entrada = os.path.join(pasta_entrada, f"ONDA{i}.csv")
        arquivo_saida = os.path.join(pasta_saida, f"ONDA{i}.xlsx")

        data = pd.read_csv(
        arquivo_entrada,
        skiprows = 3,
        delimiter = ',',
        engine = 'python',
        header = None,
        on_bad_lines = 'skip'
        )

        data.columns = ['Index', 'Valor1', 'Valor2', 'Tempo', 'Voltagem', 'Extra']

        data.to_excel(arquivo_saida, index = False)
        print(f"planilha ONDA{i} salva!")

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
       "num_arquivos": 10 
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
        "num_arquivos": 11
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
    }
    
]

for configuracao in configuracoes:
    transformar_onda(
        pasta_entrada = configuracao["pasta_entrada"],
        pasta_saida = configuracao["pasta_saida"],
        num_arquivos = configuracao["num_arquivos"]
    )

