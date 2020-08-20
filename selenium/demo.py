#!/usr/bin/python
# -*- coding: utf-8 -*-

#=== Web  Test =============
# Program : add quiz
# Author  : daniel
#===========================
import unittest, time,datetime
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

# 輸入文字
if(1):
		element = driver.find_element_by_xpath("//input[contains(@name,'MsgTitle')]")
		element.clear()                 # 清除輸入框
		element.send_keys('測試活動')
