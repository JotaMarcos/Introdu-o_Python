
lista = [1, 10]
arquivo = open('C:/Users/JM/PycharmProjects/app_python/teste.txt', 'r')
try:

    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]

    print(f'Fechando o arquivo!!!')


# except BaseException as ex:
#     print(f'Erro desconhecido. Erro: {ex}')
except ZeroDivisionError:
    print(f'Não é possível realizar um divisão por 0!!! ')
except ArithmeticError:
    print(f'Houve um erro ao realizar uma operação aritmética!!!')
except IndexError:
    print(f'Erro ao acessar um índice inválido da lista!!! ')
except Exception as ex:
    print(f'Erro desconhecido!!! Erro: {ex}')
else:
    print(f'Executa quando não ocorre uma exceção!!!')
finally:
    print(f'Sempre excuta!!!')
    print(f'Fechando o arquivo!!!')
    arquivo.close()

