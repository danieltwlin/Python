
	# 選擇班級
	selects = Select(driver.find_element_by_id('ClassID'))
	
	# 查看所有項目
	i=0
	id = 0 
	for select in selects.options:
		print( select.text)
		if( 'daniel_test' in select.text ):
			print('find it~!')
			print('index = ' + str(i))
			# 紀錄選中index
			id = i
			break;
		i=i+1
	# 選中	
	selects.select_by_index(id)
 

# 查看選中項目
# for selectx in selects.all_selected_options:
# 用文字選擇
# selects.select_by_visible_text("daniel_test(qa1234)")	


