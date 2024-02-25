#CHATGPT(API)


#import 
import openai 

#chave api
chave_api = "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"

openai.api_key = chave_api

#pergunta=mensagem

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append( 
        {"role": "user", "content": mensagem}
        )



    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens 

    
    )

    return resposta["choices"][0]["message"]

#resposta 

while True:
    texto = input("User:")
    
    if texto == "sair":
        break 
    else:
        resposta = enviar_mensagem(texto)
        print("TechStock:", resposta)
