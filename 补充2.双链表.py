
from addtion import SingleLinkList
#这里变了一下公有属性为私有属性
class Node(object):
    def __init__(self,item):
        self.elem = item
        self.next = None
        self.prev = None

class DoubleLinkList(SingleLinkList):
    def __init__(self,node=None):
        super().__init__()




    def add(self,item):

            node = Node(item)
            node.next = self.head
            self.head = node
            if node.next:
                node.next.prev = node  #如果是空的则node.next是None没有prev

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
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur







    def insert(self,pos,item):

        if pos<=0:
            self.add(item)
        elif pos>=self.length():
            self.append(item)
        else:
            cur = self.head
            count = 0
            while count !=pos:
                cur = cur.next   #count对应着指针的索引
                count+=1
            #当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node


    def search(self,item):
        """某个元素是否存在"""
        count = 0
        cur = self.head
        # while count<self.length():
        while cur!= None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
                # count+=1
        return False   #注意尾巴节点为None




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
        cur = self.head

        while cur!=None:

             if cur.elem == item:
                 #先判断是不是头节点
                 if cur == self.head:  #改变头节点
                     self.head = cur.next
                     if cur.next:

                        cur.next.prev = None
                     cur.next = None
                     break
                 else:
                     cur.prev.next = cur.next
                     if cur.next:
                         cur.next.prev = cur.prev
                     cur.next = None
                     cur.prev = None

                     break
             else:

                 cur = cur.next
        else:
            return -1



if __name__ == '__main__':
    ll = DoubleLinkList()
    print(ll.is_empty())  # True

    print(ll.length())  # 0
    ll.add(52)
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
    ll.travel()




