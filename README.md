# Sistema de Reserva de Salas

Este projeto é um sistema simples de reserva de salas, implementado em Python.

## Descrição

O sistema permite criar salas com diferentes tipos e números de assentos. Cada sala pode ter várias reservas, e o sistema pode verificar se uma sala está disponível para um determinado intervalo de tempo.

## Uso

Para usar o sistema, primeiro crie uma instância da classe `Sala`, especificando o nome, o tipo e o número de assentos da sala. Em seguida, use o método `adicionar_reserva` para adicionar reservas à sala.

Para verificar a disponibilidade de uma sala, use o método `esta_disponivel`, passando o início e o fim do intervalo de tempo desejado.

Para obter uma lista de todas as salas disponíveis para um determinado intervalo de tempo, use a função `salas_disponiveis`, passando a lista de salas e o início e o fim do intervalo de tempo.

Para obter uma lista de todas as salas que têm reservas, use a função `salas_reservadas`, passando a lista de salas.

## Exemplo

```python
sala1 = Sala('Sala 1', 'Reunião', 10)
sala1.adicionar_reserva(datetime.datetime(2022, 12, 1, 9, 0), datetime.datetime(2022, 12, 1, 11, 0))

sala2 = Sala('Sala 2', 'Palestra', 20)
sala2.adicionar_reserva(datetime.datetime(2022, 12, 1, 13, 0), datetime.datetime(2022, 12, 1, 15, 0))

sala3 = Sala('Sala 3', 'Apresentação', 30)
sala3.adicionar_reserva(datetime.datetime(2022, 12, 1, 16, 0), datetime.datetime(2022, 12, 1, 18, 0))

salas = [sala1, sala2, sala3]

inicio = datetime.datetime(2022, 12, 1, 10, 0)
fim = datetime.datetime(2022, 12, 1, 12, 0)
disponiveis = salas_disponiveis(salas, inicio, fim)

if disponiveis:
    print('Salas disponíveis:')
    for sala in disponiveis:
        print(sala)
else:
    print('Nenhuma sala disponível para o intervalo de tempo fornecido.')

reservadas = salas_reservadas(salas)

if reservadas:
    print('Salas reservadas:')
    for sala in reservadas:
        print(sala)
else:
    print('Nenhuma sala foi reservada.')
