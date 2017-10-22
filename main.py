__author__ = 'Sunando Bhattacharya'

import Util.Helper as helper

class Main:
	def __init__(self):
		self.__url__='https://urllib3.readthedocs.io/en/latest/user-guide.html'
		self.__helper__=helper.Helper()
	def main(self):
		page = self.__helper__.getPage(self.__url__)
		soup=self.__helper__.getSoup(page)


if __name__ == '__main__':
	Main().main()
