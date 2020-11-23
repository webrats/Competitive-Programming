
col = [0]*8
ld = [0]*15
rd = [0]*15
res = 0
GRID = [input() for i in range(8)]


def n_queen(r):
    # if all queen place succesfully
    if(r == 8):
        global res
        res += 1
        return
    for c in range(8):
        if(not col[c] and not ld[r+c] and not rd[r-c+7] and GRID[r][c] != "*"):
            # safe place for queen , putting queen
            # after putting queen make column , left daigonal and
            #  right daigonal unsafe (or putting 1)  for next queen
            col[c] = ld[r+c] = rd[r-c + 7] = 1
            # going to next row for next queen place
            n_queen(r+1)
            # if next queen can'nt get any safe place then backtrack
            # backtracking is done by making safe safe that unsafe place
            col[c] = ld[r+c] = rd[r-c + 7] = 0


n_queen(0)
print(res)
