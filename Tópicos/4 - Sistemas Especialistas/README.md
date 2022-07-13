[< Página principal](../../README.md) 

### Sumário
- [1 - Introdução a Sistemas Especialistas](#1---introdução-a-sistemas-especialistas)


# 1 - Introdução a Sistemas Especialistas

AI
Dados -> Algoritmo -> Conhecimento

Ausência de Dados:
- Porque ausência de dados?
  - Problema novo:
    - Viagem a outro sistema solar
    - Seguro de novo tipo de veículo
  - Sigilo:
    - Ameaça terrorista
    - Fusão nuclear

Especialistas -> Inferência -> Base de conhecimento

Tipos:
- Sistemas Baseados em Conhecimento
- Sistemas Especialistas

Incerteza
- Sistemas especialistas são utilizados para reduzir a incerteza

Especialista
- Humano
- Perito, Especialista no Assunto (não generalista)
- Caoaz de aprender e se aperfeiçoar
- Capaz de reconhecer exceções
- Sistemas de informação que buscam emular a capacidade de decisão de um perito no assunto
- Aplicação Limitada a uma área especifica do conhecimento
- Capaz de Aprender
- Heurístico:
  - Não possui resposta pronta e exata, busca aproximação
- Lógica Difusa

Porque?
- É raro
- Perecível (envelhece, morre etc.)
- Cansa
- Não pode estar em toda parte
- Custa caro

Sistema Especialista:
- Alta disponibilidade: 24x7, em qualquer lugar
- Baixo Custo
- Duração Infinita
- Replicável

Aplicações:
- Diagnóstico médico
- Diagnóstico de mal funcionamento de sistema ou equipamento
- Agendamento
- Decisões Financeiras
- Monitoramento de Processos
- Classificação
- Segurança publica
- Mudanças climáticas

Modelo Clássico
- Proposto por R. Cooke (1991)
- Agregar a avaliação dos especialistas em uma distribuição de probabilidade


- Importância de cada consulta

- Calibração através de seeds:
  - Determinar as características, e consequentemente a importância da estimativa de um especialista através da elicitação de variáveis cujos valores reais não são conhecidos pelos especialistas
  - Isso ajuda a calibrar o peso (importância) da variável de interesse 
  - A calibração é feita com os mesmos quantis que a variável de interesse
  - Pode-se utilizar n variável de calibração
  - 