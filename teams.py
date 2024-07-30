class Node:
    def __init__(self, da) -> None:
        self.data = da
        self.data1 = Linklist()
        self.child = []
class teamplayer:
    def __init__(self,name,country,sp) -> None:
        self.name=name
        self.country=country
        self.sp=sp
        self.next=None
class Linklist:
    def __init__(self) -> None:
        self.head=None
        self.sz=0
    def insert(self,name,country,sp):
        newnode=teamplayer(name,country,sp)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        self.sz+=1
    def display(self):
        if self.head is None:
            print("No Players")
        else:
            n=self.head
            while n:
                print(n.name,n.country,n.sp)
                n=n.next
class Teams:
    def __init__(self) -> None:
        self.root = None
        self.budget =200000
        self.foriegnplayers=0
        self.indianplayers=0
        self.sz=self.foriegnplayers+self.indianplayers
    def biddingcheck(self,bsp,nationality):
        a=self.budget
        if a-bsp>0:
            if self.sz<15 and nationality=='foreign'and self.foriegnplayers<4:
                return True
            elif self.sz>=15 and nationality=='foreign'and self.foriegnplayers>=4:
                print("exceeding foreingn player limit")
                return False
            elif self.sz<15 and nationality=='Indian':
                return True
            elif self.sz>=15 and nationality=='Indian':
                return False
        else:
            print("excedding budget")
            return False

    

RCB = Teams()
RCB.root = Node('RCB')
RCB.root.child.append(Node('bowlers'))
RCB.root.child.append(Node('batter'))
RCB.root.child.append(Node('allrounder'))
RCB.root.child.append(Node('wicketkeeper'))
CSK=Teams()
CSK.root=Node("CSK")
CSK.root.child.append(Node('bowlers'))
CSK.root.child.append(Node('batter'))
CSK.root.child.append(Node('allrounder'))
CSK.root.child.append(Node('wicketkeeper'))
SRH=Teams()
SRH.root=Node("SRH")
SRH.root.child.append(Node('bowlers'))
SRH.root.child.append(Node('batter'))
SRH.root.child.append(Node('allrounder'))
SRH.root.child.append(Node('wicketkeeper'))
MI=Teams()
MI.root=Node('MI')
MI.root.child.append(Node('bowlers'))
MI.root.child.append(Node('batter'))
MI.root.child.append(Node('allrounder'))
MI.root.child.append(Node('wicketkeeper'))
teams=[]
teams.append(RCB)
teams.append(CSK)
teams.append(SRH)
teams.append(MI)
