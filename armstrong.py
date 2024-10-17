'''n=str(int(input("Enter a number ")))
sum=0
for i in n :
    sum=sum+int(i)**len(n)
if int(n)==sum:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")


n=input('Enter the number ').split()
for i in range(len(n)):
    n[i]=int(n[i])
for j in range(len(n)):
    if(n[j]==n[-1:j]):
        print('The given  number is palindrome')
    else:
        print('The given number is not a palindrome')'''

# n=int(input('Enter the number'))
# for i in range(1,n):
#     if(i%n==0):
#         sum=sum+i
# if(n==sum):
#     print('The given number is a perfect number')

lst1=[22,33,44,55]
lst1.extend([433,22])
print(lst1)