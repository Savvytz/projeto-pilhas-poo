const { Pilha, PilhaCheiaErro, PilhaVaziaErro, TipoErro } = require('./pilha');

function executarTestes() {
    console.log("=== INICIANDO BATERIA DE TESTES DE ESTRESSE (JavaScript) ===");

    // Inicializa uma pilha de tamanho capacidade 3
    const minhaPilha = new Pilha(3, 'number');

    // 1. Teste de Pilha Vazia inicial
    console.log("\n[Teste 1] Verificando se a pilha recém-criada está vazia:");
    console.log("-> pilha_esta_vazia():", minhaPilha.pilha_esta_vazia()); // Esperado: true

    try {
        console.log("Tentando desempilhar pilha vazia...");
        minhaPilha.Desempilha();
    } catch (e) {
        console.log("[SUCESSO] Exceção capturada esperada:", e.name, "-", e.message);
    }

    // 2. Teste de Restrição de Tipos isolado (com pilha com espaço livre)
    console.log("\n[Teste 2] Tentando inserir dado com tipo incorreto (string em pilha de numbers vazia):");
    try {
        minhaPilha.empilha("texto_invalido");
    } catch (e) {
        console.log("[SUCESSO] Exceção capturada esperada:", e.name, "-", e.message);
    }

    // 3. Teste de Estresse de Capacidade (Pilha Cheia)
    console.log("\n[Teste 3] Empilhando até atingir a capacidade máxima (3 elementos):");
    minhaPilha.empilha(10);
    minhaPilha.empilha(20);
    minhaPilha.empilha(30);
    console.log("Tamanho atual:", minhaPilha.tamanho()); // Esperado: 3
    console.log("-> pilha_esta_cheia():", minhaPilha.pilha_esta_cheia()); // Esperado: true

    try {
        console.log("Tentando empilhar o 4º elemento com a pilha cheia (estouro de capacidade)...");
        minhaPilha.empilha(40);
    } catch (e) {
        console.log("[SUCESSO] Exceção capturada esperada:", e.name, "-", e.message);
    }

    // 4. Teste do Método Auxiliar 'troca' Refinado
    console.log("\n[Teste 4] Testando o método 'troca' otimizado:");
    console.log("Elementos antes da troca (topo é o último):", minhaPilha.elementos); // [10, 20, 30]
    minhaPilha.troca();
    console.log("Elementos após a troca do topo (30) com o elemento abaixo (20):", minhaPilha.elementos); // [10, 30, 20]

    // 5. Esvaziando a pilha
    console.log("\n[Teste 5] Esvaziando a pilha completamente:");
    console.log("Desempilhando:", minhaPilha.Desempilha()); // Esperado: 20
    console.log("Desempilhando:", minhaPilha.Desempilha()); // Esperado: 30
    console.log("Desempilhando:", minhaPilha.Desempilha()); // Esperado: 10
    console.log("-> pilha_esta_vazia() final:", minhaPilha.pilha_esta_vazia()); // Esperado: true

    console.log("\n=== TESTES DE ESTRESSE CONCLUÍDOS COM SUCESSO ===");
}

executarTestes();
