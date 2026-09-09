from pilha import Pilha, PilhaCheiaErro, PilhaVaziaErro, TipoErro
import time


# ============================================================
# 1. TESTE DE EMPILHAR E DESEMPILHAR
# ============================================================

def teste_empilhar_desempilhar():
    print("\n--- Teste de empilhar e desempilhar ---")

    pilha = Pilha(int, 5)

    pilha.empilha(10)
    pilha.empilha(20)
    pilha.empilha(30)

    assert pilha.tamanho() == 3
    assert pilha.desempilha() == 30
    assert pilha.desempilha() == 20
    assert pilha.desempilha() == 10
    assert pilha.tamanho() == 0

    print("OK")


# ============================================================
# 2. TESTE DE PILHA CHEIA
# ============================================================

def teste_pilha_cheia():
    print("\n--- Teste de pilha cheia ---")

    pilha = Pilha(int, 3)

    pilha.empilha(10)
    pilha.empilha(20)
    pilha.empilha(30)

    try:
        pilha.empilha(40)
        print("ERRO: PilhaCheiaErro não foi gerada")
    except PilhaCheiaErro:
        print("OK: PilhaCheiaErro foi gerada")


# ============================================================
# 3. TESTE DE TIPO INVÁLIDO
# ============================================================

def teste_tipo():
    print("\n--- Teste de tipo inválido ---")

    pilha = Pilha(int, 5)

    try:
        pilha.empilha("10")
        print("ERRO: TipoErro não foi gerada")
    except TipoErro:
        print("OK: TipoErro foi gerada")


# ============================================================
# 4. TESTE DE PILHA VAZIA
# ============================================================

def teste_pilha_vazia():
    print("\n--- Teste de pilha vazia ---")

    pilha = Pilha(int, 5)

    try:
        pilha.desempilha()
        print("ERRO: PilhaVaziaErro não foi gerada")
    except PilhaVaziaErro:
        print("OK: PilhaVaziaErro foi gerada")


# ============================================================
# 5. TESTE DO MÉTODO TROCA
# ============================================================

def teste_troca():
    print("\n--- Teste de troca ---")

    pilha = Pilha(int, 5)

    pilha.empilha(10)
    pilha.empilha(20)

    pilha.troca()

    # Depois da troca, 10 deve estar no topo
    assert pilha.desempilha() == 10
    assert pilha.desempilha() == 20

    print("OK")


# ============================================================
# 6. TESTE DE PILHA VAZIA E CHEIA
# ============================================================

def teste_estado_pilha():
    print("\n--- Teste de estado da pilha ---")

    pilha = Pilha(int, 2)

    assert pilha.pilha_esta_vazia() == True
    print("Pilha inicialmente vazia: OK")

    pilha.empilha(10)
    pilha.empilha(20)

    assert pilha.pilha_esta_cheia() == True
    print("Pilha cheia: OK")

    pilha.desempilha()
    pilha.desempilha()

    assert pilha.pilha_esta_vazia() == True
    print("Pilha vazia após remoção: OK")


# ============================================================
# 7. TESTE DOS TIPOS SUPORTADOS
# ============================================================

def teste_tipos_suportados():
    print("\n--- Teste dos tipos suportados ---")

    # Inteiros
    pilha_int = Pilha(int, 3)
    pilha_int.empilha(10)
    pilha_int.empilha(20)

    assert pilha_int.desempilha() == 20

    # Ponto flutuante
    pilha_float = Pilha(float, 3)
    pilha_float.empilha(10.5)
    pilha_float.empilha(20.5)

    assert pilha_float.desempilha() == 20.5

    # Strings
    pilha_str = Pilha(str, 3)
    pilha_str.empilha("A")
    pilha_str.empilha("B")

    assert pilha_str.desempilha() == "B"

    print("OK")


# ============================================================
# 8. TESTE DE ESTRESSE
# ============================================================

def teste_estresse():
    print("\n--- Teste de estresse ---")

    quantidade = 1_000_000

    pilha = Pilha(int, quantidade)

    inicio = time.perf_counter()

    # 1 milhão de inserções
    for i in range(quantidade):
        pilha.empilha(i)

    # 1 milhão de remoções
    for i in range(quantidade):
        pilha.desempilha()

    fim = time.perf_counter()

    tempo = fim - inicio

    assert pilha.pilha_esta_vazia() == True

    print(f"Quantidade de operações: {quantidade * 2:,}")
    print(f"Tempo total: {tempo:.6f} segundos")
    print("Pilha vazia após os testes: OK")


# ============================================================
# EXECUÇÃO DE TODOS OS TESTES
# ============================================================

if __name__ == "__main__":

    teste_empilhar_desempilhar()
    teste_pilha_cheia()
    teste_tipo()
    teste_pilha_vazia()
    teste_troca()
    teste_estado_pilha()
    teste_tipos_suportados()
    teste_estresse()

    print("\n===================================")
    print("TODOS OS TESTES FORAM EXECUTADOS!")
    print("===================================")
