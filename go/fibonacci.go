// Go Programm using memoization to calculate the fibonacci number of a given number.
// A recursive solution would have a time complexity of O(2^n) and threrefore is not feasible.
//
// @File = fibonacci.go
// @Date = 2022-12-28
// @Author = Jannis Metrikat
// @Version = 1.0

package main

import (
	"fmt"
	"os"
	"strconv"
)

// calculate the fibonacci number of a given number
func fibonacci(n int) int {
	fib := make([]int, n+1, n+2)

	if n < 2 {
		fib = fib[0:2]
	}

	fib[0] = 0
	fib[1] = 1

	for i := 2; i <= n; i++ {
		fib[i] = fib[i-1] + fib[i-2]
	}

	return fib[n]
}

// main is the entry point for the program
func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: go run fibonacci.go <number>")
		os.Exit(1)
	}

	in := os.Args[1]
	n, err := strconv.Atoi(in)
	if err != nil {
		panic(err)
	}

	fmt.Println(fibonacci(n))
}
