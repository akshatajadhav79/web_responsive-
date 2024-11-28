# # Programe By Akshata Jadhav

# import array as arr
# a = arr.array('i')
# ch = int()
# max = int()
# def insert(a,s):
#     if s>0:
#         for i in range(s):
#             no = int(input("Enter NO:"))
#             a.append(no)
#         print("Elements inserted ")
        
#         mymain()
            
        
# def show(a):
#     print("Array==")
#     for i in a:
#         print(i , end=" ")
#     mymain()
    
# def delete(no):
#     for i in a:
#         if i == no:
#             a.remove(no)
#             print("element is deleted")
#     mymain()
    
# def sum(a):
#     mysum = 0
#     for i in a:
#         mysum = mysum+i
#     print("sum is =",mysum)
        
#     mymain()
    
# def arrmax(a):
#     for i in a:
#         if i>max:
#             max = i
#     print("max element == ",max)
#     mymain()
        
# def mymain():
#     print("\n1:Insert 2:Display 3:Delete 4:sum 5:max 6:Exit")
#     ch = int(input("Enter Choice:"))
#     if ch == 1:
#         size = int(input('enter Size of array:'))
#         insert(a,size)
#     elif ch == 2:
#         show(a)
#     elif ch == 3:
#         no = int(input('enter element of array:'))
#         delete(no)
#     elif ch == 4:
#         sum(a)
#     elif ch == 5:
#         arrmax(a)
#     elif ch == 6:exit()
#     else:print("\n Enter Right choice")
    
# mymain()



balls = [5, 2, 8, 5, 7]

# array size
n = 5
# index of element to be deleted
pos = 2
# adjusting the value of loop counter to pos
j = 0

while j < n:
    if pos == balls[j]:
        j=
        balls[j]=balls[j+1]
    j = j + 1
    
n=n-1
print("\nThe chairs and the corresponding number of balls after removing a ball")
for i in range(n):
    print(str(balls[i]))
    