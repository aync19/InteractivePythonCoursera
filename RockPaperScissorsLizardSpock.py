#rock paper scissors lizard Spock
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
#
#rock beats lizard and scissors and loses to Spock and paper
#Spock beats rock and scissors and loses to paper and lizard
#paper beats rock and Spock and loses to lizard and scissors
#lizard beats Spock and paper and loses to scissors and rock
#scissors beats paper and lizard and loses to rock and Spock

import random

def name_to_number(name):
    '''Converts name into corresponding number'''
    if(name=="rock"): return 0
    elif(name=="Spock"): return 1
    elif(name=="paper"): return 2
    elif(name=="lizard"): return 3
    elif(name=="scissors"): return 4
    else: return "invalid name"

def number_to_name(number):
    '''Converts number to corresponding name'''
    if(number==0): return "rock"
    elif(number==1): return "Spock"
    elif(number==2): return "paper"
    elif(number==3): return "lizard"
    elif(number==4): return "scissors"
    
def rpsls(player_choice): 
    print ""
    print "The player chooses " + player_choice
    player_number = name_to_number(player_choice)
    if(player_number=="invalid name"): 
        print "This is an invalid name"
        return
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "The computer chooses " + comp_choice
    winning_number = (player_number-comp_number)%5
    if(winning_number==1 or winning_number==2): 
        print "Player wins!"
    elif(winning_number== 3 or winning_number==4): 
        print "Computer wins!"
    else: print "Player and computer tie!"
    
#enter commands below

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
