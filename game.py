from random import randint
import random
from time import sleep

def main():
    playerHp = 100
    enemyHp = 100
    playerPoints = 0
    playerAttackPower = 10
    turn = 0
    enemyNames=["Abra", "Aggron","Arbok","Bellsprout","Bulbasaur","Caterpie", "Charizard", "Charmeleon", "Clefairy",
                "Cubone", "Dratini", "Diglett", "Ekans", "Gastly", "Geodude", "Igglypuff", "Jigglypuff", "Koffing",
                 "Machamp", "Mankey", "Nidoran", "Pidgey", "Pikachu", "Psyduck", "Snorlax" ] #25 tane
    enemyName = random.choice(enemyNames)
    game(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
    

def playerAttack(playerHp, enemyHp, playerPoints, turn, playerAttackPower, enemyName, enemyNames):
    print("Player attacked!")
    attackChance = randint(1, 10)
    sleep(1)
    if attackChance >= 9:
        print("Critical hit!")
        playerAttackPower = playerAttackPower * 2
        enemyHp = enemyHp - playerAttackPower
        if enemyHp > 0:
                sleep(1)
                enemyAttack(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
        game(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
    elif attackChance >= 6 and attackChance < 9:
        print("Hit!")
        enemyHp = enemyHp - playerAttackPower
        if enemyHp > 0:
                sleep(1)
                enemyAttack(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
        game(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
    else:
        print("Miss!")
        if enemyHp > 0:
                sleep(1)
                enemyAttack(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
        game(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
    print("Remaining Enemy HP: ", enemyHp)

def enemyAttack(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames):
    print("Enemy HP: ", enemyHp)
    print(f"{enemyName}'s turn!")
    sleep(1)
    enemyAttackPower = randint(5, 20)
    print(f"{enemyName} attacked you!")
    attackChance = randint(1, 10)
    if attackChance >= 9:
        print("Critical hit!")
        enemyAttackPower = enemyAttackPower * 2
        playerHp = playerHp - enemyAttackPower
        game(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
    elif attackChance >= 6:
        print("Hit!")
        playerHp = playerHp - enemyAttackPower
        game(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
    else:
        print("Miss!")
        game(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
    print("Remaining Player HP: ", playerHp)

def defend(playerHp, playerAttackPower, turn, enemyHp, playerPoints, enemyName, enemyNames):
    print("Player defended!")
    defenceChance = randint(1, 10)
    if defenceChance >= 9:
        print("Attack blocked!")
        game(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
    else:
        print("Attack not blocked!")
        enemyAttack(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)


def heal(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames):
    print("Player healed!")
    healAmount = randint(5, 10)
    print("Healed for ", healAmount)
    playerHp = playerHp + healAmount
    print("Remaining Player HP: ", playerHp)
    enemyAttack(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)


def run(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames):
    runChance = randint(1, 10)
    if runChance >= 7:
        print("Player run away!")
        exit()
    else:
        print("Player couldn't run away!")
        enemyAttack(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)

def addPoint(playerHp, playerPoints):
    playerPoints = playerPoints + playerHp
    print("Player points: ", playerPoints)
    return playerPoints

def game(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames):
    turn += 1
    
    if playerHp > 0 and enemyHp > 0:
        print("Player HP: ", playerHp, "\nSelect what you want to do. \n1. Attack \n2. Defend \n3. Heal \n4. Run")
        
        playerChoice = int(input("Enter your choice: "))
        if playerChoice == 1:
            playerAttack(playerHp, enemyHp, playerPoints, turn, playerAttackPower, enemyName, enemyNames)
        elif playerChoice == 2:
            defend(playerHp, playerAttackPower, turn, enemyHp, playerPoints, enemyName, enemyNames)
            enemyAttack(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
        elif playerChoice == 3:
            heal(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
            enemyAttack(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
        elif playerChoice == 4:
            run(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
        else:
            print("Invalid choice")
            game(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
    elif playerHp <= 0:
        print("You lost at turn ", turn)
        exit()
    elif enemyHp <= 0:
        print(f"{enemyName} ran away!\n")
        print("You won")
        addPoint(playerHp, playerPoints)
        enemyHp = 100
        enemyName = random.choice(enemyNames)
        game(playerHp, enemyHp, playerPoints, playerAttackPower, turn, enemyName, enemyNames)
    else:
        print("An error occurred!")
        exit()

if __name__ == "__main__":
    main()