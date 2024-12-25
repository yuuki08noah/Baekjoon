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

	var n, m int
	fmt.Fscanln(reader, &n, &m)
	fruits := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &fruits[i])
	}
	sort.Ints(fruits)
	for i := 0; i < n; i++ {
		if fruits[i] <= m {
			m++
		} else {
			break
		}
	}
	fmt.Fprintln(writer, m)
}
