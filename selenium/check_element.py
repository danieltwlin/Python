# 檢查網頁文字或元件是否存在
driver.find_element_by_xpath("//*[contains(text(), 'hello ')]").is_displayed()
driver.find_element_by_xpath(" xxxx").is_displayed() 

# 由page_source 檢查是文字是否存在
html = driver.page_source		
#print(html)

keyword = 'Baab'
if(keyword in html ):
	print('刪除學生失敗~!')
else:
	print('成功刪除~!')

	
# 檢查連結是否存在
strRes = "example.xls"
driver.find_element_by_xpath("//a[contains(text(),'" + strRes + "')]").is_displayed()
		
