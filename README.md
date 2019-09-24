# compute complexity:
* Order of growth, like differentiation.


# insert sort

* desc: insert sorting like play card
* comleexity: inserting sort complexity: sum(1, ..., n). conside the move instruction
* [] < [a1, a2, a3, ...., an]
* 和到手的一个个比, 比到正确的位置, 放置


# divide-and-conquer
```
Many useful algorithms are recursive in structure: to solve a given problem, they call themselves recursively one or more times to deal with closely related sub- problems. These algorithms typically follow a divide-and-conquer approach: they break the problem into several subproblems that are similar to the original prob- lem but smaller in size, solve the subproblems recursively, and then combine these solutions to create a solution to the original problem.
The divide-and-conquer paradigm involves three steps at each level of the recursion:
Divide the problem into a number of subproblems that are smaller instances of the same problem.
Conquer the subproblems by solving them recursively. If the subproblem sizes are small enough, however, just solve the subproblems in a straightforward manner.
Combine the solutions to the subproblems into the solution for the original prob- lem.
```

# merge sort
* desc: like merge two sorted array.
* complexity: 
* best condition: 
    ```python
    [1, 2, 3, 4] [5, 6, 7, 8]
    ```
* bad condition:
```python
[1, 3, 5] [0, 2, 4]
```
* merge sort 主要是解决什么问题
* 
```

```


# Binary heap
* desc: A binary heap is a heap data structure that takes the form of a binary tree. Binary heaps are a common way of implementing priority queues.
* desc: Heaps where the parent key is greater than or equal to (≥) the child keys are called max-heaps; those where it is less than or equal to (≤) are called min-heaps. 
* desc: Efficient (logarithmic time) algorithms are known for the two operations needed to implement a priority queue on a binary heap: inserting an element, and removing the smallest or largest element from a min-heap or max-heap, respectively. Binary heaps are also commonly employed in the heapsort sorting algorithm, which is an in-place algorithm because binary heaps can be implemented as an implicit data structure, storing keys in an array and using their relative positions within that array to represent child-parent relationships.
* 树, 维护一个半顺序化, 或全顺序化结构. 成本来自己维护成本. 


