class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


# node = Node(100)


class SingleCycleLinkList(object):
    """单向循环链表"""

    def __init__(self, node=None):
        # 私有变量__
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """ 链表是否为空 """
        return self.__head == None

    def length(self):
        """ 链表长度 """
        if self.is_empty():
            return 0
        # cur游标,用来移动遍历元素节点
        cur = self.__head
        # count记录数量
        count = 1
        while cur.next != self.__head:  # 条件要与count匹配
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """ 遍历整个链表 """
        if self.is_empty():
            return 0
        # cur游标,用来移动遍历元素节点
        cur = self.__head
        # count记录数量
        while cur.next != self.__head:  # 条件要与count匹配
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环时，没打印尾结点
        print(cur.elem)

    def add(self, item):
        """ 链表头部添加元素 头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:  # 条件要与count匹配
                cur = cur.next
            # 退出循环时，没打印尾结点
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self, item):
        """ 链表尾部添加元素 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:  # 条件要与count匹配
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """ 指定位置添加元素 
        :param pos 起始为0
        """
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            count = 0
            pre = self.__head
            while count < pos - 1:
                pre = pre.next
                count += 1
            # 当循环退出之后pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """ 删除节点 """
        if self.is_empty():
            return 
        cur = self.__head
        pre = None
        while cur.next != self.__head:  # 条件要与count匹配
            if cur.elem == item:
                # 先判断是否头结点 
                if cur == self.__head:
                    #头结点 
                    # 找尾结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间
                    pre.next = cur.next 
                return 
            else:
                pre = cur
                cur = cur.next
        #尾结点
        if cur.elem == item:
            # 判断是否只有一个结点
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next 


    def search(self, item):
        """ 查找节点 """
        if self.is_empty():
            return False 
        cur = self.__head
        while cur.next != self.__head:  # 条件要与count匹配
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环时，比较最后一个元素
        if cur.elem == item:
            return True
        return False 


if __name__ == "__main__":
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.add(8)
    ll.append(4)
    ll.append(5)
    ll.append(6)
# 8, 1, 2, 4, 5, 6
    ll.insert(-1, 9)
    ll.travel()
    ll.insert(2, 100)
    ll.travel()
    ll.insert(10, 200)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(8)
    ll.travel()
    ll.remove(200)
    ll.travel()
    ll.remove(9)
    ll.travel()
