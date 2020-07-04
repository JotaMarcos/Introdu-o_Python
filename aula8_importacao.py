from aula7_televisao import Televisao
from aula7_calculadora1 import  Calculadora
from aula8_contador_letras import  contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
    print(calculadora.resto())

    lista = {'cachorro', 'gato', 'elefante'}
    total_letras = contador_letras(lista)
    print(f'Total de Letras por Palavra na Lista: {total_letras}')

    print(teste())

