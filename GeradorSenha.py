import random
import string

print("Olá, seja bem-vindo! Aqui você está no gerador de senha.\n")

try:
    tamanho = int(input("Na sua senha você deseja que tenha quantos caracteres?: "))
except ValueError:
    print("Entrada inválida. Por favor, digite apenas um número inteiro.")
    exit()

minuscula = input("\nVocê quer letras minúsculas em sua senha?(true/false): ").strip().lower()
while minuscula not in ['true', 'false']:
    print("Entrada inválida. Por favor, digite 'true' ou 'false'.")
    minuscula = input("\nVocê quer letras minúsculas em sua senha?(true/false): ").strip().lower()

maiscula = input("\nVocê quer letras maiúsculas em sua senha?(true/false): ").strip().lower()
while maiscula not in ['true', 'false']:
    print("Entrada inválida. Por favor, digite 'true' ou 'false'.")
    maiscula = input("\nVocê quer letras maiúsculas em sua senha?(true/false): ").strip().lower()

numeros = input("\nVocê quer números em sua senha?(true/false): ").strip().lower()
while numeros not in ['true', 'false']:
    print("Entrada inválida. Por favor, digite 'true' ou 'false'.")
    numeros = input("\nVocê quer números em sua senha?(true/false): ").strip().lower()

simbolos = input("\nVocê quer símbolos em sua senha?(true/false): ").strip().lower()
while simbolos not in ['true', 'false']:
    print("Entrada inválida. Por favor, digite 'true' ou 'false'.")
    simbolos = input("\nVocê quer símbolos em sua senha?(true/false): ").strip().lower()

senha = []
pool = ""


if minuscula:
    pool += string.ascii_lowercase
    senha.append(random.choice(string.ascii_lowercase))
if maiscula:
    pool += string.ascii_uppercase
    senha.append(random.choice(string.ascii_uppercase))
if numeros:
    pool += string.digits
    senha.append(random.choice(string.digits))
if simbolos:
    pool += string.punctuation
    senha.append(random.choice(string.punctuation))


tamanho_restante = tamanho - len(senha)

if tamanho_restante > 0:
    for _ in range(tamanho_restante):
        senha.append(random.choice(pool))

# Embaralhando a senha para garantir que os caracteres fiquem aleatórios
random.shuffle(senha)

# Junta a lista de caracteres em uma única string para formar a senha
senha_final = "".join(senha)


print("\nSenha gerada:")
print(senha_final)
