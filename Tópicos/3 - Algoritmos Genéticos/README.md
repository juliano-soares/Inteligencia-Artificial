# 3 - Algoritmos Genéticos
São métodos heurísticos

## Evolução:
Melhoria a cada nova geração criada.

## Individuo
Ser capaz de exercer gerações

## Seleção natural
Seleção de uma vantagem genética que faz com que ele se reproduza e evolua mais. 

## Algoritmos genéticos
Buscam imitar o processo de evolução das espécies, simplificado, porém eficiente.
Aplicado em problemas de busca, otimização agendamento etc.
Diferenças: Na natureza não existe condição de parada

## Cromossomo
É uma solução proposta para o problema

## População
É o conjunto de cromossomos com proposta de solução para o problema, a população não deve ser muito pequena e também muito grande (aumenta processamento e não otimiza a solução)

## Genes
Um cromossomo é composto por genes, que podem ser valores binários, numéricos, texto etc, dependendo do problema.
Cada cromossomo carrega um conjunto diferentes de genes, ou seja, propostas diferentes para a solução do problema.

## Cruzamento/Recombinação (Crossover) 
Processo de combinar alguns cromossomos produzindo uma nova geração (descendentes). Objetiva gerar descendentes melhores, estes novos cromossomos possuem uma combinação de seus genes gerando mutações, a combinação de dois indivíduos ocorre de acordo com uma probabilidade, por exemplo (0.5, 0.7), os cromossomos são selecionados com reposição, esses pontos de cruzamento são selecionados aleatoriamente, utiliza-se um método de seleção, como por exemplo a Roleta (Roulette wheel)

> Formas de recombinação
- Ponto único
- Dois pontos

> Formas de seleção
- Seleção por roleta
  - Cromossomos mais ajustados, tem mais chances de seleção, e serão selecionados mais vezes
  - Desvantagem: cromossomos com baixa adequação tem poucas chances
- Seleção por classificação
  - Os piores cromossomos recebem uma classificação igual a 1, o segundo pior igual a 2 e assim sucessivamente
  - Assim há um balanceamento na chance de seleção dos cromossomos, mesmo os com ajuste muito baixo.

## Elitismo
A fim de não se perder alguns cromossomos com melhor adaptação, uma cópia destes é mantida sem alterações (sem crossover)  e transmitidos para novas gerações 

## Codificação
Basicamente diz qual será a estrutura dos genes do cromossomo
- Binária (O que levar na mochila)
- Permutação (Caixeiro viajante)
- Valores (Equação matemática)

## Mutação
Conjunto de características diferentes dos seus genes provindos de seus antecedentes. Cada gene pode ser modificado aleatoriamente de acordo com uma probabilidade. Normalmente a probabilidade é muito baixa (por exemplo, 0.001 ou 0.0001).

## Adaptação (Fitness)
A cada geração, quanto maior a adaptação dos descendentes, maior a chance de ele ser escolhido para produzir a próxima geração e assim aumentam as chances de sucesso (como ocorre na natureza). Na natureza, a adaptação é medida mediante o ambiente, cada Individuo recebe uma "nota", quanto maior a nota, mais chances do individuo tem de permanecer para reproduzir a próxima geração. Indivíduos com baixas notas, tem mais chances de serem descartados.

## Descendentes
Através de crossover, mutação e elitismo, uma nova geração é gerada, a geração anterior é completamente substituída, sendo a nova geração com a mesma população (cromossomos) da geração anterior.