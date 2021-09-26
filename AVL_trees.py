class AVLTreeMap:


    def __init__(self, value=None, key=None):
        self.left = None
        self.right = None
        self.value = value 
        self.key = key
        self.height = 1
    
    def put(self, root, value, key):
        # inserts a new node into the binary search tree   
        # checks to see if there is already a node in place, if there is not, initalize a new node using value 
        # some code in this function was taken and modifed from the classnotes/the webpage associated with the class notes
        if root == None:
            return AVLTreeMap(value, key)
        # if there is a node there, check to see if value is smaller than the current node
        elif key < root.key:
        # keep checking until you hit a node with no value 
            root.left = root.put(root.left, value, key)
        # same thing as above but for values greater/equal to current node 
        else:
            root.right = root.put(root.right, value, key)
        # returns new binary search tree with updated values
        
        # update height 
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
 
        # check the balance of the new tree
        balance = self.getBalance(root)
 
        # if the balance is off, check cases (LL, LR, RL, RR)
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
 
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
 
        return root


    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)


    def getHeight(self, root):
    # returns the height of the current node
    # if node is empty, then there is no node, return 0
        if not root:
            return 0
        
        return root.height


    def leftRotate(self, z):
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        # Return the new root
        return y
    

    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        return y

    def printTree(self, root):
    # test function
        if root:
            root.printTree(root.left)
            print(root.value)
            root.printTree(root.right)


    def get(self, root, target_key):
        # get the value of a node by searching for its key
        # if there is not value in root, return None
        if not root:
            return None
        # if the current node = target key
        if target_key == root.key:
            return root.value
        # otherwise search left/right side based on relation to current nodes key value
        else:
            if target_key < root.key:
                return root.get(root.left, target_key)
            else:
                return root.get(root.right, target_key)
        # basically just a regular iterative search through a normal BST
        return None


    def print2DUtil(self, root, space) :
        COUNT = [10]  
        # Base case  
        if (root == None) : 
            return
    
        # Increase distance between levels  
        space += COUNT[0] 
    
        # Process right child first  
        root.print2DUtil(root.right, space)  
    
        # Print current node after space  
        # count  
        print()  
        for i in range(COUNT[0], space): 
            print(end = " ")  
        print(root.value, root.key)  
    
        # Process left child  
        root.print2DUtil(root.left, space)  


if __name__ == "__main__":
    # creates new BST 
    new = AVLTreeMap('Bob',15)
    new = new.put(new,'Anna',20)
    new = new.put(new,'Tom',24)
    new = new.put(new,'David',10)
    new = new.put(new,'David',13)
    new = new.put(new,'Ben',7)
    new = new.put(new,'Karen',30)
    new = new.put(new,'Erin',36)
    new = new.put(new,'David',25)
    # fills BST with same nodes from assignment page, but adds a key 
    new.print2DUtil(new, 0)
    # Anna
    print("Value is: ", new.get(new,20))
    # David
    print("Value is: ", new.get(new,10))
    # None
    print("Value is: ", new.get(new,12))
    # Karen
    print("Value is: ", new.get(new,30))
