class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
    def __repr__(self) -> str:
        return f"value: {self.value}"
