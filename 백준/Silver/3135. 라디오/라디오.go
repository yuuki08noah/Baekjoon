package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var a, b int
	var n int
	var temp float64 = 1000000000

	fmt.Fscanln(reader, &a, &b)
	fmt.Fscanln(reader, &n)
	for i := 0; i < n; i++ {
		var value float64
		fmt.Fscanln(reader, &value)
		if temp > math.Abs(float64(b)-value) {
			temp = math.Abs(float64(b) - value)
		}
	}
	if math.Abs(float64(a-b)) <= temp {
		fmt.Fprintln(writer, math.Abs(float64(a-b)))
	} else {
		fmt.Fprintln(writer, temp+1)
	}
}
