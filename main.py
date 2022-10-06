age = int(input("Enter your age: "))
  
if age >= 17:
    print("you can watch a R rated movie alone")
elif age >= 13:
    print("you can watch a PG-13 movie alone")
elif age >= 5:
    print("You can watch see a G or PG movie alone")
else:
    print("you are too young") 