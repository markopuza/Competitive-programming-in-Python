'''
    Implements a min-heap with a custom comparator. Runtime comparable to heapq library.
'''

#########################################################################

# custom comparator
_less = lambda x, y: x < y

def heapify(h, i):
    curr = i
    while curr < len(h):
        left, right = (curr << 1) + 1, (curr << 1) + 2
        if right >= len(h) or _less(h[left], h[right]):
            chil = left
        else:
            chil = right
        if chil >= len(h):
            break
        if not _less(h[curr], h[chil]):
            h[curr], h[chil] = h[chil], h[curr]
            curr = chil
        else:
            break

def build_heap(h):
    for i in range(min(len(h), len(h)//2+1)-1, -1, -1):
        heapify(h, i)

def _bubble_up(h, i):
    curr = i
    while curr > 0:
        par = (curr - 1) >> 1
        if _less(h[curr], h[par]):
            h[curr], h[par] = h[par], h[curr]
            curr = par
        else:
            break

def heap_add(h, v):
    h.append(v)
    _bubble_up(h, len(h)-1)

def heap_pop(h):
    if len(h) > 0:
        h[0], h[-1] = h[-1], h[0]
        ret = h.pop()
        heapify(h, 0)
        return ret

#########################################################################








'''    Verification test    '''
if __name__ == "__main__":
    # compare aganst the heapq library
    from random import randint
    import heapq as hq

    a = [randint(1, 10000) for _ in range(1000)]
    b = list(a)
    hq.heapify(a)
    build_heap(b)
    assert a == b

    while len(a) > 10:
        assert hq.heappop(a) == heap_pop(b)
        assert a == b

    for _ in range(1000):
        t = randint(-1000, 1000)
        hq.heappush(a, t)
        heap_add(b, t)
        assert a == b
