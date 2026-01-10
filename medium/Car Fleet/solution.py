class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Map the position with corresponding speed.
        position_speed_map = {}
        for i in range(len(speed)):
            position_speed_map[position[i]] = speed[i]

        # Sort the starting position of car from nearest to furthest from the destination
        position.sort(reverse=True)
        longest_time_to_destination = 0
        fleet_count = 0

        for i in range(len(position)):
            # Calculate the time it takes a car to reach the destination: times = distance / speed
            time_to_destination = (
                float(target - position[i]) / position_speed_map[position[i]]
            )
            # If the times of current car is longer than the current fleet, it cannot join the fleet
            # Therefore, the new fleet is formed.
            # We update the time to the new fleet as well.
            if time_to_destination > longest_time_to_destination:
                longest_time_to_destination = time_to_destination
                fleet_count += 1
        return fleet_count

        # Time complexity: O(nlogn)
        #   - sorting
        # Space complexity:
        #   - A dictionary to map position / map
