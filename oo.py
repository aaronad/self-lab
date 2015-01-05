#!/usr/bin/python
import os,sys,subprocess,datetime,re
from time import strftime

fs = subprocess.Popen(['ping', '-c 1', '-w 1', '8.8.9.9'], stdout=subprocess.PIPE).communicate()[0]
if re.search('100%',fs) :
   print 'Found a match!'
else:
   print 'no match'
