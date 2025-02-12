import random
import os
import time
import sys 


class yourPlayer:
    def __init__(self, username, mycards, handval, balance, currentbet):
        self.username = " "
        self.mycards = []
        self.handval = int 
        self.balance = int
        self.currentbet = int

class theDealer:
    def __init__(self, dealername, dealercards, dealerhandval):
        self.dealername = dealername
        self.dealercards = []
        self.dealerhandval = int 

class card:
    def __init__(self):
        self.value = random.choice(cardvalues)
        self.suit = random.choice(cardsuits)
        if self.value in ['Jack', 'Queen', 'King']:
            self.numeric_value = 10
        elif self.value == 'Ace':
            self.numeric_value = 11
        else:
            self.numeric_value = int(self.value)
    
    def __str__(self):
        return f"{self.value} of {self.suit}"
    


cardvalues = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
cardsuits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

def clear_terminal():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def showWelcomeMessg():
    print("loading...")
    time.sleep(3)
    clear_terminal()
    print("( ͝סּ ͜ʖ͡סּ): Hello There! Welcome to Taylor's Blackjack 21!")
    time.sleep(1)
    print(f"( ͝סּ ͜ʖ͡סּ): My name is {theDealer.dealername}, your dealer! I hope you're excited to get started!")
    yourPlayer.username = input("( ͝סּ ͜ʖ͡סּ): What's your name? ")
    time.sleep(1)
    print("( ͝סּ ͜ʖ͡סּ): Thanks!")
    time.sleep(1)
    clear_terminal()
    instructionsqfunc()
  
def instructionsqfunc():
    instructionsq = input(f"( ͝סּ ͜ʖ͡סּ): Okay, {yourPlayer.username}, Would you like a quick overview of the instructions on how to play the game before we jump in? [y/n]: ")
    if instructionsq.lower() == "y":
        loadinstructions()
    if instructionsq.lower() == "n":
        startgame()
    else:
        print("( ͝סּ ͜ʖ͡סּ): Sorry, didn't get that. Try Again!")
        time.sleep(2)
        clear_terminal()
        instructionsqfunc()



def loadinstructions():
    print("( ͝סּ ͜ʖ͡סּ): Okay, pay close attention!")
    time.sleep(1)
    clear_terminal()
    for instruction in all_instructions:
        for key, value in instruction.items():  
            print(value)  
            ifcontinue = input("Press y to continue.. ")
            if ifcontinue.lower() == "y": 
                time.sleep(1)
                clear_terminal()
    print("( ͝סּ ͜ʖ͡סּ): Okay! You're ready to start!")
    time.sleep(1)
    clear_terminal()
    print("loading game...")
    time.sleep(3)
    clear_terminal()
    startgame()
             
 

all_instructions = [
    {"instruobjective": "( ͝סּ ͜ʖ͡סּ): OBJECTIVE: Your goal is to draw cards that total 21, or come closer to 21 than the dealer without going over."},
    {"instrustep1": "( ͝סּ ͜ʖ͡סּ): The dealer and each player start with two cards. The dealer's first card faces up, the second faces down. Face cards each count as 10, Aces count as 11, all others count at face value. An Ace with any 10, Jack, Queen, or King is a 'Blackjack.'"},
    {"instrustep2": "( ͝סּ ͜ʖ͡סּ): If you have a Blackjack, the dealer pays you one-and-a-half times your bet — unless the dealer also has a Blackjack, in which case it's a 'push' and neither wins."},
    {"instrustep3": "( ͝סּ ͜ʖ͡סּ): If you don't have Blackjack, you can ask the dealer to 'hit' when prompted."},
    {"instrustep4": "( ͝סּ ͜ʖ͡סּ): You may draw as many cards as you like (one at a time), but if you go over 21, you 'bust' and lose. If you do not want to 'hit,' you may 'stand' when prompted."},
    {"instrustep5": "( ͝סּ ͜ʖ͡סּ): After all players are satisfied with their hands, the dealer will turn his or her down card face up and stand or draw as necessary."}
]


