class Tabuleiro:
    def __init__(self, cor1, cor2):
        self.cor = cor1
        self.cor2 = cor2

class TabuleiroXadrez(Tabuleiro):
    def __init__(self, cor1, cor2):
        super().__init__(cor1, cor2)
        self.tamanho = 64

class TabuleiroBatalhaNaval(Tabuleiro):
    def __init__(self, cor1, cor2):
        super().__init__(cor1, cor2)
        self.tamanho = 100

class Peca:
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro

class PecaXadrez(Peca):
    def __init__(self, tabuleiro, cor, movimento, ataque):
        super().__init__(self, tabuleiro)
        self.cor = cor
        self.movimento = movimento
        self.ataque = ataque

class Peao(PecaXadrez):
    def __init__(self, tabuleiro, cor):
        super().__init__(self, tabuleiro, cor, 'Uma casa por vez, em linha reta', 'Diagonal')
        self.nome = 'Peao'

class Bispo(PecaXadrez):
    def __init__(self, tabuleiro, cor):
        super().__init__(self, tabuleiro, cor, 'Diagonal', 'Diagonal')
        self.nome = 'Bispo'

class Torre(PecaXadrez):
    def __init__(self, tabuleiro, cor):
        super().__init__(self, tabuleiro, cor, 'Linha reta', 'Linha reta')
        self.nome = 'Torre'

class Cavalo(PecaXadrez):
    def __init__(self, tabuleiro, cor):
        super().__init__(self, tabuleiro, cor, 'Em L', 'Em L')

class Rei(PecaXadrez):
    def __init__(self, tabuleiro, cor):
        super().__init__(self, tabuleiro, cor, 'Em todas as direções', 'De todas as direções')

class Rainha(PecaXadrez):
    def __init__(self, tabuleiro, cor):
        super().__init__(self, tabuleiro, cor, 'Em todas as direções, uma casa por vez', 'De todas as direções')

class PecaBatalhaNaval(Peca):
    def __init__(self, tabuleiro):
        super().__init__(self, tabuleiro)

class PortaAvioes(PecaBatalhaNaval):
    def __init__(self, tabuleiro):
        super().__init__(self, tabuleiro)
        self.nome = 'Porta Aviões'
        self.tamanho = 5