while True:
    try:
        nome = input("Digite seu nome completo: ")
        ano_nascimento = int(input("Digite o ano que voçê nasceu: "))

        if ano_nascimento >= 1922 and ano_nascimento <= 2021:
            idade = 2022 - ano_nascimento
            print("Nome: ",nome)
            print("Idade: ",idade)
            break
        else:
            raise ValueError("Ano de nascimento inválido. Por favor, insira um ano entre 1922 e 2021.")
    except ValueError as e:
        print(e)
