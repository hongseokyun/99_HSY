from collections import deque
from collections import defaultdict

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        buses = defaultdict(set)
        start = deque()
        
        if source == target :
            return 0

        for bus, route in enumerate(routes) :
            for rot in route :
                buses[bus+1].add(rot)
                if rot == source :
                    start.append(bus+1)

        if not start :
            return -1
        
        cnt = 0
        visit = [False for _ in range(10**5)]
        next_start = deque()
        while start :
            bus = start.popleft()
            route = buses[bus]
            if target in route :
                return cnt+1 

            while route :
                rot = route.pop()
                if not visit[rot-1] :
                    visit[rot-1] = True
                    for bus_key in buses :
                        if rot in buses[bus_key] :
                            if bus_key not in next_start :
                                next_start.append(bus_key)

            if not start :
                start = next_start
                next_start = deque()
                cnt += 1
        return -1


        


        