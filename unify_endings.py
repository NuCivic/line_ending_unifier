#! /usr/bin/python

import csv
import sys
import re


types = {
	'windows': '\r\n',
	'mac': '\r',
	'unix': '\n'
}

def guess_line_ending(csvfile):
	filedata = csvfile.read(10 * 1024);
	line_ending_guessed = '\n'
	max_value = 0;
	for platform, line_ending in types.items():
		occurrences = len(re.findall(line_ending, filedata))
		if occurrences > max_value:
			max_value = occurrences
			line_ending_guessed = line_ending
	return line_ending_guessed

def convert(csvpath, dest):
	csvfile = open(csvpath, 'rb')
	line_ending = guess_line_ending(csvfile)
	print 'Current line terminator: ' + repr(line_ending)
	if (line_ending != dest):
		print 'Converting...'
		csvfile.seek(0)
		filedata = csvfile.read()
		filedata = filedata.replace(line_ending, dest)
		csvfile.close()
		csvfile = open(csvpath, 'w')
		csvfile.write(filedata)
		csvfile.close()
	else:
		print 'Nothing to convert'


path = sys.argv[1]
dest = sys.argv[2]
try:
	convert(path, types[dest])
	print 'Finished'
except Exception, e:
	print "usage: unify_endings.py file-path line-ending-dest-platform"
	print "example: unify_endings.py ~/Downloads/mycsvfile.csv unix"
else:
	pass
finally:
	pass