class Navio:
    quantidade = 0
    def __init__(self, nome, tamanho, time, hp, atk):
        Navio.quantidade += 1
        self.id = Navio.quantidade
        self.nome = nome
        self.tamanho = tamanho
        self.time = time
        self.hp = hp
        self.atk = atk
        
    def causar_dano(self, alvo):
        if alvo.hp > 0 and alvo.time != self.time:
            alvo.hp -= self.atk
            if alvo.hp < 0:
                print(f'A unidade {alvo.nome} (ID: {alvo.id}) do time {alvo.time} foi destruída!')
                alvo.hp = 0
        else:
            print('Não é possível atacar!')
        
'''Duas frotas, dispostas nos times Azul e Vermelho, e compostas por 2 Porta-Aviões, 4 Cruzadores/Destroyers, 8 Fragatas, 8 Corvetas, 12 Barcos de Ataque Rápido, 6 Navios-Patrulha e 10 Submarinos;'''

class PortaAvioes(Navio):
    def __init__(self, time):
        super().__init__('Porta Aviões', 10, time, 100, 10)
        self.avioes = 10
        
    def lancar_aviao(self, alvo):
        if self.avioes > 0:
            print('Avião lançado!')
            self.avioes -= 1
            self.causar_dano(alvo)
        else:
            print('Sem aviões!')

class Cruzador(Navio):
    def __init__(self, time):
        super().__init__('Cruzador', 8, time, 60, 5)
        
class Fragata(Navio):
    def __init__(self, time):
        super().__init__('Fragata', 5, time, 50, 10)
        
class Corveta(Navio):
    def __init__(self, time):
        super().__init__('Corveta', 4, time, 5, 10)
        
class AtRapido(Navio):
    def __init__(self, time):
        super().__init__('Barco de Ataque Rápido', 3, time, 1, 25)
        
class Patrulha(Navio):
    def __init__(self, time):
        super().__init__('Navio Patrulha', 2, time, 10, 20)
        
class Submarino(Navio):
    def __init__(self, time):
        super().__init__('Submarino', 1, time, 1, 5)
        
        # FROTA VERMELHA
        
paVermelho = [PortaAvioes('Vermelho'), PortaAvioes('Vermelho')]

crVermelho = [Cruzador('Vermelho'), Cruzador('Vermelho'), Cruzador('Vermelho'), Cruzador('Vermelho')]

frVermelho = [Fragata('Vermelho'),Fragata('Vermelho'),Fragata('Vermelho'),Fragata('Vermelho'),
              Fragata('Vermelho'),Fragata('Vermelho'),Fragata('Vermelho'),Fragata('Vermelho')]

corVermelho = [Corveta('Vermelho'),Corveta('Vermelho'),Corveta('Vermelho'),Corveta('Vermelho'),
              Corveta('Vermelho'),Corveta('Vermelho'),Corveta('Vermelho'),Corveta('Vermelho')]

atrVermelho = [AtRapido('Vermelho'),AtRapido('Vermelho'),AtRapido('Vermelho'),AtRapido('Vermelho'),
              AtRapido('Vermelho'),AtRapido('Vermelho'),AtRapido('Vermelho'),AtRapido('Vermelho'),
              AtRapido('Vermelho'),AtRapido('Vermelho'),AtRapido('Vermelho'),AtRapido('Vermelho')]

nvpVermelho = [Patrulha('Vermelho'),Patrulha('Vermelho'),Patrulha('Vermelho'),Patrulha('Vermelho'),
              Patrulha('Vermelho'),Patrulha('Vermelho')]

subVermelho = [Submarino('Vermelho'),Submarino('Vermelho'),Submarino('Vermelho'),Submarino      ('Vermelho'), Submarino('Vermelho'),Submarino('Vermelho'),Submarino('Vermelho'),Submarino('Vermelho'), Submarino('Vermelho'), Submarino('Vermelho')]

        # FROTA AZUL
        
paAzul = [PortaAvioes('Azul'), PortaAvioes('Azul')]

crAzul = [Cruzador('Azul'), Cruzador('Azul'), Cruzador('Azul'), Cruzador('Azul')]

frAzul = [Fragata('Azul'),Fragata('Azul'),Fragata('Azul'),Fragata('Azul'),
              Fragata('Azul'),Fragata('Azul'),Fragata('Azul'),Fragata('Azul')]

corAzul = [Corveta('Azul'),Corveta('Azul'),Corveta('Azul'),Corveta('Azul'),
              Corveta('Azul'),Corveta('Azul'),Corveta('Azul'),Corveta('Azul')]

atrAzul = [AtRapido('Azul'),AtRapido('Azul'),AtRapido('Azul'),AtRapido('Azul'),
              AtRapido('Azul'),AtRapido('Azul'),AtRapido('Azul'),AtRapido('Azul'),
              AtRapido('Azul'),AtRapido('Azul'),AtRapido('Azul'),AtRapido('Azul')]

nvpAzul = [Patrulha('Azul'),Patrulha('Azul'),Patrulha('Azul'),Patrulha('Azul'),
              Patrulha('Azul'),Patrulha('Azul')]

subAzul = [Submarino('Azul'),Submarino('Azul'),Submarino('Azul'),Submarino('Azul'), Submarino('Azul'),Submarino('Azul'),Submarino('Azul'),Submarino('Azul'), Submarino('Azul'), Submarino('Azul')]

paVermelho[0].lancar_aviao(subAzul[9])
paVermelho[0].lancar_aviao(subAzul[8])
paVermelho[0].lancar_aviao(paAzul[1])
paVermelho[0].lancar_aviao(atrAzul[5])
paVermelho[0].lancar_aviao(corAzul[5])
paVermelho[0].lancar_aviao(corAzul[5])
        