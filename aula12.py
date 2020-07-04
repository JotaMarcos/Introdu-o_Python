# import requests
#
# def retorna_dados_cep(cep):
#     response = requests.get('https://viacep.coom.br/ws/{}/json/'.format(cep))
#     print(requests.status_codes)
#     print(response.json())
#     dados_cep = response.json()
#     print(dados_cep[f'logradouro'])
#     print(dados_cep[f'complemento'])
#     return dados_cep
#
# def retorna_dados_pokemon(pokemon):
#     response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
#     dados_pokemon = response.json()
#     return dados_pokemon
#
# def retorna_response(url):
#     response = requests.get(url)
#     return response.text
#
# if __name__ == '__main__':
#     response = retorna_response('https://globallab.org/en/#.Xv_bvihKjcc')
#     print(response)
#     # dados_cep = retorna_dados_cep('22041001')
#     # dados_pokemon = retorna_dados_pokemon('pikachu')
#     # print(dados_pokemon['sprites']['front_shiny'])





import requests
busca = requests.get('https://viacep.com.br/ws/01001000/json/')
status = busca.status_code

def interpretarMensagem(mensagem):
    print('{} {}'.format())
    if status == 400:
      print('Mensagem não chegou')
    elif status == 200:
      mensagem = busca.json()
      interpretarMensagem(mensagem)