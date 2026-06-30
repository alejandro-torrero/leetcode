package main

import "fmt"

func longestPalindrome(s string) string {
	fmt.Println("Running for", s)
	if len(s) == 1 {
		return s
	}

	i := 0          // Left index
	j := len(s) - 1 // right index
	//dir := 0        // Direction control

	left := ""
	right := ""

	direction := 0

	for i != j {

		if direction == 0 {
			fmt.Println("Direccion en j")
			// Advance on j
			goal := string(s[i])
			current := string(s[j])
			for goal != current && j != i {
				j--
				current = string(s[j])
			}
			if j == i {
				// No hubo match con i, ignorar ese i
				// Reiniciar j y cambiar dirección
				right = ""
				left = ""
				j = len(s) - 1
				i++
				direction = 1
				fmt.Println("Sin match, cambiando dirección", i, j)
			} else {
				// Se encontró match
				fmt.Println("Match encontrado con", goal, "i: ", i, "j: ", j)
				left = left + goal
				right = goal + right
				// Avanzar a las siguientes posiciones
				i++
				j--
				if i > j {
					break
				}
			}
		} else {
			fmt.Println("Direccion en i")
			// Advance on i
			goal := string(s[j])
			current := string(s[i])
			for goal != current && j != i {
				i++
				current = string(s[i])
			}
			if j == i {
				// No hubo match
				// Reiniciar j y cambiar dirección
				left = ""
				right = ""
				i = 0
				j--
				direction = 1
				fmt.Println("Sin match, cambiando dirección", i, j)
			} else {
				// Se encontró match
				fmt.Println("Match encontrado con", goal, "i: ", i, "j: ", j)
				left = left + goal
				right = goal + right
				// Avanzar a las siguientes posiciones
				i++
				j--
				if i > j {
					break
				}
			}
		}

		fmt.Println("left:", left, "right: ", right)

	}

	if i == j {
		// Apuntan al mismo caracter
		return left + string(s[i]) + right
	}

	return left + right
}

func main() {
	str := "babad"
	res := longestPalindrome(str)
	fmt.Println("Longest palindromic string", res, "on", str)

	str = "cbbd"
	res = longestPalindrome(str)
	fmt.Println("Longest palindromic string", res, "on", str)

	str = "bacabac"
	res = longestPalindrome(str)
	fmt.Println("Longest palindromic string", res, "on", str)

	str = "a"
	res = longestPalindrome(str)
	fmt.Println("Longest palindromic string", res, "on", str)

	str = "hjklayu"
	res = longestPalindrome(str)
	fmt.Println("Longest palindromic string", res, "on", str)

	str = "bb"
	res = longestPalindrome(str)
	fmt.Println("Longest palindromic string", res, "on", str)

	str = "bbcbb"
	res = longestPalindrome(str)
	fmt.Println("Longest palindromic string", res, "on", str)

	str = "abbcccba"
	res = longestPalindrome(str)
	fmt.Println("Longest palindromic string", res, "on", str)

	str = "aacabdkacaa"
	res = longestPalindrome(str)
	fmt.Println("Longest palindromic string", res, "on", str)
}
