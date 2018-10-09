while True: 
 print ("                         Supernatural \n                             Pilot\n                             Act 1\n\n You are going to play as Sam Winchester, a colege student\n with a tragic past. When you were a baby, your mother was \nmurdered by being lit on fire through some supernatural force. \n It's the middle of the night. You are suddenly woken up by some rumbling in your apartment. \n __________________________________________________________\n Choose either yes or no. ")
 quest = input ("Do you get up and go investigate?")
 if quest == ("yes"):
   print ("\n __________________________________________________________\n You spot the figure of a man, but you can't make out their face. It's pitch black.")
   quest = input("Do you tackle him?")
   if quest == ("yes"):
       print("\n __________________________________________________________\nYou tackle him, but can't land a solid hit. After you exchange some blows, he manages to pin you to the ground and you find out it's Dean, your big brother. He tells you you're out of shape, but suddenly you end up being the one on top. You help him get up.")
   elif quest == ("no"):
     print("\n __________________________________________________________\nHe attacks you, but you fight back. After you exchange some blows, he manages to pin you to the ground and you find out it's Dean, your big brother. He tells you you're out of shape, but suddenly you end up being the one on top. You help him get up.")
   else:
     continue
   quest = input("Do you want to ask him what the hell's going on?")
   if quest == ("yes"):
     print("\n __________________________________________________________\nYou ask him what's going on. He tells you in these exact words, which have been heard dozens of times despite being said only once on the show, except recaps: Dad is on a hunting trip, and he hasnt been home in a few days.")
   elif quest == ("no"):
     print("\n __________________________________________________________\nYou ask him what's going on. He tells you in these exact words, which have been heard dozens of times despite being said only once on the show, except recaps: Dad is on a hunting trip, and he hasnt been home in a few days.")
   else:
     continue
   quest = input("Do you want to go and find your dad?")
   if quest == ("yes"):
     print("\n __________________________________________________________\n\n                          End of Act 1\n\n The following segment is a work in progress. Plese, excuse our support team for the inconvenience.")
     break
   elif quest == ("no"):
     print("\n __________________________________________________________\nYou tell Dean that you aren't going, because you believe your dad will be fine. You and Dean reminisce about your life up till now. You have a job interview in a bit more than 48 hours.")
     quest = input ("Do you help Dean on the condition that you come back on time?")
     if quest == ("yes "):
       print("\n __________________________________________________________\n\n                          End of Act 1\n\n The following segment is a work in progress. Plese, excuse our support team for the inconvenience.")
     elif quest == ("no"):
       print("\n __________________________________________________________\nYou aren't playing as Sam in that case. The logic of the world fall apart as you stare at the white text printed on the black background of the console.")
     else:
       continue
 elif quest == ("no"):
   print ("\n __________________________________________________________\nThen go home. Go on, what are you doing here, reading this? Just switch off the program.")
 else :
   continue
 break
