for i in range(10):
	print(i)

myList=['A','B','C']
for i in range(len( myList )):
	print(i)

for i in myList:
	print(i)

dict={'1':'a',2:'b',3:'c'}
for k, v in dict.items():
	print(k,v)	


#字典配合 index Loop 的作法
AppPlay_ID ={
		'AA':'aa',
		'BB':'bb',
		'CC':'cc'
	}

listary = [   
	['','','ok'],
	['','','ok'],
	['','','ok']
]

i = 0
for k, v in AppPlay_ID.items():
	print(k,v,i)
	listary[i][0] = i
	listary[i][1] = k
	i=i+1
	
print(listary)
