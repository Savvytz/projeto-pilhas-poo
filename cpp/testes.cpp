#include <iostream>
#include <exception>
#include <stdexcept>
#include <string>
#include <cassert>

// ============================================================================
// EXCEÇÕES CUSTOMIZADAS
// ============================================================================
class PilhaCheiaErro : public std::exception {
public:
    const char* what() const noexcept override {
        return "Erro: A pilha esta cheia!";
    }
};

class PilhaVaziaErro : public std::exception {
public:
    const char* what() const noexcept override {
        return "Erro: A pilha nao possui elementos suficientes para a operacao!";
    }
};

// ============================================================================
// CLASSE PILHA REFATORADA (TEMPLATE + RAII)
// ============================================================================
template <typename T>
class Pilha {
private:
    T* array;
    int capacidade;
    int topo_index;

public:
    explicit Pilha(int cap) : capacidade(cap), topo_index(-1) {
        if (cap <= 0) {
            throw std::invalid_argument("A capacidade da pilha deve ser maior que zero.");
        }
        array = new T[capacidade];
    }

    ~Pilha() {
        delete[] array;
    }

    // REGRA DOS TRÊS: Impede cópia rasa e Double Free Error
    Pilha(const Pilha&) = delete;
    Pilha& operator=(const Pilha&) = delete;

    bool pilha_esta_vazia() const { return topo_index == -1; }
    bool pilha_esta_cheia() const { return topo_index == capacidade - 1; }
    int tamanho() const { return topo_index + 1; }

    void empilha(T dado) {
        if (pilha_esta_cheia()) throw PilhaCheiaErro();
        array[++topo_index] = dado;
    }

    T desempilha() {
        if (pilha_esta_vazia()) throw PilhaVaziaErro();
        return array[topo_index--];
    }

    void troca() {
        if (tamanho() < 2) throw PilhaVaziaErro();
        T temp = array[topo_index];
        array[topo_index] = array[topo_index - 1];
        array[topo_index - 1] = temp;
    }
};

// ============================================================================
// ROTINAS DE TESTE DE UNIDADE E ESTRESSE
// ============================================================================

void executar_teste(const std::string& nome, void (*funcao_teste)()) {
    std::cout << "[TESTE] " << nome << " ... ";
    try {
        funcao_teste();
        std::cout << "PASSOU ✅\n";
    } catch (const std::exception& e) {
        std::cout << "FALHOU ❌ (" << e.what() << ")\n";
    }
}

// 1. Teste de Operações Básicas LIFO
void teste_operacoes_basicas() {
    Pilha<int> p(3);
    assert(p.pilha_esta_vazia() == true);
    
    p.empilha(10);
    p.empilha(20);
    assert(p.tamanho() == 2);
    assert(p.desempilha() == 20);
    assert(p.desempilha() == 10);
    assert(p.pilha_esta_vazia() == true);
}

// 2. Teste da Função troca()
void teste_funcao_troca() {
    Pilha<char> p(3);
    p.empilha('A');
    p.empilha('B');
    
    p.troca(); // 'B' (topo) troca com 'A'. Agora 'A' deve ser o topo.
    
    assert(p.desempilha() == 'A');
    assert(p.desempilha() == 'B');
}

// 3. Teste de Disparo de Exceção: PilhaCheiaErro
void teste_excecao_pilha_cheia() {
    Pilha<double> p(2);
    p.empilha(1.1);
    p.empilha(2.2);
    
    bool capturou_excecao = false;
    try {
        p.empilha(3.3); // Deve disparar PilhaCheiaErro
    } catch (const PilhaCheiaErro&) {
        capturou_excecao = true;
    }
    assert(capturou_excecao == true);
}

// 4. Teste de Disparo de Exceção: PilhaVaziaErro (na troca sem elementos suficientes)
void teste_excecao_troca_insuficiente() {
    Pilha<int> p(5);
    p.empilha(100); // Apenas 1 elemento na pilha
    
    bool capturou_excecao = false;
    try {
        p.troca(); // Exige pelo menos 2 elementos
    } catch (const PilhaVaziaErro&) {
        capturou_excecao = true;
    }
    assert(capturou_excecao == true);
}

// 5. Teste de Validação no Construtor
void teste_capacidade_invalida() {
    bool capturou_excecao = false;
    try {
        Pilha<int> p(-5);
    } catch (const std::invalid_argument&) {
        capturou_excecao = true;
    }
    assert(capturou_excecao == true);
}

// 6. Teste de Carga e Custo Assintótico (1.000.000 de Operações)
void teste_estresse_carga() {
    int total_operacoes = 1000000;
    Pilha<int> p(total_operacoes);
    
    for (int i = 0; i < total_operacoes; i++) {
        p.empilha(i);
    }
    assert(p.pilha_esta_cheia() == true);
    
    for (int i = total_operacoes - 1; i >= 0; i--) {
        assert(p.desempilha() == i);
    }
    assert(p.pilha_esta_vazia() == true);
}

// ============================================================================
// PROGRAMA PRINCIPAL
// ============================================================================
int main() {
    std::cout << "=====================================================\n";
    std::cout << "      SUÍTE DE TESTES AUTOMATIZADOS - PILHA C++      \n";
    std::cout << "=====================================================\n\n";

    executar_teste("1. Operacoes Basicas (Empilha/Desempilha)", teste_operacoes_basicas);
    executar_teste("2. Inversao do Topo com troca()", teste_funcao_troca);
    executar_teste("3. Captura de Transbordo (PilhaCheiaErro)", teste_excecao_pilha_cheia);
    executar_teste("4. Captura de Subfluxo em troca()", teste_excecao_troca_insuficiente);
    executar_teste("5. Validação Defensiva de Capacidade Negativa", teste_capacidade_invalida);
    executar_teste("6. Teste de Carga/Estresse (1.000.000 elementos)", teste_estresse_carga);

    std::cout << "\n-----------------------------------------------------\n";
    std::cout << "Nota de Segurança: O teste de copia rasa (Pilha p2 = p1)\n";
    std::cout << "foi validado via falha intencional de compilacao (= delete).\n";
    std::cout << "=====================================================\n";

    return 0;
}