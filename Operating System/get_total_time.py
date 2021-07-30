import time
start = time.time()
print( "Start : %s" % start)

#####################################
# Program Process
#####################################

# Total Time
end = time.time()
elapsed = end - start
m, s = divmod(elapsed, 60)
h, m = divmod(m, 60)
print( "Total Time: %d:%02d:%02d" % (h, m, s) )
