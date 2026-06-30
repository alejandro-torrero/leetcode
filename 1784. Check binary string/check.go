package main

import "fmt"

func checkOnesSegment(s string) bool {
	isValid := false
	checkNext := false

	if s == "1" {
		return true
	}

	for _, value := range s {
		str := string(value)
		if str == "1" && checkNext {
			isValid = true
			break
		} else if checkNext && str != "1" {
			checkNext = false
		} else if str == "1" {
			checkNext = true
		}
	}
	return isValid
}

func main() {
	fmt.Println(checkOnesSegment("10"))
	// fmt.Println(checkOnesSegment("110"))
}
