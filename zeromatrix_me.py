def zero_matrix(M):
    rows = []
    cols = []

    for row_id in range(len(M)):
        if 0 in M[row_id]:
            rows.append(row_id)
            cols += [i for i, val in enumerate(M[row_id]) if val == 0]

    for row_id in range(len(M)):
        if row_id in rows:
            M[row_id] = [0] * len(M[row_id])
        else:
            for col_id in range(len(M[row_id])):
                if col_id in cols:
                    M[row_id][col_id] = 0

    print(M)

zero_matrix([
    [1,0,1],
    [1,1,1],
    [1,1,1]
])