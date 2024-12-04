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
nome = "Marcos"
sobrenome = "Faquete"
nome_completo = "Marcos Faquete"

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

# Step tree
nome = "Marcos"
sobrenome = "Faquete"
nome_completo = "Marcos Faquete"

nome_completo.count("a") 
R:2 | Count contar quantos iguais

nome_completo.find("a")
R:1 | Find a primeira posição que está o "a"
Retorna o indice da ocorrencia dessa letra dentro dessa string




nome = "Marcos"
nome.encode()       codificar em bytes
b'Marcos'

nome.encode().decode()      decodificar
'Marcos'



nome = "Marcos"
sobrenome = "Faquete"
nome_completo = "Marcos Faquete"

nome_completo.replace("a","W")
MWrcos

nome_completo.replace("a", "123")
M123rcos

telefone = "(19) 98456-2758"
telefone.replace("(", ""))
R: 19)98456-2758

telefone.replace("(", "").replace(")", "").replace("-", "")
R: 1998456-2758




nome = "Marcos"
sobrenome = "Faquete"
nome_completo = "Marcos Faquete"
"-".join("Marcos")
R: M-a-r-c-o-s

nome_completo.split()
R: ['Marcos', 'Faquete']

nome_completo.split(" - ")
R: ['Marcos Faquete']



nome = "WWMarcosWW"
nome.strip("W")     remover a string, se não achar não remove nada
R: Marcos

nome.rstrip("W")    r de rigth remove da direita
R: WWMarcos

nome.lstrip("W")    l de left remove da esquerda
R: MarcosWW



nome_completo = "Marcos Faquete"
nome_completo.startswith("Ma")
R: True

nome_completo.startswith("WW")
R: False

"Ma" in nome_completo          Se existe me volte verdadeiro
R: True

"el" in nome_completo
R: False

"abc" not in nome_completo      Se não existe me volte verdadeiro
R: True

"Mar" not in nome_completo
R: False



# -----------------------------------------------------------------------



# Boleanos
True or False
if True:
    print("Bloco IF vai ser executado")
else:
    print("Bloco ELSE não será executado")


# Operadores lógicos: and e or

AND
if True and True:
    print("Bloco será executado")

if True and False:
    print("Bloco não será executado")

if False and False:
    print("Bloco não será executado")

OR
if True or False:
    print("Bloco OR vai ser executado")

if False or False:
    print("Bloco OR não vai ser executado")

if True or True:
    print("Bloco OR vai ser executado")



# -----------------------------------------------------------------------



# Lista
minha_lista = [1, 2, 3, 4, 5, Haven, True, False]

print("Minha lista de exemplo", minha_lista)

print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[2:]", minha_lista[2:])


# Trocando elementos dentro da lista:
minha_lista = [a, b, c, d, e, f, g, h]

minha_lista[0] = "Python"
R: 'Python', '2', '3'

# Métodos de lista
# Método append(): Adciiona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# Método index
indice = minha_lista.index(7)
print("indice do elemento 7:", indice)

# Método insert: Insere um elemento em um índice específico
minha_lista.insert(2, 10)
print("Após o insert(2, 10):", minha_lista)

# Método pop
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após pop(3):", minha_lista)

# Método remove
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

# Método sort orgraniza em ordem crescente
minha_lista.sort()
print("Após sort()", minha_lista)



# -----------------------------------------------------------------------



# Tupla (n pode ser alterada)

minha_tupla = (1, 2, 2, 3, 4)
print("Minha tupla:", minha_tupla)

print("Minha tupla[0]:", minha_tupla[0])
print("Minha tupla[2]:", minha_tupla[2])
print("Minha tupla[-1]:", minha_tupla[-1])

# Método count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

indice = minha_tupla. index(3)
print("Indice da primeira ocorrência do elemento 3:", indice)



# -----------------------------------------------------------------------



# Dicionários

# Criando um dicionário de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Exibindo o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
print("Sobrenome:", pessoa["sobrenome"])

pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]

# Métodos: keys(), values(), items()
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Métodos values
valores = listpessoa.values()
print("Valores do dicionários:", valores)
print("Primeiro valor do dicionário:", valores[0])

# Métodos items
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeira chave-valor: %$ = %$" % (itens[0][0], itens[0][1]))



# -----------------------------------------------------------------------



# Condicionais
# if, elif e else

# Exemplo de "if"
idade = 18
print("Exemplo de comando if")
if idade >= 18:
    print("Você é maior de idade.")

if idade == 19:
    print("Você tem 19 anos")

if idade <= 18:
    print("Você é menor de idade")

if idade != 10:
print("Você não tem 10 anos")



# -----------------------------------------------------------------------

# Exemplo input
name = str(input("Qual seu nome? "))
idade = int(input("Qua sua idade? "))

# -----------------------------------------------------------------------





# FOR

# Lista
print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

# Tupla
print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

# Dicionário chaves
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("For utilizando dicionario - chaves")
for chave in pessoa.keys():
    print(chave)

print("For utilizando dicionario - valores")
for valor in pessoa.values():
    print(valor)

print("For utilizando dicionario - items")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


# Range
range(): intervalo numérico
[0,1,2,3,4,5]

print("Utilizando a função range()")
for numero in range(5):
    print("Número:", numero)


print("Utilizadno a função range() com len()")
lista = [1,2,3,4,5]
for indice in range(0, len(lista)):
    print("Indice:", indice)
    print("Elemento:", lista[indice])



lista = [1,2,3,4,5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)
  

# enumerate()
lista_enumerate = ["a","b","c"]
for indice, valor in enumerate(lista_enumerate)
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")


# -----------------------------------------------------------------------


# while
print("Exemplo de while")
contador = 0
while True:
    print("Contagem:", contador)
    contador += 1
    if contador == 5:
        break
print("Programa finalizado")

while True:
    print("Menu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Completadas")
    print("6. Sair")

escolha = input("Digite a sua escolha: ")

if escolha == "6":
    break

print("Programa Finalizado")




# -----------------------------------------------------------------------


# Funções

def saudacao(nome):
    print(f"Olá, {nome}!")

print("Chamado a função saudação:")
saudacao("Alice")
saudacao("Bob")

# Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("Chamando função quadrado:")
resultado_quadrado = quadrado(6)
print("Resultado da funcao quadrado:", resultado_quadrado)



# Função com multiplos parametros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("Chamando a função soma:")
numero1 = 25
numero2 = 30
resultado_soma = soma(numero1, numero2)
print("A soma do numero %s e o numero %s é %s" % (numero1, numero2, resultado_soma))



# -----------------------------------------------------------------------



# While and Functions

def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("Lista de tarefas:")
    for indice, tarefa in enumerate(tarefas):
        status = "x" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
        


tarefas = []
while True:
    print("Menu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Completadas")
    print("6. Sair")

escolha = input("Digite a sua escolha: ")

if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
    adicionar_tarefa(tarefas, nome_tarefa)


elif escolha == "2":
    ver_tarefas(tarefas)



elif escolha == "6":
    break

print("Programa Finalizado")













