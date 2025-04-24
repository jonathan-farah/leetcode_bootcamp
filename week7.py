from collections import Counter,deque,defaultdict
import heapq

def rightSideView(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # If it's the last node in this level, add to result
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    fresh = 0
    queue = deque()

    # Initialize the queue with all rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # row, col, time
            elif grid[r][c] == 1:
                fresh += 1

    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    time = 0

    while queue:
        r, c, time = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, time + 1))

    return time if fresh == 0 else -1

def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    # Build graph and in-degree array
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1

    # Start with nodes having no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == numCourses else []