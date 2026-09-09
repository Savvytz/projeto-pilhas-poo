
class PilhaCheiaErro(Exception):
    pass

class PilhaVaziaErro(Exception):
    pass

class TipoErro(Exception):
    pass


class Pilha:
    def __init__(self, tipo, capacidade):

        if tipo not in (int, float, str):
            raise TipoErro("A pilha só pode armazenar int, float ou str.")

        self.tipo = tipo
        self.capacidade = capacidade

        if tipo == int:
            self.dados = array('i')
        elif tipo == float:
            self.dados = array('d')
        else:
            self.dados = []


    def empilha(self, dado):
        """Empilha um dado no topo da pilha."""

        if self.pilha_esta_cheia():
            raise PilhaCheiaErro("PilhaCheiaErro")

        # Verifica se o dado possui o tipo correto
        if type(dado) is not self.tipo:
            raise TipoErro("TipoErro")

        self.dados.append(dado)


    def desempilha(self):
        if self.pilha_esta_vazia():
            raise PilhaVaziaErro("PilhaVaziaErro")
        return self.dados.pop()

    def pilha_esta_vazia(self):
        return len(self.dados) == 0


    def pilha_esta_cheia(self):
        return len(self.dados) == self.capacidade


    def troca(self):
        if self.tamanho() < 2:
            raise PilhaVaziaErro(
                "É necessário ter pelo menos dois elementos para trocar."
            )
        self.dados[-1], self.dados[-2] = self.dados[-2], self.dados[-1]

    def tamanho(self):
        return len(self.dados)sse Array da biblioteca padrão
