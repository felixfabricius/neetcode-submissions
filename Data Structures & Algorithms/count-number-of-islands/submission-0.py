"""
Approaches:
- start looping through grid from top left until we reach land the first time
  - once we have land: go in all possible directions. if in our direction we get land,
    then add that to this island. keep doing that iteratively for everything we add to the land
    Queue makes sense for this
  - Also maintain a set of every part of land we've seen already
- Complexity:
  - Space: for the queue and for the set: O(m * n)
  - Time: I think this might be O(m * n) - if I'm smart about only checking in certain directions
    (e.g. i could only check towards right and bottom)
    (Is this important for O(m * n) time complexity? Intuitively: yes. Actually: not necessarily.
     And: if I do this, then I might need more space? No. Not necessarily. 
     But then I would need to keep track of the numerous islands I've already seen and perhaps
     also search which island something belongs to. And then might also have to merge islands later on.
     This is just obviously more annoying.)
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        current_island = deque()

        num_islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0" or (row, col) in visited:
                    continue
                visited.add((row, col))
                current_island.append((row, col))
                num_islands += 1
                print(f"Island start: ({row}, {col})")
                while len(current_island) > 0:
                    r, c = current_island.popleft()
                    for r_inc, c_inc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        candidate = (r + r_inc, c + c_inc)
                        if (
                            not 0 <= r + r_inc < rows
                            or not 0 <= c + c_inc < cols
                            or candidate in visited
                            or grid[r + r_inc][c + c_inc] == "0"
                        ):
                            print(f"  not added to island: {candidate}")
                            continue
                        visited.add(candidate)
                        print(f"  add to island: {candidate}")
                        current_island.append(candidate)
                    print(f"  island size: {len(current_island)}")
                    print(f"  island: {current_island}")
        
        return num_islands
                

