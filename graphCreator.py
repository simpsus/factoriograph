import networkx as nx
from parse_console_output import parse

input_dump = 'res/recipe_0.18.19.txt'


def read_dump(source=input_dump):
    with open(source,'r') as f:
        dump = f.read()
        dump = dump.replace('/n','')
        dump = dump.replace(' ','')
        dump = dump.replace('\n','')
        dump = dump.replace('=',':')
        return parse(dump)
    
recipes = read_dump()