from datetime import timedelta
from datetime import datetime

#datetime.timedelta( days=0 , seconds=0 , microseconds=0 , milliseconds=0 , minutes=0 , hours=0 , weeks=0 )

# 假設 local 為 utf +8 時區
t1 = datetime.now()
print (t1)

# 轉變為 utf 0
t2 = t1 + timedelta(hours =-8)

print(t2)

