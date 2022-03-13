# Aprendizagem por Reforço com Deep Learning, PyTorch e Python

## O que é aprendizagem por reforço?
> Descrição
    - É a capacidade de um agente aprender com base de seus erros, e a casa vez que o agente aprende algo ele recebe uma recompensa ou não fazendo com que ele sempre busque a melhor solução para que ele receba a maior quantidade de recompensas.

> Componente
- Ambiente
- Estado
- Recompensa
- Ação
- Agente

## A equação de Bellman
> Conceitos
- s - Estados
- a - Ação
- R - Recompensa
- γ - Fator de Desconto

~~~~
V(S) = max(R(s, a) + γV(s'))
        a
~~~~

## Markov Decision Process - MDP
