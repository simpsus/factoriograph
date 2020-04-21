import networkx as nx

input_dump = 'res/recipe_0.18.19.txt'


def read_dump(source=input_dump):
    with open(source,'r') as f:
        dump = f.read()
        dump = dump.replace('\\n','')
        dump = dump.replace(' ','')
        return dump
    
read_dump()