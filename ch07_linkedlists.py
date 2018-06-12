# 7.1 MERGE TWO SORTED LISTS
class ListNode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def merge_sorted_lists(L1, L2):
    result = head = ListNode()
    while L1 and L2:
        if L1.data <= L2.data:
            result.next = L1
            result = result.next
            L1 = L1.next
        elif L2.data < L1.data:
            result.next = L2
            result = result.next
            L2 = L2.next
    if L1:
        result.next = L1
    if L2:
        result.next = L2
    head = head.next
    return head

def merge_two_sorted_lists_BOOK(L1, L2):
    # create a placeholder for the result
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # Append the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next

# 7.2 REVERSE A SINGLE SUBLIST
def reverse_sublist(L, s, f):
    # splice out subarray
    head, count = L, 1
    if not L or not L.next:
        return head
    sub_L = None
    while L.next:
        if count == s-1:
            sub_L = L.next
            sub_head = sub_L
            temp_node = L
        if count == f:
            temp_node.next = L.next 
            sub_L.next = None
            break
        count += 1
        L = L.next
        if sub_L:
            sub_L = sub_L.next

    L = head
    sub_L = sub_head
    # reverse sublist
    sub_tail = sub_L
    prev, curr = None, sub_L
    while current:
        next = current.next
        curr.next = prev
        prev = curr
        curr = next
    sub_head = prev

    # re-insert reversed subarray
    while L:
        if L == temp_node:
            sub_tail.next = L.next
            L.next = sub_head
            break
        L = L.next
    return head

