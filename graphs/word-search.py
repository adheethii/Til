"""
Problem: Word Search
Difficulty: Medium
Category: Backtracking / DFS
LeetCode: #79

Problem Statement:
Given an m x n grid of characters and a string word, return true
if word exists in the grid. The word can be constructed from
adjacent cells (horizontally/vertically), same cell not reused.

Example:
Input:
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
Output: True
"""

# ─────────────────────────────────────────────
# APPROACH: Backtracking (DFS with undo)
# Time: O(m*n*4^L) | Space: O(L) — L = word length
# ─────────────────────────────────────────────

def exist(board, word):
    """
    Key insight:
    Try starting the search from every cell. At each step,
    explore all 4 directions looking for the NEXT character.
    If a path fails, "undo" the mark and try another direction
    — this undo step is what makes it "backtracking".

    Example walkthrough:
    board has 'A' at (0,0), word="ABCCED"

    Start at (0,0)='A' matches word[0]='A' ✅
      → try (0,1)='B' matches word[1]='B' ✅
        → try (0,2)='C' matches word[2]='C' ✅
          → try (1,2)='C' matches word[3]='C' ✅
            → try (2,2)='E' matches word[4]='E' ✅
              → try (2,1)='D' matches word[5]='D' ✅
                → word fully matched! return True
    """
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, index):
        # Base case: matched entire word
        if index == len(word):
            return True

        # Out of bounds or character doesn't match
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or board[r][c] != word[index]):
            return False

        # Mark current cell as visited (temporarily)
        temp = board[r][c]
        board[r][c] = "#"

        # Try all 4 directions
        found = (
            backtrack(r+1, c, index+1) or
            backtrack(r-1, c, index+1) or
            backtrack(r, c+1, index+1) or
            backtrack(r, c-1, index+1)
        )

        # Undo the mark (backtrack!) — critical step
        board[r][c] = temp

        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True

    return False


# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────

if __name__ == "__main__":
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist([row[:] for row in board1], "ABCCED") == True
    assert exist([row[:] for row in board1], "SEE") == True
    assert exist([row[:] for row in board1], "ABCB") == False

    print("✅ All test cases passed!")


# ─────────────────────────────────────────────
# COMPLEXITY ANALYSIS
# ─────────────────────────────────────────────

"""
Backtracking:
- Time:  O(m*n*4^L) — try each cell as start, branch 4 ways per character
- Space: O(L) — recursion depth equals word length

KEY PATTERN LEARNED:
Backtracking = DFS + undo. Mark a cell as visited, explore,
then UNMARK it before returning — this lets other paths reuse
that cell. Using "#" as a temporary marker avoids needing a
separate visited set. This pattern extends to: Permutations,
N-Queens, Sudoku Solver.
"""
