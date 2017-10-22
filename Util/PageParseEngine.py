__author__ = 'Sunando Bhattacharya'


from bs4 import BeautifulSoup as bsoup

class PageParseEngine:

	""" used to parse custom Syntax parser"""
	def __init__(self, soup,pattern,type='Inline',*args):
		
		self.parsePattern=pattern
		self.soup=soup
		self.type='Inline'
		if self.type == 'File':
			self.filePath=args[0]

	def __getFile__(self,path):
		file=open(path,'r')
		data=''
		for line in file:
			data+=line
			data+='\n'
		return data
	def __updateSoup__(self,data):
		self.soup=bsoup(data,'html5lib')

	def __getFromTaglist__(self,tag,*args):
		tagList={
		'body':self.soup.body,
		'a:first':self.soup.a,
		'a':self.soup.find_all('a'),
		'a:last':self.soup.find_all('a')[-1],
		'a:nth': lambda x:self.soup.find_all('a')[x],
		'h1':self.soup.h1,
		'h2':self.soup.h2,
		'h3':self.soup.h3,
		'h4':self.soup.h4,
		'h5':self.soup.h5,
		'h6':self.soup.h6,
		'div':self.soup.div,
		'div class':lambda x:self.soup.find_all('div',{'class':x})
		}
		if len(args)==0:
			return tagList[tag]()
		else:
			return tagList[tag](args)

	def getTag(self,data,tag,*args):
		self.__updateSoup__(data)
		print(self.__getFromTaglist__(tag,*args))
		

		
