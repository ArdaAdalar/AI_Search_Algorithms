
====================================
AI_Search_Algorithms
====================================

This project implements fundamental search algorithms including BFS, DFS, UCS, and A*. 
It is based on the foundational artificial intelligence curriculum developed by UC Berkeley. 
The project involves solving search problems and designing heuristics for A*.

-----------------
Project Overview
-----------------

This repository contains implementations of the following search algorithms:

1. **Breadth-First Search (BFS)**:
   - Explores all nodes at the present depth level before moving on to the nodes at the next depth level.
   - Guarantees the shortest path in an unweighted graph.

2. **Depth-First Search (DFS)**:
   - Explores as far as possible along each branch before backtracking.
   - May not guarantee the shortest path but is efficient in exploring deep trees.

3. **Uniform Cost Search (UCS)**:
   - Explores nodes in order of their cumulative cost from the start node.
   - Guarantees the optimal solution in a weighted graph.

4. **A* Search**:
   - Combines the path cost from the start node with an admissible heuristic.
   - Guarantees the optimal solution in a weighted graph.

5. **Heuristic Design**:
   - Designed custom heuristics to guide the A* algorithm for specific problems.
   - Focused on reducing unnecessary node expansions while maintaining optimality.

----------------------
Key Files and Modules
----------------------

- **search.py**: Contains implementations for BFS, DFS, UCS, and A* algorithms.
- **searchAgents.py**: Defines the problem space and integrates search algorithms with problem-specific agents.
- **searchTestClasses.py**: Tests to verify the correctness of the implemented algorithms.
- **README.txt**: Documentation for the project.

------------
How to Run
------------


