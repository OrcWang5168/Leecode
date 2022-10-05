class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
class SingleLinkList(object):
    def __init__(self, node=None):
        self.head = node
    def is_empty(self):
        return self.head==None
    def length(self):
        "“”链表长度"""
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
    def travel(self):
        """遍历链表"""
        current = self.head
        while current != None:
            print(current.elem)
            current = current.next

    def add(self):
         """头部添加元素"""

    def append(self,item):
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.head = node
        # return
        else:

            current = self.head

            while current.next!= None:
                current = current.next
            current.next=node



    def insert(self,pos,item):
        """插入元素"""
        if pos<0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
             node=Node(item)
             count=1
             pre=self.head   #pre就是第一个元素
             while count<pos:
                  count+=1
                  pre=pre.next
             node.next=pre.next
             pre.next=node





    def remove(self):
        """移除元素"""

    def search(self):
        """搜索元素"""
if __name__ == "__main__":
    ll=SingleLinkList()
    print(ll.is_empty())
    ll.append(2)
    # print(ll.length())
    print(ll.is_empty())
    # ll.append(6)
    # ll.append(7)
    # ll.append(4)
    # ll.append(9)