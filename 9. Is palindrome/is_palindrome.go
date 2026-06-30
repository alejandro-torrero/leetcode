package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	strNum := strconv.Itoa(x)
	isPalindrome := true

	i := 0
	j := len(strNum) - 1

	for i != j && i < j {
		if strNum[i] != strNum[j] {
			isPalindrome = false
			break
		}
		i++
		j--
	}

	return isPalindrome
}

func main() {
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(1))
	fmt.Println(isPalindrome(11))
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(121))
}
