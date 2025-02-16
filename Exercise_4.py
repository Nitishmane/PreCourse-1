# Python program to insert element in binary tree
class newNode():

    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


""" Inorder traversal of a binary tree"""


def inorder(temp):
    if temp:
        inorder(temp.left)
        print(temp.key)
        inorder(temp.right)


"""function to insert element in binary tree """


def insert(temp, key):
    if temp is None:
        temp = newNode(key)
        return temp
    elif temp.key > key:
        temp.left = insert(temp.left,key)
    elif temp.key < key:
        temp.right = insert(temp.right,key)
    return temp



# Driver code
if __name__ == '__main__':
    root = newNode(10)
    insert(root,11)
    insert(root,7)
    insert(root,9)
    insert(root,15)
    insert(root,8)
    # root.left = newNode(11)
    # root.left.left = newNode(7)
    # root.right = newNode(9)
    # root.right.left = newNode(15)
    # root.right.right = newNode(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    key = 12
    insert(root, key)

    print()
    print("Inorder traversal after insertion:", end=" ")
    inorder(root)