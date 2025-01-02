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

	var n, cnt int
	fmt.Fscanln(reader, &n)
	var mtr = make([]int, n)
	var mtrUsed = make([]bool, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &mtr[i])
	}
	sort.Ints(mtr)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if mtr[i] < mtr[j] && !mtrUsed[j] {
				mtrUsed[j] = true
				mtr[i] = 100
				break
			}
		}
	}
	for i := 0; i < n; i++ {
		if mtr[i] != 100 {
			cnt++
		}
	}
	fmt.Fprintln(writer, cnt)
}
