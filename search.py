class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def linear_search(self, target):
        temp = self.head
        index = 0
        while temp:
            if temp.data == target:
                return index
            temp = temp.next
            index += 1
        return -1

    def get_middle(self, start, end):
        slow = start
        fast = start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        return slow

    def binary_search(self, target):
        start = self.head
        end = None
        while start != end:
            mid = self.get_middle(start, end)
            if mid.data == target:
                return True
            elif mid.data < target:
                start = mid.next
            else:
                end = mid
        return False


def linear_search_array(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search_array(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print("1. Linear Search using Array")
print("2. Linear Search using Linked List")
print("3. Binary Search using Array")
print("4. Binary Search using Linked List")

choice = int(input("Choose an option: "))

if choice == 1:
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))
    result = linear_search_array(arr, target)
    if result != -1:
        print("Found at index", result)
    else:
        print("Not found")

elif choice == 2:
    ll = LinkedList()
    values = list(map(int, input("Enter linked list values: ").split()))
    for v in values:
        ll.insert(v)
    target = int(input("Enter target: "))
    result = ll.linear_search(target)
    if result != -1:
        print("Found at position", result)
    else:
        print("Not found")

elif choice == 3:
    arr = list(map(int, input("Enter sorted array elements: ").split()))
    target = int(input("Enter target: "))
    result = binary_search_array(arr, target)
    if result != -1:
        print("Found at index", result)
    else:
        print("Not found")

elif choice == 4:
    ll = LinkedList()
    values = list(map(int, input("Enter sorted linked list values: ").split()))
    for v in values:
        ll.insert(v)
    target = int(input("Enter target: "))
    result = ll.binary_search(target)
    if result:
        print("Found")
    else:
        print("Not found")

else:
    print("Invalid choice")