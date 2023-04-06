ALGARISMOS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")


def converter_digito(digito: str) -> int:
    return ALGARISMOS.index(digito.upper())

def validar_numero(numero: str, base: int) -> bool:
    for digito in numero:
        if converter_digito(digito) >= base:
            return False
    return True

def validar_partes(partes: list) -> bool:
    if len(partes) != 2:
        print("\nDigite o número e a base que ele está: <número> <base>\n")
        return False
    numero = partes[0]
    base = partes[1]
    if not numero.isnumeric():
        print("\nDigite um número válido\n")
        return False
    if not base.isnumeric() or int(base) < 2:
        print("\nDigite uma base válida\n")
        return False
    if int(base) > 36:
        print(f"A maior base de conversão é 36\n")
        return False
    return True

def converter_numero(numero: str, base: int) -> int:
    tamanho_do_numero = len(numero) - 1
    resultado = 0

    resolucao = "\n"
    for indice, digito in enumerate(numero):
        resultado += converter_digito(digito) * (base ** (tamanho_do_numero - indice))
        resolucao += f"{digito} * {base}^{tamanho_do_numero - indice} {'+ ' if indice != tamanho_do_numero else ''}"

    return resultado, resolucao


print("Como funciona:\n")

print("Digite o número e a base que ele está: <número> <base>\n")

print("Exemplo:\n")

print("Digite o número e a base que ele está: 200 4")

converter_numero("200", 4)

print(f"A maior base de conversão possível é {len(ALGARISMOS)}\n")

print("Pressione o ENTER sem digitar nada, para sair do programa.\n")


while True:
    escolha = input("Digite o número e a base que ele está: ")
    
    if escolha == "":
        break

    partes = escolha.split(" ")

    if not validar_partes(partes):
        continue

    numero = partes[0]
    base = partes[1]
    if not base.isnumeric() and int(base) > 36:
        print(f"A base {base} não é válida\n")
        continue
    
    base = int(base)

    if validar_numero(numero, base):
        resultado, resolucao = converter_numero(numero, base)
        print(f"{resolucao}= {resultado}\n")

        print(f"{numero} na base {base} é {resultado} na base 10\n")
    else:
        print(f"{numero} é inválido na base {base}\n")
