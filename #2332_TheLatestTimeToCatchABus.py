# No solution found yet
from typing import List


class Solution:
    def latestTimeCatchTheBus(
        self, buses: List[int], passengers: List[int], capacity: int
    ) -> int:
        if len(buses) < 1 or len(passengers) < 1 or capacity > 10000:
            return 0
        for bus in buses:
            if bus < 2:
                return 0
        for passenger in passengers:
            if passenger > 1000000000:
                return 0

        buses.sort()
        passengers.sort()
        mapping = {str(bus): [] for bus in buses}

        def check_times(you: int):
            for bus in mapping:
                if you in mapping[str(bus)]:
                    you -= 1
                    check_times(you)
            return you

        for b, bus in enumerate(buses):
            curr_passengers = passengers[:capacity]
            for p, passenger in enumerate(curr_passengers):
                if passenger < bus:
                    if b == len(buses) - 1 and p == len(curr_passengers) - 1:
                        you = passenger - 1
                        return check_times(you)
                    passengers.remove(passenger)
                    mapping[str(bus)].append(passenger)


if __name__ == "__main__":
    buses = [3]
    passengers = [2, 4]
    capacity = 2
    print(Solution().latestTimeCatchTheBus(buses, passengers, capacity))
