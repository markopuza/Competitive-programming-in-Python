''' Finds the maximum subarray sum of a. '''


#########################################################################

def max_subarray(a):
    max_so_far = max_ending_here = 0
    for el in a:
        # in case a speed-up is required, change the below max/min to if-else statements.
        max_ending_here = max(0, max_ending_here + el)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


#########################################################################




'''    Verification test    '''
if __name__ == "__main__":
    for arr in [[-1,2,-3,4,-5,5], [-1,-2,-3], [], [0], [2, -2, 1, 2, -1, 3, -1, -1, -1]]:
        print('{:s} has maximum subarray sum {:d}.'.format(str(arr), max_subarray(arr)))
