#LOL
def dec2bin(numero_decimal, numero_bits):
    numero_binario = bin(numero_decimal)
    if numero_decimal >= 0:
        numero_binario = numero_binario[2:len(numero_binario)]  # quita el "0b" del principio
    
        while len(numero_binario) < numero_bits:      #XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
            numero_binario = "0" + numero_binario
    else:
        numero_binario = numero_binario[3:len(numero_binario)] #quita el "-0b" del principio
        while len(numero_binario) < numero_bits: #si lees esto enhorabuena has ganado "perdida de tiemp"
            numero_binario = "1" + numero_binario

    return numero_binario

#Lo importante
if __name__ == "__main__":

    numero_decimal = int(input("Escribe el número en decimal que quieres convertir: "))
    numero_bits = int(input("Cuantos bits tendrá el número binario: "))

    # se llama a la función dec2bin() para hacer la conversión
    numero_binario = dec2bin(numero_decimal, numero_bits)

#fjkcjcjcjcjcjcjcjcjcjcjcjcjcjcjjcjcjjcjcjcjjcjcjcjjcjcjjcjcjcjjcjcjcjjcjcjc
    print("El numero " + str(numero_decimal) + " es " + numero_binario + " en binario con " + str(numero_bits) + " bits.")
