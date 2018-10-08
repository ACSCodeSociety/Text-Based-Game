while True:  
  print ("                  The Tale about the Shapherd\n\n You are going to play as a shepherd from Zmeyovo in Rodopa planina. Your name is Stoyu. \n  One night you go out to pasture your held and sit next to a tree close to a illuminated by the moon plain... \n __________________________________________________________\n Choose either yes or no. ")
  quest = input ("Do you want to play on your wooden whistle?")
  if quest == ("Yes"):
    print ("\n __________________________________________________________\n You start playing, after some time you hear soft laughs and turn around... You see outlandishly gorgeous women,samodivas, dancing a horo.")
    quest = input ("Do you want to join them?")
    if quest == "Yes":
      print ("\n __________________________________________________________\n You joined the horo, but you will not exit it... For now on to the endlessness...\n                        You are dead")
      lq=input(" Do you want to start again?")
      if lq == "Yes":
        continue
      elif lq=="No":
        break   
    elif quest == "No":
      print("You remember your baba's tales about people who joined the horo disappear. You ")
  elif quest == ("No"):
    print ("\n __________________________________________________________\n  You finish with pasturing and go home through the thick, dark green forest. You walk around the village's lake and see snow white woman,samodiva, bathing in the water reflecting the full moon in this moment you fall in love with her. Her cloth and belt are at the coast. You heard folk tales about stealing samodiva's belt and they are in your control.")
    quest = input("Do you want to steal her clothes?")
    if quest=="Yes":
      print ("\n__________________________________________________________\n You steal her clothes without seeing you. When she gets out, she understands that her chothes are gone. While she is searching, she sees you holding her cloth and most importanly her belt. In that moment, she erects like frightened little animal before being shaughtered by a predator, but in the next moment she claims her destiny and says with woe that she is under your control. You marry her and she gives to two gorgeous children, boy and girl. In all that time she start to love you but she misses her sisters and freedom. \n One day she asks you may you free her.")
      quest = input("Do you want to free her")
      if quest == "No":
        print("\n__________________________________________________________\n You say that you can't because you love her and don't want to miss her. She understands that but she can't suppress her nature desires.")
        print ("To be continued")
        break
      elif quest == "Yes":
        print ("To be continued")
        break
