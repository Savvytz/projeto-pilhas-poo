"""
Flood Fill - versoes recursiva e iterativa (pilha baseada em array)
Refatorado a partir do codigo bruto gerado pela IA.
"""
import sys
import os


# ---------------------------------------------------------------------------
# Estrutura de dados: Pilha baseada em array (nao usa list.append/pop "cru")
# ---------------------------------------------------------------------------
class Pilha:
    """Pilha (stack) baseada em array com capacidade dinamica (dobra quando cheia).
    Todas as operacoes de topo sao O(1) amortizado."""

    def __init__(self, capacidade_inicial=64):
        if capacidade_inicial <= 0:
            raise ValueError("Capacidade inicial da pilha deve ser positiva.")
        self.capacidade = capacidade_inicial
        self.dados = [None] * self.capacidade
        self.topo = -1  # indice do elemento no topo; -1 = vazia

    def empilha(self, item):
        if self.pilha_cheia():
            self._redimensiona(self.capacidade * 2)
        self.topo += 1
        self.dados[self.topo] = item

    def desempilha(self):
        if self.pilha_vazia():
            raise IndexError("PilhaVaziaErro: tentativa de desempilhar pilha vazia.")
        item = self.dados[self.topo]
        self.dados[self.topo] = None
        self.topo -= 1
        return item

    def pilha_vazia(self):
        return self.topo == -1

    def pilha_cheia(self):
        return self.topo == self.capacidade - 1

    def tamanho(self):
        return self.topo + 1

    def _redimensiona(self, nova_capacidade):
        nova = [None] * nova_capacidade
        for i in range(self.tamanho()):
            nova[i] = self.dados[i]
        self.dados = nova
        self.capacidade = nova_capacidade


