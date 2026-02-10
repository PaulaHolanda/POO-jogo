class BasePlayer():
    nome: str
    vida: int
    dano: int

    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.dano = 20
    
    def __str__(self):
        return f"{self.nome} | {self.vida} HP"
    
    def atacar(self, alvo: BasePlayer):
        print(f"{self.nome} atacando {alvo.nome}")
        print(f"{alvo.nome} perdeu {self.dano} de vida")
        alvo.vida -= self.dano

class Jogador(BasePlayer):
    def __init__(self, nome):
        super().__init__(nome)

   

    def curar(self, cura):
        self.vida += cura

class Monstro(BasePlayer):
    def __init__(self, nome):
        super().__init__(nome)
        self.vida = 150

jogador1 = Jogador('Paula')
jogador2 = Jogador('Ana')

print(jogador1)
print(jogador2)

jogador1.atacar(jogador2)

print(jogador1)
print(jogador2)

monstro1 = Monstro("Kworgs")
monstro1 = Monstro("Args")


