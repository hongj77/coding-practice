
matrix = [[1,2,3,4],
          [4,5,6,7],
          [7,8,9,10]]


def spiralPrint(matrix):
    m = len(matrix)
    n = len(matrix[0])

    c, r = 0, 0

    while (c < n and r < m):
        for i in range(c,n):
            print matrix[r][i]
        r += 1

        for i in range(r, m):
            print matrix[i][n-1]
        n -= 1

        if r < m:
            for i in range(n-1,c-1,-1):
                print matrix[m-1][i]
            m -= 1

        if c < n:
            for i in range(m-1,r-1,-1):
                print matrix[i][c]
            c += 1


spiralPrint(matrix)