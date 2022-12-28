// Recursive Go program to calculate the factorial of a given number.
//
// @File = factorial.go
// @Date = 2022-12-28
// @Author = Jannis Metrikat
// @Version = 1.0

package main

import (
	"fmt"
	"os"
	"strconv"
)

// Calculates the factorial of a given number.
func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

// main is the entry point for the program.
func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: go run factorial.go <number>")
		os.Exit(1)
	}

	in := os.Args[1]
	n, err := strconv.Atoi(in)
	if err != nil { panic(err) }

	fmt.Println(factorial(n))
}
