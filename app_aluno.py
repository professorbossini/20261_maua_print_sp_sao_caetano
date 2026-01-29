import webbrowser
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()

#desafio 1 - Dê uma mensagem de boas-vindas ao usuário do sistema. Além das boas-vindas, você pode falar para ele, por exemplo, que ele está utilizando um sistema de recomendação de viagens.


#desafio 2 - Declare uma variável para armazenar o tipo de viagem que o usuário deseja. Faça a entrada instruindo-o a informar Montanha ou Praia.


#desafio 3 - Declare uma variável para armazenar o valor de orçamento do usuário. Suponha que o valor será inteiro. Instrua o usuário a digitar este valor.


#desafio 4 - Verifique se o orçamento do usuário é menor do que R$3000. Se for o caso, diga a ele que vamos sugerir destinos econômicos. Caso contrário, diga a ela que vamos sugerir destinos premium.


#desafio 5 - Monte o seu primeiro prompt, pedindo a sugestão ao ChatGPT. Envolva as variáveis que representam o tipo da viagem e o orçamento do usuário.

# Remova o comentário indicado para ver o resultado.
# prompt_sugestao = ""

#Remova esse comentário quando o professor pedir, ok? :)
# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": f'{prompt_sugestao}. max:100 tokens'}
#     ]
# )
#print(completion.choices[0].message.content)

#desafio 6 - Monte seu segundo prompt, pedindo ao ChatGPT uma imagem.

#o que você quer ver? # Uma praia? Pessoas? Mochilas? Montanha? Um cachorro correndo atrás de uma bola? Seja criativo(a)!
#Remova esse comentário quando o professor pedir, ok? :)
# prompt_imagem = ""
# response = client.images.generate(
#     model="dall-e-3",
#     prompt=prompt_imagem,
#     n=1,
#     size="1024x1024"
# )


#webbrowser.open(response.data[0].url)