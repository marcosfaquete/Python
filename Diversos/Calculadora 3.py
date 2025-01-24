def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida!"

def calculadora():
    print("Bem-vindo à Calculadora em Python!")
    print("Selecione a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    while True:
        try:
            escolha = int(input("Digite sua escolha (1/2/3/4): "))
            if escolha not in [1, 2, 3, 4]:
                print("Opção inválida. Tente novamente.")
                continue

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == 1:
                print(f"Resultado: {num1} + {num2} = {soma(num1, num2)}")
            elif escolha == 2:
                print(f"Resultado: {num1} - {num2} = {subtracao(num1, num2)}")
            elif escolha == 3:
                print(f"Resultado: {num1} * {num2} = {multiplicacao(num1, num2)}")
            elif escolha == 4:
                print(f"Resultado: {num1} / {num2} = {divisao(num1, num2)}")

            continuar = input("Deseja realizar outra operação? (s/n): ").lower()
            if continuar != 's':
                print("Encerrando a calculadora. Até a próxima!")
                break

        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

if __name__ == "__main__":
    calculadora()
