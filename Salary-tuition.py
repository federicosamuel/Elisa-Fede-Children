https://replit.com/join/ubcfxjxqha-federicoolmos

print("Is there a seller?")
seller = input()

while seller == "yes":
  name = input("What is your name?")
  salary = float(input("What is your base salary?"))
  sales = float(input("How much money have you made in sales?"))
  if sales < 3500:
    total = salary + (sales*.07)
  elif 3500 < sales < 7000:
    total = salary + (sales*.1)
  elif sales > 7000:
    total = salary + (sales*.15)
  print("The total salary for", name, "is", total)  
  print("Is there another seller?")
  seller = input()
