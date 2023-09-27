import heapq
from typing import List
from colorama import Fore


class Node:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


def manhattan_distanace(x1: int, y1: int, x2: int, y2: int) -> int:
    """
    INPUT: coordinates of two points
    OUTPUT: Manhattan distance between the two points
    """
    return abs(x1 - x2) + abs(y1 - y2)


def greedy_best_first_search(graph: List[List], start: Node, end: Node) -> None:
    """
    INPUT: graph, start node and end node
    OUTPUT: path from start to end using greedy best first search
    heuristic function :
        f(n) = h(n) (manhattan distance of the current node from the goal node)
    """

    rows = len(graph)
    cols = len(graph[0])

    visited = {}  ## dictionary to keep the visited nodes

    queue = (
        []
    )  ## priority queue to keep the nodes to be visited in order of their hueristic value

    time = 0
    heapq.heappush(
        queue,
        (manhattan_distanace(start.x, start.y, end.x, end.y), start.x, start.y, time),
    )

    while queue:
        _, x, y, time = heapq.heappop(queue)

        if x == end.x and y == end.y:
            print(Fore.GREEN + f"\t Time to reach the goal is -> {time}")
            print("\t Goal Node reached")
            return

        if (x, y) not in visited:
            visited[(x, y)] = True
            dx = [-1, 1, 0, 0]  ## directions in x axis
            dy = [0, 0, -1, 1]  ## directions in y axis

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < rows and ny >= 0 and ny < cols:
                    ## Now we check the condition of obstacle and not visited
                    if graph[nx][ny] != "#" and (nx, ny) not in visited:
                        heapq.heappush(
                            queue,
                            (
                                manhattan_distanace(nx, ny, end.x, end.y),
                                nx,
                                ny,
                                time + 1,
                            ),
                        )

    print(Fore.RED + "\t Goal Node cannot be reached")


def A_star(graph: List[List], start: Node, end: Node) -> None:
    """
    INPUT: graph, start node and end node
    OUTPUT: path from start to end using A* search
    heuristic function:
        f(n) = g(n) + h(n)
        where, g(n) = distance travelled to reach current node from the start node
               h(n) = manhattan distance of the current node from the goal node
    """

    rows = len(graph)
    cols = len(graph[0])

    visited = {}  ## dictionary to keep the visited nodes

    queue = (
        []
    )  ## priority queue to keep the nodes to be visited in order of their hueristic value
    time = 0  ## time taken by the algorithm to reach the goal node
    current_distance = 0

    heapq.heappush(
        queue,
        (
            current_distance + manhattan_distanace(start.x, start.y, end.x, end.y),
            start.x,
            start.y,
            time,
        ),
    )

    while queue:
        current_distance += 1
        _, x, y, time = heapq.heappop(queue)

        if x == end.x and y == end.y:
            print(Fore.GREEN + f"\t Time to reach the goal is -> {time}")
            print("\t Goal Node reached")
            return

        if (x, y) not in visited:
            visited[(x, y)] = True
            dx = [-1, 1, 0, 0]  ## directions in x axis
            dy = [0, 0, -1, 1]  ## directions in y axis

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < rows and ny >= 0 and ny < cols:
                    ## Now we check the condition of obstacle and not visited
                    if graph[nx][ny] != "#" and (nx, ny) not in visited:
                        heapq.heappush(
                            queue,
                            (
                                current_distance
                                + manhattan_distanace(nx, ny, end.x, end.y),
                                nx,
                                ny,
                                time + 1,
                            ),
                        )

    print(Fore.RED + "\t Goal Node cannot be reached")


if __name__ == "__main__":
    start = Node(1, 1)
    end = Node(7, 7)
    graph = [
        [".", ".", ".", ".", ".", ".", "#", "."],
        [".", ".", "#", "#", "#", ".", "#", "."],
        [".", ".", "#", ".", "#", ".", "#", "."],
        [".", ".", "#", "#", "#", ".", "#", "."],
        [".", ".", "#", ".", "#", ".", "#", "."],
        [".", ".", "#", "#", "#", ".", "#", "."],
        [".", ".", ".", ".", ".", ".", "#", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
    ]

    graph = graph[::-1] ## reversing because the bottom left is (0,0) and top right is (row-1,col-1)

    print(Fore.CYAN + "Using Greedy Best First Search ->")
    greedy_best_first_search(graph, start, end)

    print(Fore.CYAN + "Using Greedy Best First Search ->")
    A_star(graph, start, end)

    exit(0)
