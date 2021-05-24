#  set timezone
def set_timezone():
        db = MySQLdb.connect(host="localhost",
                user="backup", passwd="backup", db="sokradeo",charset="utf8")
        cursor = db.cursor()

        cmd ='SET time_zone = "+8:00";'
        # set Timezone
        cursor.execute(cmd)

        cmd ='SELECT NOW();'
        cursor.execute(cmd)

        # fetchall
        result = cursor.fetchall()
        #print(result)

        #if(0):
        #       # ....
        #       for record in results:
        #               col1 = record[0]
        #               col2 = record[1]
        #       print( "%s, %s" % (col1, col2) )

        # close
        db.close()

        return result

if __name__ == "__main__":

        ret = set_timezone()
        print(ret)
        
