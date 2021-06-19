#!/usr/bin/env  python3
# !-*-coding:utf-8 -*-
# !@File : $[name].py


#该文件中是二分法的例子
#涉及到的题目，均来自于leetcode


#在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，
#而不是第 k 个不同的元素。
#题目链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
import random
from typing import List
def findKthLargest(nums: List[int], k: int) -> int:
    #patition的作用是找到，当前元素在数组中，应该所站的位置
    # def patition(nums, left, right):
    #     # 使用类似快排的方式
    #     # x = nums[left]
    #     pivot = left
    #     # 此时的index永远指向，比x大的最小一个数所在的位置
    #     index = pivot + 1
    #     for i in range(index, right + 1):
    #         # 如果有小于标杆的，就交换
    #         # 如果此前一直都是小于的，就不用交换
    #         # index每增加一次，就是标杆的位置向前挪动1
    #         if nums[i] < nums[pivot]:
    #             nums[i], nums[index] = nums[index], nums[i]
    #             index += 1
    #     nums[left], nums[index - 1] = nums[index - 1], nums[left]
    #     print(nums)
    #     return left+index - 1

    #另一种patition
    def patition(nums,left, right):
        x = nums[left]
        while right > left:
            while left < right and nums[right] > x:
                right -=1
            nums[left] = nums[right]
            while left < right and nums[left] < x:
                left +=1
            nums[right] =nums[left]
        return left

    def quitsort(nums,left,right,k):
        while True:
            #随机抽取一个数
            index = random.randint(left,right)
            nums[left], nums[index] = nums[index], nums[left]
            pat = patition(nums,left,right)
            if pat == k:
                return nums[left]
            elif pat < k:
                left = pat+1
            else:
                right = pat-1
    n = len(nums)
    return quitsort(nums,0,n-1,n-k-1)

#快速排序的思想是分治，首先得到一个标杆，然后经过一次排序，比标杆大的，排在右边
#比标杆小的，排在左边
#一次便利，可以确定一个数的位置
#然后将确定位置的数的左边和右边，再递归排序

#除了使用快速排序之外，还可以使用堆排序
#维护一个小根对，最小的，就是第k个大
import heapq
def findKthLargest2( nums: List[int], k: int) -> int:
    s = []
    n = len(nums)
    for i in range(n):
        # 此时的数组个数小于n-k,不存在第k大的数
        if i < k:
            heapq.heappush(s, nums[i])
        else:
            if nums[i] > s[0]:
                s[0] = nums[i]
                heapq.heapify(s)
    return s[0]


# 编写一个高效的算法来搜索mxn矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#题目链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        start = 0
        end = m-1
        if matrix[i][end] < target or matrix[i][start] > target:
            continue
        else:
            while start <= end:
                mid = (start+end)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    start = mid + 1
                else:
                    end = mid -1
    return False


#从题目的描述可以看出来，输入的矩阵是从左到右增大，从上到下增大
#因此我们可以先判断target 有可能再哪一个行，
#如果这一行的最小数大于target 或者最大数小于target,则该数不可能在这一行
#当找到目标可能在的行之后，使用二分法来查找，如果不在这一样，则继续往下一行找，如果在，则直接返回True
#当把整个矩阵都找完，还没有找到时，直接返回False

