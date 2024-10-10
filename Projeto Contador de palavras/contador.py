

frase = str(input("Digite alguma coisa: "))


# Vai separar as palavras em partes

palavras_separadas = frase.split()


# Conta quantas palavras estão presentes no input

total_palavras = len(palavras_separadas)


print("\nFrase do usuário: ", frase)
print("\nO total de palavras separadas pelo usuário é: ", total_palavras)

