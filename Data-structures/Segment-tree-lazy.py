'''
    Segment tree with lazy propagation. Supports two main  operations:
        - Update all elements in range [l, r] to a new value
        - Query a given operation (min, max, sum, ...) on range [l, r]
'''

#########################################################################


def build_tree(node, start, end, op=(lambda x,y: x+y)):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) >> 1
        build_tree(node<<1, start, mid)
        build_tree(node<<1|1, mid + 1, end)
        tree[node] = op(tree[node<<1], tree[node<<1|1])

def update_range(node, start, end, l, r, val, op=(lambda x,y: x+y)):
    if lazy[node]:
        tree[node] = lazy[node]
        if start != end:
            lazy[node<<1] = lazy[node]
            lazy[node<<1|1] = lazy[node]
        lazy[node] = 0
    if start > end or start > r or end < l:
        return
    if start >= l and end <= r:
        tree[node] = val
        if start != end:
            lazy[node<<1] = val
            lazy[node<<1|1] = val
        return
    mid = (start + end) >> 1
    update_range(node<<1, start, mid, l, r, val)
    update_range(node<<1|1, mid + 1, end, l, r, val)
    tree[node] = op(tree[node<<1], tree[node<<1|1])

def query_range(node, start, end, l, r, op=(lambda x,y: x+y), out_of_bound_value=0):
    if start > end or start > r or end < l:
        return out_of_bound_value
    if lazy[node]:
        tree[node] = lazy[node]
        if start != end:
            lazy[node<<1] = lazy[node]
            lazy[node<<1|1] = lazy[node]
        lazy[node] = 0
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
lazy = [0 for _ in range(len(arr)<<2)]

#########################################################################











'''    Verification test    '''
if __name__ == "__main__":
    # Passed
    # https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/help-ashu-1/editorial/
    if 0:
        n = int(input())
        arr = list(map(lambda x: int(x)&1, input().split()))

        tree = [-1 for _ in range(len(arr)<<2)]
        lazy = [0 for _ in range(len(arr)<<2)]
        build_tree(1, 0, len(arr) - 1)

        for _ in range(int(input())):
            q, a, b = map(int, input().split())
            # print(q, a, b)
            if q == 0:
                update(a-1, a-1, b&1)
            elif q == 1:
                print(b - a + 1 - query(a-1, b-1))
            else:
                print(query(a-1, b-1))
