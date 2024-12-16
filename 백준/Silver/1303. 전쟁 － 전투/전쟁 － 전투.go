package main

import (
	"bufio"
	"fmt"
	"os"
)

var dx = []int{0, 0, 1, -1}
var dy = []int{1, -1, 0, 0}
var n, m int
var graph [][]rune

func main() {
	var writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var reader = bufio.NewReader(os.Stdin)
	var w, b int

	fmt.Fscanln(reader, &m, &n)

	for i := 0; i < n; i++ {
		var temp []rune
		for j := 0; j <= m; j++ {
			var value rune
			fmt.Fscanf(reader, "%c", &value)
			if value == '\n' {
				continue
			}
			temp = append(temp, value)
		}
		graph = append(graph, temp)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if graph[i][j] == 'W' {
				v := bfs('W', i, j)
				w += v * v
			} else if graph[i][j] == 'B' {
				v := bfs('B', i, j)
				b += v * v
			}
		}
	}

	fmt.Fprintln(writer, w, b)
}

func bfs(ch rune, i int, j int) int {
	queue := [][]int{{i, j}}
	cnt := 0
	for len(queue) > 0 {
		x, y := queue[0][0], queue[0][1]
		queue = queue[1:]
		if graph[x][y] != ch {
			continue
		}
		//fmt.Println(queue)
		cnt++
		graph[x][y] = '^'
		for k := 0; k < 4; k++ {
			nx, ny := x+dx[k], y+dy[k]
			if nx >= 0 && nx < n && ny >= 0 && ny < m {
				if graph[nx][ny] == ch {
					queue = append(queue, []int{nx, ny})
				}
			}
		}
	}
	return cnt
}
