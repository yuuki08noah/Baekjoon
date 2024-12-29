package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n, m, cnt int
	fmt.Fscanln(reader, &n, &m)
	var books = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &books[i])
	}
	for i := 0; i < n; {
		l := m
		for i < n && l-books[i] >= 0 {
			l -= books[i]
			i++
		}
		cnt++
	}
	fmt.Fprintln(writer, cnt)
}
