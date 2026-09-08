class PilhaCheiaErro extends Error {
    constructor(mensagem) {
        super(mensagem);
        this.name = "PilhaCheiaErro";
    }
}

class PilhaVaziaErro extends Error {
    constructor(mensagem) {
        super(mensagem);
        this.name = "PilhaVaziaErro";
    }
}

class TipoErro extends Error {
    constructor(mensagem) {
        super(mensagem);
        this.name = "TipoErro";
    }
}

class Pilha {
    constructor(capacidade, tipoDado) {
        this.capacidade = capacidade;
        this.tipoDado = tipoDado; // Ex: 'number', 'string'
        this.elementos = [];
    }

    empilha(dado) {
        if (this.pilha_esta_cheia()) {
            throw new PilhaCheiaErro("A pilha está cheia.");
        }
        if (typeof dado !== this.tipoDado) {
            throw new TipoErro(`O dado deve ser do tipo ${this.tipoDado}.`);
        }
        this.elementos.push(dado);
    }

    Desempilha() {
        if (this.pilha_esta_vazia()) {
            throw new PilhaVaziaErro("A pilha está vazia.");
        }
        return this.elementos.pop();
    }

    pilha_esta_vazia() {
        return this.elementos.length === 0;
    }

    pilha_esta_cheia() {
        return this.elementos.length >= this.capacidade;
    }

    troca() {
        if (this.tamanho() < 2) {
            throw new PilhaVaziaErro("Elementos insuficientes para a operação de troca.");
        }
        // Refatoração: Acesso direto aos índices do topo, eliminando pops/pushes redundantes
        const topoIdx = this.elementos.length - 1;
        const abaixoIdx = this.elementos.length - 2;

        const temp = this.elementos[topoIdx];
        this.elementos[topoIdx] = this.elementos[abaixoIdx];
        this.elementos[abaixoIdx] = temp;
    }

    tamanho() {
        return this.elementos.length;
    }
}

module.exports = { Pilha, PilhaCheiaErro, PilhaVaziaErro, TipoErro };

