# Mafia intro in py file

input( "press enter to start:")
print ( "wire sounds ")
print (" flashing lights")
print ( " woow you are spining out of control" )
print ( " try to stop the spining")
input (" press your enter to stop")

print ( " it seems like you have entered a time machine " )
print ( " Welcome, or should I say good luck..." )
## player selection
input("press enter to continue:")
print(" my name is Fern. I am the all seeing eye... I will be the narrator of this story")
print ("I dont often see many new people around this town...Lets find out who you are")
choice = input ( "Press 1 for Murder or 2 for Detective enter:")
if choice == '1':
  print ("ooo scary a murder is in town")
elif choice == '2':
  print (" so theres a new sherif in town then...")
else:
  print("Pick again 1 or 2.")
  
## inventory 
if choice == '1':
 ##   print('murder inventory')
  choice = input("Pick your murder method: p for pillow, k for knife, g for gun: ")
  if choice == 'p':
    print("Night night it is...")
  elif choice == 'k':
    print("Didn't anyone ever tell you to be careful running around with knives?")
  elif choice == 'g':
    print("Ah, a classic one and done kind of deal.")
  else:
    print("Invalid choice. Please choose either p, k, or g.")
print(f"Night is falling, its your time to shine")

if choice == '1':
# murder pick who 
  townpeople_list = [ "Joe", "Eve", "Max", "Ari","Jack","Bob"]
  print(f"Our victum options are:" ,townpeople_list)
  victim_name = input ("Enter victim name here: ").strip().lower()



#import doc roll here
print(f" But who did the doctor save?")

#doctor here picks who to save
#Importing the classes from mafia_chara.py
from mafia_chara import Townperson, Doctor

# Create a list of townspeople (instances of the townperson class
townslist = [
    Townperson("Max", "Townsman", "Injured", 1),
    Townperson("Eve", "Townsman", "Alive", 2),
    Townperson("Bob", "Townsman", "Injured", 3),
    Townperson("Jack", "Townsman", "Alive", 4),
    Townperson("Ari", "Townsman", "Alive", 5)
]

# Create a doctor (instance of the Doctor class)
doctor = Doctor("Dr. Smith", "Doctor", "Alive")

# Simulate the doctor trying to heal someone
print("The doctor is trying to heal a townsperson...")
doctor.heal(townslist)

# Optionally, print the status of all townspeople after the doctor attempts to heal
print("\nCurrent statuses of all townspeople:")
for person in townslist:
    print(f"{person.name}: {person.status}")



if choice == '2':
  print (f"well dectetive it seems like you have your work cut out for ")
  print(f"Night is falling...")
  # roll for the murder call from file
# detective side of things

#auto pick
from Murder_rolls import roll_dice
name= roll_dice()
print(f"The murder has struck...{name} was attacked.")

#import doc roll here
print(f" But who did the doctor save?")
#doctor here picks who to save





 ## PRINT (DECTETIVE INVENTORY)
if choice == '2':
  choice = input (" pick your method of pursuit: s for picking a suspect, f to follow tracks, l look for clues, w wait out the perp: ").strip().lower()

  if choice.lower () == 's':
              print ("who is the most sus here")
  elif choice.lower() == 'f':
              print ("ooo follow those steps")
  elif choice.lower() == 'l':
              print ("take out your magnifying glass.")
  elif choice.lower() == 'w':
              print(" ok then keep waiting...")
  else:
         print("Invalid choice. Please choose from 's', 'f', 'l', or 'w'.")
#### charator list  method will pull from file 
  if choice ==  's':

    townpeople_list = [ "Joe", "Eve", "Max", "Ari","Jack","Bob"]
    print (f" suspect options are:{townpeople_list}")
    suspect_name = input("Who do you pick...:").strip().lower().capitalize()
    print(f"Our the supect is:",suspect_name)


  if (choice == 'f') or 'l':

    print(f"Is that...the murder weapon?")


##swap and pull status from the chara file
## the death of a charator and removal
## these are the town people 




## the end  up date stats 
##swap and pull status from the chara file
#if victim_name in [name.lower() for name in townpeople_list]:
 #   townpeople_list = [name for name in townpeople_list if name.lower() != victim_name]
  #  print("status updates... the living are:", townpeople_list)

#else:
 #   print(f"{victim_name} was not found.")
