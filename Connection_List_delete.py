class Node:
    def __init__(self, data, next = None):
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
    global node_A # node_A로 선언한 연결 리스트를 사용한다.
    pre_node = node_A # 연결 리스트를 가리키는 노드로 pre_node를 선언하고
    next_node = pre_node.next # pre_node의 다음 노드에 해당하는 pre_node.next를 next_node로 선언한다.

    if pre_node.data == del_data: # 현재 연결 리스트의 첫 번째 노드인 pre_node.data가 삭제할 del_data와 같다면 삭제할 노드가 가장 첫번째 노드이므로
        node_A = next_node # node_A에 next_node를 저장하고
        del pre_node # 현재 노드인 pre_node를 삭제한 후에 
        return # 해당 함수를 리턴한다.
    
    # 첫 번쨰 노드가 아닌 두 번째 이상의 노드를 삭제하는 경우는 어떻게 할까?
    # 그 떄는 삭제할 노드를 찾아야 한다.
    while next_node: # 현재 연결 리스트를 가리키는 next_node가 존재하는 동안 위의 while 문은 반복된다.
        if next_node.data == del_data: # next_node의 data가 인수로 받은 삭제할 데이터인 del_node와 같다면 
            pre_node.next = next_node.next # next_node의 다음 노드를 가리키는 링크를 이전 노드인 pre_node의 next에 저장하고
            del next_node # next_node를 삭제한 후에 리턴한다.
            break
        # 그러나 현재 노드를 가리키는 next_node.data가 인수로 받은 del_data와 같지 않다면, 
        pre_node = next_node # 이전 노드인 pre_node는 현재 노드인 next_node를 가리키도록 하고,
        next_node = next_node.next # next_node는 다음 노드에 해당하는 nexsdt_node.next를 가리키도록 한다.
        # 이 과정을 next_node에 노드가 존재하는 동안 반복한다. 

def insert_node(data):
    global node_A
    new_node = Node(data)
    node_P = node_A
    node_T = node_A
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next
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
    print("노드 D를 삭제한 후")
    delete_node("D")
    print_list()


"""
연결 리스트의 삭제 알고리즘의 분석

1. 시간의 효율성
    - 삽입 알고리즘과 마찬가지로 삭제 알고리즘도 삭제할 노드를 검색하는 과정과 찾은 노드를 삭제하는 과정이 필요하다.
    노드를 삭제하는 경우에 배열은 삭제한 데이터 이후의 데이터들을 앞으로 한 칸씩 이동해야하는 반면에
    연결리스트는 링크를 끊어주고 삭제할 노드만 해제해주면 된다. 따라서 시간적인 효율성은 배열보다 훨씬 좋다.

2. 공간의 효율성
    - 메모리를 할당하고, 또 삭제한 메모리를 해제 하기 때문에 공간적인 효율성이 높다.

3. 코드의 효율성
    - 삽입 알고리즘과 마찬가지로 배열의 경우 인덱스로 처리하기 때문에 더 쉬울 수 있다.
"""
