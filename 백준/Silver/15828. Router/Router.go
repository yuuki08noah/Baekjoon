package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

type CircularQueue[T any] struct {
	data              []T
	rear, front, size int
}

func InitCircularQueue[T any](size int) *CircularQueue[T] {
	queue := new(CircularQueue[T])
	queue.data = make([]T, size)
	queue.front = 0
	queue.rear = 0
	queue.size = size
	return queue
}

func (q *CircularQueue[T]) isEmpty() bool {
	return q.front == q.rear
}

func (q *CircularQueue[T]) isFull() bool {
	return (q.rear+1)%q.size == q.front
}

func (q *CircularQueue[T]) Enqueue(value T) error {
	if q.isFull() {
		return errors.New("Queue is full")
	}
	q.rear = (q.rear + 1) % q.size
	q.data[q.rear] = value
	return nil
}

func (q *CircularQueue[T]) Dequeue() (T, error) {
	var value T
	if q.isEmpty() {
		return value, errors.New("Queue is empty")
	}
	q.front = (q.front + 1) % q.size
	value = q.data[q.front]
	return value, nil
}

func (q *CircularQueue[T]) PrintCircularQueue() {
	for i := (q.front + 1) % q.size; i != (q.rear+1)%q.size; i = (i + 1) % q.size {
		fmt.Fprint(writer, q.data[i], " ")
	}
	fmt.Fprintln(writer)
}

func main() {
	defer writer.Flush()
	var n, m int
	fmt.Fscanln(reader, &n)
	q := InitCircularQueue[int](n + 1)
	for {
		fmt.Fscanln(reader, &m)
		if m == -1 {
			break
		} else if m != 0 {
			err := q.Enqueue(m)
			if err != nil {
				continue
			}
		} else {
			_, err := q.Dequeue()
			if err != nil {
				continue
			}
		}
	}
	if q.isEmpty() {
		fmt.Fprintln(writer, "empty")
	} else {
		q.PrintCircularQueue()
	}
}
