#a=10
# b,c=20,30
# d=e=f=40
# print(a)
# print(c)
# print(f)

# 

# age=18
# if age>18:
#     print("Eligible")
# elif age==18:
#     print("Welcome new voter")    
# else:
#     print("not eligible")
# print("if condition execution")        


# 



# for i in range(10,100):
#     if i%10==7 or i//10==7:
#         print(i,end=" ")


n=10
list1=[]
for i in range(n):
    if i%2==0:
        list1.append(i)
print(list1) 
list2=[x for x in range(n) if x%2==1]
print(list2)       