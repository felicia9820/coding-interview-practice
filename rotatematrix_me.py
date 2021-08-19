def rotate_matrix(M):
    n = len(M)

    for i in range(n//2):
        first, last = i, n-1-i
        for j in range(i, n-1-i):
            pix = [
                M[i][j],
                M[j][n-1-i],
                M[n-1-i][n-1-j],
                M[n-1-j][i]
            ]
            M[i][j] = pix[3]
            M[j][n-1-i] = pix[0]
            M[n-1-i][n-1-j] = pix[1]
            M[n-1-j][i] = pix[2]

    print(M)
    

rotate_matrix([
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ])
