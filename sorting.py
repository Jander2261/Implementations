def merge(ary, start, partition, end):
    lAry = ary[start:partition]
    rAry = ary[partition:end]

    lAry.append(float('inf'))
    rAry.append(float('inf'))

    lIndex = 0
    rIndex = 0

    for i in range(start, end):
        if lAry[lIndex] <= rAry[rIndex]:
            ary[i] = lAry[lIndex]
            lIndex += 1
        else:
            ary[i] = rAry[rIndex]
            rIndex += 1
    return

def mergeSort(ary, start = None, end = None):
    if start is None:
        start = 0
    if end is None:
        end = len(ary)
    if not((end - start) > 1):
        return

    partition = (start + end) // 2
    mergeSort(ary, start, partition)
    mergeSort(ary, partition, end)
    merge(ary, start, partition, end)

# main
ary = [7, 5, 2, 10, 17, 1, -5, 1, 0, 7, -18]
mergeSort(ary)
print(ary)