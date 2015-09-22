#LOOP
names = ['eamon','ad','edward']
for name in names:
	print(name)

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum += x
print(sum)

list(range(10))

sum = 0
for x in range(101):
	sum = sum+x
print('iteral range(101)',sum)

sum=0
n=99
while n> 0:
	sum+=n
print('while loop 0-99:',sum)
	n-=2