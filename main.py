"""
-------------------------------------------------------------------------------
Name:   malwaregame.py
Purpose:  a game that generates a scenario that will allow for the user to figure out what the malware is and choose a solution that would best work for the malware that happens
 
Author: Lue.Kyle
 
Created: 26/03/2021
------------------------------------------------------------------------------
"""
#Create title for the game
print ("******Malware Detection Game******")
print ("")
#Add description
print ("This bot will generate a scenario where a virus invades your computer. You wil have to determine the type of virus that has infected your computer and find out between two options on which one is better to help stop the virus.")
print ("")

#Generate adware scenario
adware = input("One day, your computer starts to send different targeted ads. What type of malware is it?: ")
if adware == "adware" or "Adware":
  print ("You are correct")
  adware_solution = input("Which one of these solutions could help with the getting rid of it? 1. Uninstall apps that might be causing it. 2. Install programs on your computer to try and help get rid of it. ")
  if adware_solution == '1':
    print ("Correct")
  while adware_solution == '2':
    print ("Incorrect. Try again")
    adware_solution = input("Which one of these solutions could help with the getting rid of it? 1. Uninstall apps that might be causing it. 2. Install programs on your computer to try and help get rid of it. ")
  while adware_solution != '1' and adware_solution != '2':
    print ("Invalid answer.")
    adware_solution = input("Which one of these solutions could help with the getting rid of it? 1. Uninstall apps that might be causing it. 2. Install programs on your computer to try and help get rid of it. ")
while adware != 'adware' and adware != 'Adware':
  print ("Incorrect. Try again")
  adware = input("One day, your computer starts to send different targeted ads. What type of malware is it?: ")

#Generate spyware scenario
print ("")
spyware = input("One day, your computer suddenly has some unknown software on it which seems to be sending data to an unknown location. What type of malware is this?: ")
if spyware == "spyware" or "Spyware":
  spyware_solution = input("Which solution would be better to get rid of it? 1. Visiting sketchy sites 2. Don't click on targeted ads")
  if spyware_solution == '2':
   print ("Correct")
  while spyware_solution == '1':
    print ("Incorrect")
    spyware_solution = input("Which solution would be better to get rid of it? 1. Visiting sketchy sites 2. Don't click on targeted ads")
  while spyware_solution != '1' and spyware_solution != '2':
    print ("Invalid answer")
    spyware_solution = input("Which solution would be better to get rid of it? 1. Visiting sketchy sites 2. Don't click on targeted ads. ")
while spyware != 'spyware' and spyware != 'Spyware':
  print ("Incorrect. Try again.")
  spyware = input("One day, your computer suddenly has some unknown software on it which seems to be sending data to an unknown location. What type of malware is this?: ")

#Generate virus scenario
print ("")
virus = input("One day, your computer has some random files on it that you don't have any recollection of installing. What malware is this?: ")
if virus == "virus" or "Virus":
  print ("You are correct")
  virus_solution = input("Which solution would be better to get rid of it? 1. Get an anti-virus 2. Open a suspicious email.")
  if virus_solution == 1:
    print ("Correct")
  while virus_solution == 2:
    print ("Incorrect. Please try again")
    virus_solution = input("Which solution would be better to get rid of it? 1. Get an anti-virus 2. Open a suspicious email.")
  while virus_solution != '1' and virus_solution != '2' :
     print ("Invalid answer")
     virus_solution = input("Which solution would be better to get rid of it? 1. Get an anti-virus 2. Open a suspicious email.")
while virus != 'virus' and virus != 'Virus':
  print ("Incorrect. Try again")
  virus = input("One day, your computer has some random files on it that you don't have any recollection of installing. What malware is this?: ")

