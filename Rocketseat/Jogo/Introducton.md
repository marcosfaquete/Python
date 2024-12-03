# -----------------------------------------------------------------------
# if - else
idade = 25
if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")

# -----------------------------------------------------------------------
# Inteiro
num_inteiro = 7
print("Inteiro = ", num_inteiro")

# Real Float
num_real = 3.7
print("Real com ponto flutuante = ", num_real)

# type()
print("Tipo da variavel inteiro = ", type(num_inteiro))
print("Tipo da variavel real = ", type(num_real))
# -----------------------------------------------------------------------

# Operadores aritméticos
soma = 1 + 1 
print("1 + 1 = ", soma)

subtracao = 1 - 1
print("1 - 1 = ", subtracao)

multiplicacao = 2 * 2
print("2 x 2 = ", multiplicacao)

divisao = 5 / 2
print("6 dividido por 2 = ", divisao)

int()
print("Valor em inteiro = ", int(divisao))

float()
print("Valor em float = ", float(divisao))

Modulo
modulo = 5 % 2
print("Modulo = ", modulo)

Divisao inteiro 
divisao = 5/ 2
print("5 / 2 = ", divisao)
print("Tipo da vairavel do resultado da divisao = ", type(divisao))

# -----------------------------------------------------------------------

# Texto
nome_completo = "Marcos Faquete"
nome = "Marcos"
sobrenome = "Faquete"

# Formatação
print("Nome completo (1º forma:):", nome_completo)
print("Nome completo (2º forma:):" + nome_completo)
print("Nome completo (3º forma:):" + "Marcos" + "Faquete")
print("Nome completo (4º forma:):" + "Marcos", "Faquete")
print("Nome completo (5º forma:): %s %s" % (nome, sobrenome))
print("Nome completo (6º forma:): {nome} {sobrenome}")
print("Nome completo (7º forma:): {} {}".format(nome, sobrenome))

# Step two
nome = "Marcos"
print(nome.upper())
print(nome.lower())

print(nome[0])  M
print(nome[1])  A
print(nome[2])  R
print(nome[3])  C
print(nome[4])  O
print(nome[5])  S