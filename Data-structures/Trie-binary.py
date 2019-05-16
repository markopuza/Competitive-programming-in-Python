'''
    Binary Trie with a xor-maximum operation.
'''

#########################################################################

max_size = 10**5
num_bits = 32

units = [(1<<i) for i in range(num_bits+1)]
left, right = [-1]*max_size, [-1]*max_size
size_left, size_right = [0]*max_size, [0]*max_size
counter = 1

def insert(x):
    global counter
    node = 0
    for u in units[::-1]:
        if x & u:
            if right[node] == -1:
                right[node] = counter
                counter += 1
            size_right[node] += 1
            node = right[node]
        else:
            if left[node] == -1:
                left[node] = counter
                counter += 1
            size_left[node] += 1
            node = left[node]

def max_xor_to(x):
    # gets integer in the Trie with maximal XOR sum with x
    result = 0
    node = 0
    for u in units[::-1]:
        if not (x & u):
            if right[node] == -1:
                node = left[node]
            else:
                node = right[node]
                result += u
        else:
            if left[node] == -1:
                node = right[node]
                result += u
            else:
                node = left[node]
    return result


#########################################################################






'''    Verification test    '''
if __name__ == "__main__":
    # Passed https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array
    pass
