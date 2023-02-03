# class animal:
#     def speak(self):
#         print("animal speakig")

# class dog(animal):
#     def bark(self):
#         print("dog barking")    
#d=animal()
#d.speak()     # animal speakig
#d.speak()     # animal speakig
# d=dog()
# d.speak()      # animal speakig
# d.bark()       # dog barking


# class calculation1:
#     def sum(self,a,b):
#         print("a+b =",a+b)
# class calculation2:
#     def sub(self,a,b):
#         print("a-b =",a-b)
# class calculation3(calculation1,calculation2):
#     def div(self,a,b):
#         print("a//b =",a//b)
# d=calculation3()
# d.sum(12,1)
# d.sub(23,45)
# d.div(12,45)




# class v:
#     def b(self):
#         name="vishal"
#         print("name =",name)
# d=v()
# d.b() 


# 1. single level inheritance...............................................................................
# class A:
#     x=5
#     def message ():
#         print("vishal")
        
# d = A()
# print(d.x)
# A.message()


# class A:
#     x=5
#     def message (self,para):
#         print("vishal")
        

# A.message(5,"h")


# class A:
#     x=5
#     def message (self):
#         print("vishal")
        
#print(A.x)
# A.message(2)


#  2 . inheritance class ...................................................................................
# class a:
#     def message(self):
#         print("vishal")
# class b(a):
#     def message2(self) :
#         print("Yadav")  
# d = b()  
# d.message()
# d.message2()

#  3 . multilevel inheritance class.........................................................................
# class a:
#     def v(self):
#         print("this is my name")
# class b(a):
#     def v1(self):
#         print("vishal")
# class c(b):
#     def v3(self):
#         print("yadav")
# d=c()
# d.v()
# d.v1()
# d.v3() 

# 4. Hierarchical inheritance...............................................................................
# class a:
#     def v1(self):
#         print("vishal")
# class b(a):
#     def v2(self):
#         print("vishal")        
# class c(a):
#     def v3(self):
#         print("vishal")
# class d(a):
#     def v4(self):
#         print("vishal")
# object=b()        
# object.v1()
# object.v2()

# 5. hybrid inheritance.....................................................................................
# class a:
#     def v(self):         # self is not keyword #self/abc represents the instance of the class.
#         print("vishal 1")
# class c:
#     def v1(self):
#         print("vishal 2")         
# class b(a,c):
#     def v2(self):
#         print("vishal 3")
# class f(b):
#     def v3(self):
#         print("vishal 4")         
# class g:
#     def v4(self):
#         print("vishal 5")        
# class e(f,g):
#     def v5(self):
#         print("vishal 6") 
                
# obj=e()     #  is called(obj) the instance of the class.
# obj.v()
# obj.v1()
# obj.v2()
# obj.v3()
# obj.v4()
# obj.v5()

# class A:
#     def d1(self):
#         print("vishal 1")
# class C:
#     def f1(self):
#         print("vishal 2")        
# class B(A,C):
#     def e1(self):
#         print("vishal 3")        

# class G:
#     def b1(self):
#         print("vishal 4")
# class E():
#     def c1(self):
#         print("vishal 5")        
# class F(G,E,B):
#     def a1(self):
#         print("vishal 6") 
# obj1=F() 
# obj1.d1() 
# obj1.f1() 
# obj1.e1() 
# obj1.b1() 
# obj1.c1() 
# obj1.a1()     
         
# inbulid methods

# class a_is_parent:
#     def v(self):
#         print("vishal")
# class b_is_child(a_is_parent):
#     def v1(self):
#         print("vishal 2")

# print(issubclass(b_is_child,a_is_parent))    
# print(issubclass(a_is_parent,b_is_child))                 


# class A:
#     def d1(self):
#         print("vishal 1")
# class C:
#     def f1(self):
#         print("vishal 2")        
# obj3=A()
# obj4=C()
# print(isinstance(obj3,A))   
# print(isinstance(obj4,A))      
# print(isinstance(obj3,B))    show error because B is not defined

# Access modifier............................................................................
# 1. "Public"  access khi bhi  "How will write":: a=5
# 2. "Protected"   acess 1 class to another inherted the class jaha derived ho   "How will write":: _a=5
# 3. "priuate"  outside class not access     "How will write":: __a=5
# Data hiding......................................................................................
# DATA Id is different for different class . #advantage: for secure the data ,it will the data and missue
#                            #disadvantage : do not linkange with another class,readebility of code is increase
# class A:
#     a=5
#     _b=7
#     __c=6
  
# class C(A):
#     d=3
# obj5=C()
# print(obj5.a)  # Public
# print(obj5._b)    # Protected
# print(obj5.d)  # Public  
# # print(obj5.__c) # is not access because c is private variable

# Method overriding......................................................................................
# no's of parmameter same is called overriding
# Q what is difference between method and function ???
#  ANSWER. A function is a set of instructions or procedures to perform a specific task, and a method is a set of instructions that are associated with an object


#(for method overiding rule is inhertance class is present).................................................
# class a:
#     def v(self):
#         print("vishal") 
# class b(a):
#     def v(self):  # because value is updated.
#         print("yadav")
# d=b()
# d.v()        

# class a:
#     def v(self):
#         print("vishal")
#     def v(self):             # isnot method overriding
#         print("yadav")
# d=a()
# d.v()

#  Method overing in multiple inheritance..............................................................
# class a:
#     def v(self):
#         print("this is my name")
# class b:
#     def v(self):
#         print("vishal")
# class c(b,a):
#     def v(self):
#         print("yadav")
# d=c()
# d.v()

# using class name
# class a:
#     def v(self):
#         print("this is my name")
# class b(a):
#     def v(self):
#         a.v(self)  # a is classname() acess the class
#         print("vishal")
# d=b()
# d.v()

# Super() method
# class a:
#     def v(self):
#         print("this is my name")
# class b(a):
#     def v(self):
#         super().v(self)  # a is super() acess the class
#         print("vishal")
# d=b()
# d.v()


# def p(a,b):
#     p=a*b
#     print(p)
# def p(a,b,c):
#     p=a*b*c
#     print(p)
# p(4,5)
# p(4,5,5)


