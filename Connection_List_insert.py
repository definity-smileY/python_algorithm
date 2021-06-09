# 연결 리스트의 삽입알고리즘
# 배열과는 달리 연결 리스트는 각각의 노드가 링크로 연결되어 있다. 따라서 연결리스트의 중간에 어떤 값을 노드를 연결시키는 것도 간단하다.

"""
예를 들어 A, B, D, E 총 4개의 노드가 있다고 가정해보자.
노드 B와 노드 D사이에 노드 C를 삽입하기 위해서는 새로 삽입되는 노드 C가 노드 D를 가리키도록하고,
노드 B가 노드 C를 가리키도록 해야 한다.
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_D
    node_D.next = node_E

def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next

    if pre_node.data == del_data:
        node_A = next_node
        del pre_node
        return
    
    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next

def insert_node(data): # 인수로 data를 받는다.
    global node_A # node_A를 global로 선언한다. 전역변수인 node_A는 이미 init_list()함수에서 생성된 연결리스트의 첫 번째 노드인 node_A 값을 갖고 있다.
    new_node = Node(data) # 인수로 받은 data를 저장할 new_node를 선언한다.
    # node_A와 node_B를 선언한다. 연결 리스트를 탐색하면서 새로운 노드를 삽입할 노드의 위치를 보관하기 위해 선언한 변수
    node_P = node_A
    node_T = node_A
    # node_T의 data와 인수로 받은 data와 인수로 받은 data를 비교하여, 그 결과가 작으면 node_T는 다음 링크의 노드를 가리키도록 한다.
    while node_T.data <= data:
        print("data :",data)
        node_P = node_T
        node_T = node_T.next # 바로 이 코드가 연결 리스트의 노드를 탐색하는 코드다.
    # node_T.data가 인수로 받은 data보다 크게 되면, 해당 위치가 인수로 받은 data를 사용하여 생성한 new_node가 삽입될 위치가 된다.
    new_node.next = node_T
    node_P.next = new_node

def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next

if __name__ == '__main__':
    print("연결 리스트 초기화 후")
    init_list()
    print_list()
    print("노드 C를 추가한 후")
    insert_node("C")
    print_list()
        

"""
연결리스트의 삽입 알고리즘의 분석

1. 시간의 효율성
    - 배열 혹은 연결리스트를 사용하던 데이터나 노드를 삽입하기 위해서는 삽입합 데이터의 위치 검색 과정과 실제 데이터를 삽입하는 과정이 필요한데,
    연결 리스트는 배열에 비해 시간의 효율성이 훨씬 높다. 전체 배열의 크기와 연결 리스트의 노드의 수가 많으면 많을수록 현격한 차이를 보여준다.

2. 공간의 효율성
    - 배열은 프로그램의 실행 중에 배열의 크기를 변경시키지 못하기에 공간의 효율성이 떨어진다.
    연결 리스트는 언제든지 필요할 때 동적으로 공간(메모리)를 할당하여 사용할 수 있으므로 배열에 비해 공간의 효율성이 뛰어나다.

3. 코드의 효율성
    - 연결 리스트보다 배열이 조금 더 낫다고 볼 수 도 있다. 배열의 경우 for문에서 사용하는 것처럼 배열의 인덱스만으로도 가능하기 때문에 코드를 작성할 때도 간단하고 코드를 이해하는데 쉽다.
    연결리스트의 코드는 포인터와 구조체로 되어 있기 때문에 이해하는데 어려움이 있다.
"""