# Data Structures (DS) in Python

Data Structures (DS) are essential components in computer science that allow data to be organized, managed, and stored
efficiently. Python, as a versatile programming language, offers both built-in and custom data structures that make it
an excellent choice for solving real-world problems.

## Types of Data Structures in Python

### 1. Built-in Data Structures

- **List**: Ordered and mutable collections.
- **Tuple**: Ordered and immutable collections.
- **Dictionary**: Key-value pairs for fast lookups.
- **Set**: Unordered collections of unique items.

### 2. User-Defined Data Structures

- **Stack**: LIFO (Last In, First Out) structure.
- **Queue**: FIFO (First In, First Out) structure.
- **Linked List**: Nodes connected through references.
- **Trees**: Hierarchical data structure (for example, Binary Tree, Binary Search Tree).
- **Graphs**: Nodes and edges representing relationships.

---

## Applications of Data Structures in Python

1. **Web Development**: Managing session data, caching, and database interactions.
2. **Machine Learning**: Organizing datasets, feature extraction, and implementing algorithms.
3. **Gaming**: Pathfinding, game state management, and optimization.
4. **Data Analysis**: Efficient data storage and retrieval for processing large datasets.
5. **System Design**: Designing scalable and optimized systems.

---

# Algorithms (Algo) in Python

Algorithms are step-by-step instructions or procedures designed to solve specific problems or perform computations.
Python's simplicity and readability make it an excellent choice for learning and implementing algorithms.

## Types of Algorithms in Python

### 1. Sorting Algorithms

- **Bubble Sort**: A simple comparison-based algorithm.
- **Merge Sort**: A divide-and-conquer algorithm with O(n log n) complexity.
- **Quick Sort**: Efficient and commonly used, with average-case O(n log n) complexity.

### 2. Searching Algorithms

- **Linear Search**: Sequentially checks each element in a list.
- **Binary Search**: Efficient searching in sorted lists with O(log n) complexity.

### 3. Graph Algorithms

- **Depth-First Search (DFS)**: Explore as far as possible along a branch.
- **Breadth-First Search (BFS)**: Explores all neighbors before moving to the next level.
- **Shortest Path Algorithms**:
    - Dijkstra's Algorithm
    - Bellman-Ford Algorithm

### 4. Dynamic Programming

- **Concept**: Solves problems by breaking them down into simpler problems and storing their results.
- Examples:
    - Fibonacci Sequence
    - Knapsack Problem

### 5. Greedy Algorithms

- Makes the locally optimal choice at each step with the hope of finding the global optimum.
- Examples:
    - Activity Selection Problem
    - Huffman Coding

### 6. Backtracking

- Explore all possibilities to solve problems like:
    - N-Queens Problem
    - Sudoku Solver

---

## Applications of Algorithms in Python

1. **Data Analysis**: Efficiently process and analyze large datasets.
2. **Artificial Intelligence**: Implement machine learning models and decision-making systems.
3. **Web Development**: Optimize search functionalities and user recommendations.
4. **Networking**: Solve problems like routing and packet optimization.
5. **Game Development**: Implement pathfinding and AI strategies.

---

# Unit Testing in Python

Unit testing is a software testing technique where individual units or components of software are tested in isolation.
Python provides a built-in module called `unittest` for writing and running unit tests.
---

# Linear search in Python

Linear search is a simple search algorithm that sequentially checks each element in a list until a match is found.
It has an average-case time complexity of O(n) and a worst-case time complexity of O(n).

# Pseudocode for Linear Search
```plaintext:
# input: list of elements arr, target element target
# output: index of target element in arr, or -1 if not found

START
    for each element in arr
        if element equals target
            return index of element
    return -1
END
```
---

# Binary search in Python

Binary search is an efficient search algorithm that finds the position of a target value within a sorted array.
It has a time complexity of O(log n) and requires the array to be sorted.

# Pseudocode for Binary Search
```plaintext:
# input: sorted list of elements arr, target element target
# output: index of target element in arr, or -1 if not found

START
    set low to 0
    set high to length of arr - 1

    while low is less than or equal to high
        set mid to (low + high) // 2
        if arr[mid] equals target
            return mid
        else if arr[mid] less than target
            set low to mid + 1
        else
            set high to mid - 1

    return -1
END
```
---