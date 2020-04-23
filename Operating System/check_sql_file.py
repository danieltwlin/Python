import os

workdir = '/opt/TW_DB'

os.chdir(workdir)

#os.system('ls -l')

ErrStr =''

# check sql file
sqlfile = workdir + '/product.sql'
#print(sqlfile)
if((os.path.isfile(sqlfile))== False):
        ErrStr = ErrStr +  sqlfile  + ' is not exist ! \n'

# print result
if(ErrStr !=''):
        print(ErrStr)
else:
        print('DB Backup is OK !')

