def assign_parking_spaces(n, r, c, flat_land, event_list):
    # Initialize variables    landing_spaces = [(i, j) for i in range(r) for j in range(c) if flat_land[i][j] == "=="]
    parking_spaces = {(i, j): None for i in range(r) for j in range(c) if flat_land[i][j].isdigit()}
    occupied_spaces = set()
    # Recursive function to try all combinations of landing and parking spaces    def backtrack(i):
if i == n:
return True        event = event_list[i]
        if event > 0:  # landing            for space in landing_spaces:
                if space not in occupied_spaces:
                    parking_space = parking_spaces[space]
                    if parking_space is None or parking_space == event:
                        parking_spaces[space] = event                        occupied_spaces.add(space)
                        if backtrack(i + 1):
                            return True                        parking_spaces[space] = None                        occupied_spaces.remove(space)
        else:  # taking off            for space in parking_spaces:
                if parking_spaces[space] == -event:
                    landing_space = None                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        x, y = space[0] + dx, space[1] + dy                        if 0 <= x < r and 0 <= y < c and flat_land[x][y] == "==":
                            landing_space = (x, y)
                            break                    if landing_space is not None:
                        parking_spaces[space] = None                        occupied_spaces.remove(space)
                        if backtrack(i + 1):
                            return True                        parking_spaces[space] = -event                        occupied_spaces.add(space)
        return False    # Call the backtrack function to find a feasible assignment    if backtrack(0):
        return [parking_spaces[space] for space in sorted(parking_spaces)]
    else:
        return None