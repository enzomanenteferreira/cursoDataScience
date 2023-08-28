#expressoes regulares são geralmente usadas para manipular strings e realizar tarefas como validação de entrada de dados
import re

texto = "meu e-mail é exemplo@gmail.com e voce pode me contatar em outro_email@yahoo.com"

#expressao regular para contar quantas vezes o caractere @ aparece no texto
resultado = len(re.findall("@",texto))
print("o caractere '@' apareceu", resultado,"vezes no texto.")


#expressao regular para extrair a palavra que aparece apos a palavra "voce" em um texto
resultado = re.findall(r'voce (\w+)', texto)
print("A palavra após 'voce é", resultado)

 