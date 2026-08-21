class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}

        for i in range(len(position)):
            d[position[i]] = speed[i]

        position.sort()

        fleet_counter = 1
        p_right = position.pop()
        t_right = (target - p_right) / d[p_right]

        while position:
            p_left = position.pop()
            t_left = (target - p_left) / d[p_left]

            if t_left <= t_right: # catches up
                continue # don't increase fleet size
            else: # does not catch up
                t_right = t_left # future comparisons will be made against this slower car 
                fleet_counter += 1 # since didnt catch up, increase fleet size

        return fleet_counter

