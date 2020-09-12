'''
This problem was recently asked by Microsoft:

N-Queens is the problem where you find a way to put n queens on a nxn chess board without them being able to attack each other. Given an integer n, return 1 possible solution by returning all the queen's position.

Time: O(n**n)
Space: O(n)
'''

class Solution:

    def n_queens_helper(self, n, rows, cols, diag_asc, diag_desc, queen_pos):
        if len(queen_pos) == n:
            return queen_pos
        row = len(queen_pos)
        for col in range(n):
            if rows[row] and cols[col] and diag_asc[row+col] and diag_desc[row-col]:
                rows[row] = False
                cols[col] = False
                diag_asc[row+col] = False
                diag_desc[row-col] = False
                queen_pos.append((row, col))
                self.n_queens_helper(n, rows, cols, diag_asc, diag_desc, queen_pos)
                if len(queen_pos) == n:
                    return queen_pos
                rows[row] = True
                cols[col] = True
                diag_asc[row+col] = True
                diag_desc[row-col] = True
                queen_pos.pop()
        

    def n_queens(self, n):
        rows = [True] * n
        cols = [True] * n
        diag_asc = [True] * (n*2-1)
        diag_desc = [True] * (n*2-1)
        return self.n_queens_helper(n, rows, cols, diag_asc, diag_desc, [])


print(Solution().n_queens(5))
# There can be many answers
# [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

# Q . . . .
# . . . Q .
# . Q . . .
# . . . . Q
# . . Q . .
