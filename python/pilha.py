
from array import array


class PilhaCheiaErro(Exception):
    pass


class PilhaVaziaErro(Exception):
    pass


class TipoErro(Exception):
    pass


class Pilha:
    def __init__(self, tipo, capacidade):
        # Validação do tipo
        if tipo not in (int, float, str):
            raise TipoErro(
                "A pilha só pode armazenar int, float ou str."
            )

        # Validação da capacidade
        if not isinstance(capacidade, int) or capacidade <= 0:
            raise ValueError(
                "A capacidade deve ser um inteiro positivo."
            )

        self.tipo = tipo
        self.capacidade = capacidade

       
        if tipo is int:
            self.dados = array('i')
        elif tipo is float:
            self.dados = array('d')
        else:
            self.dados = []


    def empilha(self, dado):
        # Primeiro verifica se o tipo do dado é válido
        if type(dado) is not self.tipo:
            raise TipoErro(
                "O dado possui tipo incompatível com a pilha."
            )

        # Depois verifica se há espaço
        if self.pilha_esta_cheia():
            raise PilhaCheiaErro(
                "A pilha está cheia."
            )

        self.dados.append(dado)


    def desempilha(self):
        if self.pilha_esta_vazia():
            raise PilhaVaziaErro(
                "A pilha está vazia."
            )

        return self.dados.pop()


    def pilha_esta_vazia(self):
        return not self.dados


    def pilha_esta_cheia(self):
        return len(self.dados) >= self.capacidade


    def troca(self):
        if self.tamanho() < 2:
            raise PilhaVaziaErro(
                "É necessário ter pelo menos dois elementos para trocar."
            )

        self.dados[-1], self.dados[-2] = (
            self.dados[-2],
            self.dados[-1]
        )


    def tamanho(self):
        return len(self.dados)
