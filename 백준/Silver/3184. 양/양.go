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
	var n, m int
	var graph [][]rune
	dx := []int{0, 1, 0, -1}
	dy := []int{1, 0, -1, 0}
	var shres, vres = 0, 0
	fmt.Fscanln(reader, &n, &m)
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
			if graph[i][j] == '.' || graph[i][j] == 'v' || graph[i][j] == 'o' {
				var queue [][]int
				queue = append(queue, []int{i, j})
				var sheep, wolf = 0, 0
				for len(queue) > 0 {
					x, y := queue[0][0], queue[0][1]
					queue = queue[1:]
					if graph[x][y] == '^' {
						continue
					}
					if graph[x][y] == 'o' {
						sheep++
					} else if graph[x][y] == 'v' {
						wolf++
					}
					graph[x][y] = '^'
					for k := 0; k < 4; k++ {
						nx, ny := x+dx[k], y+dy[k]
						if nx >= 0 && nx < n && ny >= 0 && ny < m {
							if graph[nx][ny] == '.' || graph[nx][ny] == 'v' || graph[nx][ny] == 'o' {
								queue = append(queue, []int{nx, ny})
							}
						}
					}
				}
				if sheep > wolf {
					shres += sheep
				} else {
					vres += wolf
				}
			}
		}
	}

	fmt.Fprintln(writer, shres, vres)

}
