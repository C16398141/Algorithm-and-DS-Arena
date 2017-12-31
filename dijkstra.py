# initialise the graph
graph = dict() # the whole graph is a dictionary

# the graph contain the node start

graph['start'] = {} # the start has two children nodes 'a' and 'b'
graph['start']['a'] = 6 # it takes 6 units to go from start to a
graph['start']['b'] = 2 # it takes 2 units to go from start to b

''' OUTPUT of 'graph'

>>> graph
{'start': {'a': 6, 'b': 2}, 'a': {'end': 1}, 'b': {'a': 3, 'end': 5}, 'end': {}}

'''

# the graph also contain the node start
graph['a'] = {}
graph['a']['end'] = 1 # it takes one unit to go from node 'a' to the end

# this graph also contains the node b
graph['b'] = {}
graph['b']['a'] = 3 # it takes 3 units to go from 'b' to 'a'
graph['b']['end'] = 5 # it takes 5 units to go to the end from when at b

# the last node contained in the graph is the end
graph['end'] = {} # the end node points to points to nothing.(doesn't have a neighbour)










