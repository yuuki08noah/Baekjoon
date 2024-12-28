package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var t int
	fmt.Fscanln(reader, &t)
	for test := 0; test < t; test++ {
		var n, m int
		fmt.Fscanln(reader, &n, &m)
		var boxes = make([]int, m)
		for i := 0; i < m; i++ {
			var x, y int
			fmt.Fscanln(reader, &x, &y)
			boxes[i] = x * y
		}
		sort.Sort(sort.Reverse(sort.IntSlice(boxes)))
		var cnt int
		for i := 0; n > 0; i++ {
			n -= boxes[i]
			cnt++
		}
		fmt.Fprintln(writer, cnt)
	}
}
