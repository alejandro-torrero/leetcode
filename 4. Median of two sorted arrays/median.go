package main

import (
	"fmt"
	"math"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	mergeArr := make([]int, 0)

	i, j := 0, 0

	for i < len(nums1) {
		if j >= len(nums2) || nums1[i] <= nums2[j] {
			mergeArr = append(mergeArr, nums1[i])
			i++
		} else {
			fmt.Println("Must add from 2")

			for j <= len(nums2) && (nums2[j] < nums1[i]) {
				mergeArr = append(mergeArr, nums2[j])
				j++
			}
		}
	}

	mergeArr = append(mergeArr, nums2[j:]...)

	isPair := len(mergeArr)%2 == 0
	halfIndex := int(math.Floor(float64(len(mergeArr) / 2)))

	if isPair {
		return float64((mergeArr[halfIndex-1] + mergeArr[halfIndex])) / 2
	} else {
		return float64(mergeArr[halfIndex])

	}
}

func main() {

	nums1 := []int{0, 0}
	nums2 := []int{0, 0}

	res := findMedianSortedArrays(nums1, nums2)

	fmt.Printf("Res: %v", res)

}
