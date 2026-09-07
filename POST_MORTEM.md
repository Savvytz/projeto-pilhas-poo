# Relatório Post-Mortem - Projeto PILHAS

## 1. Python 

## 1.1. Log de interação e Prompts
(Fornecer os techos de código desenvolvidos pela ia antes de quaisquer modificações manuais)

* **Prompt Utilizado:** 
* **Código Bruto da IA:**
  ```python
  #Códgio aqui

## 1.2 Code Review Crítico
*(Análise da solução inicial gerada pela IA, identificando falhas de eficiência, complexidade e segurança nas três linguagens)*

* **Eficiência**
* **Complexidade**
* **Segurança**

## 1.3. Justificativa de Refatoração
*(Adicionar detalhadamente quais alterações foram realizadas no código para atender aos requisitos de desempenho, correção e testes solicitados)*

Após a análise do código bruto gerado pela IA, realizamos as seguintes refatorações manuais nas três linguagens do projeto:

### Tratamento de Exceções Obrigatórias
* **Problema inicial:**
  
* **Alteração realizada:**
  

### Ajustes de Desempenho e Estrutura 

  
### Refinamento dos Métodos Auxiliares (`troca` e `tamanho`)
* **Alteração realizada:**

## 1.4. Evidência de Testes
*(Relatório simples dos testes de estresse executados, demonstrando que o código refatorado por você supera o código ingênuo gerado inicialmente pelo modelo).*

  
## 2. C++
## 2.1. Log de interação e Prompts
(Fornecer os techos de código desenvolvidos pela ia antes de quaisquer modificações manuais)

* **Prompt Utilizado:** 
* **Código Bruto da IA:**
  ```C++
  #Códgio aqui
  
## 2.2 Code Review Crítico
*(Análise da solução inicial gerada pela IA, identificando falhas de eficiência, complexidade e segurança nas três linguagens)*

* **Eficiência**
* **Complexidade**
* **Segurança**

## 2.3. Justificativa de Refatoração
*(Adicionar detalhadamente quais alterações foram realizadas no código para atender aos requisitos de desempenho, correção e testes solicitados)*

Após a análise do código bruto gerado pela IA, realizamos as seguintes refatorações manuais nas três linguagens do projeto:

### Tratamento de Exceções Obrigatórias
* **Problema inicial:**
  
* **Alteração realizada:**

  

### Ajustes de Desempenho e Estrutura 

  
### Refinamento dos Métodos Auxiliares (`troca` e `tamanho`)
* **Alteração realizada:**

## 2.4. Evidência de Testes
*(Relatório simples dos testes de estresse executados, demonstrando que o código refatorado por você supera o código ingênuo gerado inicialmente pelo modelo).*


## 3. JavaScript 

## 3.1. Log de interação e Prompts 
(Fornecer os techos de código desenvolvidos pela ia antes de quaisquer modificações manuais)

* **Prompt Utilizado:** Gere um código em javascript que implementa uma estrutura de dados do tipo PILHA com classes POO que deve aceitar apenas dados de um mesmo tipo básico da linguagem. O armazenamento interno pode ser inicialmente um array padrão da biblioteca.

    A especificação das funções (métodos) da interface dessa classe Pilha é a seguinte:
    
        empilha(dado) : empilha um dado no topo da pilha. Se a pilha estiver cheia, deve levantar a exceção       “PilhaCheiaErro”. Se o dado não for do tipo básico armazenado pela Pilha, deve levantar a exceção           “TipoErro”
        desempilha() -> dado : desempilha o dado do topo da pilha, retornando-o. Se a pilha estiver vazia deve levantar a exceção “PilhaVaziaErro”
        pilha_esta_vazia() : retorna True se a pilha estiver vazia
        pilha_esta_cheia() : retorna True se a pilha estiver cheia
        troca() : troca o dado do topo da pilha com o dado imediatamente abaixo
        tamanho() : retorna o número de dados empilhados
* **Código Bruto da IA:**
  ```JavaScript
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
            throw new Error("Elementos insuficientes para troca.");
        }
        const topo = this.elementos.pop();
        const abaixo = this.elementos.pop();
        this.elementos.push(topo);
        this.elementos.push(abaixo);
    }

    tamanho() {
        return this.elementos.length;
    }
  }

## 3.2 Code Review Crítico
*(Análise da solução inicial gerada pela IA, identificando falhas de eficiência, complexidade e segurança nas três linguagens)*

* **Eficiência**
  * A IA utilizou um array dinâmico nativo (`[]`). Embora funcione, academicamente falando, um array dinâmico comum redimensiona a memória por baixo dos panos, oque pode causar sobrecarga(overhead).
* **Complexidade**
  * Os métodos básicos, de empilha() e desempilha() operam em tempo constante O(1), oque é ótimo. No entanto, o método auxiliar `troca()` foi implementado de forma ineficiente, utilizando múltiplos comandos `.pop()` e `.push()` em vez de um acesso direto otimizado aos índices do topo. 
* **Segurança**
  * A IA criou as classes de erro personalizadas (`PilhaCheiaErro`, `PilhaVaziaErro`, `TipoErro`), mas na classe `troca()`, quando a pilha continha menos de dois elementos, a IA lançou apenas uma exceção genérica (`throw new Error()`) em vez de utilizar uma abordagem alinhada aos padrões do projeto.


## 3.3. Justificativa de Refatoração
*(Adicionar detalhadamente quais alterações foram realizadas no código para atender aos requisitos de desempenho, correção e testes solicitados)*

Após a análise do código bruto gerado pela IA, realizamos as seguintes refatorações manuais nas três linguagens do projeto:

### Tratamento de Exceções Obrigatórias
* **Problema inicial:**
  
* **Alteração realizada:**

  

### Ajustes de Desempenho e Estrutura 

  
### Refinamento dos Métodos Auxiliares (`troca` e `tamanho`)
* **Alteração realizada:**

  

## 3.4. Evidência de Testes
*(Relatório simples dos testes de estresse executados, demonstrando que o código refatorado por você supera o código ingênuo gerado inicialmente pelo modelo).*



