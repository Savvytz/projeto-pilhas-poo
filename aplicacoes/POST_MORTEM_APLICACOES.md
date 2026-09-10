## 1. Problema I: Preenchimento de Região (Flood Fill)

### 1.1. Log de Iteração e Prompts
* **Prompt para solução recursiva:**
* Desenvolva um programa que utiliza rotina recursiva para preencher uma região de uma matriz de caracteres, ou seja, uma matriz cujos elementos são apenas zeros e uns Assim, são dados a matriz de caracteres B (originalmente era uma matriz binária, porém para facilitar a visualização dos resultados optou-se pela matriz de caracteres) e uma posição inicial X (linha, coluna). A partir desta posição inicial o programa deverá preencher com 0´s as posições vizinhas até o limite das bordas preenchidas com 0´s. Se porventura a borda não formar uma figura fechada, o programa irá preencher toda a matriz com 0´s. Esta rotina é utilizada para preencher (colorir) figuras em editores tipo o Paint do MS-Windows© (onde a matriz é uma matriz de pixels), ou mesmo para percorrer labirintos (usado em robótica). Para este último, produza uma solução também.
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
* **Código bruto retornado pela IA (Interativo):**
* Desenvolva um programa que utiliza utiliza uma pilha de posições (linha, coluna)  para preencher uma região de uma matriz de caracteres, ou seja, uma matriz cujos elementos são apenas zeros e uns Assim, são dados a matriz de caracteres B (originalmente era uma matriz binária, porém para facilitar a visualização dos resultados optou-se pela matriz de caracteres) e uma posição inicial X (linha, coluna). A partir desta posição inicial o programa deverá preencher com 0´s as posições vizinhas até o limite das bordas preenchidas com 0´s. Se porventura a borda não formar uma figura fechada, o programa irá preencher toda a matriz com 0´s. Esta rotina é utilizada para preencher (colorir) figuras em editores tipo o Paint do MS-Windows© (onde a matriz é uma matriz de pixels), ou mesmo para percorrer labirintos (usado em robótica). Para este último, produza uma solução também.

    A matriz de caracteres deve ser lida de um arquivo e ser apresentada na tela antes e depois do preenchimento. Permita que o usuário especifique uma quantidade P de passos a serem executados entre cada apresentação da matriz para acompanhar a evolução do algoritmo. Se P for zero, então a rotina deverá executar até o fim sem paradas intermediárias. A cada apresentação da matriz o programa deve aguardar por um [ENTER] do usuário para prosseguir aos próximos P passos. Na página seguinte é dada uma matriz de caracteres de exemplo e a posição inicial é dada por um X (que deve virar 0 ao final da rotina). Para um melhor efeito de visualização na tela do terminal, pode-se trocar os caracteres ‘1’s por espaços em branco e os ‘0’s por um caractere que preencha mais a posição, tipo ‘@’ ou ‘#’.
    Melhore esta entrada e saída com um BITMAP, ou seja, uma matriz de Pixels. Também aceite cores diversas igual ao exemplo feito em sala de aula com o MS-Paint.
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


## QUEM FOR FAZER ESSE AQUI PODE CITAR QUE A VERSÃO GERADA POR IA NÃO IMPLEMENTOU UMA ESTRUTURA DE LEITURA EM ARQUIVO
## Outra exigência tamém não implementada pela ia foi a exigencia de renderização com bitmap, e tampouco teve o suporte a cores em estilo Microsoft PAINT, exigido no prompt inicial!!!!!

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

## 2. Problema II: Torre de Hanoi

### 2.1. Log de Iteração e Prompts
* **Prompt para solução recursiva:**
  * **Código bruto retornado pela IA (Recursivo):**
  ```python
  # [Cole aqui o código bruto inicial que a IA gerou sem alterações]

* **Prompt para solução interativa:**
* **Código bruto retornado pela IA (Interativo):**
  ```python
  # [Cole aqui o código bruto inicial que a IA gerou sem alterações]

## 2.2 Code Review Crítico
*(Análise da solução inicial gerada pela IA, identificando falhas de eficiência, complexidade e segurança nas três linguagens)*

* **Eficiência**
* **Complexidade**
* **Segurança**

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


