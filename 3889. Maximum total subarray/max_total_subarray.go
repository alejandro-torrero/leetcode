package main

import (
	"fmt"
	"math"
)

/* func maxTotalValue(nums []int, k int) int64 {
	maxVal := uint64(0)
	minVal := uint64(math.MaxUint64)

	for _, num := range nums {
		fmt.Println(maxVal, minVal)
		maxVal = uint64(math.Max(float64(num), float64(maxVal)))
		minVal = uint64(math.Min(float64(num), float64(minVal)))
	}
	return int64(int(maxVal-minVal) * k)
} */

func maxTotalValue(nums []int, k int) int64 {
	maxVal := 0
	minVal := math.MaxInt

	for _, num := range nums {
		maxVal = max(num, maxVal)
		minVal = min(num, minVal)
	}

	return int64((maxVal - minVal) * k)
}

func main() {

	arr := []int{22}
	res := maxTotalValue(arr, 2)

	fmt.Println("Result ", res)
}
