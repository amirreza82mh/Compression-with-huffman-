import graphviz
from PIL import Image
from tkinter import Tk,Label

def draw_huffman_tree(root,dictionary):
    # Create a new graph
    dot = graphviz.Digraph()

    # Add nodes and edges to the graph
    def add_node(node):
        if node.char is not None:
            dot.node(str(id(node)), label=node.char)
        else:
            with dot.subgraph() as s:
                s.attr(rank='same')
                s.node(str(dictionary[node]), style='filled', fillcolor='lightgray')
            
        if node.left is not None:
            if node.left.char is not None:
                dot.edge(str(dictionary[node]), str(id(node.left)), label='0')
            else:
                dot.edge(str(dictionary[node]), str(dictionary[node.left]), label='0')
            add_node(node.left)

        if node.right is not None:
            if node.right.char is not None:
                dot.edge(str(dictionary[node]), str(id(node.right)), label='0')
            else:
                dot.edge(str(dictionary[node]), str(dictionary[node.right]), label='0')
            add_node(node.right)

    add_node(root)

    dot.render('huffman_tree', format='png')

    # Open and show the image file
    image = Image.open('huffman_tree.png')
    image.show()