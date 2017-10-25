__author__ = 'Sunando Bhattacharya'


from bs4 import BeautifulSoup as bsoup
from lark import Lark
from lark import Transformer
import re

class MyTransformer(Transformer):
	def start(self,item):
		print()
		# print(item)
	def string(self,item):
		# print(type(item[0].value))
		print(item[0].value)

	# WORD = list


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
		'div class':lambda x:self.soup.find_all('div',{'class':x}),
		'decendents': lambda x:x.decendents,
		'parent': lambda x:x.parent,
		'next-sibling':lambda x:x.next_sibling,
		'prev-sibling':lambda x:x.previous_sibling,
		'next-siblings':lambda x:x.next_siblings,
		'prev-siblings':lambda x:x.previous_siblings,
		'find': lambda x:self.soup.find(x),
		'find all': lambda x:self.soup.find(x),
		'find allre': lambda x:self.soup.find(re.compile(x)),
		'find all-id': lambda x:self.soup.find_all(id=x),
		'find css-sel': lambda x:self.soup.select(x),
		'get content': self.soup.get_text(),
		'get content sep': lambda x:self.soup.get_text(x)
		}
		if len(args)==0:
			return tagList[tag]()
		else:
			return tagList[tag](args)

	def getTag(self,data,tag,*args):
		self.__updateSoup__(data)
		self.langParse()
		print(self.soup)

	def langParse(self):
		l = Lark('''
			string : WORD
			start: string*
					%import common.WORD
					%ignore " "
					''',start='start', lexer='standard')
		tree = l.parse("My name is Sunando")
		print( tree.pretty() )
		MyTransformer().transform(tree)







				
		

		
