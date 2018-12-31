# Age Checker

your_age = input("How old are you? ")
friend_age = input("How old is your friend? ")

if int(your_age) >= 18 or int(friend_age) >= 18:
    print("Congrates, one of  you is old enough to vote!")
else:
    print("Sorry, one of you are to young to vote.")
    
