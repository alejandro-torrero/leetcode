package main

import (
	"fmt"
)

func maxNumberOfBalloons(text string) int {
	nBallons := 0

	strMap := map[string]int{
		"b": 0,
		"a": 0,
		"l": 0,
		"o": 0,
		"n": 0,
	}

	for _, val := range text {
		if _, exists := strMap[string(val)]; exists {
			strMap[string(val)]++
		}
	}

	fmt.Println(strMap)

	// Process ballons
	// map[a:1 b:1 l:2 n:1 o:2]
	cycleControl := true

	for cycleControl {
		if strMap["b"] >= 1 {
			strMap["b"]--
		} else {
			cycleControl = false
			break
		}
		if strMap["a"] >= 1 {
			strMap["a"]--
		} else {
			cycleControl = false
			break
		}
		if strMap["l"] >= 2 {
			strMap["l"] -= 2
		} else {
			cycleControl = false
			break
		}
		if strMap["o"] >= 2 {
			strMap["o"] -= 2
		} else {
			cycleControl = false
			break
		}
		if strMap["n"] >= 1 {
			strMap["n"]--
		} else {
			cycleControl = false
			break
		}
		nBallons++
	}

	return nBallons
}

func main() {
	fmt.Println(maxNumberOfBalloons("nlaebolko"))
	fmt.Println(maxNumberOfBalloons("loonbalxballpoon"))
}
