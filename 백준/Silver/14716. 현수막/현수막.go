package main

import (
	"bufio"
	"fmt"
	"os"
)

var n int
var m int
var dx = [8]int{0, 0, -1, 1, 1, 1, -1, -1}
var dy = [8]int{-1, 1, 0, 0, 1, -1, 1, -1}
var graph [][]int
var cnt = 0

func main() {
	var reader = bufio.NewReader(os.Stdin)
	var writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	fmt.Fscanln(reader, &n, &m)

	for i := 0; i < n; i++ {
		var temp []int
		for j := 0; j < m; j++ {
			var value int
			fmt.Fscan(reader, &value)
			temp = append(temp, value)
		}
		graph = append(graph, temp)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if graph[i][j] == 1 {
				cnt++
				dfs(i, j)
			}
		}
	}

	fmt.Fprintln(writer, cnt)

}

func dfs(x int, y int) {
	graph[x][y] = 0
	for i := 0; i < 8; i++ {
		nx := x + dx[i]
		ny := y + dy[i]
		if (0 <= nx && nx < n) && (0 <= ny && ny < m) {
			if graph[nx][ny] == 1 {
				dfs(nx, ny)
			}
		}
	}
}
