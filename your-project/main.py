import random
import re


# Ask for the number of defending soldiers. It has to be an integer bigger than 0. 
# To get a short game, it is limited to 10.

def_soldiers = int(input("How many soldiers are DEFENDING your territory?"))
while def_soldiers < 1 or def_soldiers > 10:
    print("The number of soldiers must be between 1 and 10")
    def_soldiers = int(input("How many soldiers are DEFENDING your territory?"))

    # Ask for the number of attacking soldiers. It has to be an integer bigger than 0. 
# To get a short game, it is limited to 10.

att_soldiers = int(input("How many soldiers are ATTACKING the new territory?"))
while att_soldiers < 1 or att_soldiers > 10:
    print("The number of soldiers must be between 1 and 10")
    att_soldiers = int(input("How many soldiers are ATTACKING the new territory?"))

# Here is where the round starts. 
# There are some rules to take into account: 
    # The number of defending dices can be 1 or 2.
    # The number of attacking dices can be 1, 2 or 3.

two_dices = [1, 2]
three_dices = [1, 2, 3]

# It will be a loop until there is a winner.

while def_soldiers > 0 and att_soldiers > 0:
    print('\n')
    print(f'For the next round, there are {def_soldiers} DEFENSIVE soldiers and {att_soldiers} ATTACKING soldiers')
        
    # at the beggining of the loop, the dice are set to 0, then the players will choose, if they can.
    def_dices = 0
    att_dices = 0

    # check the number of remaining defending soldiers to decide the number of dices.
    if def_soldiers == 1:
        def_dices = 1
    else:
        def_dices = int(input("How many DICES do you want to use to DEFEND your territory?"))
        while def_dices not in two_dices:
            print("The number of defending dices is limited to 2")
            def_dices = int(input("How many DICES do you want to use to DEFEND your territory?"))
            
    # check the number of remaining attacking soldiers to decide the number of dices.
    if att_soldiers == 1:
        att_dices = 1
    elif att_soldiers == 2:
        att_dices = int(input("How many DICES do you want to use to ATTACK the new territory?"))
        while att_dices not in two_dices:
            print("The number of attacking dices is limited to 2")
            att_dices = int(input("How many DICES do you want to use to ATTACK the new territory?"))
    else:
        att_dices = int(input("How many DICES do you want to use to ATTACK the new territory?"))
        while att_dices not in three_dices:
            print("The number of attacking dices is limited to 3")
            att_dices = int(input("How many DICES do you want to use to ATTACK the new territory?"))
    
    # generating random dice rolls
    def_rolls = []
    while len(def_rolls) < def_dices:
        def_rolls.append(random.randint(1,6))
    print('\n')
    print('The rolls for defending dices in this round are: ', def_rolls)
    
    att_rolls = []
    while len(att_rolls) < att_dices:
        att_rolls.append(random.randint(1,6))
    print('\n')
    print('The rolls for attacking dices in this round are: ', att_rolls)
    
    # checking the results and updating the number of alive soldiers. 
    # each round, I will check the loses for each team, so we need to initate:
    def_loses = 0
    att_loses = 0
    
    # first roll
    if max(att_rolls) > max(def_rolls):
        def_loses += 1 
    else:
        att_loses += 1
        
    # second roll, if necessary
    while len(def_rolls) > 1 and len(att_rolls) > 1:
        try:
            att_rolls.remove(max(att_rolls))
        except ValueError:
            pass
        try:
            def_rolls.remove(max(def_rolls))
        except ValueError:
            pass
        if max(att_rolls) > max(def_rolls):
            def_loses += 1
        else:
            att_loses += 1
    
    def_soldiers = def_soldiers - def_loses
    att_soldiers = att_soldiers - att_loses
    
    if def_loses > 0:
        print('\n')
        print(f'Defenders loose {def_loses} soldiers.')
    
    if att_loses > 0:
        print('\n')
        print(f'Attackers loose {att_loses} soldiers.')
    print('\n')
    print('Round is finished.')
    
if def_soldiers == 0:
    print('\n')
    print('GAME OVER. Attacking soldiers WIN!')
elif att_soldiers == 0:
    print('\n')
    print('GAME OVER. Defending soldiers WIN!')
