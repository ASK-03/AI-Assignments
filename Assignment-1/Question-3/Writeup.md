# Writeup describing the Problem Conversion: Maze Traversal as a Search Problem

## Problem Description

We are given a grid-based maze representing a terrain with varying levels of difficulty to traverse. The maze contains different types of terrain (Grass, Dirt, Rocks), each with a specific traversal cost. The goal is to find the path from the starting point to the goal point that minimizes the total traversal cost.

## Search Setup

### State Representation

In this problem, a state is represented by a combination of the current position (cell) and the cumulative traversal cost. The current position represents the location in the maze, while the cumulative traversal cost keeps track of the total cost incurred from the start to the current position. It is identical in both A* and weighted A* algorithms.

### Actions

The actions in this search problem correspond to moving from one cell to another in four cardinal directions: up, down, left, and right. However, we must ensure that the movement is only allowed to valid cells (i.e., not through walls or impassable terrain).

### Transition Model

The transition model describes how the state changes when an action is applied. In this case, the transition model involves moving from the current cell to an adjacent cell in one of the cardinal directions. The new state will have an updated position and cumulative traversal cost.

### Goal State

The goal state is defined as reaching the cell marked as the "Finish" in the maze. The search algorithm's objective is to find a path that leads to this goal state with the minimum total traversal cost.

### Heuristic Function

To guide the search, a heuristic function is defined. The heuristic estimates the cost from the current cell to the goal cell. In this problem, the heuristic is calculated based on the Manhattan distance weighted by the terrain type. The terrain type affects the cost estimation, with Grass being the easiest to traverse, followed by Dirt and then Rocks. It is identical in both A* and weighted A* algorithms.

### Cost Function

The cost function keeps track of the cumulative traversal cost from the start to the current cell. In A* algorithm, it considers the terrain type of the current cell to determine the cost of moving to neighboring cells. In Weighted A*, the cost function is influenced by an additional weight parameter. This weight is applied to the heuristic function's estimation when determining the priority of nodes in the open list. This means that the algorithm places more emphasis on the heuristic in the selection of nodes.

## Conclusion

By representing the problem as a search setup with states, actions, transition model, goal state, heuristic function, and cost function, we can effectively apply search algorithms such as A* and Weighted A* to find the optimal path through the maze while considering the varying terrain costs.