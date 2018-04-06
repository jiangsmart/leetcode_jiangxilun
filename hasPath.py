class Solution:
    def hasPath(self, matrix, rows, cols, path):
        mat=[]
        for i in range(rows):
            mat.append(matrix[i*cols:(i+1)*cols])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == path[0]:
                    history = [(i, j)]
                    if self.judge(matrix, history, 1, path):
                        return True
        return False

    def judge(self, matrix, history, nextChar, path):
        x, y = history[-1]
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if i >= len(matrix) or i < 0 or j >= len(matrix[0]) or j < 0:
                continue
            elif (i, j) in history:
                continue
            elif matrix[i][j] == path[nextChar]:
                h = history + [(i, j)]
                if len(h) == len(path):
                    return True
                return self.judge(matrix, h, nextChar + 1, path)
        return False
