# 1368. Minimum Cost to Make at Least One Valid Path in a Grid

## Questão

A questão foi resolvida no LeetCode, onde você pode conferir o enunciado completo.

[Ver questão no LeetCode](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/?envType=problem-list-v2&envId=graph)  

## Gravação

A resolução dessa questão foi gravada e você pode assistir ao vídeo para ver o passo a passo da solução.

[Clique aqui para assistir](https://youtu.be/qTtbf-izkak)

## Dificuldade

Difícil

## Enunciado

Dada uma m x ngrade. Cada célula da grade tem um sinal que aponta para a próxima célula que você deve visitar se estiver atualmente nesta célula. O sinal de grid[i][j]pode ser:

- 1que significa ir para a célula à direita. (ou seja, ir de grid[i][j]para grid[i][j + 1])
- 2que significa ir para a célula à esquerda. (ou seja, ir de grid[i][j]para grid[i][j - 1])
- 3que significa ir para a célula inferior. (ou seja, ir de grid[i][j]para grid[i + 1][j])
- 4que significa ir para a célula superior. (ou seja, ir de grid[i][j]para grid[i - 1][j])
- Observe que pode haver alguns sinais nas células da grade que apontam para fora da grade.

Você começará inicialmente na célula superior esquerda (0, 0). Um caminho válido na grade é aquele que começa na célula superior esquerda (0, 0)e termina na célula inferior direita, (m - 1, n - 1)seguindo os sinais na grade. O caminho válido não precisa ser o mais curto.

Você pode modificar o sinal em uma célula com cost = 1. Você pode modificar o sinal em uma célula apenas uma vez .

Retorne o custo mínimo para fazer com que a grade tenha pelo menos um caminho válido .

## Exemplos

![image](https://github.com/user-attachments/assets/5af60f6e-3c35-400b-b211-7bbc408a6daf)

![image](https://github.com/user-attachments/assets/3c885060-cd32-456f-a338-71d7d7092d67)

![image](https://github.com/user-attachments/assets/a99ca5eb-98b3-4cb3-bcb5-d554cc6a7602)


## Restrições

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- 1 <= grid[i][j] <= 4

## Submissões

![image](https://github.com/user-attachments/assets/4d3f5346-1c02-4dda-aa14-2ca744a9ef57)

![image](https://github.com/user-attachments/assets/800faa73-a6d5-4943-9682-8a129f1e4cdf)
