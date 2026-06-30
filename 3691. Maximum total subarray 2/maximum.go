package main

import (
	"fmt"
	"math"
	"slices"
)

func maxTotalValue(nums []int, k int) int64 {
	// Get the best scenario out of the array, which contemplates
	// l = 0     r:n-1

	maxVal := 0
	minVal := math.MaxInt
	arrResults := make([]int, 0)
	bestResultCount := 0

	for _, num := range nums {
		maxVal = max(num, maxVal)
		minVal = min(num, minVal)
	}

	goal := maxVal - minVal // Best result obtainable
	// arrResults = append(arrResults, goal)
	// bestResultCount = 1
	fmt.Println("Best case scenario", goal)

	if k == 1 {
		return int64(goal)
	}

	// Start evaluating from the
	l := 0

	for l < len(nums) {
		fmt.Println("Starting with l:", l)
		j := len(nums) - 1
		for j >= l {
			fmt.Printf("Processing for l:%v j:%v arr:%v\n", l, j, nums[l:j+1])
			maxVal = 0
			minVal = math.MaxInt

			for _, val := range nums[l : j+1] {
				maxVal = max(val, maxVal)
				minVal = min(val, minVal)
			}
			result := maxVal - minVal
			arrResults = append(arrResults, result)
			if result == goal {
				bestResultCount++
			}

			if bestResultCount == k {
				break
			}
			fmt.Printf("Result for l:%v: r: %v\n", l, result)
			j--
		}
		if bestResultCount == k {
			break
		}

		l++
	}

	if bestResultCount == k {
		return int64(goal) * int64(k)
	} else {
		// Get best results out of maxResults array
		slices.Sort(arrResults)
		fmt.Println(arrResults)
		// Take the last k elements
		result := 0
		for _, val := range arrResults[len(arrResults)-k:] {
			result += val
		}
		return int64(result)
	}
}

func main() {
	nums := []int{11, 8}
	k := 8

	res := maxTotalValue(nums, k)
	fmt.Println("Response", res)
}
