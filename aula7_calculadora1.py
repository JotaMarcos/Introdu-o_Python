class Calculadora:
    def __init__(self, num1, num2):
            self.valor_a = num1
            self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b;

    # print(f'O Valor da Soma é: {soma(1, 3)}')
    # print(f'O Valor da Soma é: {soma(3, 4)}')

    def subtracao(self):
        return self.valor_a - self.valor_b;

    # print(f'O Valor da Subtração é: {subtracao(10, 2)}')
    # print(f'O Valor da Subtração é: {subtracao(7, 4)}')



    def multiplicacao(self):
        return self.valor_a * self.valor_b;

    # print(f'O Valor da Multiplicação é: {multiplicacao(5, 3)}')
    # print(f'O Valor da Multiplicação é: {multiplicacao(9, 4)}')


    def divisao(self):
        return self.valor_a / self.valor_b;

    # print(f'O Valor da Divisão é: {divisao(20, 3)}')
    # print(f'O Valor da Divisão é: {divisao(33, 4)}')

    def resto(self):
        return self.valor_a % self.valor_b;

    # print(f'O Valor da Resto da Divisão é: {resto(22, 3)}')
    # print(f'O Valor da Resto da Divisão é: {resto(35, 4)}')
if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(f'Valor: {calculadora.valor_a}')
    print(f'Valor: {calculadora.valor_b}')
    print(f'============================================================')
    print(f'O Primeiro Valor da Soma é: {calculadora.soma()}')
    print(f'O Segundo Valor da Subtração é: {calculadora.subtracao()}')
    print(f'O Valor da Multiplicação é: {calculadora.multiplicacao()}')
    print(f'O Valor da Divisão é: {calculadora.divisao()}')
    print(f'O Valor do Resto é: {calculadora.resto()}')
    print(f'============================================================')