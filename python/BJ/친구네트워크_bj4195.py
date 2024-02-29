import sys
input = sys.stdin.readline
test = int(input())

class Tree:
    def __init__(self):
        self.totalNum = 0
        self.names = set()

def solution():
    t = int(input())
    nameDic = {}
    trees = []
    for i in range(t):
        n1, n2 = map(str, input().split())

        # 아래와 같이 풀면, 이전에 누적된 놈 쫘르르 업데이트 할 수 없음
        if nameDic.get(n1) is None and nameDic.get(n2) is None:
            nameDic[n1] = 1
            nameDic[n2] = 1

            newTree = Tree()
            newTree.totalNum += 2
            newTree.names.add(n1)
            newTree.names.add(n2)
            trees.append(newTree)
            print(newTree.totalNum)

        elif nameDic.get(n1) is None and nameDic.get(n2) is not None:
            nameDic[n1] = 1
            nameDic[n2] = 1
            for tree in trees:
                if n2 in tree.names:
                    tree.names.add(n1)
                    tree.totalNum += 1
                    print(tree.totalNum)
                    break
        elif nameDic.get(n1) is not None and nameDic.get(n2) is None:
            nameDic[n1] = 1
            nameDic[n2] = 1
            for tree in trees:
                if n1 in tree.names:
                    tree.names.add(n2)
                    tree.totalNum += 1
                    print(tree.totalNum)
                    break
        elif nameDic.get(n1) is not None and nameDic.get(n2) is not None:
            first = None
            second = None
            for tree in trees:
                if n1 in tree.names:
                    first = tree
                if n2 in tree.names:
                    second = tree
                if first is not None and second is not None:
                    break

            if first == second:
                print(first.totalNum)
            else:
                newTree1 = Tree()
                newTree1.totalNum = first.totalNum + second.totalNum
                a = first.names.copy()
                b = second.names.copy()
                newTree1.names = a.union(b)
                trees.remove(first)
                trees.remove(second)
                print(newTree1.totalNum)
                trees.append(newTree1)

for i in range(test):
    solution()

"""

1
3
Fred Barney
Betty Wilma
Barney Betty

"""
