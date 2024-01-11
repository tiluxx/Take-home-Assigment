class NestedSetModel:
    def __init__(self):
        self.root = None
        self.cur_right = None
        self.relationships = {}
    
    # Convert hierarchical data into the nested set model
    def covert_to_nested_set(self, hierarchy_data_root):
        # Initialize the root node
        if self.root is None:
            hierarchy_data_root.left = 1
            hierarchy_data_root.right = 2
            self.root = hierarchy_data_root
            self.cur_right = 2
        else:
            hierarchy_data_root.left = self.cur_right
            self.cur_right += 1
            
        # Iterate over the children
        for child in hierarchy_data_root.children:
            self.covert_to_nested_set(child)
            
        hierarchy_data_root.right = self.cur_right
        self.cur_right += 1
        self.root.right = self.cur_right
      
    # Retrieve Parent-Child relationships
    def get_relationships(self):
        self.get_relationships_wrapper()
        return self.relationships
                
    def get_relationships_wrapper(self, child_node=None):
        if child_node is None:
            for child in self.root.children:
                self.relationships.setdefault(self.root.id, [])
                self.relationships[self.root.id].append(self.get_relationships_wrapper(child))
        else:
            for child in child_node.children:
                self.relationships.setdefault(child_node.id, [])
                self.relationships[child_node.id].append(self.get_relationships_wrapper(child))
            return child_node.id