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
	var n int

	fmt.Fscanln(reader, &n)
	list := make([]int, n)
	for i := 0; i < n; i++ {
		var m int
		fmt.Fscan(reader, &m)
		list[i] = m
	}
	sort.Sort(sort.Reverse(sort.IntSlice(list)))
	m := list[0] - n + 1
	for i := 1; i < n; i++ {
		list[i] = list[i] - n + i + 1
		if m < list[i] {
			m = list[i]
		}
	}

	fmt.Fprintln(writer, m+n+1)
}
