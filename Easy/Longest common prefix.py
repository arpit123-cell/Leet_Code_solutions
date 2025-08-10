def Longest_common_prefix(arr):
    arr.sort()
    first = arr[0]
    last = arr[1]

    prefix = ""

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            break
        else:
            prefix += first[i]
            continue
        break