def reverse_sublist_BOOK(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # reverse sublist
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp

    return dummy_head.next

# 7.3 TEST FOR CYCLICITY

def check_for_cycles(L):
    while L:
        L2 = L.next
        while L2: 
            if L2 == L:
                return L
            L2 = L2.next
        L = L.next
    return None

# 7.4 TEST FOR OVERLAPPING LISTS - LISTS ARE CYCLE-FREE 

# 7.5 TEST FOR OVERLAPPING LISTS - LISTS MAY HAVE CYCLES

# 7.6 DELETE A NODE FROM A SINGLY LINKED LIST
def delete_node(L, data):
    head = L
    while L and L.next and L.next.next:
        if L.next.data == data:
            L.next = L.next.next
            return head

def delete_node2(node):
    node.data = node.next.data
    node.next = node.next.next

# 7.7 REMOVE THE KTH LAST ELEMENT FROM A LIST
def remove_kth_from_end(L, k):
    count = k
    iter1 = iter2 = L
    while count > 0:
        iter1 = iter1.next
        count -= 1
    while iter1:
        iter1 = iter1.next
        iter2 = iter2.next
    delete_node2(iter2)

def remove_kth_last_BOOK(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next
    second = dummy_head
    while first:
        first, second = first.next, second.next
    # second points to (k+1)th last node, delete its successor
    second.next = second.next.next
    return dummy_head

# 7.8 REMOVE DUPLICATES FROM A SORTED LIST
def delete_duplicates(L):
    dummy_head = ListNode(0, L)
    while L.next:
        if L.next.data == L.data:
            L.next = L.next.next
        else:
            L = L.next
    return dummy_head.next

# 7.9 IMPLEMENT CYCLIC RIGHT SHIFT FOR SINGLY LINKED LIST
def rotate_right(L, k):
    def get_length(L):
        length = 1
        while L:
            L = L.next
            length += 1
        return length

    head = L
    k = k % get_length(L)
    iter1 = L
    for _ in range(k):
        iter1 = iter1.next

    iter2 = L
    while iter1.next:
        iter1 = iter1.next
        iter2 = iter2.next
    iter1.next = head
    head = iter2.next
    iter2.next = None
    return head

# 7.10 IMPLEMENT EVEN ODD MERGE
def even_odd_merge(L):
    dummy_head1 = ListNode(None, L)
    dummy_head2 = ListNode()
    L2 = dummy_head2
    count = 0
    while L.next:
        next_node = L.next
        if count % 2 == 0:
            L.next = L.next.next
            L = next_node
        else:
            L2.next = L
            L2 = L2.next
            L = next_node
        count += 1 
    L.next = dummy_head2.next
    return dummy_head1.next

def even_odd_merge_BOOK(L):
    if not L:
        return L
    dummy_head_even, dummy_head_odd = ListNode(0), ListNode(0)
    tails, turn = [dummy_head_even, dummy_head_odd], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1
    tails[1].next = None
    tails[0].next = dummy_head_odd.next
    return dummy_head_even.next

# 7.11 TEST WHETER A SINGLY LINKED LIST IS PALINDROMIC
def is_palindrome(L):
    iter1 = iter2 = L
    while iter2 and iter2.next:
        iter2 = iter2.next.next
        iter1 = iter1.next
    L1, L2 = L, reverse_linked_list(iter1)
    while L1 and L2:
        if L1.data != L2.data:
            return False
        L1 = L1.next
        L2 = L2.next
    return True

def is_linked_list_a_palindrome_BOOK(L):
    slow = fast = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    first_half_iter, second_half_iter = L, reverse_linked_list(slow)
    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = second_half_iter.next, first_half_iter.next
    return True

# 7.12 IMPLEMENT LIST PIVOTING
def pivot_linked_list(L, k):
    less = equal = greater = ListNode(0)
    tails = [less, equal, greater]
    while L:
        if L.data < k:
            tails[0].next = L
            tails[0] = tails[0].next
        elif L.data == k:
            tails[1].next = L
            tails[1] = tails[1].next
        else:
            tails[2].next = L
            tails[2] = tails[2].next
        L = L.next
    tails[2].next = None
    tails[1].next = greater.next
    tails[0].next = equal.next
    return less.next

def list_pivoting_BOOK(L, k):
    less_head = less_iter = ListNode()
    equal_head = equal_iter = ListNode()
    greater_head = greater_iter = ListNode()

    while L:
        if L.data < k:
            less_iter.next = L
            less_iter = less_iter.next
        elif L.data == k:
            equal_iter.next = L
            equal_iter = equal_iter.next
        else:
            greater_iter.next = L
            greater_iter = greater_iter.next
        L = L.next
    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next
    return less_head.next

# 7.13 ADD LIST BASED INTEGERS
def add_two_lists(L1, L2):
    result = dummy_head = ListNode()
    while L1 and L2:
        L1.data += L2.data
        result.next = L1
        result, L1, L2 = result.next, L1.next, L2.next
    if L1:
        result.next = L1
    if L2:
        result.next = L2

    result = dummy_head.next
    while result.next:
        if result.data > 9:
            result.data %= 10
            result.next.data += 1 
        result = result.next
    if result.data > 9:
        result.data %= 10
        result.next = ListNode(1)
    return dummy_head.next


def reverse_linked_list(L): 
    prev, curr = None, L
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def print_list_nodes(L):
    while L:
        print(L.data)
        L = L.next

def main():

    node1_3 = ListNode(4)
    node1_2 = ListNode(1, node1_3)
    node1_1 = ListNode(3, node1_2)

    node2_3 = ListNode(9)
    node2_2 = ListNode(0, node2_3)
    node2_1 = ListNode(7, node2_2)

    print_list_nodes(add_two_lists(node1_1, node2_1))




    # L1_4 = ListNode(12)
    # L1_3 = ListNode(7, L1_4)
    # L1_2 = ListNode(3, L1_3)
    # L1_1 = ListNode(2, L1_2)

    # L2_4 = ListNode(100)
    # L2_3 = ListNode(12, L2_4)
    # L2_2 = ListNode(11, L2_3)
    # L2_1 = ListNode(4, L2_2)

    # merged_list = merge_sorted_lists(L1_1, L2_1)

    # node8 = ListNode(8)
    # node7 = ListNode(7, node8)
    # node6 = ListNode(6, node7)
    # node5 = ListNode(5, node6)
    # node4 = ListNode(4, node5)
    # node3 = ListNode(3, node4)
    # node2 = ListNode(2, node3)
    # node1 = ListNode(1, node2)

    # lst = reverse_sublist_BOOK(node1, 3, 6)

    # while lst:
    #     print(lst.data)
    #     lst = lst.next

    # node7 = ListNode(11)
    # node6 = ListNode(5, node7)
    # node5 = ListNode(7, node6)
    # node4 = ListNode(11, node5)
    # node3 = ListNode(2, node4)
    # node2 = ListNode(2, node3)
    # node1 = ListNode(3, node2)
    
    # print_list_nodes(list_pivoting_BOOK(node1, 7))

    # print(is_linked_list_a_palindrome_BOOK(node1))

    # print_list_nodes(reverse_linked_list(node1))

    # print_list_nodes(rotate_right(node1, 13))

    # duplicates_removed = delete_duplicates(node1)
    # print_list_nodes(duplicates_removed)

    # print("before delete: ")
    # print_list_nodes(node1)
    
    # delete_node2(node4)

    # print("after delete: ")
    # print_list_nodes(node1)

    # remove_kth_from_end(node1, 3)
    # print_list_nodes(node1)    
 
main()