Mone = 100
hp = 10
damage = 0
enemymone = 150
enemyhp = 10
enemydamage = 2
elvl = 1
enemy = 1
lvl = 0
defaehp = 10
defaedmg = 2
def training():
  global hp
  global Mone
  global damage
  global enemydamage
  global lvl 
  global enemyhp
  global enemy
  global elvl
  print("Your health:" + str(hp))
  print("Your money: " + str(Mone))
  print("Your attack damage: " + str(damage))
  print("")
  print("What do you want to do?")
  print("A) Workout (-$10 +1 attack damage + 0.5+ hp)")
  print("B) Go back to the menu")
  inpuput = input()
  if inpuput == "A" or inpuput == "a" and Mone < 10:
    print("You dont have enough money to workout.")
    training()
  if inpuput == "A" or inpuput == "a" and Mone > 0:
    Mone = Mone - 10
    damage = damage + 1
    hp = hp + 0.5
    training()

  if inpuput == "B" or inpuput == "b":
    menu()



def szutyok():

  global hp
  global Mone
  global damage
  global enemydamage
  global lvl 
  global enemyhp
  global enemy
  global elvl
  global enemymone
  global defaehp
  global defaedmg
  for blank in range(100):
    print("")
  print("Enemy's level: " + str(elvl))
  print ("Enemy's attack damage: " + str(enemydamage))
  print("Enemy's money: $" + str(enemymone))
  print("Enemy's health: " + str(enemyhp))
  print("")
  print("Your level: "+str(lvl) )
  print("Your health: " + str(hp))
  print("Your money: " + str(Mone))
  print("Your attack damage: " + str(damage))
  print("")
  print("What do you want to do?")
  print("A) Fight back")
  print("B) Give up")
  answer = input()
  if answer == "A" or "a":
      enemyhp = enemyhp - damage
      print("You dealt " +str(damage) + " hp to the enemy. Now the enemy has " + str(enemyhp) + " hp.")
      hp = hp - enemydamage
      print("The enemy turns.")
      print("The enemy dealt " +str(enemydamage) + " hp to you." )
      if hp <= 0 or answer == "b" or answer == "B":
        print('You died!')
        enemymone = enemymone - Mone /45
      
        Mone = Mone - Mone /50
        print("now the enemy has $" + str(enemymone) + ", and you have $" +str(Mone) + ".")
        hp = 5
        return menu()
      if enemyhp <= 0:
        Mone = Mone + enemymone
        lvl = lvl + 1
        elvl = elvl + 1
        enemymone = enemymone * 5
        enemydamage = enemydamage * 5
        
        enemyhp = defaehp * 5
        defaehp = defaehp * 5
        enemydamage = defaedmg * 5
        print("You won!")
        inpupuput = input("Press enter to continue!")
        menu()
      szutyok()

def menu():
  for sonkaisthebest in range(100):
    print("")
  global hp
  global Mone
  global damage
  global enemydamage
  global lvl 
  global enemyhp
  global enemy

  global enemymone

  print("Current health:" + str(hp))
  print("Current money: " + str(Mone))
  print("Current attack damage: " + str(damage))
  print("")
  print("A) Fight")
  print("B) Go to Workout")
#(Soon) print("C) Bet")
  ans = input()
  if ans == "a" or ans == "A":
    szutyok()
  if ans == "b" or ans == "B":
    training()


print("a game ™")
print("© theultimatesonka1999, 2022")
print("")

inp = input("press enter to start")
menu()