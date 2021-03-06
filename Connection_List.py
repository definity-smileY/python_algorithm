# 연결 리스트
"""
대부분의 알고리즘에서 사용하는 기본 자료구조
알고리즘에서 사용하는 데이터와 다음 노드를 가리키는 링크를 묶어서 노드로 정의하여 사용

연결 리스트에는 기본적으로 노드(Node)와 링크(Link)라는 용어를 사용
"""

# 연결 리스트를 사용하기 위해서는 노드를 다음과 같이 클래스로 정의하여 사용한다.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Node 클래스는 데이터를 저장하는 data와 링크를 저장하는 next를 멤버로 갖고 있다.
# 기본적인 개념은 파이썬의 배열과 동일하나 배열을 사용하지 않고 연결 리스트를 사용하는 이유는 연결 리스트의 장점은 곧 배열의 단점이 된다.
# 배열은 동일한 자료형을 갖는 데이터의 집합이다. 그 특성은 연속적이라는 것이다.
# 배열의 특징은 배열을 생성할 때 한번에 총 메모리를 확보하여 사용할 수 있도록 하기 때문에 프로그램이 실행되는 중간에 배열의 크기를 바꾸거나 할 수 없다.
# 배열의 단점은 배열 안에 저장되어 있는 값들을 정렬할 때도 일일이 메모리에 저장되어 있는 값을 바꾸어주어야 한다. 연결 리스트는 이와 같은 배열의 단점을 해결해준다.

# 연결 리스트는 반드시 연속적이라고는 볼 수 없고 오히려 연결 리스트는 연속적이지 않는 데이터들을 링크로 서로 연결하는 개념이라고 볼 수 있다.

# 2개 이상의 데이터를 노드에 저장하여 서로 연결하게 되는 연결리스트의 초기화
def init_list():
    # Node 객체를 생성하되, 처음에는 "A"라는 data 값을 갖는 객체를 생성하여 node_A에 저장하고 다음과 같이 동일하게 작업을 수행
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_C = Node("C")
    node_D = Node("D")
    node_A.next = node_B
    node_B.next = node_C
    node_C.next = node_D

def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next

if __name__ == '__main__':
    init_list()
    print_list()