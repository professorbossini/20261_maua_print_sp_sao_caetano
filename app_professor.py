import webbrowser
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()

#desafio 1 - Dê uma mensagem de boas-vindas ao usuário do sistema. Além das boas-vindas, você pode falar para ele, por exemplo, que ele está utilizando um sistema de recomendação de viagens.
print("Bem vindo ao sistema de recomendação de viagens")

#desafio 2 - Declare uma variável para armazenar o tipo de viagem que o usuário deseja. Faça a entrada instruindo-o a informar Montanha ou Praia.
tipo_viagem = input("Escolha seu tipo de viagem: Praia ou montanha")

#desafio 3 - Declare uma variável para armazenar o valor de orçamento do usuário. Suponha que o valor será inteiro. Instrua o usuário a digitar este valor.
orcamento = int(input("Quanto quer gastar?"))

#desafio 4 - Verifique se o orçamento do usuário é menor do que R$3000. Se for o caso, diga a ele que vamos sugerir destinos econômicos. Caso contrário, diga a ela que vamos sugerir destinos premium.
if orcamento < 3000:
    print('Vamos sugerir destinos econômicos')
else:
    print('Vamos sugerir destinos premium')


#desafio 5 - Monte o seu primeiro prompt, pedindo a sugestão ao ChatGPT. Envolva as variáveis que representam o tipo da viagem e o orçamento do usuário.

# Remova o comentário indicado para ver o resultado.
prompt_sugestao = "Sugira uma viagem para a " + tipo_viagem + " restrita ao orcamento de " + str(orcamento)


#Remova esse comentário quando o professor pedir, ok? :)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": f'{prompt_sugestao}. max:100 tokens'}
    ]
)
print(completion.choices[0].message.content)

#desafio 6 - Monte seu segundo prompt, pedindo ao ChatGPT uma imagem.
prompt_imagem = "Uma foto de " + tipo_viagem + ". Pessoa viajando com orçamento restrito a " + str(orcamento)
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt_imagem,
    n=1,
    size="1024x1024"
)

print(response.data[0].url)
webbrowser.open(response.data[0].url)