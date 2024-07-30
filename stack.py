class StackNode:
    def __init__(self,team,price) -> None:
        self.team=team
        self.price=price
        self.next=None
class Stack:
    def __init__(self) -> None:
        self.top=None
    def push(self,team,price):
        newnode=StackNode(team,price)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
    def deletestack(self):
        self.top=None
priceStack=Stack()