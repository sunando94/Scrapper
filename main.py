__author__ = 'Sunando Bhattacharya'

import Util.Helper as helper
import Util.PageParseEngine as pe

class Main:
	def __init__(self):
		self.__url__='https://urllib3.readthedocs.io/en/latest/user-guide.html'
		self.__helper__=helper.Helper()
		
	def main(self):
		page = self.__helper__.getPage(self.__url__)
		soup=self.__helper__.getSoup(page)
		self.__pe__=pe.PageParseEngine(soup,'var hello=helloworld;var tokens=helloworld;','Inline')
		self.__pe__.getTag(page,'a:last')



if __name__ == '__main__':
	Main().main()
