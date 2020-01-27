


class Node:
    # 자식노드 없는 노드 생성 (맨끝노드)
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # key 값을 삽입한다. (전위순회 순서대로)
    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            current = self.root
            while True:
                if current.key > key:
                    # 왼쪽트리에 삽입
                    if current.lchild == None:
                        current.lchild = Node(key)
                        break
                    # 왼쪽트리로 이동
                    else:
                        current = current.lchild

                elif current.key < key:
                    # 오른쪽트리에 삽입
                    if current.rchild == None:
                        current.rchild = Node(key)
                        break
                    # 오른쪽트리로 이동
                    else:
                        current = current.rchild

    #후위순회
    def postorder(self, node):
        s = []
        while True:
            while node:
                if node.rchild:
                    s.append(node.rchild)
                s.append(node)
                node = node.lchild
            node = s.pop()
            if node.rchild and (s[-1] if len(s) else None) == node.rchild:
                s.pop()
                s.append(node)
                node = node.rchild
            else:
                print(node.key)
                node = None
            if not s:
                break




bst = BinarySearchTree()
while True:
    try:
        key = int(input())
        bst.insert(key)
    except:
        break

bst.postorder(bst.root)
