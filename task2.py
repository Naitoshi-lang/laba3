def postorderTraversal(root):
    """
    Postorder: Левый -> Правый -> Корень
    """
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)      # Левый
        traverse(node.right)     # Правый
        result.append(node.val)  # Корень
    
    traverse(root)
    return result

# Тестирование
if __name__ == "__main__":
    # Пример дерева: 1 -> 2 -> 3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    print("Postorder:", postorderTraversal(root))  # [3, 2, 1]
