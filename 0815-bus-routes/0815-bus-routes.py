from collections import deque, defaultdict

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        stop_to_buses = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(bus)

        visited_bus = set()
        visited_stop = set([source])
        queue = deque()

        for bus in stop_to_buses[source]:
            visited_bus.add(bus)
            queue.append(bus)

        cnt = 1
        while queue:
            for _ in range(len(queue)):
                bus = queue.popleft()
                for stop in routes[bus]:
                    if stop == target:
                        return cnt
                    if stop not in visited_stop:
                        visited_stop.add(stop)
                        for next_bus in stop_to_buses[stop]:
                            if next_bus not in visited_bus:
                                visited_bus.add(next_bus)
                                queue.append(next_bus)
            cnt += 1

        return -1