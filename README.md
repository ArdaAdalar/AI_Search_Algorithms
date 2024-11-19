====================================
AI_Search_Algorithms 🤖
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
How to Run 🚀
------------

## Clone This Repository

To get started with this project, clone the repository to your local machine using the following command:

git clone https://github.com/ArdaAdalar/AI_Search_Algorithms.git 


Running Tests
To verify the correctness of the search algorithms:

python searchTest.py
Using the Search Agents
To test the algorithms on predefined problems, run:

python searchAgents.py -l <layout_name> -p <algorithm_name>
Replace <layout_name> with the problem environment (e.g., tinyMaze) and <algorithm_name> with the desired algorithm (e.g., bfs, dfs, ucs, or astar).

-----------------
Features ✨
-----------------

## Core Algorithms 🧠

Breadth-First Search (BFS):
Explores nodes layer by layer.
Guarantees shortest path in unweighted graphs.

Depth-First Search (DFS):
Explores as deeply as possible before backtracking.
May not guarantee shortest path.

Uniform Cost Search (UCS):
Expands the least-cost node.
Guarantees optimal path in weighted graphs.

A Search*:
Uses heuristics to guide the search.
Guarantees optimal path if heuristic is admissible and consistent.

Custom Heuristics:
Designed for specific problem domains to reduce search time and unnecessary expansions.

## Core Files 📚 
search.py: Core search algorithm implementations.
searchAgents.py: Problem spaces and agents for testing.
README.md: Project documentation.


