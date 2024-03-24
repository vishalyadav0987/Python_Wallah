# #  1. star pattern
# a="*"
# for i in range(0,int(input("Range: "))):
#     for j in range(0,i+1):
#         print(a,end=" ")       
#     print()     


# print()


# #  2. invereterd star pattern
# a="*"
# b=int(input("Range: "))
# for i in range(0,b):
#     for j in range(b-i):
#         print(a,end=" ")       
#     print()   


# print()


            
# # #  3. index se repeat           
# # a=str(input("Name : "))
# # for i in a:
# #     b=a.index(i)
# #     c=b+1
# #     d=c*i
# #     print(d,end="")


# print()    

    
# #  4. single  line reapted surname
# a="vishal" 
# b="yadav"       
# for j in  b:
#     c=b[0:]
#     d=c*3
#     print(a,d,sep=" ")
# print(end=" ")     
            

# print()



              
# #  5. line reapted surname reapted
# a=["vishal"]
# b=["yadav"]
# for i in a:
#     for j in b:
#         print(i,j,j,j)



# print()        


# #  6.  range deke reapted surname repeat
# a=["vishal"]
# b=["yadav"]
# for i in a:
#     for j in b:
#         for k in range(int(input("Range:  "))):
#             print(i,j,j,j)



# print()             


# #  7.  with help of "WHILE LOOP" print 4 by 5 star pattern
# for i in range(4):
#     print("*",end=" ")
#     a=1
#     while a<=4:
#         print("*",end=" ")
#         a+=1
#     print()                    
                  
            



# #  8.  with help of "FOOR LOOP" print 4 by 5 star pattern
# for i in range(4):
#     for j in range(1,5):
#         print(j,end=" ")
#         print("*",end=" ")
#     print()



# # 9.  counting print through the oun row no's
# a=int(input("range: "))
# s=1
# for i in range(1,a):
#     for j in range(1,i+1):
#         print(s,end=" ")
#         s+=1
#     print()    



# print()


#  10.

# l=[]    # 0,1,2
# for i in range(3):
#     l.append(i)  # i 0 1 2
#     b=l[0:]  
#     c=str(b)
#     for j in c:
#         d=c.index(j)
#         e=d+1
#         f=e*j
#         print(f)




# 10>>>>>>

# print("New Program")
# for i in range(1,int(input("Range: "))):
#     for j in range(i,i+i):
#         print(i,end=" ")
#     print()   



# print("reverse")
# n=int(input("n : "))
# for i in range(1,n):
#     for j in range(n-i):
#         print(i,end=" ")
#     print()    


# print("reverse")
# n=int(input("n : "))
# for i in range(1,n):
#     for j in range(n-i,(n*2)+1):
#         print(j,end=" ")
#     print()  


#  15. reverse of 10>>>>>>
print("new program") 
n=int(input("n : "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(i,end=" ")
    print()    


  
