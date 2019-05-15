'''
    Segment tree with lazy propagation. Supports two main  operations:
        - Update all elements in range [l, r] to a new value
        - Query a given operation (min, max, sum, ...) on range [l, r]
'''

#########################################################################

# Short implementation

def build_tree(node, start, end, op=(lambda x,y: x+y)):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) >> 1
        build_tree(node<<1, start, mid)
        build_tree(node<<1|1, mid + 1, end)
        tree[node] = op(tree[node<<1], tree[node<<1|1])

def update_range(node, start, end, l, r, val, op=(lambda x,y: x+y)):
    if start > end or start > r or end < l:
        return
    if start >= l and end <= r:
        tree[node] = val
        return
    mid = (start + end) >> 1
    update_range(node<<1, start, mid, l, r, val)
    update_range(node<<1|1, mid + 1, end, l, r, val)
    tree[node] = op(tree[node<<1], tree[node<<1|1])

def query_range(node, start, end, l, r, op=(lambda x,y: x+y), out_of_bound_value=0):
    if start > end or start > r or end < l:
        return out_of_bound_value
    if start >= l and end <= r:
        return tree[node]
    mid = (start + end) >> 1
    return op(query_range(node<<1, start, mid, l, r), query_range(node<<1|1, mid + 1, end, l, r))

def update(l, r, val):
    ''' Updates all elements in [l, r] to val. inclusive, indexed from 0 '''
    update_range(1, 0, len(arr) - 1, l, r, val)

def query(l, r):
    ''' inclusive, indexed from 0'''
    return query_range(1, 0, len(arr) - 1, l, r)

arr = []
tree = [-1 for _ in range(len(arr)<<2)]
build_tree(1, 0, len(arr) - 1)





#########################################################################

# Class ortiented implementation

class Node(object):
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total, self.left, self.right = 0, None, None

class SegmentTree(object):
    def operation(self, x, y):
        return max(x, y)

    def __init__(self, nums):
        def createTree(nums, l, r):
            if l > r:
                return None
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            mid = (l + r) // 2
            root = Node(l, r)
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            root.total = self.operation(root.left.total, \
                root.right.total)
            return root
        self.root = createTree(nums, 0, len(nums)-1)

    def update(self, i, val):
        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val
            mid = (root.start + root.end) // 2
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            root.total = self.operation(root.left.total, \
                root.right.total)
            return root.total
        return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            mid = (root.start + root.end) // 2
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            else:
                return self.operation(rangeSum(root.left, i, \
                    mid), rangeSum(root.right, mid+1, j))
        return rangeSum(self.root, i, j)



#########################################################################






'''    Verification test    '''
if __name__ == "__main__":
    # Passed
    # https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/help-ashu-1/editorial/
    pass
