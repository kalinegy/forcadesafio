palavra = "maromba"
dica = "Estilo de vida"

estagios = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

def jogar_forca():
    letras_adivinhadas = []
    letras_erradas = []
    erros = 0
    max_erros = 6

    print("=== JOGO DA FORCA ===")
    print("Digite 'dica' se precisar de ajuda.")
    print("Categoria:ACADEMIA")

    while erros < max_erros:
        print(estagios[erros])
        exibicao = [letra if letra in letras_adivinhadas else "_" for letra in palavra]
        print("\nPalavra: " + " ".join(exibicao))
        print("Letras tentadas: " + ", ".join(sorted(letras_adivinhadas + letras_erradas)))

        if "_" not in exibicao:
            print("Parabéns! Você acertou a palavra!")
            break

        tentativa = input("Digite uma letra ou 'dica': ").lower().strip()

        if tentativa == "dica":
            print(f" Dica: {dica}")
            continue

        if not tentativa.isalpha() or len(tentativa) != 1:
            print("Digite apenas uma letra válida.")
            continue

        if tentativa in letras_adivinhadas or tentativa in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if tentativa in palavra:
            letras_adivinhadas.append(tentativa)
        else:
            letras_erradas.append(tentativa)
            erros += 1
            print("Letra errada!")

    if erros == max_erros:
        print(estagios[erros])
        print(f"Você perdeu! A palavra era: {palavra}")


jogar_forca()
