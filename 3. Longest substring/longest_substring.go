package main

import (
	"fmt"
	"strings"
	"time"
)

func lengthOfLongestSubstring(s string) int {
	substring := ""
	maxLen := 0
	for i, value := range s {
		val := string(value)
		isPresent := strings.IndexAny(substring, val)
		if isPresent < 0 {
			substring += val
			if len(substring) > maxLen {
				maxLen = len(substring)
			}
		} else {
			if len(substring) > maxLen {
				maxLen = len(substring)
			}
			temp := substring[isPresent+1:]
			if (len(temp) + (len(s) - i - 1)) < maxLen {
				break
			}
			substring = temp + val
		}
	}
	return maxLen
}

func main() {
	start := time.Now()
	str := "abcabcbb"
	r := lengthOfLongestSubstring(str)
	fmt.Println(r)
	str = "bbbbb"
	r = lengthOfLongestSubstring(str)
	fmt.Println(r)
	str = "pwwkew"
	r = lengthOfLongestSubstring(str)
	fmt.Println(r)
	str = "hkcpmprxxxqw"
	r = lengthOfLongestSubstring(str)
	fmt.Println(r)

	elapsed := time.Now().Sub(start)
	fmt.Println("Finished in", elapsed)
}
