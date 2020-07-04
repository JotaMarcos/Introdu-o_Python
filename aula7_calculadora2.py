class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b;

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b;

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b;

    def divisao(self, valor_a, valor_b):
        return valor_a /valor_b;

    def resto(self, valor_a, valor_b):
        return valor_a % valor_b;

calculadora = Calculadora()

print(f'============================================================')
print(f'O Primeiro Valor da Soma é: {calculadora.soma(7, 5)}')
print(f'O Segundo Valor da Subtração é: {calculadora.subtracao(5, 3)}')
print(f'O Valor da Multiplicação é: {calculadora.multiplicacao(100, 2)}')
print(f'O Valor da Divisão é: {calculadora.divisao(10, 5)}')
print(f'O Valor do Resto é: {calculadora.resto(15,4)}')
print(f'============================================================')