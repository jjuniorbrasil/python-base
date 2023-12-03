class Navio:
    def __init__(self, nome, tamanho, time):
        self.nome = nome
        self.tamanho = tamanho
        self.time = time
        
'''Duas frotas, dispostas nos times Azul e Vermelho, e compostas por 2 Porta-Aviões, 4 Cruzadores/Destroyers, 8 Fragatas, 8 Corvetas, 12 Barcos de Ataque Rápido, 6 Navios-Patrulha e 10 Submarinos;'''

class PortaAvioes(Navio):
    def __init__(self, time):
        super().__init__('Porta Aviões', 10, time)
        self.avioes = 10
        
    def lancar_aviao(self):
        if self.avioes > 0:
            print('Avião lançado!')
            self.avioes -= 1
        else:
            print('Sem aviões!')

class Cruzador(Navio):
    def __init__(self, time):
        super().__init__('Cruzador', 8, time)
        
class Fragata(Navio):
    def __init__(self, time):
        super().__init__('Fragata', 5, time)
        
class Corveta(Navio):
    def __init__(self, time):
        super().__init__('Corveta', 4, time)
        
class AtRapido(Navio):
    def __init__(self, time):
        super().__init__('Barco de Ataque Rápido', 3, time)
        
class Patrulha(Navio):
    def __init__(self, time):
        super().__init__('Navio Patrulha', 2, time)
        
class Submarino(Navio):
    def __init__(self, time):
        super().__init__('Submarino', 1, time)