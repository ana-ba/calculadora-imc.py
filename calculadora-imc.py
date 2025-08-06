def calcular_imc():
    peso = float(input("Digite seu peso em Kg: "))
    altura = float(input("Digite sua altura em metros: "))
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M/F): ").upper()

    imc = peso / (altura ** 2)
    print(f"Seu cálculo de IMC é: {imc:.2f}")

    if idade < 18:
        if imc <= 14.5:
            print("Você está abaixo do peso para sua idade.")
        elif imc <= 22:
            print("Você está no peso ideal para sua idade.")
        else:
            print("Você está acima do peso para sua idade.")

    elif sexo == 'F':
        if imc <= 18.5:
            print("Você está abaixo do peso.")
        elif imc <= 25:
            print("Você está no peso ideal.")
        else:
            print("Você está acima do peso.")

    elif sexo == 'M':
        if imc <= 20:
            print("Você está abaixo do peso.")
        elif imc <= 25:
            print("Você está no peso ideal.")
        else:
            print("Você está acima do peso.")

    else:
        print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")


resposta = input("Deseja calcular Novamente? (S/N): ") .upper()
while resposta == "S":
    calcular_imc()
    resposta = input("Deseja calcular novamente? (S/N): ").upper()
