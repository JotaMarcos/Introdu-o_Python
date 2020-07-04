# a = 10
# b = 5

a = int(input('Digite o Primeiro Valor: '))
b = int(input('Digite o Segundo Valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b



# print('soma: ' + str(soma))
# print('O Valor da Soma é: ', soma)
# print('O Valor da Subtração é: ', subtracao)
# print('O Valor da Multiplicação é: ', multiplicacao)
# print('O Valor da Divisão é: ', int(divisao))
# print('O Valor do Resto da Divisão é: ', resto)
# x = '1'
# soma2 = int(x) + 1
# print('O Valor da Soma é: ', soma2)
#print('Soma: {}. Subtração: {}'.format(soma, subtracao))

resultdo = ('Soma: {soma}'
      '\nSubtração: {subtracao}'
      ' \nMultiplicação: {multiplicacao}'
      ' \nDivisão: {divisao} '
      '\nResto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))
print(resultdo)