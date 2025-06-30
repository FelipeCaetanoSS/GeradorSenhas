import random   
import string

print("Olá, seja bem-vindo! Aqui você está no gerador de senha.\n")

try:
  tamanho = int(input("Na sua senha você deseja que tenha quantos caracteres?: "))
except ValueError:
  print("Entrada inválida. Por favor, digite apenas um número inteiro.")
  exit()

minuscula = input("\nVocê quer letras minúsculas em sua senha?(true/false): ").lower() == "true"
maiscula = input("\nVocê quer letras maísculas em sua senha?(true/false): ").lower() == "true"
numeros = input("\nVocê quer números em sua senha?(true/false): ").lower() == "true"
simbolos = input("\nVocê quer simbolos em sua senha?(true/false): ").lower() == "true"

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

random.shuffle(senha)

# Junta a lista de caracteres em uma única string para formar a senha
senha_final = "".join(senha)

print("\nSenha gerada:")
print(senha_final)
