[< Página principal](../../README.md)
# 2 - Algoritmos de Busca e Otimização


Existem problemas computadores que (ainda) não resolvidos com uma equação ou fórmula. É preciso buscar uma possível entre todas as soluções possíveis (espaço de busca).

## Para muitos destes problemas, se acredita que tal equação não existe

Exemplos de problemas:
- Problema do caixeiro viajante
- Jogos de tabuleiro e quebra-cabeça
- Problemas de encontrar caminhos
- Problemas de agendamentos
- Problemas lógicos e matemáticos
- Otimização de espaços

## Porque não sempre uma busca completa?

Na maioria dos problemas e impossível do ponto de vista de tempo e custo computacional

## Diferentes problemas, muitas soluções

Não existe um algoritmo que atenda de forma ótima todos os tipos de problema!
Quanto mais informações temos do objetivo da busca, mas fácil ela fica

- Diferentes técnicas buscam otimização o processo de busca de uma solução:
  - Redução do espaço de busca de uma soluçãoAlgoritmos Heurísticos
  - Elementos Estocásticos (não determinísticos)

## Classificação dos Algoritmos

- Solução? 
  - Existem garantia que o algoritmo encontrará uma solução?
- Solução ótima? 
  - A solução encontrada, será a melhor?
- Complexidade de tempo.
  - Quanto tempo o algoritmo vai levar?
- Complexidade de espaço.
  - Quanta memória o algoritmo vai precisar?

## Elementos de um problema de busca

- S: conjunto finito de estados: Search Space
- I: conjunto finito de estados iniciais
- O: conjunto finito de objetivos
- FS: função que recebe o estado atual e retorna os estados alcançáveis
- FC: função de custo, recebe o estado atual e um possível estado, e retorna o custo

## Busca Local vs Global

Global: buscam a melhor solução global teoricamente explorando todo o espaço de busca. Encerram quando se encontra a melhor solução global, expira um tempo determinado de busca ou quando exploram todo o espaço de busca.

Local: buscam a melhor solução na região ou nas "vizinhanças". Encerram quando expira um tempo determinado ou quando não consegue melhorar o resultado a partir de uma função de avaliação.

## Local Optima

- Alguns algoritmos buscam uma solução nas proximidades (vizinhanças)
- Nestas vizinhanças eles podem encontrar uma solução, que localmente é a melhor
- Quanto menos a vizinhanças estabelecida, mais rápido ele vai encontrar a melhor solução local
- Não há garantia de que esta seja a melhor solução global

## Função de Avaliação (Custo)

- Objective function: diz o quanto boa está a solução encontrada
- (Função de custo, função de adaptação)
- Posso avaliar se o resultado é a solução ótima global:
  - Equação matemática ou lógica
  - Quebra cabeças
- Só posso avaliar se a solução é boa, mas não ótima global:
  - Jogada em jogo de tabuleiro
  - Rota do caixeiro viajante
- Difícil (ou impossível) avaliar a qualidade da solução
  - Caminho

## Transformação do mapa em Grafo

- Nodo no inicio
- Nodo no fim
- Nodo a cada divisão no labirinto (intermediários)
- Nodo a cada ponto sem saída (local optima)
- Apenas o nodo de inicio e os intermediários podem ter mais de uma aresta

## Projetos
- Linguagem R:
  - [01 - Problema da loja 711 - R](./Projetos/Tabu%20Search/R/01/Problema%20da%20Loja%20711.md)

### Heuristic
- [Manhattan]()
- [Euclidean]()
- [Octile]()
- [Chebyshev]()
## Algoritmos
- [Hill Climbing](#hill-climbing)
- [Best First search](#best-first-search)
- [Tabu Search](#tabu-search)
- [Simulated Annealing](#simulated-annnealing-arrefecimento-simulado)
- [BFS - (Breadth-First Search)](#breadth-first)
- [DFS - (Depth-First Search)](#depth-first-search)
- [Dijkstra](#-dijkstra)
- [Jump Point Search](#-jump-point-search)
- [Orthogonal Jump Point Search](#-orthogonal-jump-point-search)
- [A*](#A*)
- [Iterative Deepening (IDA*)]()
- [Alpha-beta pruning]()
- [Bachtracking]()
- [Beam search]()
- [Branch and bound]()
- [British Museum algorithm]()
- [Iterative deepening depth-first search]()
- [Lexicographic breadth-first search]()
- [Shortestpath]()
- [B*]()
- [Bellman-Ford algorithm]()
- [Bidirectional search]()
- [D*]()
- [Floyd-Warshall algorithm]()
- [Fringe search]()
- [Iterative Deepening (IDA*)]()
- [Johnson's algorithm]()
- [Kruskal's algorithm]()
- [Lifelong Planning A* (LPA*)]()
- [Simplified Memory Bounded A*]()

---
### Hill Climbing
- Inicia a busca em um único ponto
- Escolhe um novo ponto na vizinhança
- Se o novo ponto é uma solução melhor, passa a ser a melhor solução
- Se não, escolhe um novo ponto na vizinhança
- Até não ter mais como subir ou acabar o tempo
- Tem grande probabilidade de ficar preso no local optima
- Reiniciar o algoritmo com esperança de ter uma solução melhor
- Segue apenas em um sentido, explorando a "vizinhança"
- Não garante obter o global optima
- Existem muitas variações, principalmente incluindo elementos não determinísticos no algoritmo
---
### Best First search
- Usa heurística para avaliar o valor de cada nó
- Sua performance depende da heurística
---
### Tabu Search
- Mantém uma lista de locais proibidos (Tabu) em memória
- Proibidos ou por já terem sido visitados ou por não otimizarem a função objetivo
- Bom para problemas combinatórios
- Critério de parada: número de iterações, tempo, iterações sem melhoria na função objetivo
--- 
### Simulated Annnealing (Arrefecimento Simulado)
- Principio básico: não busca sempre a otimização, mas também explorar
  - (subir VS explorar) 
- Annealing: processo de aquecer e resfriar metal para alterar sua estrutura. Quando ocorre o resfriamento o metal tende a manter a nova estrutura
- Uma variável "temperatura" é criada
  - A "temperatura" é  alterada  dinamicamente
  - Com "temperatura" alta, o algoritmo vai explorar soluções que aparentemente não otimizam a função objeto, saindo de um local optima
  - Com "temperatura" baixa, o algoritmo tende a explorar a vizinhança e aceitar o local optima, que pode estar mais próximo do global ótima
---
### BFS - (Breadth-First Search)
- Capaz de retornar de uma vizinhança em busca de uma solução melhor
  - "Backtracing"
---
### DFS - (Depth-First Search)
- Explora uma vizinhança, retornando e tentando outras ramificações
---
### Dijkstra


---
### Jump Point Search
---
### Orthogonal Jump Point Search
---
### A*
---