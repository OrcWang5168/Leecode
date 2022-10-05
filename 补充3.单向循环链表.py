
from addtion import SingleLinkList
#这里变了一下公有属性为私有属性
class Node(object):
    def __init__(self,item):
        self.elem = item
        self.next = None


class Single_Cycle_LinkList(SingleLinkList):
    def __init__(self,node=None):
        super().__init__(node)
        if node:
            node.next = node

    def length(self):
        #cur游标，用来移动遍历节点
        cur = self.head
        #count记录数
        count = 1
        if cur==None:
            return 0
        else:
            while cur.next!= self.head:
                count+=1
                cur = cur.next
            return count

    def travel(self):
        cur = self.head
        if self.is_empty():
            return
        while cur.next != self.head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)  #退出前打印一下当前节点得elem





    def add(self,item):             #python只是贴标签，给的值变了，之前赋值的变量不会随之变化

            #方法一，先变头节点，然后找到尾节点做变换
            # node = Node(item)
            # if self.is_empty():
            #     node.next = self.head
            #     self.head = node
            #     node.next = node
            # else:
            #     node.next = self.head
            #     self.head = node
            #     cur = self.head.next
            #     while cur.next!=node.next:
            #         cur =cur.next
            #     cur.next = node

            #方法二，先找到尾节点，
            node = Node(item)
            if self.is_empty():
                self.head = node
                node.next = node
            else:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next

                node.next = self.head
                self.head = node
                cur.next = node




    def append(self,item):
        # cur = self.head
        # count = 0
        # node = Node(item)
        # if self.length()>0:
        #     while count<self.length()-1:
        #         cur = cur.next
        #         count+=1
        #
        #     cur.next = node
        #     node.prev = cur
        # else:
        #     self.add(node)
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head







    def insert(self,pos,item):

        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            pre = self.head
            count = 0
            while count < (pos - 1):
                pre = pre.next
                count += 1
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node


    def search(self,item):
        """某个元素是否存在"""
        # count = 0
        # cur = self.head
        # # while count<self.length():
        # if self.is_empty():
        #     return False
        # else:
        #     while cur.next!=self.head:
        #         if cur.elem == item:
        #             return True
        #         else:
        #             cur = cur.next
        #     if cur.elem == item:
        #         return True
        #     else:
        #         return False
        if self.is_empty():
            return False
        cur = self.head
        while cur.next!= self.head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False





    def remove(self,item):
        # cur = self.__head
        # count = 0
        # if self.search(item):
        #     while count<self.length():
        #         if cur.elem == item and count==0:
        #             self.__head = cur.next
        #             cur.next = None
        #             break
        #
        #         elif cur.next.elem == item:
        #             temp = cur.next.next
        #             cur.next.next = None
        #             cur.next = temp
        #             break
        #
        #         cur = cur.next
        # else:
        #     return -1
        if self.is_empty():
            return
        cur = self.head
        pre = None
        while cur.next != self.head:

            if cur.elem == item:
                # 先判断是不是头节点
                if cur == self.head:  # 改变头节点
                    rear = self.head
                    while rear.next!= self.head:
                        rear = rear.next
                    rear.next = self.head.next
                    self.head = self.head.next
                    return
                else:
                    pre.next = cur.next
                    cur.next = None
                    return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:          #循环链表再删除最后一个元素的时候要考虑是长的还是单个的因为pre可能是None
            if cur ==self.head:  #链表只有一个节点
                self.head =None #此时不用考虑cur链表按照头节点进行读取
                return

            else:
                pre.next = cur.next
                cur.next = None
                return


        else:
            return -1


if __name__ == '__main__':
    ll = Single_Cycle_LinkList()
    print(ll.is_empty())  # True

    print(ll.length())  # 0
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())  # 1
    ll.append(2)
    ll.add(8)

    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()  ##8 1 2 3 4 5 6
    print()

    ll.insert(-1, 9)  # 9 8 1 2 3 4 5 6
    ll.insert(3, 100)  # 9 8 1  100 2 3 4 5
    ll.insert(10, 200)  # 9 8 1 100 2 3 4 5 6 200

    ll.travel()
    print()
    print(ll.search(100))
    ll.remove(100)
    ll.travel()
    print()
    ll.remove(9)
    ll.travel()
    print()
    ll.remove(200)
    # ll.remove(201)
    ll.travel()
