from busqueda_anchura import *
class TreeNode():
    def __init__(self, matrix):
        self.matrix = matrix
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        self.child = self
        self.children.append(child)
    
    def create_tree(self, matrix):
        matrix = self.matrix
        list_movements = Busqueda_anchura().possible_movements(matrix)
        for i in list_movements:
            matrix_cp = copy.deepcopy(matrix)
            row = i[0]
            col = i[1]
            new_matrix = Busqueda_anchura().do_movement(row,col)
            if self.parent == None:
                child = TreeNode(new_matrix)
                self.add_child(child)
            elif new_matrix != self.parent:
                child = TreeNode(new_matrix)
                self.add_child(child)
        return TreeNode
                
    def create_level(self):
        pass

