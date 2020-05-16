import networkx as nx
import re
from slpp import slpp

input_dump = 'res/recipe_dyworld_0.9.7_etc.txt'


def read_dump(source=input_dump):
    with open(source,'r') as f:
        dump = f.read()

    # Add quotes around hyphenated strings
    dump = re.sub(r'\w+(?:-\w+)+', r'"\g<0>"', dump)

    # Parse the dump as LUA data structure
    return slpp.decode(dump)

recipes = read_dump()

def create_graph(recipes=recipes):
    G = nx.DiGraph()
    for recipe in recipes:
        name = recipe['name'] + ' ' + recipe['category']
        G.add_node(name, energy=recipe['energy'])
        for ingredient in recipe['ingredients']:
            G.add_edge(ingredient['name'], name, amount=ingredient['amount'])
        for product in recipe['products']:
            if not 'amount' in product:
                if 'amount_min' in product:
                    amount = product['amount_min'] + (product['amount_max'] - product['amount_min']) / 2
                    G.add_edge(name, product['name'], \
                        amount=amount, amount_min=product['amount_min'], amount_max=product['amount_max'])
            else:    
                G.add_edge(name, product['name'], amount=product['amount'])
    return G

G = create_graph()