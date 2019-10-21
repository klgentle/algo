class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


# node = Node(100)


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        # 私有变量__
        self.__head = node

    def is_empty(self):
        """ 链表是否为空 """
        return self.__head == None

    def length(self):
        """ 链表长度 """
        # cur游标,用来移动遍历元素节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:  # 条件要与count匹配
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """ 遍历整个链表 """
        # cur游标,用来移动遍历元素节点
        cur = self.__head
        # count记录数量
        while cur != None:  # 条件要与count匹配
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """ 链表头部添加元素 头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """ 链表尾部添加元素 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
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
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断是否头结点 
                if cur == self.__head:
                    self.__head = cur.next 
                else:
                    pre.next = cur.next 
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """ 查找节点 """
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False 

    def rev(self):
        """link reverse"""
        p = None
        while self.__head is not None:
            q = self.__head
            self.__head = q.next    # 摘下原来的首结点
            q.next = p
            p = q   # 将刚摘下的结点加入P引用的结点序列
        self.__head = p # 反转后的结点序列已经做好，重置表头链接


if __name__ == "__main__":
    ll = SingleLinkList()
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
    ll.rev()
    ll.travel()
