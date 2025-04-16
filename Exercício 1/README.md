# 785. Is Graph Bipartite?

## Questão

A questão foi resolvida no LeetCode, onde você pode conferir o enunciado completo.

[Ver questão no LeetCode](https://leetcode.com/problems/is-graph-bipartite/)  

## Gravação

A resolução dessa questão foi gravada e você pode assistir ao vídeo para ver o passo a passo da solução.

[Clique aqui para assistir](COLE_AQUI_O_LINK_DA_GRAVAÇÃO)

## Dificuldade

Média

## Enunciado

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

## Exemplos

### Exemplo 1

![image](https://github.com/user-attachments/assets/adc4e548-a81c-4e6d-8413-53542506fc50)

>Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]<br>
>Output: false<br>
>Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

### Exemplo 2

![image](https://github.com/user-attachments/assets/4dc95138-76d5-4891-989e-c8d46c93bc6e)

>Input: graph = [[1,3],[0,2],[1,3],[0,2]]<br>
>Output: true<br>
>Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

## Restrições

- `graph.length == n`
- `1 <= n <= 100`
- `0 <= graph[u].length < n`
- `0 <= graph[u][i] <= n - 1`
- `graph[u]` does not contain `u`.
- All the values of `graph[u]` are unique.
- If `graph[u]` contains `v`, then `graph[v]` contains `u`.

## Submissões
