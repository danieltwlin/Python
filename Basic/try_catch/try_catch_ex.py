# 直接拋出異常，中止程式
'''
raise语句
主动抛出异常。
格式：
主动抛出异常终止程序
raise 异常名称(‘异常描述’)
'''
raise RuntimeError('testError')

# 人工產生異常
try:
	raise BaseException("錯誤原因")   # raise ErrorType(" Error Message ")  
except Exception as e:
    	print(e)

# 斷言
self.assertEqual(ret,'OK')


