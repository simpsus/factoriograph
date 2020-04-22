import networkx as nx
from parse_console_output import parse

input_dump = 'res/recipe_dyworld_0.9.7_etc.txt'


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
                 + [(p,'amount') for p in r['products']] + [(p,'probability') for p in r['products']]\
                 + [(p,'amount_min') for p in r['products']] + [(p,'amount_max') for p in r['products']]:
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
            if not 'amount' in product:
                if 'amount_min' in product:
                    amount = product['amount_min'] + (product['amount_max'] - product['amount_min']) / 2
                    G.add_edge(name, product['name'], \
                        amount=amount, amount_min=product['amount_min'], amount_max=product['amount_max'])
            else:    
                G.add_edge(name, product['name'], amount=product['amount'])
    return G

G = create_graph()