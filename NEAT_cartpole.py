# from cartpole import observation
import gym 
import numpy as np                
import math
import random
env = gym.make('CartPole-v0')
class Genome:
    def __init__(self, observation, edges, hidden_nodes, reward=0):
        # Creating 4 inputnodes
        self.input_nodes = [Node(i,observation[i], 0) for i in range(len(observation))]
        # Creating 2 outputnodes
        self.output_nodes = [Node(i,0,0) for i in range(2)]
        self.hidden_nodes = hidden_nodes
        #Matrix with edges
        self.edges = edges
        self.reward = reward
        #treger denne for species
        self.feed_observation = observation

    def best_move(self):
        for i in range(len(self.output_nodes)):
            for j in range(len(self.edges)):
                for k in range(len(self.edges[0])):
                    # Setting value of outputnodes to weight*inputnode.value
                    if self.edges[j][k].output == self.output_nodes[i].index:
                        value_of_input_node = self.input_nodes[self.edges[j][k].input].value
                        weight_of_edge = self.edges[j][k].weight
                        self.output_nodes[i].value += value_of_input_node*weight_of_edge
                    
        # Returns best move
        highest_value = 0
        highest_index = 0
        for i in range(len(self.output_nodes)):
            if self.output_nodes[i].value > highest_value:
                print("Weight:", self.edges[0][0].weight)
                highest_value = self.output_nodes[i].value
                highest_index = self.output_nodes[i].index
        # Returns 1 or 0 which is the actions
        return highest_index
    
    def feed_observation(self,observation):
        for i in range(len(observation)):
            self.input_nodes[i].value = observation[i]

    # def mutation():
            # def add_hidden_node():
    
            # def add_edge():
    
    # def pair_genome(best_agents):

    # def add_hidden_node():
    

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
    
    # Paal
    # def used_edges():
        # Tuples of input-node to output-node


class Species():
    def __init__(self, genomes):
        self.specie = genomes
    
    def sharing_function(self,genomes):
        





        genomeList = []
        for genome in genomes:
            genomeList.append(genome.observation)
        equalGenomes = 0
        for x in genomeList:
            for y in genomeList:
                if(x==y):
                    equalGenomes+=1
        # For genome in genomes:
            # Sjekker hvor mange som er innenfor treashold d
                # D = sum(genomes)???
        # Returnere hvor mange genomes som er like innenfor verdien d
        return equalGenomes

    def change_reward(self,genomes):
        reward = 0
        for genome in genomes:
            reward+=genome.reward
        return reward/(self.sharing_function(genomes))
    
    # def pair_genome(best_agents):


def initial_generation(observation):
    # Edges from all input nodes to all output_nodes
    init_edges = [[Edge(i, j, random.uniform(0,1), True, 0) for i in range(4)] for j in range(2)]
    # No hidden nodes at the start
    init_hidden_nodes = []
    return Genome(observation, init_edges, init_hidden_nodes) 

def cartpole_action(best_move):
    env.render()
    observation, reward, done, info = env.step(best_move)
    return observation,reward,done,info

def main():
    # Initial generation. Making 50 agent
    first_agents = [initial_generation([0,0,0,0]) for i in range(50)]
    for i in range(50):
        env.reset()
        while True:
            best_move = first_agents[i].best_move()        
            observation,reward,done,info = cartpole_action(best_move)
            first_agents[i].feed_observation(observation)
            # Breaks if observation values are to high
            if done:
                env.reset()
                break
        print(reward)


if __name__ == "__main__":
    main()
