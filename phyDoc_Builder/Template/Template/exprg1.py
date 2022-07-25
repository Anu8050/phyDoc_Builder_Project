# double=lambda x:x*2
# print(double(3))

# old_list=[1,2,3,4,5,6,7,8]
# new_list=list(filter(lambda x:x%2==0,old_list))
# print(new_list)

list1=[2,3,1,4,5,7,6,8]
new_list=set(map(lambda x:x*2,list1))
print(new_list)