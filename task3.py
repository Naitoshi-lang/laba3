def maxDepth(root):
    """
    Максимальная глубина бинарного дерева
    """
    if not root:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return max(left_depth, right_depth) + 1

# Тестирование
if __name__ == "__main__":
    # Пример дерева глубины 3
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    print("Глубина:", maxDepth(root))  # 3
