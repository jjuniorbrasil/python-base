class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f"Olá, me chamo {self.nome} e tenho {self.idade} anos.")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

    def apresentacao(self):
        print(f"Olá, me chamo {self.nome} e tenho {self.idade} anos. Trabalho como {self.cargo} e recebo {self.salario} reais por mês.")
        
class Conta:
    def __init__(self, nomeBanco, cod, agencia):
        self.nomeBanco = nomeBanco
        self.cod = cod
        self.agencia = agencia
        self.saldo = 0

class FormaGeometrica:
    def __init__(self, lado, area, perimetro):
        self.lado = lado
        self.area = area
        self.perimetro = perimetro

class Veiculo:
    def __init__(self, marca):
        self._marca = marca

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, novamarca):
        self._marca = novamarca

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca)
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def MarcaCarro(self):
        return super().marca

class Pais:
    def __init__(self, nome, are, pop):
        self.nome = nome
        self.are = are
        self.pop = pop
        self.dens = pop/are

class Cidade:
    def __init__(self, nome, nhab, Pais):
        self.nome = nome
        self.nhab = nhab
        self.pais = Pais

def apresentacao_pessoa(pessoa):
    pessoa.apresentacao()

# INSTANCIAÇÃO

p = Pessoa('Carlos', 26)
c = Conta('Bradesco', 29600, 243)
f = FormaGeometrica(5, 500, 20)
br = Pais('Brasil', 320423.23, 70239523)

print(p.nome)
print(c.nomeBanco)
print(f.lado)

# AGREGAÇÃO

cid = Cidade('São Luís', 700000, br)
print(cid.pais.nome)
print(cid.nome)

# ENCAPSULAMENTO

car = Carro('Peugeot', 'Mustang', 'Azul', 1999)
print(car.MarcaCarro())
car.marca = 'Chevrolet'
print(car.MarcaCarro())

# POLIMORFISMO

func = Funcionario('José', 26, 'Vendedor', 2800.00)

apresentacao_pessoa(p)
apresentacao_pessoa(func)

