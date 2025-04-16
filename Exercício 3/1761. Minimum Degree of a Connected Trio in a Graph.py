class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        """
        Encontra o grau mínimo de um trio conectado em um grafo não direcionado.

        Parâmetros:
        - n: Número de vértices no grafo.
        - edges: Lista de arestas, onde cada aresta conecta dois vértices.

        Retorna:
        - O menor grau externo de um trio conectado (3 vértices conectados entre si),
          ou -1 se não houver nenhum trio conectado.
        """

        # Cria uma matriz de adjacência para verificar conexões rapidamente
        connected = [[False] * (n + 1) for _ in range(n + 1)]

        # Array para armazenar o grau de cada vértice
        degree = [0] * (n + 1)

        # Preenche a matriz de adjacência e os graus dos vértices
        for u, v in edges:
            connected[u][v] = True
            connected[v][u] = True
            degree[u] += 1
            degree[v] += 1

        # Inicializa a variável com infinito para buscar o mínimo grau
        min_degree = float('inf')

        # Percorre todas as combinações de trios (i, j, k)
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if connected[i][j]:  # i e j devem estar conectados
                    for k in range(j + 1, n + 1):
                        # Verifica se os três vértices formam um trio completamente conectado
                        if connected[i][k] and connected[j][k]:
                            # Soma os graus dos três vértices e subtrai 6 (as 3 arestas internas ao trio são contadas 2 vezes)
                            total = degree[i] + degree[j] + degree[k] - 6
                            # Atualiza o menor grau externo encontrado
                            min_degree = min(min_degree, total)

        # Se não encontrou nenhum trio conectado, retorna -1
        return min_degree if min_degree != float('inf') else -1
