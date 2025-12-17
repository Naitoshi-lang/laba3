def deleteNode(root, key):
    """
    Удаление узла из BST
    """
    if not root:
        return None
    
    # Поиск узла для удаления
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Узел найден, начинаем удаление
        
        # Случай 1: Узел - лист
        if not root.left and not root.right:
            return None
        
        # Случай 2: Узел имеет одно поддерево
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # Случай 3: Узел имеет два поддерева
        # Находим минимальный элемент в правом поддереве
        successor = root.right
        while successor.left:
            successor = successor.left
        
        # Копируем значение преемника
        root.val = successor.val
        
        # Удаляем преемника
        root.right = deleteNode(root.right, successor.val)
    
    return root

def inorderTraversal(root):
    """Вспомогательная функция для демонстрации"""
    result = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    
    traverse(root)
    return result

# Тестирование
if __name__ == "__main__":
    # Пример BST
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    
    print("До удаления:", inorderTraversal(root))  # [2, 3, 4, 5, 6, 7]
    
    # Удаляем узел со значением 3
    root = deleteNode(root, 3)
    print("После удаления 3:", inorderTraversal(root))  # [2, 4, 5, 6, 7]
