class Peca:
    def __init__(self, nome, cor, pos, ataque, movimento):
        self.nome = nome
        self.cor = cor
        self.pos = pos
        self.ataque = ataque
        self.movimento = movimento
        self.movimentos = 0
        
    def movimentar_peca(self):
        self.movimentos += 1
        print(f'Movimentando peça em {self.movimento}.')
        
    def atacar(self):
        print(f'Atacando em {self.ataque}')

class Peao(Peca):
    def __init__(self, cor, pos):
        super().__init__('Peão', cor, pos, 'diagonal', 'linha reta')
    
    def movimentar_peca(self, casas=1):
        super().movimentar_peca()
        if casas > 1 and self.movimentos == 1:
            print('(duas casas)')
    
class Torre(Peca):
    def __init__(self, cor, pos):
        super().__init__('Torre', cor, pos, 'horizontal e vertical', 'linha reta')

class Cavalo(Peca):
    def __init__(self, cor, pos):
        super().__init__('Cavalo', cor, pos, 'L', 'em L')

class Bispo(Peca):
    def __init__(self, cor, pos):
        super().__init__('Bispo', cor, pos, 'diagonal', 'em diagonal')

class Rainha(Peca):
    def __init__(self, cor, pos):
        super().__init__('Rainha', cor, pos, 'horizontal, vertical e diagonal', 'linha reta e diagonal')

class Rei(Peca):
    def __init__(self, cor, pos):
        super().__init__('Rei', cor, pos, 'horizontal, vertical e diagonal', 'uma casa em qualquer direção')


p = Peao('Preto', (1, 1))
p.movimentar_peca(2)
p.movimentar_peca(2)
p.atacar()