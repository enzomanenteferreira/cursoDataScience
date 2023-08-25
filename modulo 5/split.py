#fazendo split dos dados
def split_string_palavras(text):
    return text.split(" ")

texto = "Esta função será bastante util para separar grandes volumes de dados."

print(split_string_palavras(texto))

#ou tambem armazenar o resultado da funcao em uma variavel

token = split_string_palavras(texto)
print(token)

#fazendo split dos dados
def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)

split_string_letras(texto)