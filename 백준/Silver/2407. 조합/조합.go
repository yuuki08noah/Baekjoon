package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

var n, m int
var dp [101][101]*big.Int

func main() {
	var reader = bufio.NewReader(os.Stdin)
	var writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	fmt.Fscanln(reader, &n, &m)

	for i := 1; i <= n; i++ {
		for j := 1; j <= m && j <= i; j++ {
			if i == j {
				dp[i][j] = big.NewInt(int64(1))
				continue
			}
			if j == 1 {
				dp[i][j] = big.NewInt(int64(i))
				continue
			}

			dp[i][j] = new(big.Int).Add(dp[i-1][j], dp[i-1][j-1])
		}
	}
	if dp[n][m].Cmp(big.NewInt(1)) < 0 {
		fmt.Fprintln(writer, 1)
	} else {
		fmt.Fprintln(writer, dp[n][m])
	}
}
