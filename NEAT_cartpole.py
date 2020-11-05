# from cartpole import observation
import gym
import numpy as np                    
import math
import random
env = gym.make('CartPole-v0')
class Genome:
    def __init__(self, observation, edges, hidden_nodes, reward):
        # Creating 4 inputnodes
        self.input_nodes = [Node(i,observation[i], 0) for i in range(len(observation))]
        # Creating 2 outputnodes
        self.output_nodes = [Node(i,0,0) for i in range(5,7)]
        self.hidden_nodes = hidden_nodes
        #Matrix with edges
        self.edges = edges
        self.reward = reward

    def best_move(self):
        for i in range(2):
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
                # print("Weight:", self.edges[0][0].weight)
                highest_value = self.output_nodes[i].value
                highest_index = self.output_nodes[i].index
        # Returns 1 or 0 which is the actions
        print(highest_index)
        return highest_index

    def feed_reward(self, reward):
        self.reward = reward
    
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

def check_edge(in_node, out_node, used_edges):
    if (in_node, out_node) not in used_edges:
        used_edges.append((in_node, out_node))
        innov = len(used_edges)
    elif (in_node, out_node) in used_edges:
        innov = used_edges.index((in_node,out_node))
    # print(used_edges)
    return innov

def best_genomes(agents):
    # Sorts list of agents by reward
    agents.sort(key=lambda x: x.reward, reverse=True)
    best_agents = agents[0:20]

    # Returns 20 best agents. 
    return best_agents

def initial_generation(observation):
    # Edges from all input nodes to all output_nodes
    used_edges = []
    init_edges = [[Edge(i, j, random.uniform(0,1), True, check_edge(i,j, used_edges)) for i in range(1,5)] for j in range(5,7)]
    # No hidden nodes at the start
    init_hidden_nodes = []
    return Genome(observation, init_edges, init_hidden_nodes, 0) 
    
    # Paal
    # def used_edges():

    #     # Tuples of input-node to output-node



# class Species():
#     def __init__(self, genomes):
#         self.specie = genomes

    # Sank
    # def sharing_function(genomes):
        # For genome in genomes:
            # Sjekker hvor mange som er innenfor treashold d
                # D = 
        # Returnere hvor mange genomes som er like innenfor verdien d

    # Sank
    # def change_reward():
        # New reward = old reward/ (sharing_function(genomes))
    
    # Ivar kan se på det
    # def pair_genome(best_agents):

def cartpole_action(best_move):
    env.render()
    observation, reward, done, info = env.step(best_move)
    return observation,reward,done,info

def main(agents):
    # Sank - drittjobben
    # Initial generation. Making 50 agents
    # Running agents
    for i in range(50):
        env.reset()
        points = 0
        while True:
            best_move = agents[i].best_move()        
            observation,reward,done,info = cartpole_action(best_move)
            agents[i].feed_observation(observation)
            # print(agents[i].edges[0][0].weight)
            # print("Points", points)
            points += reward
            # Breaks if observation values are to high
            if done:
                env.reset()
                agents[i].feed_reward(points)
                # print(agents[i].reward)
                break
                
    best_agents = best_genomes(agents)
    # childs_of_best_agents = pair_agents(best_agents)
    # new_generation = mutation(childs_of_best_agents, best_agents)
    # main(new_generation)

def first_agents():
    return [initial_generation([0,0,0,0]) for i in range(50)]



if __name__ == "__main__":
    main(first_agents())