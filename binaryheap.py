"""
binary heap.
initate: new array, 
insert: 
    1. Add the element to the bottom level of the heap at the most left.
    2. Compare the added element with its parent; if they are in the correct order, stop.
    3. If not, swap the element with its parent and return to the previous step.

delete max, (min):
    # We always remove the item from the root. 
    1. Replace the root of the heap with the last element on the last level.
    2. Compare the new root with its children; if they are in the correct order, stop.
    3. If not, swap the element with one of its children and return to the previous step. (Swap with its smaller child in a min-heap and its larger child in a max-heap.)


-------
heapsort:
    * Heapsort is performed by somehow creating a heap and then removing the data items one at a time. The heap could start as an empty heap, with items inserted one by one. However, there is a relatively easy routine to convert an array of items into a heap, so that method is often used. This routine is described below. Once the array is converted into a heap, we remove the root item (the smallest), readjust the remaining items into a heap, and place the removed item at the end of the heap (array). Then we remove the new item in the root (the second smallest), readjust the heap, and place the removed item in the next to the last position, etc.

"""