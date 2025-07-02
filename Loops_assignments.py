# For Loop
for m in range (1 , 11) :
    print(m)
    
# While Loop
x = 1
while x <= 5 :
    print(x)
    x += 1

# Loop Condition
count = int(input("Tell your number:"))
a = count
while a >= 0 :
    print(a)
    a -= 1

# Nested Loop
for x in range(1 , 4) :
 for y in range(1 , 4) :
    print(f"{x} * {y} = {x*y}")

# Bresk Loop
for i in range(0 , 11) :
 if i == 6 :
    break
 print(i)

# Continue Loop
for n in range(0 , 6) :
 if n == 3 :
    continue
 print(n)

# Bonus Task
word = str(input("Enter a word :"))
for a in word :
   print(a)