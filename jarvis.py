print("welcome to the quiz game :)")
a=input("do you want to play: ")
if a.lower()!="yes":
	quit() 
else:
	print("All the best , lets play !")
score=0
q1=input("what CPU stands for? ")
if q1.lower()=="central processing unit":
	score+=1

q2=input("what RAM stands for? ")
if q2.lower()=="random access memory":
	score+=1

q3=input("what ROM stands for? ")
if q3.lower()=="read only memory":
	score+=1

q4=input("what SSD stands for? ")
if q4.lower()=="solid state drive":
	score+=1

q5=input("what HDD stands for? ")
if q5.lower()=="hard disk drive":
	score+=1

print("your score is :",score)
print("your score percentage is :" ,(score/5)*100)