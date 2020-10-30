# from cartpole import observation
import gym                    
import math
import random
env = gym.make('CartPole-v0')
class Genome:
    def __init__(self, observation, edges, hidden_nodes, reward):
        # Creating 4 inputnodes
        self.input_nodes = [Node(i,observation[i], 0) for i in range(len(observation))]
        # Creating 2 outputnodes
        self.output_nodes = [Node(i,0,0) for i in range(2)]
        self.hidden_nodes = hidden_nodes
        #Matrix with edges
        self.edges = edges
        self.reward = reward

    def best_move(self):
        for i in range(len(self.output_nodes)):
            for j in range(len(self.edges)):
                for k in range(len(self.edges[0])):
                    # Setting value of outputnodes to weight*inputnode.value
                    if self.edges[j][k].output == self.output_nodes[i].index:
                        value_of_input_node = self.input_nodes[self.edges[j][k].input].value
                        weight_of_edge = self.edges[j][k].weight
                        self.output_nodes[i].value += value_of_input_node*weight_of_edge
                        # print(self.output_nodes[i].value)
                    
        # Returns best move
        highest_value = 0
        highest_index = 0
        for i in range(len(self.output_nodes)):
            if self.output_nodes[i].value > highest_value:
                # print(highest_value)
                # print("Weight:", self.edges[0][0].weight)
                highest_value = self.output_nodes[i].value
                highest_index = self.output_nodes[i].index
        # Returns 1 or 0 which is the actions
        return highest_index
    
    def feed_reward(self, reward):
        self.reward = reward
    
    def feed_observation(self,observation):
        for i in range(len(observation)):
            self.input_nodes[i].value = observation[i]
    
    # def add_node():
    # Splits existing connection and puts inside node between
    # Old connection is disabled
    # New connection into the new node is weighted 1
    # New connection out of the new node is weighted the same as previous
    
    # def add_connection():
    # Connection two unconnected nodes
        
    # def mutation():
    
    # def pair_best_genome():

    # def pairing(self, best_genomes):
        


# Nodes
class Node:
    def __init__(self, index, value, innov):
        # The index of the node
        self.index = index
        self.value = value
        self.innov = innov
    

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

def best_genomes(agents):
    # Sorts list of agents by reward
    agents.sort(key=lambda x: x.reward, reverse=True)
    best_agents = agents[0:20]

    # Returns 20 best agents. 
    return best_agents

def initial_generation(observation):
    # Edges from all input nodes to all output_nodes
    init_edges = [[Edge(i, j, random.uniform(0,1), True, i*(j+1)) for i in range(4)] for j in range(2)]
    # No hidden nodes at the start
    init_hidden_nodes = []
    return Genome(observation, init_edges, init_hidden_nodes, 0) 

def cartpole_action(best_move):
    env.render()
    observation, reward, done, info = env.step(best_move)
    return observation,reward,done,info

def main(agents):
    # Initial generation. Making 50 agents
    for i in range(50):
        print(agents[i].reward)
        env.reset()
        points = 0
        while True:
            best_move = agents[i].best_move()        
            observation,reward,done,info = cartpole_action(best_move)
            agents[i].feed_observation(observation)
            print("Points", points)
            points += reward
            # Breaks if observation values are to high
            if done:
                env.reset()
                agents[i].feed_reward(points)
                break
    best_agents = best_genomes(agents)
    # childs_of_best_agents = pair_agents(best_agents)
    # new_generation = mutation(childs_of_best_agents, best_agents)
    # main(new_generation)

def first_agents():
    return [initial_generation([0,0,0,0]) for i in range(50)]



if __name__ == "__main__":
    main(first_agents())