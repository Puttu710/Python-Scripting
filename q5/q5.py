import array as arr
count=0
class newNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None

def insertLevelOrder(arr, root, i, n):   
    if i < n: 
        temp = newNode(int(arr[i]))  
        root = temp  
        root.left = insertLevelOrder(arr, root.left,2 * i + 1, n)    
        root.right = insertLevelOrder(arr, root.right,2 * i + 2, n) 
    return root

def Leaves(root): 
    if(root): 
        Leaves(root.left)  
        if root.left is None and root.right is None: 
            if(root.data!= -1):
                global count
                print(root.data)
                count=count+(root.data) 
        Leaves(root.right)

def LeftBoundary(root): 
    global count  
    if(root): 
        if (root.left):
            if(root.data!=-1):
                print(root.data) 
                count=count+(root.data) 
            LeftBoundary(root.left) 
          
        elif(root.right):
            if(root.data!=-1):
                print(root.data)
                count=count+(root.data) 
            LeftBoundary(root.right)        

def RightBoundary(root): 
    global count  
    if(root): 
        if (root.right):
            if(root.data!=-1):
                print(root.data)
                count=count+(root.data) 
            RightBoundary(root.right) 
             
          
        elif(root.left):
            if(root.data!=-1):
                print(root.data)
                count=count+(root.data) 
            RightBoundary(root.left) 
                               

size=int(input())
arr=[]
for i in range(0,size):
    x=int(input())
    arr.append(x)
root=None
root=insertLevelOrder(arr,root,0,size)
count=count+(root.data)
print(root.data) 
LeftBoundary(root.left)
Leaves(root.left) 
Leaves(root.right)
RightBoundary(root.right)
print(count) 


