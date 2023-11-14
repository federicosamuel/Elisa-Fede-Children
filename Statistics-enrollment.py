https://replit.com/join/qlbgrwiehx-federicoolmos

Less_than_2_years = 0
Between_2_and_5_years = 0
Between_5_and_10_years = 0
Greater_than_10_years = 0
animals= 0
print("Is there an animal to be recorder?")
animal = input()

while animal == "yes":
  animals+=1
  age = int(input("How old are they?"))
  if age < 2:
    Less_than_2_years += 1
  elif age >= 2 and age <= 5:
    Between_2_and_5_years += 1
  elif age >= 5 and age <= 10:
    Between_5_and_10_years += 1
  elif age > 10:
    Greater_than_10_years += 1
  print("Is there another animal to be recorded?")
  animal = input()
less2= (Less_than_2_years*100)/animals
between2and5= (Between_2_and_5_years*100)/animals
between5and10= (Between_5_and_10_years*100)/animals
greater10= (Greater_than_10_years*100)/animals
print("Less than 2 years:", Less_than_2_years, "and they are", less2, "% of the animals")
print("Between 2 and 5 years:", Between_2_and_5_years, "and they are", between2and5, "% of the animals")
print("Between 5 and 10 years:", Between_5_and_10_years, "and they are", between5and10, "% of the animals")
print("Greater than 10 years:", Greater_than_10_years, "and they are", greater10, "% of the animals")
