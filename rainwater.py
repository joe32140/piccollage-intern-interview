import heapq
import unittest
import sys

MAXINT = sys.maxsize

def rainwater(t_map):
    ''' Calculate the volume of trapped rainwater in 2d map
    Arguments
        t_map: terrain map, saving height of each point (2d array)

    Returns
        return the volume of trapped rainwater in 2d map
    '''

    h = [] # Heap queue
    m = len(t_map) # rows
    n = len(t_map[0]) # columns
    level = [[0]*n for _ in range(m)] # create a water level map with initializing to 0

    # add the border points into heapqueue and set level to its height
    for i in range(n): # top
        heapq.heappush(h, (t_map[0][i], 0, i))
        level[0][i] = t_map[0][i]
    for i in range(n): # bottom
        heapq.heappush(h, (t_map[m-1][i], m-1, i))
        level[m-1][i] = t_map[m-1][i]
    for i in range(1, m-1): # left
        heapq.heappush(h, (t_map[i][0], i, 0))
        level[i][0] = t_map[i][0]
    for i in range(1, m-1): # right
        heapq.heappush(h, (t_map[i][n-1], i, n-1))
        level[i][n-1] = t_map[i][n-1]

    # set other point's level to MAXINT
    for i in range(1, m-1):
        for j in range(1, n-1):
            level[i][j] = MAXINT

    # start the loop from the border points
    while len(h) != 0:
        # select the point with lowest level
        cur_level, row, col = heapq.heappop(h)
        # check if adjacent points hava a higher level, than put the point into heap queue
        if row-1 >= 0: # left point
            tmp = max(t_map[row-1][col], min(level[row-1][col], cur_level))
            if tmp != level[row-1][col]:
                level[row-1][col] = tmp
                heapq.heappush(h, (level[row-1][col], row-1, col))
        if row+1 < m: # right point
            tmp = max(t_map[row+1][col], min(level[row+1][col], cur_level))
            if tmp != level[row+1][col]:
                level[row+1][col] = tmp
                heapq.heappush(h, (level[row+1][col], row+1, col))
        if col-1 >= 0: # above point
            tmp = max(t_map[row][col-1], min(level[row][col-1], cur_level))
            if tmp != level[row][col-1]:
                level[row][col-1] = tmp
                heapq.heappush(h, (level[row][col-1], row, col-1))
        if col+1 < n: # below point
            tmp = max(t_map[row][col+1], min(level[row][col+1], cur_level))
            if tmp != level[row][col+1]:
                level[row][col+1] = tmp
                heapq.heappush(h, (level[row][col+1], row, col+1))

    volume = 0
    # calculate the trapped rainwater by (level - height) for each point
    for i in range(m):
        for j in range(n):
            volume += level[i][j] - t_map[i][j]
    return volume
class Test(unittest.TestCase):
    map1 = [[3, 5, 5, 3], [5, 1, 3, 6], [3, 8, 8, 3]]
    map2 = [[1, 2, 5, 5], [2, 1, 4, 2], [5, 3, 2, 2]]
    def test_rainwater(self):
        print "map1", self.map1        
        res = rainwater(self.map1)
        print ("Volum= " + str(res))

        print "map2", self.map2
        res1 = rainwater(self.map2)
        print ("Volum= " + str(res1))

if __name__ == "__main__":
    unittest.main()