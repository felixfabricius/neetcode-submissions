"""
Approach 1:
- Sort the incoming numbers O(n log n)
- When number is added, insert it into correct place (O(n) with dynamic array because need to shift)
- Retrieve kth largest: O(1)
-> total time complexity would be O((logn + m)n), where m is number of times add is called and 
   n is maximum number of elements in the stream at a given point in time

Approach 2:
- Can maintain list of the k largest elements; min heap
- When we add a number, and it's greater than the minimum, then we need to remove
  the minimum, insert that number, and heapify down
  Then time complexity from adding is O(m log k)
- But: how do we initialise the min heap? Is there any way we can prevent having to sort the 
  nums input?
  - e
  - Suppose we iterate through the array once.
  - 

"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.min_heap = nums[-k:] # note that this works even if k > len(list)
        self.k = k
        return None

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            print("Must append.")
            # we'd only ever have the case that we're one short due to problem constraints
            # therefore: append, and then heapify up?
            # If this would only ever arise in case where k = 1, could simply append to val
            # and then no need to heapify
            self.min_heap.append(val)
            i = len(self.min_heap) - 1
            # To get from i to children:
                # 2i + 1 for left child; 2i + 2 for right child
            # To get from i to parent: i - 1 // 2
            while True:
                j = i - 1 // 2
                if j >= 0 and self.min_heap[i] < self.min_heap[j]:
                    self.min_heap[i], self.min_heap[j] = self.min_heap[j], self.min_heap[i]
                    i = j
                else:
                    break
            print(self.min_heap)
            
        elif val > self.min_heap[0]:
            self.min_heap[0] = val
            i = 0
            while True:
                if 2 * i + 2 < len(self.min_heap):
                    if self.min_heap[2 * i + 1] < self.min_heap[2 * i + 2]:
                        j = 2 * i + 1
                    else:
                        j = 2 * i + 2
                    if self.min_heap[i] > self.min_heap[j]:
                        self.min_heap[i], self.min_heap[j] = self.min_heap[j], self.min_heap[i]
                        i = j
                    else:
                        break
                elif 2 * i + 1 < len(self.min_heap) and self.min_heap[i] > self.min_heap[2 * i + 1]:
                    self.min_heap[i], self.min_heap[2 * i + 1] = self.min_heap[2 * i + 1], self.min_heap[i]
                    i = 2 * i + 1
                else:
                    break

        
        return self.min_heap[0]
        
