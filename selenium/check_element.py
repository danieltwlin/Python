driver.find_element_by_xpath("//*[contains(text(), 'hello ')]").is_displayed()

driver.find_element_by_xpath(" xxxx").is_displayed() 



# 檢查是否刪除學生是否成功		
html = driver.page_source		
#print(html)

keyword = 'Baab'
if(keyword in html ):
	print('刪除學生失敗~!')
else:
	print('成功刪除~!')
