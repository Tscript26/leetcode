"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
from collections import Counter


class MedianFinder:

    def __init__(self):
        self.even = True
        self.median = None
        self.total = 0
        self.stack = []

    def addNum(self, num: int) -> None:
        self.even = not self.even
        # self.stack.append(num)
        if not self.stack:
            self.stack.append(num)
        else:

            n = len(self.stack)

            if self.stack[n//2] > num:
                l, r = 0, n//2
            else:
                l, r = n//2, n
            i = l
            while i < r and num < self.stack[i]:
                i += 1
            self.stack.insert(i, num)

    def findMedian(self) -> float:
        self.stack.sort()
        if self.even:
            right = len(self.stack) // 2
            left = right - 1
            return (self.stack[left] + self.stack[right]) / 2
        else:
            k = (len(self.stack) - 1) // 2
            return self.stack[k]


import random

if __name__ == '__main__':
    mf = MedianFinder()
    an = mf.addNum
    fm = mf.findMedian

    # rules = [[], [1], [2], [], [3], []]
    amount = 5 * 10000
    import time
    start = time.time()
    rules = [[random.randint(-100000, 100000)] if i < 1 or random.randint(0, 1) == 1 else [] for i in range(amount)]
    print(len(rules))
    # print(rules)
    for rule in rules:
        if not rule:
            pass
            # print(fm())
        else:
            an(rule[0])
    print(time.time() -start)