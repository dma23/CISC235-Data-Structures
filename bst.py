# create binary search tree with: 
# insert function
# getTotalHeight function
# getWeightBalanceFactor 
weight = []

class Node:
    # creates the nodes for the Binary Search Tree 
    def __init__(self, value):
        # initalizes empty left/right branches and sets a value based on the parameter
        self.left = None
        self.right = None
        self.value = value

    def insert(self, root, value):
        # inserts a new node into the binary search tree   
        # checks to see if there is already a node in place, if there is not, initalize a new node using value 
        if root == None:
            return Node(value)
        # if there is a node there, check to see if value is smaller than the current node
        elif value < root.value:
        # keep checking until you hit a node with no value 
            root.left = root.insert(root.left, value)
        # same thing as above but for values greater/equal to current node 
        else:
            root.right = root.insert(root.right, value)
        # returns new binary search tree with updated values
        return root


    def getMaxHeight(self, root):
        # to get max height, we have to find the largest path going left/right along the tree
        if root == None:
            return -1
        else: 
            # path down left/right side of the tree
            lheight = root.getMaxHeight(root.left)
            rheight = root.getMaxHeight(root.right)
            # take the bigger of the 2 paths
            if (lheight > rheight):
                return lheight + 1
            else:
                return rheight + 1
    

    def getTotalHeight(self, root):
        # iterates through each node of the BST
        # gets the max height of each node and adds them together
        if root == None:
            return 0
        else:
            return (root.getTotalHeight(root.left) + root.getMaxHeight(root) + root.getTotalHeight(root.right))


    def getWeightBalanceFactor(self, root):
        # iterates through the values of the BST
        global weight
        if root:
            root.getWeightBalanceFactor(root.left)
            weight.append(root.calcWBF(root))
            root.getWeightBalanceFactor(root.right)


    def calcWBF(self, root):
        # takes a node and calculates the max height from that node
        if root == None:
            return 0
        else: 
        # path down left/right side of the tree
            lheight = root.getMaxHeight(root.left)
            rheight = root.getMaxHeight(root.right)
        # returns the absolute difference of the left and right side
        return abs(lheight-rheight)


if __name__ == "__main__":
    # creates new BST 
    new = Node(6)
    # fills BST 
    new = new.insert(new,4)
    new = new.insert(new,9)
    new = new.insert(new,5)
    new = new.insert(new,8)
    new = new.insert(new,7)
    #new = new.insert(new,6)
    # returns the max height of the BST
    print("Total height of BST is: " ,new.getTotalHeight(new))
    new.getWeightBalanceFactor(new)
    
    print("The weight balance factor of this tree is: ", max(weight))
