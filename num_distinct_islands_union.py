# We may perform an addLand operation which turns the water at position (row, col) into a land.
# Given a list of positions to operate, count the number of islands after each addLand operation.

# My solution:
    # maintain a matrix label to store the current islands and their labels
    # check positions to update their label
        # if label[position] > 0: continue
        # if label[position] == -1 and no label around:
            # add label and update parent and island_set
        # if label[position] with only one island label around:
            # update label
        # if label[position] with several islands label around:
            # update label and check the other labels to union, update island_set and parent


class Solution(object):
    def num_distinct_islands(self, m, n, positions):
        label = [[-1] * n for _ in range(m)]
        parent = []
        islands_set = set()
        color = 0
        res = []

        def check(x, y):
            r = set()
            if x-1 >= 0 and label[x-1][y] >= 0:
                r.add(label[x-1][y])
            if x+1 < m and label[x+1][y] >= 0:
                r.add(label[x+1][y])
            if y-1 >= 0 and label[x][y-1] >= 0:
                r.add(label[x][y-1])
            if y+1 < n and label[x][y+1] >= 0:
                r.add(label[x][y+1])
            return list(r)

        def find_parent(i):
            if parent[i] != i:
                parent[i] = find_parent(parent[i])
            return parent[i]

        for x,y in positions:
            if label[x][y] >= 0:
                continue
            candidate = check(x, y)
            if len(candidate) == 0:
                label[x][y] = color
                parent.append(color)
                islands_set.add(color)
                color += 1
            elif len(candidate) == 1:
                label[x][y] = candidate[0]
            else:
                label[x][y] = candidate[0]
                a = find_parent(candidate[0])
                for i in range(1, len(candidate)):
                    b = parent[candidate[i]]
                    if b != a:
                        parent[b] = a
                        islands_set.remove(b)
            res.append(len(islands_set))
        return res


s = Solution()
m = 3
n = 3
positions = [[0,0], [0,1], [1,2], [2,1]]
print(s.num_distinct_islands(m, n, positions))





