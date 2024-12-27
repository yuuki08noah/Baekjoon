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

	var b, s, d, sum int
	fmt.Fscanln(reader, &b, &s, &d)
	var burgers = make([]int, b)
	var sides = make([]int, s)
	var drinks = make([]int, d)
	for i := 0; i < b; i++ {
		fmt.Fscan(reader, &burgers[i])
		sum += burgers[i]
	}
	fmt.Fscanln(reader)
	for i := 0; i < s; i++ {
		fmt.Fscan(reader, &sides[i])
		sum += sides[i]
	}
	fmt.Fscanln(reader)
	for i := 0; i < d; i++ {
		fmt.Fscan(reader, &drinks[i])
		sum += drinks[i]
	}
	fmt.Fscanln(reader)
	fmt.Fprintln(writer, sum)
	sort.Sort(sort.Reverse(sort.IntSlice(burgers)))
	sort.Sort(sort.Reverse(sort.IntSlice(sides)))
	sort.Sort(sort.Reverse(sort.IntSlice(drinks)))

	var sale int
	var i int
	for ; i < b && i < s && i < d; i++ {
		sale += (burgers[i] + sides[i] + drinks[i]) * 9 / 10
	}
	for j := i; j < b; j++ {
		sale += burgers[j]
	}
	for j := i; j < s; j++ {
		sale += sides[j]
	}
	for j := i; j < d; j++ {
		sale += drinks[j]
	}
	fmt.Fprintln(writer, sale)
}
