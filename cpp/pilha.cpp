#include <iostream>
#include <exception>
#include <stdexcept>

class PilhaCheiaErro : public std::exception {
public:
    const char* what() const noexcept override {
        return "Erro: A pilha esta cheia!";
    }
};

class PilhaVaziaErro : public std::exception {
public:
    const char* what() const noexcept override {
        return "Erro: A pilha esta vazia ou nao contem elementos suficientes!";
    }
};

// Uso de Template para aceitar qualquer tipo básico (char, int, float, etc.)
template <typename T>
class Pilha {
private:
    T* array;
    int capacidade;
    int topo_index;

public:
    Pilha(int cap) : capacidade(cap), topo_index(-1) {
        if (cap <= 0) {
            throw std::invalid_argument("A capacidade da pilha deve ser maior que zero.");
        }
        array = new T[capacidade];
    }

    ~Pilha() {
        delete[] array;
    }

    // REGRA DOS TRÊS / SEGURANÇA: Impede cópia rasa para evitar Double Free Error
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
