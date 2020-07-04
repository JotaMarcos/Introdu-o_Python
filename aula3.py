# a = int(input('Primeiro Bimestre: '))
# if a > 10:
#     a = int(input('Você digitou errado. Primeiro Bimestre: '))
# b = int(input('Segundo Bimestre: '))
# if b > 10:
#     b = int(input('Você digitou errado. Segundo Bimestre: '))
# c = int(input('Terceiro Bimestre: '))
# if c > 10:
#         c = int(input('Você digitou errado. Terceiro Bimestre: '))
# d = int(input('Quarto Bimestre: '))
# if d > 10:
#         d = int(input('Você digitou errado. Quarto Bimestre: '))
#
# media = (a + b + c + d) / 4
#
# print('A Media é: {}'.format(media))
#
# if media >= 7:
#     print('Parabéns você foi APROVADO!!!')
# elif media >= 5:
#     print('Atenção! Você ficou em RECUPERAÇÃO!!!')
# else:
#     print('Infelizmente! Você REPROVOU!!!')


a = 0
resultado = 'neutro'
if a > 0:
    resultado = 'positivo'
elif a < 0:
    resultado = 'negativo'
a = resultado

#
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('A Media é: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada!!!')


# a = int(input('Entre com um valor: '))
# b = int(input('Entre com um valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
#
# if resto_a == 0 or not resto_b == 0:
#     print('Foi digitado um número é PAR!!!')
# else:
#     print('Nenhum número PAR foi digitado!!!')


# a = input('Digite o Primeiro Valor: ')
# b = input('Digite o Segundo Valor: ')
# c = input('Digite o Terceiro Valor: ')
#
# if a > b and a > c:
#     print('O maior número é: {}'.format(a))
# elif b > a and b > c:
#     print('O maior valor é: {}'.format(b))
# else:
#     print('O maior valor é: {}'.format(c))
# print('Final do Programa!')