#把 List 當作多維陣列使用
listary = [   
	['','','','ok'],
	['','','','ok'],
	['','','','ok']
]
print(listary)

# 由多個 List 串成一個多維陣列使用
'''
把 list1,list2 插入 list3，再用 list4, list5 取出 list 使用
list3 當作 list indx 的用述
list3[0][1] ==>直接使用
'''
list1 = ['1','2','3']
list2 = ['4','5','6']
list3=[]
 
list3.insert(0,list1)
list3.insert(1,list2)
print(list3)
print(list3[0][1])
print((list3[1][1])[0])
 
#取值的用法
list4 = list3[0]
print(list4)
print(list4[0])
list5 = list3[1]
print(list5)
print(list5[2])

