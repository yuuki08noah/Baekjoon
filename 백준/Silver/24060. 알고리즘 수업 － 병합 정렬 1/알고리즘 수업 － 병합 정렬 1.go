package main

import (
	"bufio"
	"fmt"
	"os"
)

var cnt, k int
var flag bool

func MergeSort(arr []int) {
	Divide(arr, 0, len(arr)-1)
}

func Divide(arr []int, left int, right int) {
	if left < right {
		mid := (left + right) / 2
		Divide(arr, left, mid)
		Divide(arr, mid+1, right)
		Conquer(arr, left, right)
	}
}

func Conquer(arr []int, left int, right int) {
	sorted := make([]int, right-left+1)
	low := left
	mid := (left + right) / 2
	high := mid + 1
	index := 0

	for low <= mid && high <= right {
		cnt++
		if arr[low] < arr[high] {
			if cnt == k {
				fmt.Println(arr[low])
				flag = true
			}
			sorted[index] = arr[low]
			index++
			low++
		} else {
			if cnt == k {
				fmt.Println(arr[high])
				flag = true
			}
			sorted[index] = arr[high]
			index++
			high++
		}
	}
	for low <= mid {
		cnt++
		if cnt == k {
			fmt.Println(arr[low])
			flag = true
		}
		sorted[index] = arr[low]
		index++
		low++
	}
	for high <= right {
		cnt++
		if cnt == k {
			fmt.Println(arr[high])
			flag = true
		}
		sorted[index] = arr[high]
		index++
		high++
	}
	for i := left; i <= right; i++ {
		arr[i] = sorted[i-left]
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n, &k)
	var arr = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &arr[i])
	}
	MergeSort(arr)
	if !flag {
		fmt.Fprintln(writer, -1)
	}
}
