import math

#given an input sorted array, output the shortest binary search tree
#do a binary search, find the middle element, make that the new node, then, recurse on both sides of the array
class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'
        

# My Solution

def minTree(arr):
    return helper(arr, 0, len(arr)-1)
    
def helper(arr, left, right):
    if left > right:
        return

    mid = math.floor((left + right) / 2)
    
 
    root = Node(arr[mid])

    root.left = helper(arr, left, mid - 1)
    root.right = helper(arr, mid + 1, right)
    
    return root

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
print(minTree(testArray))
        

