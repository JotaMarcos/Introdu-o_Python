import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/JM/PycharmProjects/teste.txt'
    arquivo = open(diretorio, f'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, f'a')
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, f'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, f'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(f'A sua Média é: {media(lista_notas)}')
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):

    shutil.copy(nome_arquivo, 'C:/Users/JM/PycharmProjects/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/JM/PycharmProjects/')


 if __name__ == '__main__':
      move_arquivo('Notas.txt')
    # copia_arquivo('Notas.txt')
     lista_media = media_notas('Notas.txt')
     print(f'A Lista das Médias é: {lista_media}')
    # escrever_arquivo(f'Minha Primeira Linha.\n')
    aluno = f'\nElza, 10, 8, 7, 5\n'
    # atualizar_arquivo(f'Notas.txt', aluno)
    # ler_arquivo(f'teste.txt')



# import shutil
texto = 'Primeira linha\nSegunda linha'
# file = open('arquivo.txt', 'w')
# file.write(texto)
# file.close()
shutil.copy('arquivo.txt', 'backup.txt')
texto_split = texto.split('\n')

 media = lambda notas: sum([int(i) for i in notas]) / 4

