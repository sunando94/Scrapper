__author__ = 'Sunando Bhattacharya'


from bs4 import BeautifulSoup as bsoup

class PageParseEngine(object):
	"""\used to parse custom Syntax parser"""
	def __init__(self, soup,pattern,type='Inline',*args):
		super(ClassName, self).__init__()
		self.parsePattern=pattern
		self.soup=soup
		self.type='Inline'
		if(self.type == 'File')
		self.filePath=args[0]

	def __getFile__(self,path):
		file=open(path,'r')
		data=''
		for line in file
			data+=line
			data+='\n'
		return data
	def __getTag__(self,data,tag,*args):
		soup=bsoup(data,'html5lib')
		tagList={
		'body':soup.body,
		'a:first':soup.a,
		'a':soup.find_all('a'),
		'a:last':soup.find_all('a')[-1],
		'a:nth': lambda x:soup.find_all('a')[x],
		'h1':soup.h1,
		'h2':soup.h2,
		'h3':soup.h3,
		'h4':soup.h4,
		'h5':soup.h5,
		'h6':soup.h6,
		'div':soup.div,
		
		}
		
