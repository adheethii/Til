"""
Problem: Kth Largest Element in an Array
Difficulty: Medium
Category: Heap
LeetCode: #215

Problem Statement:
Given an integer array nums and integer k, return the kth
largest element (not the kth distinct element).

Example:
Input:  nums = [3,2,1,5,6,4], k = 2
Output: 5  (sorted desc: [6,5,4,3,2,1], 2nd largest = 5)
"""

# ─────────────────────────────────────────────
# APPROACH 1: Sort
# Time: O(n log n) | Space: O(1)
# ─────────────────────────────────────────────

def find_kth_largest_sort(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]


# ─────────────────────────────────────────────
# APPROACH 2: Min-Heap of size K (Optimal for repeated queries)
# Time: O(n log k) | Space: O(k)
# ─────────────────────────────────────────────

def find_kth_largest(nums, k):
    """
    Key insight:
    Maintain a min-heap of size k containing the k LARGEST
    numbers seen so far. The top of this heap (smallest of
    the k largest) is exactly the kth largest element.

    Example walkthrough:
    nums = [3,2,1,5,6,4], k=2

    push 3 → heap=[3]
    push 2 → heap=[2,3]
    push 1 → size>2 → pop smallest(1) → heap=[2,3]
    push 5 → size>2 → pop smallest(2) → heap=[3,5]
    push 6 → size>2 → pop smallest(3) → heap=[5,6]
    push 4 → size>2 → pop smallest(4) → heap=[5,6]

    heap[0] (top/smallest of the two) = 5 ✅ (2nd largest)
    """
    import heapq

    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


# ─────────────────────────────────────────────
# APPROACH 3: Quickselect (Optimal average case)
# Time: O(n) average, O(n²) worst | Space: O(1)
# ─────────────────────────────────────────────

def find_kth_largest_quickselect(nums, k):
    import random

    target_index = len(nums) - k   # kth largest = (n-k)th smallest (0-indexed)

    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    def quickselect(left, right):
        if left == right:
            return nums[left]
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        if pivot_index == target_index:
            return nums[pivot_index]
        elif pivot_index < target_index:
            return quickselect(pivot_index + 1, right)
        else:
            return quickselect(left, pivot_index - 1)

    return quickselect(0, len(nums) - 1)


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert find_kth_largest([3,2,1,5,6,4], 2) == 5
    assert find_kth_largest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert find_kth_largest_quickselect([3,2,1,5,6,4], 2) == 5

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Min-Heap of size K:
- Time:  O(n log k) — much better than O(n log n) when k << n
- Space: O(k)

Quickselect:
- Time:  O(n) average — best for a ONE-TIME query
- Space: O(1)

KEY PATTERN LEARNED:
For "Kth largest/smallest" — min-heap of size k if you'll query
repeatedly, quickselect if it's a one-time query and you can
modify the array. Counterintuitively, a MIN-heap finds the
Kth LARGEST (keep k largest, smallest of those is the answer).
"""
