import sys
import unittest
MAXINT = sys.maxsize
def pairs(A, k):
    ''' Return number of pairs with distence k
    Arguments
        A: integer array
        k: distence of pairs
    Reutrns
        Return number of pairs
    '''
    hashmap = {} # New a hashmap

    # Put array into the hashmap
    for i in A:
        # Count the number of identical integers
        if i not in hashmap.keys():
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    count = 0

    for i in A:
        if i > 0 and (MAXINT - i) < k: # Avoid overflow
            break
        elif (i+k) in hashmap.keys(): # Find pairs
            count += hashmap[i+k]

    return count

class Test(unittest.TestCase):
    Array = [8, 12, 16, 4, 0, 0, 20]
    k = 4
    def test_pairs(self):
        res = pairs(self.Array, self.k)
        print ("Number of pairs = " + str(res))

if __name__ == "__main__":
    unittest.main()
