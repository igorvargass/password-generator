import string
import secrets

#declaracao de variaveis
senha = ''
tamanhoSenha = 12
letras = string.ascii_letters
numeros = string.digits
caracteresEspeciais = string.punctuation
alfabeto = letras + numeros + caracteresEspeciais

#geracao da senha
for i in range(tamanhoSenha):
    senha += ''.join(secrets.choice(alfabeto))

#impressao da senha gerada
print(f"Senha gerada: {senha}")