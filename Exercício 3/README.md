# 1761. Minimum Degree of a Connected Trio in a Graph

## Questão

A questão foi resolvida no LeetCode, onde você pode conferir o enunciado completo.

[Ver questão no LeetCode](https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/description/)  

## Gravação

A resolução dessa questão foi gravada e você pode assistir ao vídeo para ver o passo a passo da solução.

[Clique aqui para assistir](COLE_AQUI_O_LINK_DA_GRAVAÇÃO)

## Dificuldade

Difícil

## Enunciado

You are given an undirected graph. You are given an integer `n` which is the number of nodes in the graph and an array `edges`, where each `edges[i] = [ui, vi]` indicates that there is an undirected edge between `ui` and `vi`.

A connected trio is a set of three nodes where there is an edge between every pair of them.

The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.

Return the minimum degree of a connected trio in the graph, or `-1` if the graph has no connected trios.

## Exemplos

### Exemplo 1

![image](https://github.com/user-attachments/assets/89f4bcd6-1cc8-4992-ac55-5275946284cb)

>**Input:** n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]<br>
>**Output:** 3<br>
>**Explanation:** There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.

### Exemplo 2

![image](https://github.com/user-attachments/assets/7ce82c54-514e-4293-8d3b-1bad8c0f0894)

>**Input:**n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]<br>
>**Output:** 0<br>
>**Explanation:** There are exactly three trios:<br>
>1) [1,4,3] with degree 0.
>2) [2,5,6] with degree 2.
>3) [5,6,7] with degree 2.

## Restrições

- `2 <= n <= 400`
- `edges[i].length == 2`
- `1 <= edges.length <= n * (n-1) / 2`
- `1 <= ui, vi <= n`
- `ui != vi`
- There are no repeated edges.

## Submissões
