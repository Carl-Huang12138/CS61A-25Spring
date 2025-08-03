#Linked Lists
class Link:
    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link), "rest must be a Link or Link.empty"
        self.first = first
        self.rest = rest

    def __str__(self):
        string = '<'
        current = self      
        while current is not Link.empty:
            string += str(current.first)
            current = current.rest
            if current is not Link.empty:
                string += ', '
        string += '>'
        return string  
    
    def __repr__(self):
        if self.rest is Link.empty:
            return f'Link({self.first})'
        else:
            return f'Link({self.first}, {self.rest})'

    def __len__(self):
        if self.rest is Link.empty:
            return 1
        else:
            return 1 + len(self.rest)

s = Link(1, Link(2, Link(3)))
s.rest.first = 7
Link(8,s.rest)

#Linked Lists Processing

def square(x):
    return x * x

def odd (x):
    return x % 2 == 1

def range_link(start, end):
    """Return a Link containing the integers from start to end."""
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))
    
def map_link(f, link):
    """Return a new Link with fn applied to each element of link."""
    if link is Link.empty:
        return Link.empty
    else:
        return Link(f(link.first), map_link(f, link.rest))
    
def filter_link(predicate, link):
    """Return a new Link with only the elements of link that satisfy predicate."""
    if link is Link.empty:
        return Link.empty
    elif predicate(link.first):
        return Link(link.first, filter_link(predicate, link.rest))
    else:
        return filter_link(predicate, link.rest)
    
#Linked Lists Mutation

def add(s,v):
    if s is Link.empty:
        return Link(v)
    elif s.first == v:
       return s    
    elif s.first > v:
        return Link(v, s)
    else:
        return Link(s.first, add(s.rest, v))
    
class Tree:
    """A tree with a label and a list of branches."""
    
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree), "branches must be Tree instances"
        self.branches = list(branches)
        
    def is_leaf(self):
        return not self.branches
    
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:   
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)
    
    def __str__(self):
        return '\n'.join(self.indented())  
    
    def indented(self, level=0):
        """Return a list of strings representing the tree, indented by level."""
        result = [' ' * (level * 2) + str(self.label)]
        for branch in self.branches:
            result.extend(branch.indented(level + 1))
        return result    
    
def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 1)
        right = fib_tree(n - 2)
        return Tree(left.label + right.label, [left, right])
    
def leaves(tree):
    """Return the number of leaves in the tree."""
    if tree.is_leaf():
        return [tree.label]
    else:
        all_leaves = []
        for branch in tree.branches:
            all_leaves.extend(leaves(branch))
        return all_leaves

def height(tree):
    """Return the height of the tree."""
    if tree.is_leaf():
        return 0
    else:
        return 1 + max([height(branch) for branch in tree.branches])
    
#Tree Mutation

def prune(tree, value):
    """Remove branches with the specified value."""
    tree.branches = [branch for branch in tree.branches if branch.label != value]
    for branch in tree.branches:
        prune(branch, value)