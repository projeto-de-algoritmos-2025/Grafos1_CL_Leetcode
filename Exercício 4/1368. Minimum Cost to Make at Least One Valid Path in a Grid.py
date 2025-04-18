class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  # Tamanho da grade (linhas x colunas)

        # Mapeamento das direções possíveis de acordo com os números da grade:
        # 1 → direita, 2 → esquerda, 3 → baixo, 4 → cima
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Fila dupla para 0-1 BFS: custo 0 (movimento "correto") entra pela frente,
        # custo 1 (precisa alterar direção) entra por trás.
        dq = deque()
        dq.append((0, 0, 0))  # Começamos da posição (0, 0) com custo acumulado 0

        # Matriz para evitar visitar o mesmo nó várias vezes
        visited = [[False] * n for _ in range(m)]

        while dq:
            i, j, cost = dq.popleft()  # Pegamos a próxima célula da fila

            if visited[i][j]:
                continue  # Se já visitamos essa célula, pulamos
            visited[i][j] = True

            # Se chegamos no destino (última célula da grade), retornamos o custo atual
            if (i, j) == (m - 1, n - 1):
                return cost

            # Tentamos andar em todas as 4 direções (cima, baixo, esquerda, direita)
            for k, (dx, dy) in enumerate(directions):
                ni, nj = i + dx, j + dy  # Próxima posição candidata

                # Verificamos se está dentro da grade
                if 0 <= ni < m and 0 <= nj < n:
                    # Se a direção atual bate com o número da grade (1-4),
                    # então não precisamos alterar a seta (custo 0)
                    if grid[i][j] == k + 1:
                        dq.appendleft((ni, nj, cost))  # Sem custo → prioridade
                    else:
                        dq.append((ni, nj, cost + 1))  # Mudança de direção → custo 1

        # Caso não haja caminho possível (segundo o enunciado, sempre existe um)
        return -1
