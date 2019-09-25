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



# quick sort
* desc: Quicksort is a divide and conquer algorithm. 
* desc: first selection the mean value, split the array to less part and large part.
* 1. Pick an element, called a pivot, from the array.
* 2. Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation.
* 3. Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.



# sorting in linear time
* These algorithms share an interesting property: the sorted order they determine is based only on comparisons between the input elements. We call such sorting algorithms comparison sorts.


# radix sort:
```
Input list (base 10):
    [170, 45, 75, 90, 2, 802, 2, 66]
Starting on the right:
    [{170, 90}, {02, 802, 02}, {45, 75}, {66}]
Notice that a 0-digit is “generated” in front of the 2 for the missing digit, that 802 again comes before the second 02 as 802 comes before 2 in the previous list.
Sorting by the next digit:
    [{02, 802, 02}, {45}, {66}, {170, 75}, {90}]
And finally
    [{002, 002, 045, 066, 075, 090}, {170}, {802}]
```


# bucket sort:
    * 把数放在各自己区间. 


# decision-tree model:
    * 分类树 
    * 递归分析回归结构


# B-tree
    * 每一层 is 元素, also 区间分区点. 每一层有个order.
    * desc: In B-trees, internal (non-leaf) nodes can have a variable number of child nodes within some pre-defined range. When data is inserted or removed from a node, its number of child nodes changes. In order to maintain the pre-defined range, internal nodes may be joined or split. Because a range of child nodes is permitted, B-trees do not need re-balancing as frequently as other self-balancing search trees, but may waste some space, since nodes are not entirely full. The lower and upper bounds on the number of child nodes are typically fixed for a particular implementation. For example, in a 2-3 B-tree (often simply referred to as a 2-3 tree), each internal node may have only 2 or 3 child nodes.


# Fusion tree:
    * desc:a fusion tree is a type of tree data structure that implements an associative array on w-bit integers. When operating on a collection of n key–value pairs, it uses O(n) space and performs searches in O(logw n) time, which is asymptotically faster than a traditional self-balancing binary search tree, and also better than the van Emde Boas tree for large values of w. It achieves this speed by exploiting certain constant-time operations that can be done on a machine word. Fusion trees were invented in 1990 by Michael Fredman and Dan Willard


