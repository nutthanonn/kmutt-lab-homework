package main

import (
	"fmt"
	"sort"
	"strconv"
)

type Rows struct {
	no int
	a  int
	b  int
	c  int
}

type Pair struct {
	Key   string
	Value int
}

type PairList []Pair

func (p PairList) Len() int           { return len(p) }
func (p PairList) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func (p PairList) Less(i, j int) bool { return p[i].Value < p[j].Value }

func ABC_value(data Rows) int {
	return data.a*100 + data.b*10 + data.c
}

func CBA_value(data Rows) int {
	return data.a + data.b*10 + data.c*100
}

func BCA_value(data Rows) int {
	return data.a + data.b*100 + data.c*10
}

func SortMultiColumn(data [14]Rows) PairList {
	index_map := make(map[string]int)
	for _, v := range data {
		i := BCA_value(v) // change this function if you want to change sort
		index_map[strconv.Itoa(v.no)] = i
	}

	p := make(PairList, len(index_map))
	i := 0
	for k, v := range index_map {
		p[i] = Pair{k, v}
		i++
	}
	sort.Sort(p)
	return p
}

func main() {
	data := [][]int{
		{1, 1, 1, 4},
		{2, 3, 1, 1},
		{3, 4, 4, 4},
		{4, 2, 4, 4},
		{5, 3, 5, 3},
		{6, 4, 3, 3},
		{7, 1, 3, 3},
		{8, 2, 4, 3},
		{9, 3, 3, 5},
		{10, 1, 5, 3},
		{11, 1, 1, 4},
		{12, 4, 1, 1},
		{13, 5, 2, 3},
		{14, 3, 5, 2},
	}
	var table [14]Rows
	for i, v := range data {
		table[i].no = v[0]
		table[i].a = v[1]
		table[i].b = v[2]
		table[i].c = v[3]
	}
	sort_data := SortMultiColumn(table)

	fmt.Printf("No\tA\tB\tC\n")
	fmt.Println("---------------------------------")
	for _, v := range sort_data {
		i, err := strconv.Atoi(v.Key)

		if err != nil {
			panic(err)
		}

		fmt.Printf("%d\t%d\t%d\t%d\n", data[i-1][0], data[i-1][1], data[i-1][2], data[i-1][3])
	}

}
