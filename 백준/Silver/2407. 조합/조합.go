package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

var n, m int
var fac = []*big.Int{big.NewInt(1), big.NewInt(1)}

func main() {
	var reader = bufio.NewReader(os.Stdin)
	var writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	fmt.Fscanln(reader, &n, &m)

	if n < m {
		fmt.Fprintln(writer, "1")
		return
	}
	for i := 2; i <= n; i++ {
		fac = append(fac, new(big.Int).Mul(fac[i-1], big.NewInt(int64(i))))
	}
	fmt.Fprintln(writer, new(big.Int).Quo(fac[n], new(big.Int).Mul(fac[n-m], fac[m])))
}
