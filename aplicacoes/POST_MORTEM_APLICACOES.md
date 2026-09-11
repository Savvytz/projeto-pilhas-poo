## 1. Problema I: Preenchimento de Região (Flood Fill)

### 1.1. Log de Iteração e Prompts
* **Prompt para solução recursiva:**
 Desenvolva um programa que utiliza rotina recursiva para preencher uma região de uma matriz de caracteres, ou seja, uma matriz cujos elementos são apenas zeros e uns Assim, são dados a matriz de caracteres B (originalmente era uma matriz binária, porém para facilitar a visualização dos resultados optou-se pela matriz de caracteres) e uma posição inicial X (linha, coluna). A partir desta posição inicial o programa deverá preencher com 0´s as posições vizinhas até o limite das bordas preenchidas com 0´s. Se porventura a borda não formar uma figura fechada, o programa irá preencher toda a matriz com 0´s. Esta rotina é utilizada para preencher (colorir) figuras em editores tipo o Paint do MS-Windows© (onde a matriz é uma matriz de pixels), ou mesmo para percorrer labirintos (usado em robótica). Para este último, produza uma solução também.
 A matriz de caracteres deve ser lida de um arquivo e ser apresentada na tela antes e depois do preenchimento. Permita que o usuário especifique uma quantidade P de passos a serem executados entre cada apresentação da matriz para acompanhar a evolução do algoritmo. Se P for zero, então a rotina deverá executar até o fim sem paradas intermediárias. A cada apresentação da matriz o programa deve aguardar por um [ENTER] do usuário para prosseguir aos próximos P passos. Na página seguinte é dada uma matriz de caracteres de exemplo e a posição inicial é dada por um X (que deve virar 0 ao final da rotina). Para um melhor efeito de visualização na tela do terminal, pode-se trocar os caracteres ‘1’s por espaços em branco e os ‘0’s por um caractere que preencha mais a posição, tipo ‘@’ ou ‘#’.
 Melhore esta entrada e saída com um BITMAP, ou seja, uma matriz de Pixels. Também aceite cores diversas igual ao exemplo feito em sala de aula com o MS-Paint.

  * **Código bruto retornado pela IA (Recursivo):**
  ```python
  import sys

  def flood_fill_recursivo(matriz, linha, coluna, alvo, substituicao):
      # Verifica limites da matriz e se a posição atual corresponde ao caractere alvo
      if (linha < 0 or linha >= len(matriz) or 
          coluna < 0 or coluna >= len(matriz[0]) or 
          matriz[linha][coluna] != alvo):
          return

    # Substitui o caractere na posição atual
    matriz[linha][coluna] = substituicao

    # Chamadas recursivas para os 4 vizinhos (acima, abaixo, esquerda, direita)
    flood_fill_recursivo(matriz, linha - 1, coluna, alvo, substituicao)
    flood_fill_recursivo(matriz, linha + 1, coluna, alvo, substituicao)
    flood_fill_recursivo(matriz, linha, coluna - 1, alvo, substituicao)
    flood_fill_recursivo(matriz, linha, coluna + 1, alvo, substituicao)

    def exibir_matriz(matriz):
        for linha in matriz:
            # Substitui '1' por espaço e '0' por '#' para melhor visualização bitmap
            linha_formatada = "".inarquivavel if False else "".join(['#' if c == '0' else ' ' for c in linha])
            print(linha_formatada)
        print("-" * len(matriz[0]))
    
    
    if __name__ == "__main__":
        # Matriz de exemplo baseada no enunciado
        matriz_exemplo = [
            list("1111111111111111"),
            list("1100111111111111"),
            list("1101001111111111"),
            list("1100110000001111"),
            list("1110011111101111"),
            list("1111101111101111"),
            list("1110001111110111"),
            list("1110111111101111"),
            list("1110111100011111"),
            list("1110111001111111"),
            list("1111000011111111"),
            list("1111111111111111")
        ]
    
    print("Matriz antes do preenchimento:")
    exibir_matriz(matriz_exemplo)
    
    # Executa o Flood Fill a partir da posição inicial (6, 7) por exemplo
    flood_fill_recursivo(matriz_exemplo, 6, 7, '1', '0')
    
    print("Matriz após o preenchimento:")
    exibir_matriz(matriz_exemplo)

* **Prompt para solução interativa:**
   Desenvolva um programa que utiliza utiliza uma pilha de posições (linha, coluna)  para preencher uma região de uma matriz de caracteres, ou seja, uma matriz cujos elementos são apenas zeros e uns Assim, são dados a matriz de caracteres B (originalmente era uma matriz binária, porém para facilitar a visualização dos resultados optou-se pela matriz de caracteres) e uma posição inicial X (linha, coluna). A partir desta posição inicial o programa deverá preencher com 0´s as posições vizinhas até o limite das bordas preenchidas com 0´s. Se porventura a borda não formar uma figura fechada, o programa irá preencher toda a matriz com 0´s. Esta rotina é utilizada para preencher (colorir) figuras em editores tipo o Paint do MS-Windows© (onde a matriz é uma matriz de pixels), ou mesmo para percorrer labirintos (usado em robótica). Para este último, produza uma solução também.

    A matriz de caracteres deve ser lida de um arquivo e ser apresentada na tela antes e depois do preenchimento. Permita que o usuário especifique uma quantidade P de passos a serem executados entre cada apresentação da matriz para acompanhar a evolução do algoritmo. Se P for zero, então a rotina deverá executar até o fim sem paradas intermediárias. A cada apresentação da matriz o programa deve aguardar por um [ENTER] do usuário para prosseguir aos próximos P passos. Na página seguinte é dada uma matriz de caracteres de exemplo e a posição inicial é dada por um X (que deve virar 0 ao final da rotina). Para um melhor efeito de visualização na tela do terminal, pode-se trocar os caracteres ‘1’s por espaços em branco e os ‘0’s por um caractere que preencha mais a posição, tipo ‘@’ ou ‘#’.
    Melhore esta entrada e saída com um BITMAP, ou seja, uma matriz de Pixels. Também aceite cores diversas igual ao exemplo feito em sala de aula com o MS-Paint.
* **Código bruto retornado pela IA (Interativo):**

  ```python
   import sys
  
  def flood_fill_recursivo(matriz, linha, coluna, alvo, substituicao, P, contador):
      # Verifica os limites da matriz e se o caractere atual é o alvo
      if (linha < 0 or linha >= len(matriz) or 
          coluna < 0 or coluna >= len(matriz[0]) or 
          matriz[linha][coluna] != alvo):
          return contador

    # Realiza o preenchimento
    matriz[linha][coluna] = substituicao
    contador[0] += 1

    # Controla a quantidade P de passos entre cada exibição
    if P > 0 and contador[0] % P == 0:
        print(f"\n--- Passo {contador[0]} ---")
        exibir_matriz(matriz)
        input("Pressione [ENTER] para continuar...")

    # Chamadas recursivas para os 4 vizinhos (acima, abaixo, esquerda, direita)
    flood_fill_recursivo(matriz, linha - 1, coluna, alvo, substituicao, P, contador)
    flood_fill_recursivo(matriz, linha + 1, coluna, alvo, substituicao, P, contador)
    flood_fill_recursivo(matriz, linha, coluna - 1, alvo, substituicao, P, contador)
    flood_fill_recursivo(matriz, linha, coluna + 1, alvo, substituicao, P, contador)
    
    return contador[0]

    def ler_matriz_de_arquivo(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            return [list(linha.strip()) for linha in f.readlines()]
    
    def exibir_matriz(matriz):
        for linha in matriz:
            # Substitui '0' por '#' e '1' por espaço (simulando bitmap)
            print("".join(['#' if c == '0' else ' ' for c in linha]))
        print("-" * len(matriz[0]))
    
    if __name__ == "__main__":
        # Simula a leitura de um arquivo contendo a matriz
        nome_arquivo = "matriz.txt"
    
    # Criando um arquivo temporário de teste para rodar o código bruto
    with open(nome_arquivo, 'w') as f:
        f.write("1111111111111111\n")
        f.write("1100111111111111\n")
        f.write("1101001111111111\n")
        f.write("1100110000001111\n")
        f.write("1110011111101111\n")
        f.write("1111101111101111\n")
        f.write("1110001111110111\n")
        f.write("1110111111101111\n")
        f.write("1110111100011111\n")
        f.write("1110111001111111\n")
        f.write("1111000011111111\n")
        f.write("1111111111111111\n")

    matriz = ler_matriz_de_arquivo(nome_arquivo)
    
    print("Matriz Original antes do preenchimento:")
    exibir_matriz(matriz)
    
    # O usuário especifica a quantidade P de passos
    P = int(input("Digite a quantidade P de passos entre cada exibição (0 para ir até o fim): "))
    
    # Posição inicial X (linha, coluna) fornecida (ex: linha 6, coluna 7)
    linha_inicial, coluna_inicial = 6, 7
    
    contador = [0]
    alvo = matriz[linha_inicial][coluna_inicial]
    
    if alvo != '0':
        flood_fill_recursivo(matriz, linha_inicial, coluna_inicial, alvo, '0', P, contador)
        
    print("\nMatriz Final após o preenchimento:")
    exibir_matriz(matriz)

## 1.2 Code Review Crítico
*(Análise da solução inicial gerada pela IA, identificando falhas de eficiência, complexidade e segurança)*

Eficiência:
Os códigos, tanto o "Recursivo" quanto o "Iterativo", implementaram de fato uma estrutura de pilha: A segunda versão, apesar de o prompt pedir explictamente uma solução baseada em uma pilha de posições (Linha, Coluna), apenas reaproveita a msma função recursiva original com parâmetros extras de contagem (P, contador). Ou seja, a IA não atendeu ao que fo pedido nessa segunda entrega. Além disso, a função é chamada repetidamente com um print() por linha, gerando overhead de I/O a cada apresentação da matriz.

Complexidade:
O flood fill possui complexidade de tempo O(L x C), pois cada célula é visitada e marcada no máximo uma vez. Ainda assim, por ser implementado como uma chamada recursiva por célula, a profundidade da pilha de chamadas pode crescer proporcionalmente à área da região a preencher, o que é um risco distinto de complexidade de tempo. Ou seja, mesmo sendo O(L x C) em tempo, o programa pode esbarrar no limite de recursão do Python antes de terminar em matrizes grandes.

Segurança:
Falta validação adequada das entradas do usuário. O código bruto não trata arquivos inexistentes, matrizes malformadas e posição inicial fora dos limites. O código recursivo bruto também não ajusta sys.setrecursionlimit, o que pode causar RecursionError em matrizes com regiões grandes a preencher Observa-se ainda um resíduo de código sem sentido na função exibir_matriz do recursivo.

Além disso, duas exigências explicitas no prompt não foram atendidas, sendo elas a leitura de arquivo e a visualização em bitmap e cores no estilo de MS-Paint.

## 1.3. Justificativa de Refatoração
*(Adicionar detalhadamente quais alterações foram realizadas no código para atender aos requisitos de desempenho, correção e testes solicitados)*

Após a análise do código bruto gerado pela IA, realizamos as seguintes refatorações manuais:

### Tratamento de Exceções Obrigatórias
* **Problema inicial:**
  O código gerado pela IA não tratava arquivo inexistente, matriz malformada e tampouco posição inicial fora dos limites. Além disso, o prompt exigia que "a matriz de caracteres deve ser lida de um arquivo", mas o código bruto recursivo não implementava nenhuma leitura de arquivo (matriz hardcoded no script) e o código bruto "iterativo" fabricava o próprio arquivo antes de lê-lo de volta, não lendo de fato um arquivo fornecido pelo usuário.

* **Alteração realizada:**
  A função ler_matriz() passou a capturar FileNotFoundError/OSError e a validar que todas as linhas têm o mesmo comprimento, levantando ValueError com mensagem explicativa, lendo de fato um caminho informado pelo usuário no main() — sem gerar o próprio arquivo de teste como o código bruto fazia.

A função localizar_posicao() retorna None (tratado no main()) em vez de deixar o IndexError estourar.

A classe Pilha levanta IndexError explícito (PilhaVaziaErro) ao desempilhar uma pilha vazia, em vez de deixar o list.pop() estourar sem contexto.


### Ajustes de Desempenho e Estrutura 

Implementou-se de fato a classe Pilha como array (lista de tamanho fixo) com topo controlado manualmente e redimensionamento dinâmico (dobra de capacidade quando cheia), e a função flood_fill_iterativo() passou a usá-la para empilhar/desempilhar as posições a visitar, eliminando a recursão.

A exibição passou a montar toda a matriz em uma única string e emitir uma única chamada sys.stdout.write(), em vez de múltiplos print().

Para atender à exigência de bitmap colorido, exibir_matriz() ganhou um modo="cor" que renderiza cada célula como um bloco de pixel colorido no terminal via códigos de escape ANSI (\033[48;5;Nm), com uma paleta de 8 cores de balde de tinta (cinza, azul, laranja, amarelo, roxo, verde, rosa) inspirada na paleta do MS-Paint — o usuário escolhe a cor de preenchimento antes de rodar o flood fill, permitindo múltiplos preenchimentos coloridos na mesma matriz.

Um modo="ascii" foi mantido como alternativa para terminais sem suporte a cor.

### Refinamento dos Métodos Auxiliares (`troca` e `tamanho`)
* **Alteração realizada:**
  
A versão recursiva refatorada calcula e ajusta o limite de recursão necessário (n_linhas × n_col + margem) antes de rodar, e captura RecursionError residual com mensagem orientando o uso da versão iterativa.

A versão iterativa, usando a Pilha em array, não tem esse limite (profundidade de chamada O(1)) e por isso é a recomendada para matrizes grandes ou uso em robótica (labirintos).

Foi adicionada a função resolver_labirinto(), que interrompe a busca assim que encontra a célula de saída 'S' e devolve o caminho percorrido, em vez de preencher a matriz inteira — aplicação direta ao caso de navegação em robótica citado no enunciado

## 1.4. Evidência de Testes
*(Relatório simples dos testes de estresse executados, demonstrando que o código refatorado por você supera o código ingênuo gerado inicialmente pelo modelo).*

## 2. Problema II: Torre de Hanoi

### 2.1. Log de Iteração e Prompts
* **Prompt para solução recursiva:**
 faça um código que solucione a Torre de Hanoi com N discos usando uma rotina recursiva.

  A torre é uma pilha de n discos com raios crescentes e há 3 pinos, o objetivo é mover a pilha de discos de sua posição "pino inicial" para outro pino "Pino destino" usando como pino intermediario o terceiro pino.
  
  
  Regra de movimentação:
  
  1.     Só se pode mover um disco de cada vez, do topo de uma pilha para o topo de outra pilha;
  
  2.      Não se pode mover um disco maior para cima de um disco menor.
  
  
  O programa deve, apresentar a formação inicial e final das pilhas de discos e o número total de movimentos de discos utilizados para solucionar o problema.
  
  Permita que o usuário especifique a quantidade M de “movimentações de discos” entre duas visualizações dos pinos com as pilhas de discos, a qual deve também apresentar o número de movimentos de discos acumulados entre os dois momentos. O programa deve aguardar por um [ENTER] do usuário para prosseguir aos próximos M passos. O padrão é que o programa apresente as pilhas de discos passo a passo (M = 1), aguardando o [ENTER] do usuário para prosseguir. 
  
   formatação de saída em terminal, apresente as pilhas na vertical
  * **Código bruto retornado pela IA (Recursivo):**
  ```python
  class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.dados = []
        
    def empilha(self, dado):
        if len(self.dados) >= self.capacidade:
            raise Exception("PilhaCheiaErro")
        self.dados.append(dado)
        
    def desempilha(self):
        if not self.dados:
            raise Exception("PilhaVaziaErro")
        return self.dados.pop()
        
    def pilha_esta_vazia(self):
        return len(self.dados) == 0
        
    def pilha_esta_cheia(self):
        return len(self.dados) == self.capacidade
        
    def tamanho(self):
        return len(self.dados)


  def exibir_hanoi(pinos, n, movimentos, total_movimentos):
      print(f"\n--- Movimentos Acumulados: {movimentos} (Total: {total_movimentos}) ---")
      
    # Renderização vertical das pilhas
    # Os pinos são representados por listas. O topo da pilha é o final da lista.
    for nivel in range(n - 1, -1, -1):
        linha = []
        for pino in pinos:
            # Se a altura da pilha atingir este nível, desenha o disco
            if nivel < pino.tamanho():
                # Para exibir o disco de forma proporcional, podemos usar '#' multiplicado pelo tamanho ou valor
                # Como os discos podem ser representados por números de 1 até n:
                disco = pino.dados[nivel]
                largura = disco * 2 + 1
                bloco = "#" * largura
                # Centraliza visualmente o disco em uma coluna de largura fixa (ex: 2*n + 3)
                espacos = " " * (n - disco)
                linha.append(f"{espacos}{bloco}{espacos}")
            else:
                # Caso contrário, desenha apenas a haste central '|'
                espacos = " " * n
                linha.append(f"{espacos}|{espacos}")
        print("   ".join(linha))
    
    # Base dos pinos
    base = "-" * (2 * n + 1)
    print(f"{base}   {base}   {base}")
    print("     Pino A        Pino B        Pino C    ")
    print("=" * 45)


    def hanoi_recursivo(n, origem, destino, auxiliar, pinos, M, estado_controle):
        if n == 1:
            # Move o disco do pino de origem para o de destino
            disco = origem.desempilha()
            destino.empilha(disco)
        
        estado_controle["movimentos_bloco"] += 1
        estado_controle["total_geral"] += 1
        
        # Verifica se atingiu a quantidade M de passos para exibir
        if M > 0 and estado_controle["movimentos_bloco"] >= M:
            exibir_hanoi(pinos, estado_controle["n_discos"], estado_controle["total_geral"], estado_controle["total_geral"])
            input("Pressione [ENTER] para prosseguir...")
            estado_controle["movimentos_bloco"] = 0
        return

    # 1. Move n-1 discos da origem para o auxiliar
    hanoi_recursivo(n - 1, origem, auxiliar, destino, pinos, M, estado_controle)
    
    # 2. Move o disco restante da origem para o destino
    disco = origem.desempilha()
    destino.empilha(disco)
    
    estado_controle["movimentos_bloco"] += 1
    estado_controle["total_geral"] += 1
    
    if M > 0 and estado_controle["movimentos_bloco"] >= M:
        exibir_hanoi(pinos, estado_controle["n_discos"], estado_controle["total_geral"], estado_controle["total_geral"])
        input("Pressione [ENTER] para prosseguir...")
        estado_controle["movimentos_bloco"] = 0
        
    # 3. Move os n-1 discos do auxiliar para o destino
    hanoi_recursivo(n - 1, auxiliar, destino, origem, pinos, M, estado_controle)


    if __name__ == "__main__":
        n = int(input("Digite a quantidade de discos (N): "))
        
    # O usuário especifica a quantidade M de movimentações entre visualizações (Padrão M = 1)
    entrada_m = input("Digite a quantidade M de movimentações entre exibições (Padrão = 1): ")
    M = int(entrada_m) if entrada_m.strip() != "" else 1

    # Criação dos 3 pinos utilizando a estrutura de Pilha
    pino_a = Pilha(n)
    pino_b = Pilha(n)
    pino_c = Pilha(n)

    # Inicializa o pino A com os discos em ordem decrescente de tamanho (do maior embaixo para o menor no topo)
    # Exemplo: para N=3, empilha 3, depois 2, depois 1 no topo.
    for i in range(n, 0, -1):
        pino_a.empilha(i)

    pinos = [pino_a, pino_b, pino_c]

    print("\n--- Formação Inicial das Pilhas ---")
    exibir_hanoi(pinos, n, 0, 0)
    if M > 0:
        input("Pressione [ENTER] para iniciar a execução...")

    estado_controle = {
        "movimentos_bloco": 0,
        "total_geral": 0,
        "n_discos": n
    }

    # Executa a recursão da Torre de Hanói (Origem: A, Destino: C, Auxiliar: B)
    hanoi_recursivo(n, pino_a, pino_c, pino_b, pinos, M, estado_controle)

    print("\n--- Formação Final das Pilhas ---")
    exibir_hanoi(pinos, n, estado_controle["total_geral"], estado_controle["total_geral"])
    print(f"Resolução concluída com sucesso! Número total de movimentos: {estado_controle['total_geral']}")

## 2.2 Code Review Crítico
*(Análise da solução inicial gerada pela IA, identificando falhas de eficiência, complexidade e segurança)*

* **Eficiência**
  * A IA implementou a pilha utilizando listas nativas do Python em vez de uma estrutura de array explícita. Além disso, a função de exibição visual é executada repetidas vezes, criando um gargalo de I/O que pode deixar o programa lento para valores maiores de N.
* **Complexidade**
  * O algoritmo recursivo possui complexidade de tempo O(2^n), realizando exatamente 2^n-1 movimentos. Embora as operações da pilha, como append e pop, sejam eficientes O(1), a reconstrução da visualização no terminal a cada etapa aumenta o custo de execução. O enunciado, inclusive, exige essas visualizações entre os movimentos.
* **Segurança**
  * Falta validação adequada das entradas do usuário. Valores não numéricos causam erro e um N muito grande pode tornar a execução impraticável ou atingir o limite de recursão. Além disso, a classe Pilha não possui mecanismos próprios para impedir a colocação de um disco maior sobre um menor.

## 2.3. Justificativa de Refatoração
*(Adicionar detalhadamente quais alterações foram realizadas no código para atender aos requisitos de desempenho, correção e testes solicitados)*

Após a análise do código bruto gerado pela IA, realizamos as seguintes refatorações manuais:

### Tratamento de Exceções Obrigatórias
* **Problema inicial:**

* **Alteração realizada:**


### Ajustes de Desempenho e Estrutura 


### Refinamento dos Métodos Auxiliares (`troca` e `tamanho`)
* **Alteração realizada:**

## 2.4. Evidência de Testes
*(Relatório simples dos testes de estresse executados, demonstrando que o código refatorado por você supera o código ingênuo gerado inicialmente pelo modelo).*


