import datetime

class Sala:
    def __init__(self, nome, tipo, num_assentos):
        self.nome = nome
        self.tipo = tipo
        self.num_assentos = num_assentos
        self.reservas = []

    def adicionar_reserva(self, inicio, fim):
        self.reservas.append((inicio, fim))

    def esta_disponivel(self, inicio, fim):
        for reserva in self.reservas:
            if (inicio >= reserva[0] and inicio < reserva[1]) or (fim > reserva[0] and fim <= reserva[1]):
                return False
        return True

    def imprimir_reservas(self):
        for reserva in self.reservas:
            print(f'{self.nome}: reservada de {reserva[0]} até {reserva[1]}')

    def imprimir_disponibilidades(self):
        if not self.reservas:
            print(f'{self.nome} está disponível o dia todo.')
        else:
            self.reservas.sort(key=lambda x: x[0])
            print(f'{self.nome} está disponível até {self.reservas[0][0]}.')
            for i in range(len(self.reservas) - 1):
                print(f'{self.nome} está disponível a partir de {self.reservas[i][1]} até {self.reservas[i+1][0]}.')
            print(f'{self.nome} está disponível a partir de {self.reservas[-1][1]}.')

def salas_disponiveis(salas, inicio, fim):
    disponiveis = []
    for sala in salas:
        if sala.esta_disponivel(inicio, fim):
            disponiveis.append(f'{sala.nome} - {sala.tipo}')
    return disponiveis

def salas_reservadas(salas):
    reservadas = []
    for sala in salas:
        if sala.reservas:
            reservadas.append(f'{sala.nome} - {sala.tipo}')
    return reservadas
