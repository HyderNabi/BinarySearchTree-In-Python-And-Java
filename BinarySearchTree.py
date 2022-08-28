#Author : Hyder Nabi
#TOODO : Binary Search Tree Using Python

class Node:
   def __init__(self,value):
       self.value = value
       self.left = None
       self.right = None

#End of the class Node
#:::::::::::::::::::::::::::::::::::::::::::::::::::::CLASS BST::::::::::::::::::::::::::::::::::::::::::::::::
class BST:
    #INITIALIZATION SEQUENCE
    def __init__(self):
        self.root = None

    #::::::::::::::::INTERFACE/OPERATIONS::::::::::::::
    def Create(self,list):
        self.root = self.B_Create(list)
    def Insert(self,value):
        self.root = self.B_Insert(self.root,value)
    def Delete(self,value):
        self.root = self.B_Delete(self.root,value)
    def InOrder(self):
        self.B_InOrder(self.root)
    def PreOrder(self):
        self.B_PreOrder(self.root)
    def PostOrder(self):
        self.B_PostOrder(self.root)
    #::::::::::::::::END:::::::::::::::::::::::::::::::

    #::::::::::::::::GET ROOT::::::::::::::::::::::::::
    def GetRoot(self):
        return self.root
    #::::::::::::::::END:::::::::::::::::::::::::::::::


    #::::::::::Create BST Function ::::::::::::::::
    def B_Create(self,list):
        for i in list:
            self.root = self.B_Insert(self.root, i)
        return self.root
    #:::::::::::::::END:::::::::::::::


    #::::::Insert into the Binary Search Tree:::::::::
    def B_Insert(self,root,value):
       if root is None:
           temp = Node(value)
           root = temp
       else:
           if root.value<=value:
                root.right = self.B_Insert(root.right,value)
           else:
                root.left = self.B_Insert(root.left,value)
       return root
    #:::::::::::::::END::::::::::::::::::::::::::


    #:::::::DELETION FUNCTION::::::::::::::;
    def B_Delete(self,root,value):
        if root is None:
            print("Node Not Found")
            return
        #IF A VALUE IS GREATER THAN THE NODE ---> VISIT THE RIGHT SUBTREE
        if value > root.value:
            root.right = self.B_Delete(root.right,value)
            return root
        # IF A VALUE IS LESS THAN THE NODE ---> VISIT THE LEFT SUBTREE
        elif value < root.value:
            root.left = self.B_Delete(root.left,value)
            return root
        else: #IF THE NODE IS EQUAL TO THE VALUE(MATCH FOUND)
            #IF THE NODE WITH NO CHILD------> JUST DELETE THE NODE
            if root.left is None and root.right is None:
                return None
            #IF NODE WITH THE RIGHT CHILD ONLY----->SWAP WITH CHILD AND DELETE THE CHILD
            elif root.left is None:
                temp = root.right
                root = None
                return temp
            # IF NODE WITH THE LEFT CHILD ONLY----->SWAP WITH CHILD AND DELETE THE CHILD
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                #IF A NODE HAVE BOTH CHILDREN
                #THEN FIND THE LARGEST PREDECESSOR OF IT
                #AND REPLECE THE VALUE OF THE NODE WITH THE LARGEST PREDESSOR
                #NODE AND DELETE THE LARGEST PREDESSOR RECURSIVELY
                largest = self.FindLargestPredecessor(root.left)
                root.value = largest.value
                root.left = self.B_Delete(root.left,largest.value)
                return root
    #:::::::::::END:::::::::::::::::



    #:::::::::FIND THE LARGEST PREDESSOR OF THE GIVEN NODE::::::::::
    def FindLargestPredecessor(self,root):
        if root is None or root.right is None:
            return root
        else:
            return self.FindLargestPredecessor(root.right)
    #:::::::::::::::::::::END:::::::::::::::::::

    #::::::::::INORDER TRAVERSAL::::::::::::::::::::::::;
    def B_InOrder(self,root):
        if root is None:
            return
        else:
            self.B_InOrder(root.left)
            print(root.value)
            self.B_InOrder(root.right)
    #:::::::::::::::::END::::::::::::::::::

    #::::::::::::PREORDER TRAVERSAL:::::::::::::::
    def B_PreOrder(self,root):
        if root is None:
            return
        else:
            print(root.value)
            self.B_InOrder(root.left)
            self.B_InOrder(root.right)
    #::::::::::::END:::::::::::::::;


    #:::::::::POST ORDER TRAVERSAL::::::::::::::
    def B_PostOrder(self,root):
        if root is None:
            return
        else:
            self.B_PostOrder(root.left)
            self.B_PostOrder(root.right)
            print(root.value)
    #:::::::::::::::::::END:::::::::::::::

#:::::::::::::::::::::::::::::::::::::::::::::::::::::End of the class BST:::::::::::::::::::::::::::::::::


myTree = BST()
myTree.Create([100, 200, 34, 12, 67, 54, 34, 56, 300, 150, 175, 140, 400, 270])
myTree.Insert(600)
myTree.Delete(100)
myTree.PostOrder()