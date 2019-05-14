'''
    Finds longest common substring of two strings.

    The DP approach takes O(|a||b|) time.
'''


#########################################################################


# DP approach
def lcss(a, b):
    max_len, max_substring = 0, []
    a += [max(a+b)+1]
    b += [a[-1]+1]
    suffixes = sorted([a[i:] for i in range(len(a)-1)] + [b[i:] for i in range(len(b)-1)])
    previous = suffixes[0]
    for current in suffixes[1:]:
        if previous[-1] != current[-1]:
            for i, c in enumerate(previous):
                if c != current[i]:
                    break
            else:
                i = len(previous)
            if i > max_len:
                max_len = i
                max_substring = previous[:i]
        previous = current
    return max_substring



#########################################################################







'''    Verification test    '''
if __name__ == "__main__":
    for a in [[-1,-2,-3,4,-5,5], [0,-1,-2,-3], [], [0], [2, -2, 1, 2, -1, 3, -1, -1, -1]]:
        for b in [[-1,-2,-3,4,-5,5], [1, -1,-2,-3], [], [0], [2, -2, 1, 2, -1, 3, -1, -1, -1]]:
            if a<=b:
                print('Longest common substring of:\n    {:s}\n    {:s}'.format(str(a), str(b)))
                print('is: {:s}\n'.format(str(lcss(a,b))))
