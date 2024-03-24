# def greet(name,msg="vishal"):
#     print("hello",name,+ msg)

# greet("kate")




# def star(*name):
#     for names in name:
#         print("hello",names)

# star("kate","vishal","vishal")



# def f():
#     s="class"   # to comment 2nd output s=python python
#     print(s)
# #globle scope
# s="python"   # to comment error 1st 
# f()
# print(s)    



# def f():
#     s+="class"
#     print("inside function",s)

# # globle scope
# s="pytrhon"                          error prrogram
# f()
# print(s)    





# def f():
#     global s
#     s+="class"
#     print(s)
#     s="new python"
#     print(s)

# # globle scope
# s="python"                        
# f()
# print(s)




# a=1
# def f():
#     print("inside f()",a)

# def g():
#     a=2
#     print("inside g()",a)

# def h():
#     global a
#     a=3
#     print("inside h()",a)  

# print("global : ", a)     
# f()
# print("global : ", a)  
# g()
# print("global : ", a)  
# h()
# print("global : ", a)   


# lambda fuction
# a=lambda x:x*2
# print(a(5))


# a=map()
# b=filter('')
# l=[1,2,3,4,5,6]
# l1=list(filter(lambda x: (x%2==0),l))
# print(l1)

# l=[1,2,3,4,5,6]
# l1=list(map(lambda x: x*2,l))
# print(l1)



# def f1():
#     s="asdfgbn"
   


#     def f2():
        
#         print(s)

#     f2()
# f1()   


# a="sdfgh"
# def f():
#     print(a)
# f()    

def sum():
    a=3
    b=4
    c=a+b
sum()    
