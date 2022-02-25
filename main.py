guess = 50
low = 50
high = 50
count = 0
hlc = ""

print("Think of a random number from 1 to 100, and I will to try guess it.")

while hlc != "same":
  hlc = input("I guess " + str(guess) + ", is the answer higher, lower, or the same? ")

  if hlc == "higher":
    low = guess

    if high == 50 & low == 50:
      high = 100
      
    guess = round((high-low) / 2 + low)

    count += 1
    
  elif hlc == "lower":
    high = guess

    if high == 50 & low == 50:
      low = 0
    
    guess = round(high - (high-low) / 2)

    count += 1

  elif hlc != "lower" and hlc != "higher" and hlc != "same":
    print("That is not a vaild answer")

count += 1

if count == 1:
  print("I got it in 1 try! I guess I am the best bot :3")
else:
  print("I got it in " + str(count) + " tries! That's worse than I expected...")
