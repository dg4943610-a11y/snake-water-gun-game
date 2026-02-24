import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([-1,0,1])
youstr=str(input("enter your choice:"))
youDict={"s":1,
         "w":-1,
         "g":0}
reversedict={1:"snake",-1:"water",0:"gun"}
you=youDict[youstr]
print(f"you choose {youDict[youstr]}\ncomputer chose {reversedict[computer]}")
if computer==you:
   print("its draw")
if computer==-1 and you==1:#-1
    print("you win")
elif computer==-1 and you==0:#-1
   print("you lose")
elif computer==1 and you==-1:#-1
   print("you lose")
elif computer==0 and you==1:#1
   print("you lose")
elif computer==0 and you==-1:#-1
   print("you win")
elif computer==1 and you==0:#1
   print("you win")
else:
   print("something went wrong")
