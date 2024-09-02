def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

texto = input("Informe uma string: ")
print(f"String invertida: {inverter_string(texto)}")
