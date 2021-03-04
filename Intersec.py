from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
print(intersection(arr1,arr2))