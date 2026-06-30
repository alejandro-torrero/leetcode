package main

import "fmt"

func pivotArray(nums []int, pivot int) []int {
	lowerThan := make([]int, 0)
	greaterThan := make([]int, 0)
	pivotArr := make([]int, 0)

	for _, value := range nums {
		if value < pivot {
			lowerThan = append(lowerThan, value)
		} else if value > pivot {
			greaterThan = append(greaterThan, value)
		} else if pivot == value {
			pivotArr = append(pivotArr, value)
		}
	}
	result := lowerThan
	result = append(result, pivotArr...)
	result = append(result, greaterThan...)
	return result

}

func main() {
	arr := []int{9, 12, 5, 10, 14, 3, 10}
	pivot := 10
	res := pivotArray(arr, pivot)
	fmt.Println(res)
}
