def countNodes(root):
    """
    Количество вершин в бинарном дереве
    """
    if not root:
        return 0
    
    left_count = countNodes(root.left)
    right_count = countNodes(root.right)
    
    return left_count + right_count + 1

# Тестирование
if __name__ == "__main__":
    # Пример дерева с 5 вершинами
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Количество вершин:", countNodes(root))  # 5
