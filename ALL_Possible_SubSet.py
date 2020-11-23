
arr = [1, 2, 3, 4]
n = len(arr)


def backtrack(ind, n):
    result = []

    partial = []

    def directed_powerset(ind):
        if(ind == n):
            result.append(partial[:])
            return

        partial.append(arr[ind])
        directed_powerset(ind+1)
        partial.pop()
        directed_powerset(ind+1)
    directed_powerset(ind)
    return result


result = backtrack(0, n)

print(sorted(result))