possibnames = [
    "Azura", "Quillon", "Orion", "Lyra", "Zephyr", 
    "Cassian", "Seraphina", "Juno", "Caspian", "Elowen", 
    "Thaddeus", "Ophelia", "Balthazar", "Nyx", "Lucian", 
    "Persephone", "Ambrose", "Althea", "Calyx", "Sable", "Vesper"
]

def startgame():
    print(f"{yourPlayer.username}, your current balance is ${yourPlayer.balance}")
    currentbetnum = int(input("Place Your Bet: $"))
    if -1 < currentbetnum <= yourPlayer.balance:
        yourPlayer.currentbet = currentbetnum
        print(f"You've placed a bet of ${yourPlayer.currentbet}")
        yourPlayer.balance -= yourPlayer.currentbet
        time.sleep(2)
        clear_terminal()
        dealing()
    else:
        print("( ͝סּ ͜ʖ͡סּ): Please bet again within your means and above $0.")
        time.sleep(2)
        clear_terminal()
        startgame()



def dealing():
    print("dealing...")
    time.sleep(3)
    clear_terminal()
    mycard1 = card()
    mycard2 = card()
    dealercardshown = card()
    dealercardhidden = card()
    theDealer.dealercards = [dealercardshown, dealercardhidden]
    yourPlayer.mycards = [mycard1, mycard2]
    print(f"You've received {mycard1} and {mycard2}")
    print(f"Your total hand value is: {sum(card.numeric_value for card in yourPlayer.mycards)}")
    print(f"The dealers faceup card shows a {dealercardshown}")
    checkblackjack()
    handoptions()
   
def checkblackjack():
    if sum(card.numeric_value for card in yourPlayer.mycards) == 21 and sum(card.numeric_value for card in theDealer.dealercards) == 21:
        print(f"Aw man! You had Blackjack but so did {theDealer.dealername}. It's a push, no one wins.")
        time.sleep(1)
        clear_terminal()
        playagainq()
    elif sum(card.numeric_value for card in yourPlayer.mycards) == 21 and sum(card.numeric_value for card in theDealer.dealercards) < 21:
        print("BLACKJACK!")
        yourPlayer.balance += yourPlayer.currentbet * 1.5
        print(f"( ͝סּ ͜ʖ͡סּ): Congratulations! ${yourPlayer.currentbet * 1.5} has been added to your account.")
        time.sleep(4)
        clear_terminal()
        playagainq()
    else:
        pass

def checkbust():
    if sum(card.numeric_value for card in yourPlayer.mycards) > 21:
        print(f"Aw man! You went over 21")
        time.sleep(2)
        print(f"The dealer now overturns their down card, they held a {theDealer.dealercards[0]} and a {theDealer.dealercards[1]}")
        time.sleep(3)
        print(f"( ͝סּ ͜ʖ͡סּ): BUST! Game over.")
        time.sleep(3)
        clear_terminal()
        playagainq()
    else:
        pass

def checkdealerbust():
    if sum(card.numeric_value for card in theDealer.dealercards) > 21:
        print(f"Dealer went over 21!")
        print(f"( ͝סּ ͜ʖ͡סּ): BUST! You Win!")
        time.sleep(1)
        yourPlayer.balance += yourPlayer.currentbet * 2
        print(f"( ͝סּ ͜ʖ͡סּ): Congratulations! ${yourPlayer.currentbet * 2} has been added to your account.")
        time.sleep(3)
        clear_terminal()
        playagainq()
    else:
        pass


def playagainq():
    yourPlayer.currentbet = 0 
    pagq = input("Play again? [y/n]: ")
    if pagq.lower() == "y":
        startgame()
    elif pagq.lower() == "n":
        print("( ͝סּ ͜ʖ͡סּ): Good game! We wope to see you again. Please visit Taylor's Blackjack 21 any time!")
        time.sleep(3)
        clear_terminal()
    else:
        print("Sorry, didn't quite catch that. Please try again.")
        time.sleep(2)
        playagainq()


