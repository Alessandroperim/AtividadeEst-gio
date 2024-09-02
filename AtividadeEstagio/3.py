import json

caminho_arquivo = 'faturamento.json'

def ler_arquivo_json(caminho):
    with open(caminho, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

dados = ler_arquivo_json(caminho_arquivo)
faturamento = dados["faturamento"]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)

dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
