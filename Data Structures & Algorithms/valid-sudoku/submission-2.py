class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = [[False] * 9 for _ in range(9)]
        cols_seen = [[False] * 9 for _ in range(9)]
        boxes_seen = [[False] * 9 for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                digit_idx = int(val) - 1
                box_idx = (r // 3) * 3 + (c // 3)
                
                if rows_seen[r][digit_idx] or cols_seen[c][digit_idx] or boxes_seen[box_idx][digit_idx]:
                    return False
                
                rows_seen[r][digit_idx] = True
                cols_seen[c][digit_idx] = True
                boxes_seen[box_idx][digit_idx] = True
                
        return True   