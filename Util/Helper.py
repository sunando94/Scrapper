__author__ = 'Sunando Bhattacharya'

import urllib3
from bs4 import BeautifulSoup as bsoup



class Helper:

	def __init__(self):
		self.__http__=urllib3.PoolManager()

	def getPage(self,url):
		try:
			self.__url__=url
			req= self.__http__.request('GET',self.__url__)
			return req.data
		except urllib3.exceptions.MaxRetryError:
			print('MaxRetryError: request timeout. Please check your network connectivity')


	def getSoup(self,data,element):
		try:
			soup=bsoup(data,'html5lib')
			return soup
		except:
			 print("Error")