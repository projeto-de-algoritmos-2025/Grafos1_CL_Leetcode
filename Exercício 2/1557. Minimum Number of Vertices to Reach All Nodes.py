class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        #conjunto de nós que possuem alguma aresta entrando neles
        has_incoming = set()

        #preenche o conjunto de todos os nós de destino (to)
        for from_node, to_node in edges:
            has_incoming.add(to_node)
        
        #os nos que nao estao em has_incoming sao os que precisamos retornar
        result = []
        for node in range(n):
            if node not in has_incoming:
                result.append(node)

        return result
