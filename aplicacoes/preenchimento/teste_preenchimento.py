import copy
from codigo import *
# ============================================================
# TESTE 1 - PILHA
# ============================================================

def teste_pilha():
    print("\n=== TESTE 1 - PILHA ===")

    pilha = Pilha(2)

    pilha.empilha("A")
    pilha.empilha("B")

    assert pilha.tamanho() == 2
    assert not pilha.pilha_vazia()
    assert pilha.pilha_cheia()

    # Testa redimensionamento
    pilha.empilha("C")

    assert pilha.tamanho() == 3
    assert pilha.capacidade == 4

    assert pilha.desempilha() == "C"
    assert pilha.desempilha() == "B"
    assert pilha.desempilha() == "A"

    assert pilha.pilha_vazia()

    print("OK - operações básicas da pilha funcionaram.")
    print("OK - redimensionamento funcionou.")


# ============================================================
# TESTE 2 - DESEMPILHAR PILHA VAZIA
# ============================================================

def teste_pilha_vazia():
    print("\n=== TESTE 2 - PILHA VAZIA ===")

    pilha = Pilha(2)

    try:
        pilha.desempilha()
        assert False, "Era esperado um IndexError."
    except IndexError as e:
        print("OK - exceção capturada:")
        print(e)


# ============================================================
# TESTE 3 - LOCALIZAÇÃO DO X
# ============================================================

def teste_localizar_posicao():
    print("\n=== TESTE 3 - LOCALIZAÇÃO DO X ===")

    matriz = [
        list("1111"),
        list("11X1"),
        list("1111")
    ]

    posicao = localizar_posicao(matriz, "X")

    assert posicao == (1, 2)

    print("OK - posição encontrada:", posicao)


# ============================================================
# TESTE 4 - X NÃO EXISTE
# ============================================================

def teste_x_inexistente():
    print("\n=== TESTE 4 - X INEXISTENTE ===")

    matriz = [
        list("1111"),
        list("1111"),
        list("1111")
    ]

    posicao = localizar_posicao(matriz, "X")

    assert posicao is None

    print("OK - ausência de X foi identificada corretamente.")


# ============================================================
# TESTE 5 - FLOOD FILL RECURSIVO
# ============================================================

def teste_flood_fill_recursivo():
    print("\n=== TESTE 5 - FLOOD FILL RECURSIVO ===")

    matriz = [
        list("11111"),
        list("10001"),
        list("10101"),
        list("10001"),
        list("11111")
    ]

    # Preenche a região interna
    total = flood_fill_recursivo(
        matriz,
        2,
        2,
        "1",
        "0",
        P=0,
        pausar=False
    )

    # Apenas a célula central é alcançável
    # porque ela está cercada por zeros.
    assert total == 1
    assert matriz[2][2] == "0"

    print("OK - Flood Fill recursivo.")
    print("Células preenchidas:", total)


# ============================================================
# TESTE 6 - FLOOD FILL ITERATIVO
# ============================================================

def teste_flood_fill_iterativo():
    print("\n=== TESTE 6 - FLOOD FILL ITERATIVO ===")

    matriz = [
        list("11111"),
        list("10001"),
        list("10101"),
        list("10001"),
        list("11111")
    ]

    total = flood_fill_iterativo(
        matriz,
        2,
        2,
        "1",
        "0",
        P=0,
        pausar=False
    )

    assert total == 1
    assert matriz[2][2] == "0"

    print("OK - Flood Fill iterativo.")
    print("Células preenchidas:", total)


# ============================================================
# TESTE 7 - RECURSIVO X ITERATIVO
# ============================================================

def teste_recursivo_vs_iterativo():
    print("\n=== TESTE 7 - RECURSIVO X ITERATIVO ===")

    matriz_original = [
        list("111111"),
        list("100001"),
        list("101101"),
        list("100001"),
        list("111111")
    ]

    matriz_recursiva = copy.deepcopy(matriz_original)
    matriz_iterativa = copy.deepcopy(matriz_original)

    total_recursivo = flood_fill_recursivo(
        matriz_recursiva,
        2,
        2,
        "1",
        "0",
        P=0,
        pausar=False
    )

    total_iterativo = flood_fill_iterativo(
        matriz_iterativa,
        2,
        2,
        "1",
        "0",
        P=0,
        pausar=False
    )

    assert total_recursivo == total_iterativo
    assert matriz_recursiva == matriz_iterativa

    print("OK - as duas versões produziram o mesmo resultado.")
    print("Recursivo:", total_recursivo, "células")
    print("Iterativo:", total_iterativo, "células")


# ============================================================
# TESTE 8 - ARQUIVO INEXISTENTE
# ============================================================

def teste_arquivo_inexistente():
    print("\n=== TESTE 8 - ARQUIVO INEXISTENTE ===")

    try:
        ler_matriz("arquivo_que_nao_existe.txt")
        assert False, "Era esperado FileNotFoundError."
    except FileNotFoundError as e:
        print("OK - arquivo inexistente tratado corretamente.")
        print(e)


# ============================================================
# TESTE 9 - MATRIZ MALFORMADA
# ============================================================

def teste_matriz_malformada():
    print("\n=== TESTE 9 - MATRIZ MALFORMADA ===")

    nome = "matriz_teste_invalida.txt"

    with open(nome, "w", encoding="utf-8") as arquivo:
        arquivo.write("11111\n")
        arquivo.write("111\n")
        arquivo.write("11111\n")

    try:
        ler_matriz(nome)
        assert False, "Era esperado ValueError."
    except ValueError as e:
        print("OK - matriz malformada detectada.")
        print(e)


# ============================================================
# TESTE 10 - LABIRINTO
# ============================================================

def teste_labirinto():
    print("\n=== TESTE 10 - LABIRINTO ===")

    matriz = [
        list("00000"),
        list("0X110"),
        list("01110"),
        list("011S0"),
        list("00000")
    ]

    caminho = resolver_labirinto(
        matriz,
        1,
        1,
        livre="1",
        parede="0",
        saida="S"
    )

    assert caminho is not None
    assert caminho[0] == (1, 1)
    assert caminho[-1] == (3, 3)

    print("OK - saída encontrada.")
    print("Caminho:", caminho)


# ============================================================
# EXECUÇÃO DOS TESTES
# ============================================================

if __name__ == "__main__":

    teste_pilha()
    teste_pilha_vazia()
    teste_localizar_posicao()
    teste_x_inexistente()
    teste_flood_fill_recursivo()
    teste_flood_fill_iterativo()
    teste_recursivo_vs_iterativo()
    teste_arquivo_inexistente()
    teste_matriz_malformada()
    teste_labirinto()

    print("\n========================================")
    print("TODOS OS TESTES DO FLOOD FILL PASSARAM")
    print("========================================")
