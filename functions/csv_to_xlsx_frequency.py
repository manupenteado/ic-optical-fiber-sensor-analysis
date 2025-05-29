import pandas as pd
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

