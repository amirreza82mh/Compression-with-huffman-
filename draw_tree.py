import graphviz
from PIL import Image

def draw_huffman_tree(root,dictioanry):
    # Create a new graph
    dot = graphviz.Digraph()

    # Add nodes and edges to the graph
    def add_node(node):
        if node.char is not None:
            dot.node(str(id(node)), label=node.char)
        else:
            dot.node(str(id(node)), label=str(dictioanry[node]))
        if node.left is not None:
            dot.edge(str(id(node)), str(id(node.left)), label='0')
            add_node(node.left)
        if node.right is not None:
            dot.edge(str(id(node)), str(id(node.right)), label='1')
            add_node(node.right)

    add_node(root)

    # Save the graph to a file
    dot.render('huffman_tree', format='png')

    # Open and show the image file
    image = Image.open('huffman_tree.png')
    image.show()