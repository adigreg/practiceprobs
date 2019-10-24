class graphnode:
    def__init__(self,val):
        self.val = val 
        self.visited = False
        self.level = 0
        self.children = []

class llnode:
    def__init__(self,val,next=None):
        self.val = val
        self.next = next
    

def listsofdepths(root,lists):
  nodeq = []
  nodeq.append(root)
  lists.append(llnode(root))
  root.visited = True
  while nodeq != []:
    n = nodeq.pop(0)
    for child in n.children:
      if child.visited == False:
        child.level = n.level + 1
        if level < len(lists):
            lists[level].next = llnode(child.val)
        else:
            lists.append(llnode(child.val))
        child.visited = True
        nodeq.append(child)
   return lists