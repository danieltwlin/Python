def profile():
    name = "Danny"
    age = 30
    return name, age

# call function
print(profile())

# return tuple value
name1,age1 = profile() #直接profile()函式賦值給name1，age1

print(name1)
print(age1)


'''
cmd結果如下
D:\>python aa.py
('Danny', 30)
Danny
30
'''
