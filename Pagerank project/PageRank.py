    #This work has been done by Frederik Holbech, Janus Petersen and Christian Høst
#importing relevant modules
import networkx as nx
import random as random
import sys

#__________________________________________________#

#reading in the graph as a directed graph called G

fh=open(sys.argv[1], "rb")
G=nx.read_adjlist(fh, create_using=nx.DiGraph())
fh.close()

#__________________________________________________#

#Random Surfer

#making a function for the Random Surfer algorithm
def random_surfer(G,steps=10000000,m=0.15):
    '''This function takes a graph, G, and a number of steps, as inputs and returns the 
    top 10 most visited nodes from the Random Surfer algorithm '''
    
    #creating an empty dictionary for all the nodes
    nodes_dict = {}
    #making a list of all the nodes in G
    nodes_list = list(G.nodes())
    #randomly selecting a node from the nodes_list 
    random_node = random.choice(nodes_list)
    
    #making a dictionary containing all nodes in the graph with the value 0
    for node in nodes_list:
        nodes_dict[node] = 0
    
    #doing a random jump if random number is less than m  + moving on from dangling nodes when the surfer lands on dangling nodes
    for i in range(steps):
        if random.random() <= m or len(list(G.neighbors(random_node))) == 0: 
            #the node the surfer jumps to are random
            random_node = random.choice(nodes_list)
            
        #follow a random edge from the current node 
        else:
            random_node = random.choice(list(G.neighbors(random_node)))
        #updating the values in the dictionary consisting of nodes
        nodes_dict[random_node] += 1
    
    #creates the list of the 10 most visited nodes from the Random Surfer function
    sorted_nodes_rs = [k for k, v in sorted(nodes_dict.items(), key=lambda item: item[1], reverse=True)[:10]]

    #returning the list of nodes  
    print("For the Random Surfer:")
    print("Top 10 Nodes:", sorted_nodes_rs)

#__________________________________________________#
#PageRank

#getting the size of the graph and the number of nodes
size_of_graph = G.size()
number_nodes = len(G)

#__________________________________________________#

#reversing the edges in the graph in order to determine how many nodes point to a given node
reverse_graph = G.reverse()

#__________________________________________________#

#making a list of dangling nodes in order to distribute their importance score evenly out to all the nodes
dangling_nodes = []
for i in G.nodes:
    #if there are no edges we know it is a dangling node
    if len(list(G.neighbors(i))) == 0:
        dangling_nodes.append(i)

#__________________________________________________#

#making a function for the Pagerank algorithm
def PageRank(G):
    """This function takes a graph, G, as input and returns the top 10 most important nodes in a graph
    along with their importance score."""

    #storing the number of nodes as the variable n
    n = len(G)
    #making a list of all the nodes in G
    nodes_list = list(G.nodes())
    #creating an empty dictionary for the importance score of the nodes
    xk = {}
    #initializing the empty dictionary by multiplying S onto all the nodes in the graph outside the loop.
    #we can do this beacuse we know the sum of all entries in Xk equals 1 so it only needs to be done once
    for node in nodes_list:
        xk[node] = 1/n
    
    #setting the dampimng factor and number of iterations
    m = 0.15
    k=4
    #outer loop. we are looping k times. This is to stabalise the function
    for _ in range(k):
        #creating a new empty dictionary to store the upated importance score for each iteration
        xk_new = {}
        #first we multiply all the nodes by m cf. the formula for the approximation
        for node in nodes_list:
            xk_new[node] = m/n
            
        #summing the importance score of the dangling nodes to distribute it evenly out to the other nodes
        #in the graph
        dangling_sum = sum(xk[node] for node in dangling_nodes) / n 

            
        #updating xk_new for each node
        for node in nodes_list:
            #adding contribution from dangling nodes and multiplying by 1-m
            #i.e. the probability of doing as previous
            xk_new[node] += (1-m) * dangling_sum   
                    
            #adding contribution from a. we are adding the importance score of the nodes from the previous iteration
            for i in reverse_graph.neighbors(node):
                out_links_count = len(list(G.neighbors(i)))
                xk_new[node] += (1-m) * xk[i] / out_links_count
            
        #updating xk with the new importance scores, so that we can do an updated iteration next time
        xk = xk_new 
        
        #sorting the nodes and values to only return top 10
        sorted_nodes_pr_key = [k for k, v in sorted(xk.items(), key=lambda item: item[1], reverse=True)[:10]]
        sorted_nodes_pr_values = [v for k, v in sorted(xk.items(), key=lambda item: item[1], reverse=True)[:10]]
        sorted_nodes_dict = sorted(xk.items(), key=lambda item: item[1], reverse=True)[:10]
    
    #returning the list of top 10 nodes, their importance score and the number of iterations
    print("For the PageRank:")
    print("Top 10 Nodes:", sorted_nodes_pr_key)
    print("Importance Scores:", sorted_nodes_pr_values)
    print("Number of Iterations:", k)

#__________________________________________________#

random_surfer(G)
print("---------------")
PageRank(G)
