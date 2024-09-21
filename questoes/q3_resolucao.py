import json

# Exemplo de dados de faturamento diário 
dados_faturamento = '''
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 0.0},
    {"dia": 4, "valor": 26139.6134},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612}
]
'''

def calcular_faturamento(dados_json):
    faturamentos = json.loads(dados_json)
    
    valores = [dia['valor'] for dia in faturamentos if dia['valor'] > 0]
    
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    
    media_mensal = sum(valores) / len(valores)
    dias_acima_da_media = len([v for v in valores if v > media_mensal])
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

menor, maior, dias_acima_media = calcular_faturamento(dados_faturamento)
print(f"Menor valor de faturamento: {menor:.2f}")
print(f"Maior valor de faturamento: {maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
