/* main.go */

package main

import "fmt"

func main() {
	var (
		name   string  = "Mike"
		age    int     = 46
		height int     = 77
		weight float64 = 340.5
	)

	fmt.Print("Hello. My name is ", name, ", and my age is ", age, ".\n")
	fmt.Printf("My height is %d inches, and my weight is %.2f pounds.\n", height, weight)
}
