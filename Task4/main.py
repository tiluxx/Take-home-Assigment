from node import Node
from nested_set import NestedSetModel

if __name__ == "__main__":
    hierarchical_data = Node(id=1, children=[
        Node(id=2),
        Node(id=3),
        Node(id=4),
        Node(id=5, children=[
            Node(id=6),
            Node(id=7, children=[
                Node(id=8),
                Node(id=9),
            ]),
        ]),
    ])
    
    nested_set = NestedSetModel()
    nested_set.covert_to_nested_set(hierarchical_data)
    relationships = nested_set.get_relationships()
    for parent, children in relationships.items():
        print('Parent: {}, children: {}'.format(parent, children))