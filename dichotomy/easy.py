#!/usr/bin/env  python3
#!-*-coding:utf-8 -*-
#!@File : $[name].py

#leetcode
#easy 难度的二分法题目

#二分法的题目，是分治法的一个分支，起基本思想是将大的目标分成两个部分来操作
#这样每一次操作，就可以排除一半

#question 1
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
from typing import List
def searchInsert(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

#题解：
#典型的二分法应用：二分搜索
#left 代表寻找范围的最左边索引，right代表寻找范围最右边的索引
#mid 为搜寻中间的索引，由于数组是按顺序排列，所以如果target == nums[mid]则返回mid,
#如果target > nums[mid] 则如果存在，则该数一定在[mid+1 , right]范围，更新left的值
#如果target < nums[mid] 则如果该数存在，则该数一定在[left, mid-1]范围，更新right的值
#如果该数不存在，则此时的left则为将该数插入的索引
#题目链接： https://leetcode-cn.com/problems/search-insert-position/


#question2
# 符合下列属性的数组 arr 称为 山脉数组 ：
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i
def peakIndexInMountainArray(self, arr: List[int]) -> int:
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left+right) >> 1
        if arr[mid] > arr[mid+1]:
            right = mid
        else:
            left = mid+1
    return left

#该题也是比较典型的二分法题目
#在该数组中，存在一个索引i,使得arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#因此在数组中，可以通过不断缩小left和right的范围，来最终确定i的索引
#得到数组的中间索引mid, 如果arr[mid] > arr[mid+1]则表明mid在山峰的右半部分，且arr[mid]可能为山峰，因此此时的山峰范围为[left, mid],此时更新right=mid
#如果arr[mid] < arr[mid+1]则表明mid在山峰的左半部分，且arr[mid]不可能为山峰，因此此时的山峰范围为[mid+1， right],此时更新left=mid+1
#由于right = mid，while的循环条件修改为left < right
#此时返回left即为山峰的值
#题目链接为： https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/



