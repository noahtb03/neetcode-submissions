class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)

        # rows
        for i in range(9):
            rowset = set()
            for value in board[i]:
                if value != "." and value in rowset:
                    return False
                rowset.add(value)

        # columns
        for i in range(9):
            colset = set()
            for row in board:
                value = row[i]
                if value != "." and value in colset:
                    return False
                colset.add(value)

        # boxes
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if value in boxes[box_index]:
                    return False

                boxes[box_index].add(value)

        return True