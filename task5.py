def isValidBST(root):
    """
    Проверка, является ли дерево BST (Binary Search Tree)
    """
    
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        # Проверка текущего узла
        if min_val is not None and node.val <= min_val:
            return False
        if max_val is not None and node.val >= max_val:
            return False
        
        # Проверка левого и правого поддеревьев
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, None, None)

# Тестирование
if __name__ == "__main__":
    # Пример корректного BST
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    print("Является BST:", isValidBST(root))  # True
    
    # Пример некорректного BST
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    
    print("Является BST:", isValidBST(root2))  # False
