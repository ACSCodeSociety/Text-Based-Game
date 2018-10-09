print("You are a brand-new 18 year old bulgarian boy, waiting to start his new life in a new country. Your job is to navigate him through life-changing questions, which will lead to his new life. You must answer with yes or no. Good luck!")

q1 = input("You contemplate about studying in France.")
if q1 == "yes":
  print("You apply for a university in Paris.")
elif q1 == "no":
  print("You change your mind and apply for a university in Moscow.")
print("You are accepted to the university and you move out.")

q2 = input("You buy a small apartment.")
if q2 == "yes":
  print("You live independently, but you lack money and you ask your parents for money, which irritates them.")
elif q2 == "no":
  print("You start living in a dormitory with other international students, and you afford buying a laptop, which helps you study and relax.")
print("You live and study everyday, but then you think about starting earning money.")

q3 = input("You apply for a job with a really good salary, but it's on the other end of city.")
if q3 == "yes":
  print("You are accepted, you learn a lot of money, but you come home late and don't turn in assignments on time.")
  print("The dean of the university thinks that your low grades due to the late assignments are unacceptable and you are kicked out of the university.")
  print("To be continued...")
elif q3 == "no":
  print("You apply for a job that has a less salary, but is closer to your home and you come home early and you aren't late with assignments.")
  print("Your grades are perfect and you graduate from university with a gold medal.")
  print("Then you apply for your dream job and win a haappy life.")
  print("The End.")
