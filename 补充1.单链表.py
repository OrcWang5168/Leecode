class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    """单链表"""
    def __init__(self,node=None):    #链表的一个属性python指向的对象是什么都可以

        self.__head = node



    def is_empty(self):
        return (self.__head == None)

    def length(self):
        #cur游标，用来移动遍历节点
        cur = self.__head
        #count记录数量
        count = 0
        while cur != None:
            count+=1
            cur = cur.next
        return count


    def travel(self):
        cur = self.__head
        while cur!=None:
            print(cur.elem,end=" ")
            cur = cur.next

    def add(self,item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head       #等号右边是指向的对象
        self.__head= node
        pass

    def append(self,item):
        "链表尾部添加元素"
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
        # node = Node(item)
        # if self.is_empty():
        #     self.head = node
        #     return
        # current = self.head
        # print(current.next)
        # while current.next != None:
        #     current = current.next
        # current.next = node



    # def insert(self,pos,item):
    #     "指定位置添加元素"
    #     node =Node(item)
    #     count = 0
    #     cur = self.__head
    #     length = self.length()
    #     if pos==0:
    #         self.add(node)
    #     elif pos>length:
    #         return -1
    #     else:
    #
    #         while count!=pos-1:      #先改变新节点再改变原始节点
    #             cur = cur.next
    #             count+=1
    #         node.next = cur.next
    #         cur.next = node

    def insert(self,pos,item):

        if pos<=0:
            self.add(item)
        elif pos>=self.length():
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                pre = pre.next
                count+=1
            #当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node







        pass

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
        #         count+=1
        # else:
        #     return -1
        cur = self.__head
        pre = None
        while cur!=None:

             if cur.elem == item:
                 #先判断是不是头节点
                 if cur == self.__head:  #改变头节点
                     self.__head = cur.next
                     cur.next = None
                     break
                 else:
                     pre.next = cur.next
                     cur.next = None
                     break
             else:
                 pre = cur
                 cur = cur.next
        else:
            return -1






    def search(self,item):
        """某个元素是否存在"""
        count = 0
        cur = self.__head
        # while count<self.length():
        while cur!= None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
                # count+=1
        return False   #注意尾巴节点为None










node = Node(100)


if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())  #True

    print(ll.length())  #0

    ll.append(100)
    ll.travel()
    print(ll.is_empty())
    # print(ll.length())  #1
    # ll.append(100)
    # ll.travel()
    # ll.add(8)
    #
    # ll.append(3)
    # ll.append(4)
    # ll.append(5)
    # ll.append(6)
    # ll.travel()  ##8 1 2 3 4 5 6
    # print()
    #
    # ll.insert(-1,9) #9 8 1 2 3 4 5 6
    # ll.insert(3,100)  # 9 8 1  100 2 3 4 5
    # ll.insert(10,200) #9 8 1 100 2 3 4 5 6 200
    #
    # ll.travel()
    # print()
    # print(ll.search(100))
    # ll.remove(100)
    # ll.travel()
    # print()
    # ll.remove(9)
    # ll.travel()
    # print()
    # ll.remove(200)
    # ll.travel()
    #
