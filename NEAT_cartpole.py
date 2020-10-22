class Genome:
    def __init__(self, nodes, edge):
        self.nodes = nodes
        self.edge = edge


    def findBestNode():
        nodeList=[]

        outputnode_1 = Node(1,0,0)
        outputnode_2 = Node(2,0,0)
        nodeList.append(outputnode_1)
        nodeList.append(outputnode_2)

        for i in range(0, len(edge)-1):
            if(Genome.edge[i].output.index == outputnode_1.index):
                outputnode_1.nodeValue += edge[i].weight*edge[i].input.nodeValue
            else:
                outputnode_2.nodeValue += edge[i].weight*edge[i].input.nodeValue
        if(nodeList[0].nodeValue > nodeList[1].nodeValue):
            return nodeList[0].nodeValue
        else:
            return nodeList[1].nodeValue



    
# Nodes
class Node:
    def __init__(self, index, nodeValue, innov):
        #self.node = node
        self.index = index
        self.innov = innov
        self.nodeValue = nodeValue

# Vertecies
class Edge:
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