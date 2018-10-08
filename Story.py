print("S"*25 + "s"*10 + "S"*25)
print("\n")
print("  Welcome, fellow loners!\n  How is life going? Boring much?\n  Well, I promise you this game is going to enrich those miserable life of yours.\n  Let's get right to it!\n  Road begin!" )
print("\n")
print("S"*25 + "s"*10 + "S"*25)

while True:
 ss = input("\n  \"Do you want ice cream?\" a voice asks.\n")
 if ss == "Yes":
  print("\n   You wake up to two white eyes staring at you. The feeling brought by them - immensily ominous. You blink confused and notice the contrast between the pale skin and the black hair of the man. ")
  name = input("\nName, please: ")
  print("\n   \"Hello, "+ name +", nice to meet you.\""+ "\n   Strangely, the man doesn't bother to introduce himself. His words hang heavy in the silence." +"\n   \"Who are you?\" you ask flustered." + "\n   \"I am Order,\" says the man in a monotous tone, confusing you even further." )
  ss = input("\nAsk a question./ Remain silent.\n")
  if ss == "Ask a question.":
    print("\n   \"Is that your name?\"" + "\n   He nods." + "\n   \"You have been chosen to represent my opposite - Chaos. You are the deity of Chaos,\" he says now looking at the black robes enraping you." + "\n   \"I  don't understand. Wh-what happened?\"" + "\n   \"You were given a second chance to prove yourself after death. Forget your human life and become my counterpart,\" his deep voice echoes as he explains.\n   You begin to panic.")
    ss=input("\nAccept your role./ Struggle.\n")
    if ss=="Accept your role.":
      print("\n   The man takes your hand and helps you stand. You had silently pondered over your answer, but had finally reached the conclusion to go with the white-eyed man. \n   \"For that I'm grateful. You're brave, human. Now let's begin our glorious days as bringers of balance.\" " + "\n\nLAME END \nTO BE CONTINUED..." + "\n"*2 + "S"*25 + "s"*10 + "S"*25)
      break
    elif ss=="Struggle.":
      print("\n   \"Then forget... and let your soul never be forgiven for it has committed the great sin of disobeying divinity. Dissipate into oblivian, oh wreched spirit, let your dust fade, and never be reborn again,\" Order recites, and your body feels lighter as it begins to wash away in the sands of time.\n\n :(\n  BAD END 2" + "\n"*2 + "S"*25 + "s"*10 + "S"*25)
      re = input("\nDo you want to try again?\n")
      if re == "Yes":
        continue
      elif re == "No":
        break
      else:
        break
    else:
      print("\nPlay the game properly, dumbass!"  + "\n"*2 + "S"*25 + "s"*10 + "S"*25)
      continue
  elif ss=="Remain silent.":
    print("\n   Order sees the hesitation in you eyes.\n" + "You have been chosen to represent my opposite - Chaos. You are the deity of Chaos,\" he says." + "\n   \"I  don't understand. Wh-what happened?\"" + "\n   \"You were given a second chance to prove yourself after death. Forget your human life and become my counterpart,\" his deep voice echoes as he explains.\n  \"Come with me and you will see parts of the world you've never imagined. We can do whatever we want,\" he ensures you, mischief sparkling in his eyes.\n   You look at your black robes, then back at his white ones. Before you appears a vast ocean glazed by moonlight. You look at the flat surface, and see two figures standing there - a reflection of gods yet unknown. One dressed in pure white with dark raven hair, the other one - a little unaware as it seems - in black robes with snow white hair.\n   Your eyes focus right at the two reflections as the man grabs your hand and pulls you toward the depts of the ocean.\n   \"Let us begin our journey to collapsing reality.\"" +"\n\nCOOL END\nTO BE CONTINUED..." + "\n"*2 + "S"*25 + "s"*10 + "S"*25 )
    break
  else:
    print("\nPlay the game properly, dumbass!"  + "\n"*2 + "S"*25 + "s"*10 + "S"*25)
  continue
 elif ss == "No":
  print("\n   You're hit by a car, and die in an accident. \n  :(\n  BAD END 1" + "\n"*2 + "S"*25 + "s"*10 + "S"*25)
  re = input("\nDo you want to try again?\n")
  if re == "Yes":
    continue
  elif re == "No":
    break
  else:
    break
 else:
  print("\nPlay the game properly, dumbass!"  + "\n"*2 + "S"*25 + "s"*10 + "S"*25)
  continue
