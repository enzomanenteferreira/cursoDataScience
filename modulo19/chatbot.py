# Projeto 3 - construindo chatbot personalizado com GPT e linguagem python

import openai

# Chave
openai.api_key = "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"

# função para gerar texto a partir do modelo de linguagem
def gera_texto(texto):

    # obtem a resposta do modelo de linguagem
    response = openai.Completion.create(

        # Modelo usado
        engine = "text-davinci-003",

        # Texto inicial da conversa com o chatbot
        prompt = texto,

        # Comprimento da resposta gerada pelo modelo
        max_tokens = 150,

        # Quantas conclusões gerar para cada prompt
        n = 5,

        # O texto retornado não conterá a sequencia de parada
        stop = None,

        # Uma medida da aleatoriedade de um texto gerado pelo modelo. seu valor esta entre 0 e 1
        # valores proximos a 1 significam que a saida é mais aleatoria, enquanto valores proximos a 0 significam que a saida é muito identificavel
        temperature = 0.8,
    )
    
    return response.choices[0].text.strip()


# Funcao principal do programa
def main():

    print("\nBem vindo ao gpt Chatbot")
    print("www.datascienceacademy.com.br")
    print("(Digite  'sair' a qualquer momento para encerrar o chat)")

    #Loop
    while True:

        # Coleta a pergunta digitada pelo usuario.
        user_message = input("\nVoce: ")

        # se a mensagem for "sair" finaliza o programa
        if user_message.lower() == "sair":
            break

        # coloca a mensagem digitada pelo usuario na variavel python chamada gpt4_prompt
        gpt4_prompt = f"\nUsuario: {user_message}\nChatbot:"

        # obtem a respota do modelo executando a função gera_texto().
        chatbot_response = gera_texto(gpt4_prompt)

        #imprime a resposta do chatbot
        print(f"\nChatbot: {chatbot_response}")

# execucao do bloco main
if __name__ == "__main__":
    main()