#Generate worm scenario
print ("")
worm = input("One day, you seemed to have gotten a email with a peculiar attachment added to it.What malware is attached to the attachment?: ")
if worm == "worm" or "Worm":
  print ("You are correct")
  worm_solution = input("Which solution would be better to get rid of it? 1. Open more suspicious programs 2. Use a malware removal software. ")
  if worm_solution == '2':
   print ("Correct")
  while worm_solution == '1':
    print ("Incorrect. Please try again")
    worm_solution = input("Which solution would be better to get rid of it? 1. Open more suspicious programs 2. Use a malware removal software.")
  while worm_solution != "1" and worm_solution != "2" :
    print ("Invalid answer")
    worm_solution = input("Which solution would be better to get rid of it? 1. Open more suspicious programs 2. Use a malware removal software.")
while worm != "worm" and worm != "Worm" :
  print ("Incorrect. Try again")
  worm = input("One day, you seemed to have gotten a email with a peculiar attachment added to it.What malware is attached to the attachment?: ")

#Generate trojan scenario
print ("")
trojan = input("One day, you seemed to have downloaded a software that seems to not be what it is. What malware is it?: ")
if trojan == "trojan" or "Trojan":
  print ("You are correct")
  trojan_solution = input("Which solution would be better to get rid of it? 1. Use an antivirus 2. Do nothig about it and hope it goes away.")
  if trojan_solution == '1':
    print ("Correct")
  while trojan_solution == '2':
    print ("Incorrect. Try again")
    trojan_solution = input("Which solution would be better to get rid of it? 1. Use an antivirus 2. Do nothig about it and hope it goes away.")
  while trojan_solution != "1" and trojan_solution != "2" :
    print ("Invalid answer")
while trojan != "trojan" and trojan != "Trojan" :
  print ("Incorrect. Try again.")
  trojan = input("One day, you seemed to have downloaded a software that seems to not be what it shows up as. What malware is it?: ")

#Generate rootkit scenario
rootkit = input("One day, you find a piece of software that's hiding extremely well. What malware is it?: ")
if rootkit == "rootkit" or "Rootkit":
  print ("You are correct")
  rootkit_solution = input("Which solution would be better to get rid of it? 1. Try and figure out when it steal your data 2. Wipe your hard drive")
  if rootkit_solution == '2':
    print ("Correct")
  while rootkit_solution == '1':
    print ("Incorrect. Try again.")
  while rootkit_solution != "1" and rootkit_solution != "2" :
    print  ("Invalid answer")
    rootkit_solution = input("Which solution would be better to get rid of it? 1. Try and figure out when it steal your data 2. Wipe your hard drive")
while rootkit != "rootkit" and rootkit != "Rootkit" :  
  print ("Incorrect. Try again")
  rootkit = input("One day, you find a piece of software that's hiding extremely well. What malware is it?: ")

#Generate backdoors scenario
print ("")
backdoors = input("One day, you find some sort of entry into your desktop. What kind of malware is it?: ")
if backdoors == "backdoors"  or "Backdoors":
  print ("You are correct")
  backdoors_solution = input("Which solution would be better to get rid of it? 1. Use a firewall 2. Try and force the entryway closed")
  if backdoors_solution == '1':
    print ("Correct")
  while backdoors_solution == '2':
    print ("Incorrect. Try again.")
    backdoors_solution = input("Which solution would be better to get rid of it? 1. Use a firewall 2. Try and force the entryway closed")
  while backdoors_solution != "1" and backdoors_solution != "2" :
    print ("Invalid answer")
    backdoors_solution = input("Which solution would be better to get rid of it? 1. Use a firewall 2. Try and force the entryway closed")
while backdoors != "backdoors" and backdoors != "Backdoors" :
  print ("Invalid answer")
  backdoors = input("One day, you find some sort of entry into your desktop. What kind of malware is it?: ")

