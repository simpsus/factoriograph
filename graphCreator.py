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
        data = parse(dump)
        for r in data:
            for (d,k) in [(r,'energy')] + [(i,'amount') for i in r['ingredients']]\
                 + [(p,'amount') for p in r['products']] + [(p,'probability') for p in r['products']]:
                    try:
                        d[k] = float(d[k])
                        if d[k].is_integer():
                            d[k] = int(d[k])
                    except:
                        pass
    return data
    
recipes = read_dump()

def create_graph(recipes=recipes):
    G = nx.DiGraph()
    for recipe in recipes:
        name = recipe['name'] + ' ' + recipe['category']
        G.add_node(name, energy=recipe['energy'])
        for ingredient in recipe['ingredients']:
            G.add_edge(ingredient['name'], name, amount=ingredient['amount'])
        for product in recipe['products']:
            G.add_edge(name, product['name'], amount=product['amount'])
    return G

G = create_graph()