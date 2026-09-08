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

Após a análise do código bruto gerado pela IA, realizamos as seguintes refatorações manuais:

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

* **Prompt Utilizado:** Crie uma classe POO em C++ para implementar uma estrutura de dados Pilha usando um array nativo de capacidade fixa para armazenar um tipo básico. A classe deve implementar os seguintes métodos: empilha(dado), desempilha(), pilha_esta_vazia(), pilha_esta_cheia(), troca() e tamanho(). Trate os limites da pilha lançando exceções personalizadas chamadas PilhaCheiaErro e PilhaVaziaErro estendendo std::exception.
  
* **Código Bruto da IA:**
  ```C++
  #include <iostream>
  #include <exception>

  class PilhaCheiaErro : public std::exception {
  public:
    const char* what() const noexcept override {
        return "Erro: A pilha esta cheia!";
    }
  };

  class PilhaVaziaErro : public std::exception {
  public:
    const char* what() const noexcept override {
        return "Erro: A pilha esta vazia!";
    }
  };

  class Pilha {
  private:
    int* array;
    int capacidade;
    int topo_index;

  public:
    Pilha(int cap) : capacidade(cap), topo_index(-1) {
        array = new int[capacidade];
    }

    ~Pilha() {
        delete[] array;
    }

    bool pilha_esta_vazia() const { return topo_index == -1; }
    bool pilha_esta_cheia() const { return topo_index == capacidade - 1; }
    int tamanho() const { return topo_index + 1; }

    void empilha(int dado) {
        if (pilha_esta_cheia()) throw PilhaCheiaErro();
        topo_index++;
        array[topo_index] = dado;
    }

    int desempilha() {
        if (pilha_esta_vazia()) throw PilhaVaziaErro();
        int valor = array[topo_index];
        topo_index--;
        return valor;
    }

    void troca() {
        if (tamanho() < 2) throw PilhaVaziaErro();
        int temp = array[topo_index];
        array[topo_index] = array[topo_index - 1];
        array[topo_index - 1] = temp;
    }
  };
  
## 2.2 Code Review Crítico
*(Análise da solução inicial gerada pela IA, identificando falhas de eficiência, complexidade e segurança nas três linguagens)*

* **Eficiência**
  * A IA fez o uso de um array contíguo em memória, com isso, todas as operações operam em tempo constante $O(1)$ e aproveitam a localidade espacial de referência, otimizando o uso do cache da CPU
* **Complexidade**
  * O código da IA cumpre os requisitos de POO ao manter os membros privados(array, capacidade, topo_index, etc). A implementação ficou restrita unicamente ao tipo primitivo int, porem com essa restrição a um tipo que em caso de mudança seria preciso duplicar o código-fonte manualmente, aumentando a complexidade de manutenção do projeto.
* **Segurança**
  * O processo tem algumas falhas no quesito segurança, deixando o programa consideravelmente vulnerável, pontos como a ausência de validação defensiva na instanciação e insegurança de acesso por índices desprptegidos fez com que houvesse mudanças depois de alguns testes efetuados.

## 2.3. Justificativa de Refatoração
*(Adicionar detalhadamente quais alterações foram realizadas no código para atender aos requisitos de desempenho, correção e testes solicitados)*

  Após a análise do código bruto gerado pela IA, realizamos as seguintes refatorações manuais :

### Tratamento de Exceções Obrigatórias
* **Problema inicial:**
   * Não houve alteração estrutural no lançamento das exceções do enunciado. O código bruto inicial gerado pela IA já cumpria os requisitos de herdar de std::exception com o qualificador noexcept no método what() e disparar PilhaCheiaErro no transbordo (overflow) e PilhaVaziaErro no subfluxo (underflow).
  
* **Alteração realizada:**
   * Apenas estendeu-se o uso de exceções padrão da linguagem para cobrir falhas de validação na instanciação. Adicionou-se o lançamento de std::invalid_argument no construtor para interceptar capacidades inválidas (cap <= 0) antes que o operador new[] cause falhas de alocação de memória no Heap.


### Ajustes de Desempenho e Estrutura 
  A implementação inicial amarrava a estrutura exclusivamente ao tipo primitivo int e apresentava uma falha grave de segurança de memória por violar a Regra dos Três (Rule of Three), permitindo a ocorrência de Double Free Error e corrupção do Heap ao copiar instâncias da pilha.

 * Ajustes Realizados:

     1. **Generacidade via Templates (template <typename T>):** A classe foi convertida para um modelo genérico, permitindo reutilizar a mesma estrutura para qualquer tipo básico (char, float, double, int) sem custo de desempenho em tempo de execução.

     2. **Bloqueio de Cópia Rasa (= delete):** Foram desativados explicitamente o construtor de cópia e o operador de atribuição (Pilha(const Pilha&) = delete;). Com isso, tentativas de atribuição entre instâncias são bloqueadas diretamente pelo compilador, garantindo a integridade da memória alocada no Heap.

  
### Refinamento dos Métodos Auxiliares (`troca` e `tamanho`)
   * **Problema inicial:** O método troca() dependia do cálculo dinâmico da função de consulta tamanho() < 2, que por sua vez fazia a operação matemática topo_index + 1. Além disso, faltava o qualificador const nas funções de consulta de estado, o que impedia a leitura do estado da pilha a partir de referências ou ponteiros constantes (const Pilha<T>&).
* **Alteração realizada:**
   * **Ajuste de Imutabilidade (const correctness):** Todos os métodos de consulta (pilha_esta_vazia(), pilha_esta_cheia(), tamanho()) foram marcados com o qualificador const, garantindo a integridade dos dados e permitindo o uso seguro do objeto em contextos de leitura constante.

   * **Otimização do Método troca():** A validação do topo foi simplificada para checar diretamente a condição de limite dos índices internos, evitando chamadas indiretas desnecessárias sem perder o rigor no tratamento da exceção PilhaVaziaErro.

## 2.4. Evidência de Testes
*(Relatório simples dos testes de estresse executados, demonstrando que o código refatorado por você supera o código ingênuo gerado inicialmente pelo modelo).*
[SUÍTE DE TESTES] Iniciando validação da classe Pilha Refatorada...

   *[TESTE 1] Inserção e Remoção Sequencial (Pilha<int>)*
     -> Empilhando: 10, 20, 30
     -> Desempilhando: 30 (OK)
     -> Status: PASSOU

   *[TESTE 2] Inversão de Topo com troca() (Pilha<float>)*
     -> Topo inicial: 2.5 | Sub-topo: 1.2
     -> Executando troca()...
     -> Novo topo: 1.2 (OK)
     -> Status: PASSOU

   *[TESTE 3] Interceptação de Subfluxo (PilhaVaziaErro)*
     -> Tentando desempilhar pilha vazia...
     -> Exceção Capturada: "Erro: A pilha nao possui elementos suficientes!"
     -> Status: PASSOU

   *[TESTE 4] Interceptação de Transbordo (PilhaCheiaErro)*
     -> Preenchendo pilha (3/3)... Tentando inserir o 4º elemento...
     -> Exceção Capturada: "Erro: A pilha esta cheia!"
     -> Status: PASSOU

   *[TESTE 5] Proteção de Memória (Regra dos Três)*
     -> Tentando executar: Pilha<int> p2 = p1;
     -> Erro de Compilação: 'Pilha<T>::Pilha(const Pilha<T>&)' is deleted.
     -> Status: PASSOU (Double Free Evitado)

*[RESULTADO FINAL]:* 5/5 Testes executados com sucesso.

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
  * A IA criou as classes de erro personalizadas (`PilhaCheiaErro`, `PilhaVaziaErro`, `TipoErro`), mas na classe `troca()`, quando a pilha contém menos de dois elementos, a IA lança apenas uma exceção genérica (`throw new Error()`) em vez de utilizar uma abordagem alinhada aos padrões do projeto.


## 3.3. Justificativa de Refatoração
*(Adicionar detalhadamente quais alterações foram realizadas no código para atender aos requisitos de desempenho, correção e testes solicitados)*

Após a análise do código bruto gerado pela IA, realizamos as seguintes refatorações manuais:

### Tratamento de Exceções Obrigatórias
* **Problema inicial:**
Lançamento de exceção genérico (`throw new Error(...)`) no método auxiliar `troca()` e omite a validação prévia de quantidade mínima de elementos.
* **Alteração realizada:**
Padronizamos todas as falhas de fluxo para utilizarem as exceções , garantindo que o método `troca()` valide a presença de pelo menos dois elementos na pilha e dispare a exceção esperada.
  

### Ajustes de Desempenho e Estrutura 
* O array dinâmico nativo do JavaScript (`[]`) fornecido inicialmente foi mantido para a estrutura básica da linguagem. No entanto, implementamos travas de segurança no construtor e no método `empilha()` para assegurar que a restrição de tipo básico exigida pelo projeto seja estritamente respeitada.
  
### Refinamento dos Métodos Auxiliares (`troca` e `tamanho`)
* **Alteração realizada:**
Refatoramos a lógica do método `troca()`. O código bruto da IA removia e reinseria os elementos do array de forma redundante e ineficiente via múltiplos `.pop()` e `.push()`. Alteramos a abordagem para realizar a inversão com base direta nos índices do topo da pilha de forma limpa, segura e com validação prévia de tamanho mínimo.
  

## 3.4. Evidência de Testes
*(Relatório simples dos testes de estresse executados, demonstrando que o código refatorado por você supera o código ingênuo gerado inicialmente pelo modelo).*
* **Relatório de Estresse e Validação:**
  Desenvolvemos uma suíte de testes automatizados para submeter a pilha refatorada a cenários extremos. O script executou com sucesso as seguintes validações:
  1. **Estouro de Capacidade:** A pilha com limite fixado em 3 elementos disparou corretamente a exceção `PilhaCheiaErro` ao tentar inserir um 4º elemento.
  2. **Proteção contra Pilha Vazia:** A tentativa de remoção em uma pilha vazia foi interceptada com sucesso pela exceção `PilhaVaziaErro`.
  3. **Restrição de Tipos:** A inserção de dados de tipos diferentes (string em pilha numérico) foi bloqueada com o disparo correto de `TipoErro`.
  4. **Correção do Método Troca:** O método `troca` novo manipulou a inversão do topo por acesso direto a índices de forma segura, superando a implementação inicial da IA e operando sem falhas lógicas sob estresse.


