print("hello welcome to playing rock paper scissors")
print("Well, you can try your luck three times ")
import random
x=["rock","paper","scissors"]
rand=random.choice(x)
user = input("please enter (rock,paper,scissors) ")
while user != "rock" and user != "paper" and user !="scissors":
	user = input("please enter (rock,paper,scissors)")
else:
	None
def condition():
    if rand == "rock" and user == "rock":
        print("We got equal",)
        print("my guess was",rand)
    elif rand == "rock" and user=="paper":
        print("you have won",)
        print("my guess was ",rand)
    elif rand == "paper" and user=="rock":
        print("i won")
        print("my guess was ",rand)
    elif rand == "rock" and user == "scissors":
        print("i won")
        print("my guess was ",rand)
    elif rand == "scissors" and user == "rock":
        print("you have won")
        print("my guess was ",rand)
    elif rand == "paper" and user == "paper":
        print("We got equal")
        print("my guess was ",rand)
    elif rand=="paper" and user == "scissors":
        print("you have won")
        print("my guess was ",rand)
    elif rand == "scissors" and user == "paper":
        print("i won")
        print("my guess was ",rand)
    else:
        print("invalid string")
condition()
rand=random.choice(x)
user=input("please enter (rock,paper,scissors)")
while user != "rock" and user != "paper" and user != "scissors":
	user = input("please enter (rock,paper,scissors)")
else:
	None
condition()
rand=random.choice(x)
user=input("please enter (rock,paper,scissors)")
while user != "rock" and user != "paper" and user != "scissors":
	user = input("please enter (rock,paper,scissors)")
else:
	None
condition()

rand=random.choice(x)
user=input("please enter (rock,paper,scissors)")
while user != "rock" and user != "paper" and user != "scissors":
	user = input("please enter (rock,paper,scissors)")
else:
	None
condition()

rand=random.choice(x)
user=input("please enter (rock,paper,scissors)")
while user != "rock" and user != "paper" and user != "scissors":
	user = input("please enter (rock,paper,scissors)")
else:
	None
condition()


