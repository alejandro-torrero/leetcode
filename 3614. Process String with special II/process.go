package main

import (
	"fmt"
	"slices"
)

type StringProcessor struct {
	control []string
	length  int64
}

func (st *StringProcessor) Add(char string) {
	st.control = append(st.control, char)
	st.length = int64(len(st.control))
}

func (st *StringProcessor) RemoveLastChar() {
	if st.length > 0 {
		st.control = st.control[:st.length-1]
	}
	st.length = int64(len(st.control))
}

func (st *StringProcessor) Duplicate() {
	if st.length > 0 {
		st.control = append(st.control, st.control...)
	}
	st.length = int64(len(st.control))
}

func (st *StringProcessor) Reverse() {
	slices.Reverse(st.control)
}

func (st *StringProcessor) GetChar(k int64) byte {
	if k >= st.length {
		return byte('.')
	}
	return st.control[k][0]
}

func processStr(s string, k int64) byte {
	st := StringProcessor{
		control: make([]string, 0),
		length:  0,
	}

	for _, val := range s {
		char := string(val)

		switch char {
		case "*":
			// Remove
			st.RemoveLastChar()
		case "#":
			// Duplicate
			st.Duplicate()
		case "%":
			// reverse
			st.Reverse()
		default:
			st.Add(char)
		}
	}
	return st.GetChar(k)
}
func main() {

	res := processStr("##zly#f###a#hl#qw%#h#g#x##%vd*e#xgig##%fsr###n#*##%#bg#vw#vn", 2306)
	fmt.Println(res)
}
