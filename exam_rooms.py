# lc 855. Exam Room

# My solution: use heap
import heapq


class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.n = N
        self.pq = [(self.dist(-1, N), -1, N)]
        self.seated = [0 for i in range(N)]

    def dist(self, x, y):
        if x == -1:
            return -y
        elif y == self.n:
            return -(self.n - x - 1)
        else:
            return -(abs(x - y))

    def seat(self):
        """
        :rtype: int
        """
        dist, x, y = heapq.heappop(self.pq)
        if x == -1:
            seat = 0
        elif y == self.n:
            seat = self.n - 1
        else:
            seat = (x + y) // 2
        heapq.heappush(self.pq, (self.dist(x, seat), x, seat))
        heapq.heappush(self.pq, (self.dist(seat, y), seat, y))
        self.seated[seat] = 1
        return seat

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        head = tail = None
        for interval in self.pq:
            if interval[2] == p:
                head = interval
            if interval[1] == p:
                tail = interval
            if head and tail:
                break
        self.pq.remove(head)
        self.pq.remove(tail)
        heapq.heapify(self.pq)
        heapq.heappush(self.pq, (self.dist(head[1], tail[2]), head[1], tail[2]))
        self.seated[p] = 0


# Your ExamRoom object will be instantiated and called as such:
actions = ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
params = [[10], [], [], [], [], [4], []]
obj = ExamRoom(params[0][0])
for i in range(len(actions)):
    if actions[i] == "seat":
        obj.seat()
    elif actions[i] == "leave":
        obj.leave(params[i][0])
for i in range(len(obj.seated)):
    if obj.seated[i] == 1:
        print(i)
