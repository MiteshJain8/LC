class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        N = len(stations)

        def canDo(target_power):
            extras = k
            my_stations = stations.copy()
            
            window_power = stations[0]
            i = j = 0

            for idx in range(N):
                left, right = max(0, idx - r), min(N - 1, idx + r)

                while i < left:
                    window_power -= my_stations[i]
                    i += 1

                while j < right:
                    j += 1
                    window_power += my_stations[j]

                if window_power < target_power:
                    delta = target_power - window_power
                    if delta > extras:
                        return False
                    my_stations[right] += delta
                    extras -= delta
                    window_power += delta

            return True

        left, right = 0, 10**10 + 10**9
        while left <= right:
            mid = (left + right) // 2
            if canDo(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right