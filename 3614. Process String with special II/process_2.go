package main

import "fmt"

func processStr(s string, k int64) byte {
	strLen := int64(0)
	strIndex := k

	for _, val := range s {
		char := string(val)

		switch char {
		case "*":
			if strLen > 0 {
				strLen--
			}

			if strIndex >= strLen {

			}
		case "#":
			// Duplicate
			strLen = strLen * 2

			strIndex = strIndex % strLen
		case "%":
			// reverse
			strIndex = strLen - 1 - strIndex

		default:
			strLen++

		}
	}

	if strLen == 0 {
		return byte(".")
	} else {
		return s[strIndex]
	}
}

func main() {
	res := processStr("##zly#f###a#hl#qw%#h#g#x##%vd*e#xgig##%fsr###n#*##%#bg#vw#vn", 2306)
	fmt.Println(res)
}
