package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var reader = bufio.NewReader(os.Stdin)
	var writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int

	fmt.Fscanln(reader, &n)

	var dp = make([]int, 1001)
	dp[0] = 1
	dp[1] = 1
	for i := 2; i <= n; i++ {
		k := 1
		for ; k <= i; k++ {
			flag := false
			for j := i; j > 0; j-- {
				if i-2*j < 0 {
					continue
				}
				if k-dp[i-j] == dp[i-j]-dp[i-2*j] {
					//fmt.Println(k, i, j)
					flag = true
					break
				}
			}
			if flag {
				continue
			}
			dp[i] = k
			break
		}
	}
	fmt.Fprintln(writer, dp[n])

}
