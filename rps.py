import random
while True:
    print(" R = ROCK \n P = PAPER \n S = SCISSORS ")
    x=input("Enter your game [R/P/S]: ")
    x=x.upper()
    sample_string = ["R","P","S"]
    y=random.choice(sample_string)
    print("computer choice",y)
    if(x==y):
        print("The game is tie")
    if(x=='R' and y=='P'):
        print("You win")
    elif(x=='R' and y=='S'):
        print("Computer Wins")
    elif(x=='P' and y=='S'):
        print("Computer Wins")
    elif(x=='P' and y=='R'):
        print("You Win")
    elif(x=='S' and y=='P'):
        print("You Win")
    elif(x=='S' and y=='R'):
         print("Computer Wins")
    else:
        print("Wrong Input")
    u=input("Play Again?(y/n): ")
    u=u.lower()
    if(u=="y"):
        continue
    if(u=="n"):
        break
    else:
        print("wrong command")

        
    
        
    
        
        
        
        
    
    
    


