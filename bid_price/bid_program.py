import bid_art

print(bid_art.art)

bid_list={}

def addBider(name,bidPrice):
    bid_list[name]=bidPrice

add_more=True
max=-1
while add_more==True:
    name=input("What is your name? ")
    bidPrice=int(input("What is your bid? $"))
    addBider(name,bidPrice)

    if(bidPrice>max):
        max=bidPrice

    runAgain=input("Do you want to add more person? Yes or no? ").lower()
    if runAgain=="yes":
        add_more=True
    else:
        add_more=False

for namePerson in bid_list:
    if bid_list[namePerson]==max:
        print(f"\n\n\nThe winner is {namePerson} with a bid of ${max}.")
        break