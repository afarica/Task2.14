# Given a list of numbers, find and print all elements that are an even number. In
# this case use a for-loop that iterates over the list, and not over its indices! That
# is, don't use range
a=int(input("Enter your number:"))
i=1
for i in range(0,a+1):
	if i%2==0:
		print(i)
i+=1
