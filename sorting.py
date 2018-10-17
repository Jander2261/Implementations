#!/usr/bin/env python
'''Sorting implementations in Python'''
__author__ = "Jordan Anderson"
__email__ = "jander2261@gmail.com"

def _merge(ary, start, partition, end):
    # merge sorted sub-arrays
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


def _merge_sort_core(ary, start = None, end = None):
    # split array into sub arrays for sorting, then merge
    if start is None:
        start = 0
    if end is None:
        end = len(ary)
    if not((end - start) > 1):
        return

    partition = (start + end) // 2
    _merge_sort_core(ary, start, partition)
    _merge_sort_core(ary, partition, end)
    _merge(ary, start, partition, end)


def merge_sort(ary):
    '''Sorts an array of numbers
    
    Keyword arguments:
    ary -- list of unsorted numbers
    '''

    if ((not ary is None) and (len(ary) > 1)):
        _merge_sort_core(ary)
    return