# ---------------------------------------------------------------------------
# Leitura / exibicao da matriz
# ---------------------------------------------------------------------------
def ler_matriz(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            linhas = [list(l.rstrip("\n")) for l in f if l.strip("\n") != ""]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{caminho}' nao encontrado.")
    except OSError as e:
        raise OSError(f"Erro ao ler o arquivo '{caminho}': {e}")

    if not linhas:
        raise ValueError("Arquivo de matriz esta vazio.")

    largura = len(linhas[0])
    for i, l in enumerate(linhas):
        if len(l) != largura:
            raise ValueError(
                f"Matriz invalida: linha {i} tem {len(l)} colunas, esperado {largura}."
            )
    return linhas


def localizar_posicao(matriz, caractere="X"):
    for i, linha in enumerate(matriz):
        for j, c in enumerate(linha):
            if c == caractere:
                return i, j
    return None


PALETA_CORES_ANSI = {
    "1": "\033[48;5;255m",  # fundo / area nao pintada -> branco
    "X": "\033[48;5;196m",  # posicao inicial do clique -> vermelho
    "S": "\033[48;5;46m",   # saida do labirinto -> verde
    "0": "\033[48;5;238m",  # cor de preenchimento padrao -> cinza escuro
    "2": "\033[48;5;27m",   # azul
    "3": "\033[48;5;208m",  # laranja
    "4": "\033[48;5;226m",  # amarelo
    "5": "\033[48;5;93m",   # roxo
    "6": "\033[48;5;34m",   # verde
    "7": "\033[48;5;201m",  # rosa
}
RESET_ANSI = "\033[0m"


# Uso de escrita em buffer (uma unica chamada de escrita por matriz) em vez de
# um print() por celula/linha -> elimina o gargalo de I/O apontado na revisao.
# modo="cor": renderiza a matriz como um verdadeiro bitmap (matriz de pixels
# coloridos no terminal, via codigos ANSI), no estilo do balde de tinta do
# MS-Paint. modo="ascii": fallback em texto puro para terminais sem cor.
def exibir_matriz(matriz, modo="cor"):
    partes = []
    if modo == "cor":
        for linha in matriz:
            pixels = []
            for c in linha:
                cor = PALETA_CORES_ANSI.get(c, "\033[48;5;0m")
                pixels.append(f"{cor}  {RESET_ANSI}")
            partes.append("".join(pixels))
    elif modo == "ascii":
        for linha in matriz:
            partes.append("".join("#" if c not in ("1",) else " " for c in linha))
        partes.append("-" * len(matriz[0]))
    else:
        for linha in matriz:
            partes.append("".join(linha))
    sys.stdout.write("\n".join(partes) + "\n")


def listar_cores_disponiveis():
    nomes = {"0": "cinza (padrao)", "2": "azul", "3": "laranja", "4": "amarelo",
             "5": "roxo", "6": "verde", "7": "rosa"}
    return ", ".join(f"{d}={nome}" for d, nome in nomes.items())


def matriz_para_texto(matriz):
    return "\n".join("".join(l) for l in matriz)


# ---------------------------------------------------------------------------
# Flood fill recursivo (com limite de profundidade seguro)
# ---------------------------------------------------------------------------
def flood_fill_recursivo(matriz, linha, coluna, alvo, substituto, P=0, pausar=True):
    n_linhas, n_col = len(matriz), len(matriz[0])
    contador = [0]
    passos_bloco = [0]

    # Ajusta o limite de recursao para matrizes grandes; Python nao faz TCO,
    # entao uma matriz muito grande pode estourar o limite padrao (1000).
    limite_necessario = n_linhas * n_col + 100
    limite_atual = sys.getrecursionlimit()
    if limite_necessario > limite_atual:
        sys.setrecursionlimit(limite_necessario)

    def _passo(l, c):
        if l < 0 or l >= n_linhas or c < 0 or c >= n_col:
            return
        if matriz[l][c] != alvo:
            return
        matriz[l][c] = substituto
        contador[0] += 1
        passos_bloco[0] += 1
        if P > 0 and passos_bloco[0] >= P:
            exibir_matriz(matriz)
            if pausar:
                input("Pressione [ENTER] para continuar...")
            passos_bloco[0] = 0
        _passo(l - 1, c)
        _passo(l + 1, c)
        _passo(l, c - 1)
        _passo(l, c + 1)

    try:
        _passo(linha, coluna)
    except RecursionError:
        raise RecursionError(
            "Limite de recursao atingido. Use a versao iterativa (flood_fill_iterativo) "
            "para matrizes grandes."
        )
    return contador[0]


# ---------------------------------------------------------------------------
# Flood fill iterativo, usando a Pilha baseada em array (evita RecursionError
# e e mais eficiente para regioes grandes)
# ---------------------------------------------------------------------------
def flood_fill_iterativo(matriz, linha, coluna, alvo, substituto, P=0, pausar=True):
    n_linhas, n_col = len(matriz), len(matriz[0])
    pilha = Pilha(capacidade_inicial=64)
    pilha.empilha((linha, coluna))
    contador = 0
    passos_bloco = 0

    while not pilha.pilha_vazia():
        l, c = pilha.desempilha()
        if l < 0 or l >= n_linhas or c < 0 or c >= n_col:
            continue
        if matriz[l][c] != alvo:
            continue
        matriz[l][c] = substituto
        contador += 1
        passos_bloco += 1

        for dl, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nl, nc = l + dl, c + dc
            if 0 <= nl < n_linhas and 0 <= nc < n_col and matriz[nl][nc] == alvo:
                pilha.empilha((nl, nc))

        if P > 0 and passos_bloco >= P:
            exibir_matriz(matriz)
            if pausar:
                input("Pressione [ENTER] para continuar...")
            passos_bloco = 0

    return contador


# ---------------------------------------------------------------------------
# Variante "labirinto": para de preencher assim que encontra a saida 'S',
# devolvendo o caminho percorrido (para uso em robotica / navegacao).
# ---------------------------------------------------------------------------
def resolver_labirinto(matriz, linha_ini, coluna_ini, livre="1", parede="0", saida="S"):
    n_linhas, n_col = len(matriz), len(matriz[0])
    pilha = Pilha(capacidade_inicial=64)
    visitado = [[False] * n_col for _ in range(n_linhas)]
    pilha.empilha((linha_ini, coluna_ini, [(linha_ini, coluna_ini)]))
    visitado[linha_ini][coluna_ini] = True

    while not pilha.pilha_vazia():
        l, c, caminho = pilha.desempilha()
        if matriz[l][c] == saida:
            return caminho
        for dl, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nl, nc = l + dl, c + dc
            if 0 <= nl < n_linhas and 0 <= nc < n_col and not visitado[nl][nc]:
                if matriz[nl][nc] == livre or matriz[nl][nc] == saida:
                    visitado[nl][nc] = True
                    pilha.empilha((nl, nc, caminho + [(nl, nc)]))
    return None  # sem saida alcancavel


# ---------------------------------------------------------------------------
# Entrada validada
# ---------------------------------------------------------------------------
def ler_inteiro(mensagem, minimo=None, permitir_zero=True):
    while True:
        bruto = input(mensagem).strip()
        try:
            valor = int(bruto)
        except ValueError:
            print("Entrada invalida: digite um numero inteiro.")
            continue
        if minimo is not None and valor < minimo:
            print(f"Valor deve ser >= {minimo}.")
            continue
        if not permitir_zero and valor == 0:
            print("Valor nao pode ser zero.")
            continue
        return valor


def main():
    caminho = input("Caminho do arquivo com a matriz: ").strip() or "matriz.txt"
    try:
        matriz = ler_matriz(caminho)
    except (FileNotFoundError, ValueError, OSError) as e:
        print(f"Erro: {e}")
        return

    pos = localizar_posicao(matriz, "X")
    if pos is None:
        print("Nenhuma posicao inicial 'X' encontrada na matriz.")
        return
    linha_ini, coluna_ini = pos

    modo_exibicao = input("Exibicao [c]or (bitmap) ou [a]scii? (padrao c): ").strip().lower() or "c"
    if modo_exibicao not in ("c", "a"):
        modo_exibicao = "c"
    modo_exibicao = "cor" if modo_exibicao == "c" else "ascii"

    print("Matriz antes do preenchimento:")
    exibir_matriz(matriz, modo=modo_exibicao)

    versao = input("Versao [r]ecursiva ou [i]terativa? (padrao i): ").strip().lower() or "i"
    P = ler_inteiro("Quantidade P de passos entre exibicoes (0 = sem paradas): ", minimo=0)
    print(f"Cores de balde disponiveis: {listar_cores_disponiveis()}")
    cor_escolhida = input("Escolha o digito da cor de preenchimento (padrao 0): ").strip() or "0"
    if cor_escolhida not in PALETA_CORES_ANSI:
        print("Cor invalida, usando a padrao (0).")
        cor_escolhida = "0"

    matriz[linha_ini][coluna_ini] = "1"  # normaliza 'X' -> celula livre alvo

    def _exibir_passo(m, _total):
        exibir_matriz(m, modo=modo_exibicao)

    try:
        if versao == "r":
            total = flood_fill_recursivo(matriz, linha_ini, coluna_ini, "1", cor_escolhida, P=P)
        else:
            total = flood_fill_iterativo(matriz, linha_ini, coluna_ini, "1", cor_escolhida, P=P)
    except RecursionError as e:
        print(f"Erro: {e}")
        return

    print("\nMatriz apos o preenchimento:")
    exibir_matriz(matriz, modo=modo_exibicao)
    print(f"Total de celulas preenchidas: {total}")


if __name__ == "__main__":
    main()
