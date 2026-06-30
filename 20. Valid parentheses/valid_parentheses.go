package main

import "fmt"

func isValid(s string) bool {
	stack := make([]string, 0, len(s))
	isValid := true

	if len(s) == 0 {
		return isValid
	}

	for _, value := range s {
		str := string(value)

		switch str {
		case "[", "(", "{":
			stack = append(stack, str)
		case "]":
			if len(stack) == 0 {
				isValid = false
				continue
			}
			if stack[len(stack)-1] != "[" {
				isValid = false
			}
			stack = stack[:len(stack)-1]
		case ")":
			if len(stack) == 0 {
				isValid = false
				continue
			}
			if stack[len(stack)-1] != "(" {
				isValid = false
			}
			stack = stack[:len(stack)-1]
		case "}":
			if len(stack) == 0 {
				isValid = false
				continue
			}
			if stack[len(stack)-1] != "{" {
				isValid = false
			}
			stack = stack[:len(stack)-1]
		}

		if !isValid {
			break
		}
	}
	return isValid && len(stack) == 0
}

func main() {
	valid := isValid("]")
	fmt.Println(valid)
}
