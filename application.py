import dash
import dash_cytoscape as cyto
import dash_html_components as html
import networkx as nx

from graphCreator import create_graph, read_dump


# Create graph elements
input_dump = 'res/recipe_0.18.19.txt'
G = create_graph(read_dump(input_dump))
data = nx.readwrite.json_graph.cytoscape_data(G)
elements = data['elements']['nodes'] + data['elements']['edges']

# Create app
cyto.load_extra_layouts()
app = dash.Dash()
app.layout = html.Div([
    html.H1('Factorio graph network'),
    cyto.Cytoscape(
        elements=elements,
        layout={'name': 'dagre', 'rankDir': 'LR'},
        style={'width': '100%', 'height': '400px'},
        stylesheet=[
            {'selector': 'node', 'style': {
                'label': 'data(name)',
            }},
            {'selector': 'edge', 'style': {
                'curve-style': 'bezier',
                'target-arrow-shape': 'triangle',
            }}
        ],
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
