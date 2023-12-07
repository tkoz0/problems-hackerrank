""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    def check(root,lo,hi):
        if not root:
            return True
        return lo <= root.data <= hi and check(root.left,lo,root.data-1) and check(root.right,root.data+1,hi)
    return check(root,0,10**4)
