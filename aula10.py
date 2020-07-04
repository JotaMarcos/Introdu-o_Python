from datetime import date, time, datetime, timedelta
# data_atual = date.today()
# print(f'A Data Atual é:', data_atual.strftime('%d/%m/%y'))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(f'A data atual é: {data_atual}')
    print(f'A data atual é:', (data_atual.strftime('%d/%m/%Y %H:%M:%S')))
    print(data_atual.strftime('%c'))
    print(f'O Dia: {data_atual.day}')
    print(f'O Mês: {data_atual.month}')
    print(f'O Ano: {data_atual.year}')
    print(f'A Hora: {data_atual.hour}')
    print(f'O Minuto: {data_atual.minute}')
    print(f'O Secundo: {data_atual.second}')
    print(f'Data Atual:', data_atual.date().strftime('%d/%m/%Y'))
    print(f'Dia da Semana: {data_atual.weekday()}')
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(f'Dia da Semana: {tupla[data_atual.weekday()]}')
    data_criada = datetime(2020, 7, 2, 21, 1, 35)
    print(f'A Data Criada é: {data_criada}')
    print(f'A Data Criada é:', data_criada.strftime('%c'))
    print(f'A Data Criada é:', data_criada.strftime(''))

    data_string = '02/07/2020 21:17:53'
    print(f'A Data em String: {data_string}')
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(f'A Data Convertida é: {data_convertida}')

    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15 )
    print(f'A Nova Data é:', nova_data.strftime('%d/%m/%Y %H:%M:%S'))

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(f'O Horário Atual é: {horario}')
    # print(type(horario))
    horario_str = horario.strftime('%H:%M:%S')
    print(f'O Horário Atual é: {horario_str}')
    print(type(horario_str))

if __name__ == '__main__':
    # trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()

