import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = '''
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

bids = {}

def register_bids(bidder_name,bidding_amount):
    bids[bidder_name] = int(bidding_amount)
    
continue_bidding = True

while continue_bidding:
    name = input("Enter your name\n")
    amount = input("Enter the amount\n")
    register_bids(name,amount)

    finish_bidding = input("Anymore bidders???")
    
    if finish_bidding == "yes":
        clear_console()
    elif finish_bidding == "no":
        continue_bidding = False


highest_bid = 0
corresponding_name = ""

for key in bids:
    if bids[key] > highest_bid :
        highest_bid = bids[key]
        corresponding_name = key  

print(f"The highest amount bid is {highest_bid} by {key}")
    

    
