class Genome:
    def __init__(self, nodes, genes):
        self.
    
# Nodes
class Node:
    def __init__(self, node, innov):
        self.node = node
        self.innov = innov

# Vertecies
class Gene:
    def __init__(self, in_node, out_node, weight, enabled, innov):
        # Input node
        self.input = in_node
        # Output node
        self.output = out_node
        self.weight = weight
        # Boolean
        self.enabled = enabled
        # Historic marking
        self.innov = innov