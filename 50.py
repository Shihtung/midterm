from operator import le
from random import randrange


all=set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
en=set(['John','Mary','Fiona','Claire','Ben','Bill'])
ma=set(['Mary','Fiona','Claire','Eva','Ben'])
print('英文數學都及格:',(en&ma))
print('數學不及格:',(all-ma))
print('英文及格且數學不及格:',en&(all-ma))