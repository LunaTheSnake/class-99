message=input("enter a message")
count=0
wc=0
for i in message:
	count=count+1
	if i==" ":
		wc+=1 
print("you entered", wc,"words")