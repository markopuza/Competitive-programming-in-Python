'''
    Implements Union-Find data structure for disjoint sets

    Supports two operations:
        - find the set of an element a
        - merge the sets of elements a and b
'''


#########################################################################


def get_set_of(a):
	parent = parents[a]
	if parent == a:
		return a
	while True:
		grandparent = parents[parent]
		if grandparent == parent:
			return parent
		parents[a] = grandparent
		a = parent
		parent = grandparent


def merge_sets(a, b):
	set_a, set_b = get_set_of(a), get_set_of(b)
	if set_a == set_b:
		return False

	if ranks[set_a] == ranks[set_b]:
		ranks[set_a] += 1
	elif ranks[set_a] < ranks[set_b]:
		set_a, set_b = set_b, set_a

	parents[set_b] = set_a
	sizes[set_a] += sizes[set_b]
	sizes[set_b] = 0
	return True


numelems = 10
parents = list(range(numelems)) # parents of trees
ranks = [0] * numelems
sizes = [1] * numelems # sizes of sets


#########################################################################


'''    Verification test    '''
if __name__ == "__main__":
    # Passed the HackerEarth problem
    # https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/count-friends/description/
    if 0:
        numelems, m = map(int, input().split())
        parents = list(range(numelems))
        ranks = [0] * numelems
        sizes = [1] * numelems
        for _ in range(m):
            merge_sets(*map(lambda x: int(x)-1, input().split()))
        print(*[sizes[get_set_of(i)]-1 for i in range(numelems)])