#Generate keyloggers scenario
print ("")
keyloggers = input("One day, you find a program that had been recording your keystrokes. What malware is it?: ")
if keyloggers == "keyloggers" or "keyloggers":
  print ("You are correct")
  keyloggers_solution = input("Which solution would be better to get rid of it? 1. Use new passwords for everything 2. Use two factor authentication")
  if keyloggers_solution == '2':
    print("Correct")
  while keyloggers_solution == '1':
    print ("Incorrect. Try again.")
    keyloggers = input("One day, you find a program that had been recording your keystrokes. What malware is it?: ")
  while keyloggers_solution != "1" and keyloggers_solution != "2" :
    print ("Invalid answer")
  keyloggers_solution = input("Which solution would be better to get rid of it? 1. Use new passwords for everything 2. Use two factor authentication")
while keyloggers != "keyloggers" and keyloggers != "Keyloggers":
    print ("Invalid answer")
    keyloggers = input("One day, you find a program that had been recording your keystrokes. What malware is it?: ")

#Generate rogue security scenario
print ("")
roguesecurity = input("One day, you download a sketchy security system and it asks for random permissions for things. What malware is it?: ")
if roguesecurity == "rogue security" or "Rogue security":
  print ("You are correct")
  roguesecurity_solution = input("Which solution would be better to get rid of it? 1. Read the review of the system before downloading 2. Find another security system to get rid of the first one")
  if roguesecurity_solution == '1':
    print ("Correct")
  while roguesecurity_solution == '2':
    print ("Incorrect answer. Try again.")
    roguesecurity_solution = input("Which solution would be better to get rid of it? 1. Read the review of the system before downloading 2. Find another security system to get rid of the first one")
  while roguesecurity_solution != "1" and roguesecurity_solution != "2":
    print ("Invalid answer")
    roguesecurity_solution = input("Which solution would be better to get rid of it? 1. Read the review of the system before downloading 2. Find another security system to get rid of the first one")
while roguesecurity != "rogue security" and roguesecurity != "Rogue Security" :
  print ("Invalid answer")
  roguesecurity = input("One day, you download a sketchy security system and it asks for random permissions for things. What malware is it?: ")

#Generate browser hijacker scenario
print ("") 
browserhijacker = input("One day, you keep getting sent to random website although you aren't clicking on them. What malware is it?: ")
if browserhijacker == "browser hijacker" or "Browser Hijacker":
  print ("You are correct")
  browserhijacker_solution = input("Which solution would be better to get rid of it? 1.Use another operating system 2. Install an antivirus to find the problem")
  if browserhijacker_solution == '2':
    print ("Correct")
  while browserhijacker_solution == '1':
    print ("Incorrect. Try again")
    browserhijacker_solution = input("Which solution would be better to get rid of it? 1.Use another operating system 2. Install an antivirus to find the problem")
  while browserhijacker_solution != "1" and browserhijacker_solution != "2":
   print ("Invalid answer.")
   browserhijacker_solution = input("Which solution would be better to get rid of it? 1.Use another operating system 2. Install an antivirus to find the problem")
while browserhijacker != "browser hijacker" and browserhijacker != "Browser Hijacker":
  print ("Invalid answer")
  browserhijacker = input("One day, you keep getting sent to random website although you aren't clicking on them. What malware is it?: ")

#Generate ransomware scenario
print ("")
ransomware = input("One day, you find some kind of ransom on your computer screen. What kind of malware is it?: ") 
if ransomware == "ransomware" or "Ransomware":
  print ("You are correct")
  ransomware_solution = input("Which solution would be better to get rid of it? 1. Do a full system restore 2. Pay the ransom")
  if ransomware_solution == '1':
    print ("Correct")
  while ransomware_solution == '2':
    print ("Incorrect.Try again")
    ransomware_solution = input("Which solution would be better to get rid of it? 1. Do a full system restore 2. Pay the ransom")
  while ransomware_solution != '1' and ransomware_solution != '2':
    print ("Invalid answer")
    ransomware_solution = input("Which solution would be better to get rid of it? 1. Do a full system restore 2. Pay the ransom")
while ransomware != "Randsomware" and ransomware != "Randsomware":
  print ("Invalid answer")
  ransomware = input("One day, you find some kind of ransom on your computer screen. What kind of malware is it?: ") 