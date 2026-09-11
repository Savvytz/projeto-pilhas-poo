
"""
Torre de Hanoi - solucao recursiva, com pilha baseada em array.
Refatorado a partir do codigo bruto gerado pela IA (que continha um bug de
base case: o caso n==1 nao tinha 'return', fazendo com que a recursao
continuasse e executasse chamadas extras desnecessarias).
"""
import sys

class Pilha:

    def __init__(self, capacidade):
        if capacidade <= 0:
            raise ValueError("Capacidade da pilha deve ser positiva.")
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.topo = -1

    def empilha(self, disco):
        if self.pilha_cheia():
            raise OverflowError("PilhaCheiaErro: capacidade maxima do pino atingida.")
        if not self.pilha_vazia() and self.dados[self.topo] < disco:
            raise ValueError(
                f"MovimentoInvalido: nao e possivel colocar o disco {disco} "
                f"sobre o disco menor {self.dados[self.topo]}."
            )
        self.topo += 1
        self.dados[self.topo] = disco

    def desempilha(self):
        if self.pilha_vazia():
            raise IndexError("PilhaVaziaErro: nao ha disco para remover.")
        item = self.dados[self.topo]
        self.dados[self.topo] = None
        self.topo -= 1
        return item

    def topo_valor(self):
        if self.pilha_vazia():
            return None
        return self.dados[self.topo]

    def pilha_vazia(self):
        return self.topo == -1

    def pilha_cheia(self):
        return self.topo == self.capacidade - 1

    def tamanho(self):
        return self.topo + 1


def exibir_hanoi(pinos, n, total_movimentos):
    linhas_saida = [f"--- Movimentos acumulados: {total_movimentos} ---"]
    for nivel in range(n - 1, -1, -1):
        celulas = []
        for pino in pinos:
            if nivel < pino.tamanho():
                disco = pino.dados[nivel]
                largura = disco * 2 + 1
                bloco = "#" * largura
                espacos = " " * (n - disco)
                celulas.append(f"{espacos}{bloco}{espacos}")
            else:
                espacos = " " * n
                celulas.append(f"{espacos}|{espacos}")
        linhas_saida.append("   ".join(celulas))
    base = "-" * (2 * n + 1)
    linhas_saida.append(f"{base}   {base}   {base}")
    linhas_saida.append("     Pino A        Pino B        Pino C    ")
    linhas_saida.append("=" * (6 * n + 12))
    sys.stdout.write("\n".join(linhas_saida) + "\n")


def hanoi(n, origem, destino, auxiliar, pinos, M, estado, pausar=True):
    if n == 0:
        return  # caso base correto: nao ha disco a mover
    hanoi(n - 1, origem, auxiliar, destino, pinos, M, estado, pausar)

    disco = origem.desempilha()
    destino.empilha(disco)
    estado["movimentos_bloco"] += 1
    estado["total"] += 1

    if M > 0 and estado["movimentos_bloco"] >= M:
        exibir_hanoi(pinos, estado["n_discos"], estado["total"])
        if pausar:
            input("Pressione [ENTER] para continuar...")
        estado["movimentos_bloco"] = 0

    hanoi(n - 1, auxiliar, destino, origem, pinos, M, estado, pausar)


def ler_inteiro(mensagem, minimo=None, maximo=None, padrao=None):
    while True:
        bruto = input(mensagem).strip()
        if bruto == "" and padrao is not None:
            return padrao
        try:
            valor = int(bruto)
        except ValueError:
            print("Entrada invalida: digite um numero inteiro.")
            continue
        if minimo is not None and valor < minimo:
            print(f"Valor deve ser >= {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"Valor deve ser <= {maximo}.")
            continue
        return valor


def main():
    # N limitado a 25 na entrada interativa: 2^25-1 ~ 33 milhoes de movimentos,
    # ja impraticavel para exibir; evita que o usuario trave o programa sem querer.
    n = ler_inteiro("Quantidade de discos (N, 1-25): ", minimo=1, maximo=25)
    M = ler_inteiro("Movimentacoes M entre exibicoes (padrao 1, 0 = sem paradas): ",
                     minimo=0, padrao=1)

    pino_a = Pilha(n)
    pino_b = Pilha(n)
    pino_c = Pilha(n)
    for disco in range(n, 0, -1):
        pino_a.empilha(disco)
    pinos = [pino_a, pino_b, pino_c]

    print("--- Formacao inicial ---")
    exibir_hanoi(pinos, n, 0)
    if M > 0:
        input("Pressione [ENTER] para iniciar...")

    estado = {"movimentos_bloco": 0, "total": 0, "n_discos": n}
    try:
        hanoi(n, pino_a, pino_c, pino_b, pinos, M, estado)
    except (OverflowError, ValueError, IndexError) as e:
        print(f"Erro durante a execucao: {e}")
        return

    print("--- Formacao final ---")
    exibir_hanoi(pinos, n, estado["total"])
    print(f"Numero total de movimentos: {estado['total']} (esperado: {2**n - 1})")


if __name__ == "__main__":
    main()
