"""
Problem: Subarray Sum Equals K
Difficulty: Medium
Category: Arrays / Prefix Sum
LeetCode: #560

Problem Statement:
Given an array of integers nums and an integer k, return the
total number of subarrays whose sum equals k.

Example:
Input:  nums = [1,1,1], k = 2
Output: 2  (subarrays [1,1] at indices [0,1] and [1,2])

Input:  nums = [1,2,3], k = 3
Output: 2  ([1,2] and [3])
"""

# ─────────────────────────────────────────────
# APPROACH: Prefix Sum + HashMap (Optimal)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────

def subarray_sum(nums, k):
    """
    Key insight:
    If prefix_sum[j] - prefix_sum[i] = k, then the subarray
    between i+1 and j sums to k.
    Rearranged: prefix_sum[i] = prefix_sum[j] - k

    So: for each position, check how many EARLIER prefix sums
    equal (current_prefix_sum - k) — that's how many subarrays
    ending here sum to k.

    Example walkthrough:
    nums = [1,1,1], k=2

    prefix_sum=0, count_map={0:1}, count=0

    i=0, num=1: prefix_sum=1
      need prefix_sum - k = 1-2 = -1 → not in map
      count_map={0:1, 1:1}

    i=1, num=1: prefix_sum=2
      need prefix_sum - k = 2-2 = 0 → IS in map (appears 1 time)!
      count += 1 → count=1
      count_map={0:1, 1:1, 2:1}

    i=2, num=1: prefix_sum=3
      need prefix_sum - k = 3-2 = 1 → IS in map (appears 1 time)!
      count += 1 → count=2
      count_map={0:1, 1:1, 2:1, 3:1}

    Final count = 2 ✅
    """
    count_map = {0: 1}   # prefix_sum: how many times seen (0 seen once initially)
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num

        # How many earlier prefix sums equal (prefix_sum - k)?
        if (prefix_sum - k) in count_map:
            count += count_map[prefix_sum - k]

        # Record this prefix sum
        count_map[prefix_sum] = count_map.get(prefix_sum, 0) + 1

    return count


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    assert subarray_sum([1,1,1], 2) == 2
    assert subarray_sum([1,2,3], 3) == 2
    assert subarray_sum([1,-1,0], 0) == 3
    assert subarray_sum([1], 0) == 0

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Prefix Sum + HashMap:
- Time:  O(n) — single pass
- Space: O(n) — hashmap stores up to n distinct prefix sums

KEY PATTERN LEARNED:
Prefix Sum + HashMap is THE pattern for "subarray sum equals X"
type problems — including with negative numbers (which rules out
sliding window). The key algebraic trick: sum(i,j) = prefix[j] - prefix[i],
so rearrange to look up prefix[i] = prefix[j] - target in a hashmap.
"""
