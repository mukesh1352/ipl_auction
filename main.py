from prettytable import PrettyTable
from replit import clear
from art import logo
from players import nl
from teams import teams
from stack import priceStack


#nl.head.data.name='kaushik'
n1=nl.head
#print(nl.head.data.name)
#print(nl.head.next.data.name)
d={'Bowler':0,'Batsman':1,'All-Rounde1r':2,'Wicketkeeper':3}

# nl.print_by_name('eswar')
def findteam(t):
    for i in range(len(teams)):
        if t==teams[i].root.data:
            return teams[i]
    return" Team Not Found"
def getplayer():
    global n1 
    if n1 is nl.head:
        player = n1
        n1=n1.next
        return player
    elif n1 is not None:
        player = n1
        n1=n1.next
        return player
    elif n1 is None:
        return n1
    

def Home():
    while True:
            temp=input("Enter 'Home' For Home Page: ").upper()
            if temp == "HOME":
                clear()
                break
while True:

    print(logo)
    print("Welcome to IPL Auction 2024")
    print("1.Enter 1 view all players.")
    print("2.Enter 2 view a team's player list.")
    print("3.Enter 3 to start bidding.")
    print("4.Enter 4 view unsold players.")
    print("5.Enter 5 to exit the Auction.")
    ch=int(input("Enter Your Choice: "))
    if(ch==1):
        nl.print_all_details()
        Home()

    elif ch==2:
        print("Choose From Four Teams:\n1.RCB\n2.CSK\n3.SRH\n4.MI")
        t=input("Enter Team Name: ").upper()
        f=0

        for i in range(len(teams)):
            
            if t==teams[i].root.data:
                print("BUDGET REMAINING: ",teams[i].budget)
                print("BOWLERS")
                teams[i].root.child[0].data1.display()
                print("NO OF PLAYERS:",teams[i].root.child[0].data1.sz)
                print("BATTERS")
                teams[i].root.child[1].data1.display()
                print("NO OF PLAYERS:",teams[i].root.child[1].data1.sz)
                print("ALLROUNDERS")
                teams[i].root.child[2].data1.display()
                print("NO OF PLAYERS:",teams[i].root.child[2].data1.sz)
                print("WICKETKEPPER")
                teams[i].root.child[3].data1.display()
                print("NO OF PLAYERS:",teams[i].root.child[3].data1.sz)

                f=1
        if f==0:
            print("No Such Team..")
            
          
        Home()
        
    elif ch==3:
        player=getplayer()
        if player is not None:
            playername=player.data.name
            role=player.data.role
            bsp=player.data.baseprice
            nationality=player.data.nationality
            print(playername)
            print(player.data.role)
            print('Base Price: ',bsp)
            bch=input("Enter 'X' To Skip Player Or To Continue The Auction, Press Any Key: ").lower()
            if bch!='x':
                while True:
                    print("Four Teams:\n1.RCB\n2.CSK\n3.SRH\n4.MI")
                    t=input("Enter The Team Name To Bid: ").upper()
                    while findteam(t) is None:
                        print("Four Teams:\n1.RCB\n2.CSK\n3.SRH\n4.MI")
                        t=input("Enter The Team Name To Bid: ").upper()
                        findteam(t)
                    team=findteam(t)
                        
                    vaild=team.biddingcheck(bsp,nationality)
                    if(priceStack.top is None):
                        if vaild:
                            price=bsp
                            priceStack.push(team,bsp)
                            con=input("If No Other Team Wants To Bid Press 'N': ").lower()
                            if(con=='n'):
                                team.root.child[d[role]].data1.insert(player.data.name,nationality,priceStack.top.price)
                                player.data.soldprice=priceStack.top.price
                                team.budget-=priceStack.top.price
                                if nationality=='foreign':
                                    team.foriegnplayers+=1
                                else:
                                    team.indianplayers+=1
                                priceStack.deletestack()
                                break
                    else:
                        price=int(input("Enter Bid Amount: "))
                        if vaild and priceStack.top.price < price and priceStack.top.team!=team:
                            priceStack.push(team,price)
                            con=input("If No Other Team Wants To Bid Press 'N': ").lower()
                            if(con=='n'):
                                team.root.child[d[role]].data1.insert(playername,nationality,priceStack.top.price)
                                player.data.soldprice=priceStack.top.price
                                team.budget-=priceStack.top.price
                                if nationality=='foreign':
                                    team.foriegnplayers+=1
                                else:
                                    team.indianplayers+=1
                                priceStack.deletestack()
                                break
                        else:
                            print("Enter Vaild Price...")
                            

            else:
                player.data.soldprice=-1          
                        
                        
        else:
            print("REACHED TO END OF PLAYERS")

    


    elif ch==4:
        n2=nl.head
        if n2 == None:
            print("Players Are Either Unauctioned or Selected for a team.... ")
        else:
            print("The Unsold Players Are: ")
        while n2 is not None:
            if n2.data.soldprice ==-1:
                print(n2.data.name)
            n2=n2.next
        Home()


    elif ch==5:
        clear()
        print("Exited IPL Auction 2024.. ")
        break

        


        