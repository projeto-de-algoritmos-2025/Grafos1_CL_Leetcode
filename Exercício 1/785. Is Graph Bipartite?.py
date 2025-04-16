from collections import deque

class Solution:
    def isBipartite(self, graph):
        """
        Verifica se um grafo é bipartido utilizando BFS.

        Parâmetros:
        - graph: Lista de adjacência representando um grafo não direcionado.

        Retorna:
        - True se o grafo for bipartido, False caso contrário.
        """

        n = len(graph)  # Número de vértices no grafo
        color = [-1] * n  # Inicializamos todas as cores como -1 (não visitado)

        # Verificamos todos os vértices, pois o grafo pode ser desconexo
        for start in range(n):
            if color[start] == -1:
                # Iniciamos uma BFS a partir do vértice não visitado
                queue = deque([start])
                color[start] = 0  # Atribuímos uma cor inicial (0)

                while queue:
                    node = queue.popleft()
                    # Iteramos sobre os vizinhos do vértice atual
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            # Se ainda não foi colorido, atribuimos a cor oposta
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            # Se o vizinho já tem a mesma cor, não é bipartido
                            return False
        # Se passamos por todos os vértices sem conflitos de cor, o grafo é bipartido
        return True
