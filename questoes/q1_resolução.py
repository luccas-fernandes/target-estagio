def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K += 1
        SOMA += K
    return SOMA

resultado = calcular_soma()
print(f"Valor final da variável SOMA: {resultado}")
