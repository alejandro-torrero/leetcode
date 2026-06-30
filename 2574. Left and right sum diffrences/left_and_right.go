package main

import (
	"fmt"
	"math"
)

func leftRightDifference(nums []int) []int {
	leftSum := make([]int, len(nums))
	rightSum := make([]int, len(nums))

	result := make([]int, len(nums))

	i := 0
	j := len(nums) - 1

	for i < len(nums) {
		if i == 0 {
			leftSum[i] = 0
		} else {
			leftSum[i] = nums[i-1] + leftSum[i-1]
		}

		if j == len(nums)-1 {
			rightSum[j] = 0
		} else {
			rightSum[j] = nums[j+1] + rightSum[j+1]
		}

		// Next
		i++
		j--
	}

	i = 0

	for i < len(nums) {
		// Calculate result
		result[i] = int(math.Abs(float64(leftSum[i]) - float64(rightSum[i])))
		i++
	}

	return result
}

func main() {
	res := leftRightDifference([]int{10, 4, 8, 3})
	fmt.Print(res)
}
