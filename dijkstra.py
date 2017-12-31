# initialise the graph
graph = dict() # the whole graph is a dictionary

# the graph contain the node 'start'

graph['start'] = {} # the start has two children nodes 'a' and 'b'
graph['start']['a'] = 6 # it takes 6 units to go from start to a
graph['start']['b'] = 2 # it takes 2 units to go from start to b

''' OUTPUT of 'graph'

>>> graph
{'start': {'a': 6, 'b': 2}, 'a': {'end': 1}, 'b': {'a': 3, 'end': 5}, 'end': {}}

'''

# the graph also contain the node 'a'
graph['a'] = {}
graph['a']['end'] = 1 # it takes one unit to go from node 'a' to the end

# this graph also contains the node 'b'
graph['b'] = {}
graph['b']['a'] = 3 # it takes 3 units to go from 'b' to 'a'
graph['b']['end'] = 5 # it takes 5 units to go to the end from when at b

# the last node contained in the graph is the 'end'
graph['end'] = {} # the end node points to nothing. i.e it doesn't have a neighbours.


# next create a hastable to store the cost of each node
# this is the how many units it takes to come to this node counted from first node used

# e.g from start to 'a' it takes 6 units, and from start to 'b' it takes 2 units.
# but as the transversal continues this will change.
# e.g from start then b then 'a' the cost to get to 'a' will be 5, this is the '5' it
# the 2 it takes from the start to b plus the 3 it takes from b to a
# if the cost of a node is not known it is initialised to infinity

cost = {}
infinity = float('inf')

cost['a'] = 6
cost['b'] = 2
cost['end'] = infinity

# add the parents. This will add the parent of each node. usefull for bacjtracking

parent = {}
parent['a'] = 'start'
parent['b'] = 'start'
parent['end'] = Node

