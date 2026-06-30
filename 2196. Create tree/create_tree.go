package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func createBinaryTree(descriptions [][]int) *TreeNode {
	var rootTree *TreeNode = nil

	nodes := map[int]*TreeNode{}
	hasParent := map[int]bool{}

	for _, value := range descriptions {

		// -------------------------- Prepare data --------------------------
		fmt.Println("Processing", value)
		parentValue := value[0]

		childValue := value[1]

		nodeIsLeft := value[2] == 1

		var childNode *TreeNode = nil
		var parentNode *TreeNode = nil

		// -------------------------- Search for nodes --------------------------

		if node, exists := nodes[childValue]; exists {
			childNode = node
			hasParent[childValue] = true
		} else {
			childNode = &TreeNode{
				Val:   childValue,
				Left:  nil,
				Right: nil,
			}
			nodes[childValue] = childNode
		}

		if node, exists := nodes[parentValue]; exists {
			parentNode = node
		} else {
			parentNode = &TreeNode{
				Val:   parentValue,
				Left:  nil,
				Right: nil,
			}
			nodes[parentValue] = parentNode
			hasParent[parentValue] = false
		}

		// -------------------------- Link nodes --------------------------

		if nodeIsLeft {
			parentNode.Left = childNode
		} else {
			parentNode.Right = childNode
		}

		fmt.Println("Linked parent to child", parentNode)

		// -------------------------- Redefined root tree --------------------------

		if rootTree == nil {
			rootTree = parentNode
			continue
		}

	} // For cycle

	fmt.Println(hasParent)

	for key, isChild := range hasParent {
		if !isChild {
			rootTree = nodes[key]
		}
	}

	return rootTree
}

func main() {

	array := [][]int{{85, 82, 1}, {74, 85, 1}, {39, 70, 0}, {82, 38, 1}, {74, 39, 0}, {39, 13, 1}}
	// array := [][]int{{39, 70, 1}, {13, 39, 1}, {85, 74, 1}, {74, 13, 1}, {38, 82, 1}, {82, 85, 1}}
	// array := [][]int{{39, 70, 1}, {13, 39, 1}, {85, 74, 1}, {74, 13, 1}, {38, 82, 1}, {82, 85, 1}}
	//array := [][]int{{8, 25, 1}, {60, 61, 1}, {90, 1, 1}, {4, 3, 1}, {100, 22, 0}, {8, 4, 0}, {1, 100, 1}, {60, 65, 0}, {22, 60, 1}, {100, 8, 1}, {52, 90, 1}, {65, 28, 0}}
	// array := [][]int{{3, 4, 1}, {1, 90, 1}, {100, 61, 1}, {22, 1, 1}, {90, 52, 1}, {28, 22, 1}, {25, 8, 1}, {60, 65, 1}, {65, 28, 1}, {61, 60, 1}, {8, 3, 1}, {4, 100, 1}}

	createBinaryTree(array)
	// output := printTree(tree)
	// fmt.Println(output)

}
