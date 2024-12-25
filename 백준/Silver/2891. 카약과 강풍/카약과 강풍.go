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

	var n, s, r, cnt int
	fmt.Fscanln(reader, &n, &s, &r)
	arr := make([]int, n+1)

	for i := 0; i < s; i++ {
		var value int
		fmt.Fscan(reader, &value)
		arr[value]--
	}
	for i := 0; i < r; i++ {
		var value int
		fmt.Fscan(reader, &value)
		arr[value]++
	}
	for i := 1; i <= n; i++ {
		if arr[i] > 0 {
			if i > 1 && arr[i-1] == -1 {
				arr[i-1]++
				arr[i]--
			} else if i < n && arr[i+1] == -1 {
				arr[i+1]++
				arr[i]--
			}
		}
	}
	for i := 1; i <= n; i++ {
		if arr[i] == -1 {
			cnt++
		}
	}
	fmt.Fprintln(writer, cnt)
}
