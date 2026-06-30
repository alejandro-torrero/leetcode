package main

import "fmt"

func twoSum(nums []int, target int) []int {
	res := []int{}

	i := 0
	ctrlFlag := false

	for index, val := range nums {
		i = index + 1

		for i < len(nums) {
			if (val + nums[i]) == target {
				// Found target
				res = append(res, index, i)
				ctrlFlag = true
				break
			}
			i++
		}

		if ctrlFlag {
			break
		}

	}

	return res
}

func main() {
	numbers := []int{3, 2, 4}

	result := twoSum(numbers, 6)
	fmt.Println(result)
}
