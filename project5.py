import os

def find_winner(bidder_details):  # nayan:10000 , ram:30000 , shyam:50000
    highest_bid=0
    winner=""
    for bidder in bidder_details:   #nayan
        bidding_price=bidder_details[bidder]    #10000
        if bidding_price>highest_bid:
            highest_bid=bidding_price   
            winner=bidder
    print(f"the winner is {winner} and his bid price is {highest_bid} ")        


bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("what is your name ?:")
    price=int(input("what is your bid price ?:"))    
    bidder_data[name]=price
    more_bidders=input("Are there more bidders ? Type 'yes' or 'no': ").lower()
    if more_bidders=="no":
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=="yes":
        os.system('cls')