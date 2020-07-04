class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1
print(__name__)
if __name__ == '__main__':

    televisao = Televisao()
    print(f'=========================================================')
    print(f'A Televisão está Ligada: {televisao.ligada}')
    televisao.power()
    print(f'A Televisão está Ligada: {televisao.ligada}')
    televisao.power()
    print(f'A Televisão está Ligada: {televisao.ligada}')
    print(f'O Canal: {televisao.canal}')
    televisao.power()
    print(f'A Televisão está Ligada: {televisao.ligada}')
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print(f'O Canal: {televisao.canal}')
    televisao.diminui_canal()
    print(f'O Canal: {televisao.canal}')
    print(f'=========================================================')



