class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    """
    Preorder: Корень -> Левый -> Правый
    """
    result = []
    
    def traverse(node):
        if not node:
            return
        result.append(node.val)  # Корень
        traverse(node.left)      # Левый
        traverse(node.right)     # Правый
    
    traverse(root)
    return result

# Тестирование
if __name__ == "__main__":
    # Пример дерева: 1 -> 2 -> 3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    print("Preorder:", preorderTraversal(root))  # [1, 2, 3]
