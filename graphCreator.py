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
        for l in data:
            if isinstance(l,dict):
                for k,v in l.items():
                    try:
                        l[k] = float(v)
                        if float(v).is_integer():
                            l[k] = int(float(v))
                    except:
                        pass                  
        return data
    
recipes = read_dump()