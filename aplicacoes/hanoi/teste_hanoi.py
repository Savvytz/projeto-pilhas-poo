
from codigo import Pilha, hanoi
# ============================================================
# FUNÇÃO AUXILIAR
# ============================================================

def executar_hanoi(n):
    pino_a = Pilha(n)
    pino_b = Pilha(n)
    pino_c = Pilha(n)

    # Coloca os discos no pino A
    for disco in range(n, 0, -1):
        pino_a.empilha(disco)

    pinos = [pino_a, pino_b, pino_c]

    estado = {
        "movimentos_bloco": 0,
        "total": 0,
        "n_discos": n
    }

    hanoi(
        n,
        pino_a,
        pino_c,
        pino_b,
        pinos,
        M=0,
        estado=estado,
        pausar=False
    )

    return pino_a, pino_b, pino_c, estado["total"]


# ============================================================
# TESTE 1 - PILHA BÁSICA
# ============================================================

def teste_pilha():
    print("\n=== TESTE 1 - PILHA ===")

    pilha = Pilha(3)

    pilha.empilha(3)
    pilha.empilha(2)
    pilha.empilha(1)

    assert pilha.tamanho() == 3
    assert pilha.topo_valor() == 1
    assert pilha.pilha_cheia()
    assert not pilha.pilha_vazia()

    assert pilha.desempilha() == 1
    assert pilha.desempilha() == 2
    assert pilha.desempilha() == 3

    assert pilha.pilha_vazia()
    assert pilha.tamanho() == 0

    print("OK - operações da pilha funcionando.")


# ============================================================
# TESTE 2 - PILHA VAZIA
# ============================================================

def teste_pilha_vazia():
    print("\n=== TESTE 2 - PILHA VAZIA ===")

    pilha = Pilha(3)

    try:
        pilha.desempilha()
        assert False, "Era esperado IndexError."
    except IndexError as e:
        print("OK - exceção capturada:")
        print(e)


# ============================================================
# TESTE 3 - MOVIMENTO INVÁLIDO
# ============================================================

def teste_movimento_invalido():
    print("\n=== TESTE 3 - MOVIMENTO INVÁLIDO ===")

    pilha = Pilha(3)

    pilha.empilha(1)

    try:
        # 2 é maior que 1
        pilha.empilha(2)
        assert False, "Era esperado ValueError."
    except ValueError as e:
        print("OK - movimento inválido bloqueado.")
        print(e)


# ============================================================
# TESTE 4 - HANOI N = 1
# ============================================================

def teste_hanoi_n1():
    print("\n=== TESTE 4 - HANOI N = 1 ===")

    pino_a, pino_b, pino_c, total = executar_hanoi(1)

    esperado = 2 ** 1 - 1

    assert total == esperado
    assert pino_a.pilha_vazia()
    assert pino_b.pilha_vazia()
    assert pino_c.tamanho() == 1
    assert pino_c.topo_valor() == 1

    print("OK")
    print("Movimentos:", total)
    print("Esperado:", esperado)


# ============================================================
# TESTE 5 - HANOI N = 2
# ============================================================

def teste_hanoi_n2():
    print("\n=== TESTE 5 - HANOI N = 2 ===")

    pino_a, pino_b, pino_c, total = executar_hanoi(2)

    esperado = 2 ** 2 - 1

    assert total == esperado
    assert pino_a.pilha_vazia()
    assert pino_b.pilha_vazia()

    assert pino_c.tamanho() == 2
    assert pino_c.dados[:pino_c.tamanho()] == [2, 1]

    print("OK")
    print("Movimentos:", total)
    print("Esperado:", esperado)


# ============================================================
# TESTE 6 - HANOI N = 3
# ============================================================

def teste_hanoi_n3():
    print("\n=== TESTE 6 - HANOI N = 3 ===")

    pino_a, pino_b, pino_c, total = executar_hanoi(3)

    esperado = 2 ** 3 - 1

    assert total == esperado
    assert pino_a.pilha_vazia()
    assert pino_b.pilha_vazia()

    assert pino_c.tamanho() == 3
    assert pino_c.dados[:pino_c.tamanho()] == [3, 2, 1]

    print("OK")
    print("Movimentos:", total)
    print("Esperado:", esperado)


# ============================================================
# TESTE 7 - HANOI N = 5
# ============================================================

def teste_hanoi_n5():
    print("\n=== TESTE 7 - HANOI N = 5 ===")

    pino_a, pino_b, pino_c, total = executar_hanoi(5)

    esperado = 2 ** 5 - 1

    assert total == esperado
    assert pino_a.pilha_vazia()
    assert pino_b.pilha_vazia()

    assert pino_c.tamanho() == 5
    assert pino_c.dados[:pino_c.tamanho()] == [5, 4, 3, 2, 1]

    print("OK")
    print("Movimentos:", total)
    print("Esperado:", esperado)


# ============================================================
# TESTE 8 - TESTE DE ESTRESSE
# ============================================================

def teste_estresse():
    print("\n=== TESTE 8 - TESTE DE ESTRESSE ===")

    valores = [10, 15, 20]

    for n in valores:

        _, _, pino_c, total = executar_hanoi(n)

        esperado = 2 ** n - 1

        assert total == esperado
        assert pino_c.tamanho() == n

        print(
            f"N = {n}: "
            f"{total} movimentos "
            f"(esperado: {esperado})"
        )


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    teste_pilha()
    teste_pilha_vazia()
    teste_movimento_invalido()

    teste_hanoi_n1()
    teste_hanoi_n2()
    teste_hanoi_n3()
    teste_hanoi_n5()

    teste_estresse()

    print("\n========================================")
    print("TODOS OS TESTES DA TORRE DE HANOI PASSARAM")
    print("========================================")
