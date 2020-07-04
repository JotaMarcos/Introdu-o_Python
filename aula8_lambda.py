# contador_letras = lambda  lista: [len(x) for x in lista]
#
# lista_animais = ['cachorro', 'gato', 'elefante']
# print(f'O Valor em Caracteres de cada Palavara da Lista é: {contador_letras (lista_animais)}')
#
# # soma = lambda a, b: a + b
# # print(f'O Valor da Soma é: {soma(5,10)}')
# #
# # subtracao = lambda a, b: a - b
# # print(f'O Valor da Subtração é: {subtracao(5,10)}')
# #
# # multiplicacao = lambda a, b: a * b
# # print(f'O Valor da Multiplicação é: {multiplicacao(5,10)}')
# #
# # divisao = lambda a, b: a / b
# # print(f'O Valor da Divisão é: {divisao(5,10)}')
# #
# # resto = lambda a, b: a % b
# # print(f'O Valor do Resto da Divisão é: {resto(5,10)}')
#
#
# calculadora = {
#         'soma': lambda a, b: a + b,
#         'subtracao': lambda a, b: a - b,
#         'multiplicacao': lambda a, b: a * b,
#         'divisao': lambda a, b: a / b,
#         'resto': lambda a, b: a % b
# }
#
# # print(type(calculadora))
# #soma =  lambda a, b: a +b
# soma = calculadora['soma']
# print(f'O Valor da Soma é: {soma(10, 5)}')
# subtracao = calculadora['subtracao']
# print(f'O Valor da Subtração é: {subtracao(10,2)}')
# multiplicacao = calculadora['multiplicacao']
# print(f'O Valor da Multiplicação é: {multiplicacao(10, 5)}')
# divisao = calculadora['divisao']
# print(f'O Valor da Divisão é: {divisao(10,2)}')
# resto = calculadora['resto']
# print(f'O Valor da Resto da Divisão é: {resto(10,2)}')


valida_numero = {
    'par': lambda a: True if a % 2 == 0 else False,
    'impar': lambda b: True if b % 2 == 0 else False
}
resultado = valida_numero['par'](10)