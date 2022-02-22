#Hierarchy type data structure
#Tree is a non linear data structure
#Rote node at the top of the hiearchty
#Leaf node has no nodes below it 
# Children Nodes are nodes below a node
#Nodes above a node are parent


print("Tree Traversal------------------------")
#Breadth First Search print all the nodes left to right
#Depth First Search processes the left subtree all the way to the root then middle then right

class TreeNode:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.none=None

    def printTree(self):
        print(self.data)

root=Node(10)
root.printTree()