# Day 9 - Jun 18 '24
# Secret Auction Program

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
otherBidders = True
biddersList=[]
highBid=0

def addBids(name,bid):
    newBid = {}
    newBid['name']=name
    newBid['bid']=bid
    biddersList.append(newBid)
    
while otherBidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    
    addBids(name,bid)
    
    biddersInfo = input("Are there any other bidders? Type 'yes or 'no'.\n")
    
    if biddersInfo == 'yes':
        otherBidders = True
    else:
        otherBidders = False

for bid in biddersList:
    if  bid['bid']>highBid:
        highBid=bid['bid']
        bidName=bid['name']

print(f"The winner is {bidName} with a bid of ${highBid}.")