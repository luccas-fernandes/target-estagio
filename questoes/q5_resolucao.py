def inverter_string(texto):
    invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

texto = input("Informe uma string para inverter: ")
texto_invertido = inverter_string(texto)
print(f"String invertida: {texto_invertido}")
