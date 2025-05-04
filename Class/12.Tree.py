#Tree
def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch),'branches must be trees'
    return [label]+list(branches)
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
def is_tree(tree):
    if type(tree) != list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n<=1:
        return tree(n)
    else:
        left,right=fib_tree(n-2),fib_tree(n-1)
    return tree(label(left)+label(right),[left,right])

def leaf_counts(n):
    if is_leaf(n):
        return 1
    else:
        branch_counts =[leaf_counts(b)for b in branches(n)]
        return sum(branch_counts)

def leaves(tree):
    """Returning a list containing the leaf labels of tree"""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree) ],[])
    
def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented. """
    if is_leaf(t):
        return tree(label(t)+1)
    else:
        bs = [increment_leaves(b) for b in branches(t)] 
        return tree(label(t),bs)

def print_tree(tree,indent=0):
    print(' '*indent+str(label(tree)))
    for b in branches(tree):
        print_tree(b,indent+1)

def print_sum(t,sum):
    sum+=label(t)
    if is_leaf(t):
        print(sum)
    else:
        for b in branches(t):
            print_sum(b,sum)

def count_path(t,total):
    """Return the number of paths from the root to any node in
     tree t for which the labels along the path sum up to total"""
    if label(t) == total:
        found =1
    else:
        found = 0
    return found+sum([count_path(b,total-label(t))for b in branches(t)]) 

#Discussion 5
t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])
"""
>>> result = label(min(branches(max([t1, t2], key=label)), key=label))
6"""