def handoptions():
    print("Hit - Stand")
    turnchoice = input("Choice: ")
    if turnchoice.lower() == "hit":
        hit()
    elif turnchoice.lower() == "stand":
        stand()
    else:
        print("Sorry, didn't quite catch that. Please try again.")
        time.sleep(2)
        handoptions()

def dealerhit():
    print("Dealer hits and draws a card.")
    new_card = card()
    theDealer.dealercards.append(new_card)
    time.sleep(1)
    print(f"Dealer draws {theDealer.dealercards[-1]} which is valued at {theDealer.dealercards[-1].numeric_value}.")
    time.sleep(3)
    clear_terminal()
    dealerplay()


def dealerstand():
    print(f"Dealer stands with a hand value of {sum(card.numeric_value for card in theDealer.dealercards)}")
    time.sleep(2)
    if (sum(card.numeric_value for card in theDealer.dealercards)) > (sum(card.numeric_value for card in yourPlayer.mycards)):
        print("( ͝סּ ͜ʖ͡סּ): Looks like I beat you! Better luck next time.")
        time.sleep(2)
        playagainq()
    elif (sum(card.numeric_value for card in theDealer.dealercards)) == (sum(card.numeric_value for card in yourPlayer.mycards)):
         yourPlayer.balance += yourPlayer.currentbet
         print("( ͝סּ ͜ʖ͡סּ): Looks like we draw! Your bet money has been returned to your account.")
         time.sleep(2)
         clear_terminal()
         playagainq()
    elif (sum(card.numeric_value for card in theDealer.dealercards)) < (sum(card.numeric_value for card in yourPlayer.mycards)):
        yourPlayer.balance += yourPlayer.currentbet * 2
        print("( ͝סּ ͜ʖ͡סּ): Looks you won!")
        time.sleep(1)
        print(f"( ͝סּ ͜ʖ͡סּ): Congratulations! ${yourPlayer.currentbet * 2} has been added to your account.")
        clear_terminal()
        playagainq()




def dealerplay():
    if sum(card.numeric_value for card in theDealer.dealercards) < 17:
        dealerhit()
    elif sum(card.numeric_value for card in theDealer.dealercards) >= 17:  
        checkdealerbust()
        dealerstand()
    




def hit():
    print("You hit.")
    time.sleep(2)
    cardname = (f"mycard{len(yourPlayer.mycards) + 1}")
    globals()[cardname] = card()
    yourPlayer.mycards.append(globals()[cardname])
    print(f"You've recieved a {globals()[cardname]}")
    time.sleep(3)
    checkblackjack()
    print(f"Your total hand value is now at: {sum(card.numeric_value for card in yourPlayer.mycards)}")
    time.sleep(2)
    checkbust()
    handoptions()



def stand():
    dealercardhidden = theDealer.dealercards[1]
    print("You stand.")
    time.sleep(2)
    print(f"Your final hand is valued at {sum(card.numeric_value for card in yourPlayer.mycards)}")
    time.sleep(1)
    print(f"The dealer overturns their down card to reveal a {dealercardhidden}")
    time.sleep(1)
    print(f"The dealer's current hand contains {theDealer.dealercards[0]} and {theDealer.dealercards[1]} which is valued at {sum(card.numeric_value for card in theDealer.dealercards)}")
    time.sleep(2)
    if (sum(card.numeric_value for card in theDealer.dealercards)) > (sum(card.numeric_value for card in yourPlayer.mycards)):
        print("( ͝סּ ͜ʖ͡סּ): Looks like I beat you! Better luck next time.")
        time.sleep(2)
        playagainq()
    else: 
        print("( ͝סּ ͜ʖ͡סּ): Now, its my turn to play!")
        time.sleep(1)
        dealerplay()






def main():

    theDealer.dealername = random.choice(possibnames)
    yourPlayer.balance = random.randint(10, 10000)
    showWelcomeMessg()


main()


