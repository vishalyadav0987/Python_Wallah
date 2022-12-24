# import random
# x=[1,2,3,4,5,6]
# d=random.choice(x)
# print(d)

# l=[]
# user=input("take mail from the user:---")
# for i in user:
#     l.append(i)
# print(l)



#question 1

# i=0
# l=[]
# n=int(input("the user-----"))
# while i<n:
#     i=i+2
#     l.append(i) 
# a=l[0]   
# b=int(a**2)
# x=l[1]
# z=int(x**2)
# c=l[2]
# e=int(c**2)
# print(b+z+e)





# ques 2


# n=int(input("a---- "))
# i=1
# while n>0:
#     if i%2==1:
       
#         print(i,end=" ") 
#         n=n-1  
#     i=i+1           
        


# n=int(input("a---"))
# i=1
# while n>0:
#     if i%2==0:
#         m=i**2
#         print(m,end=" ")
#         n=n-2
#     i=i+1       





user=input("take mail from the user:---")

i=0
l=[]
while i<len(user):
    l.append(user[i])
    i=i+1 
print("Username:--",l[-9:],"domain:--",l[:-10])    
print()  
print()     
