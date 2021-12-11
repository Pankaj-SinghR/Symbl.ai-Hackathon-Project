#!/bin/python

import argparse

def argument_function():
	try:	
		parser = argparse.ArgumentParser(description="Subtite Generator Using Symbl.ai")

		parser.add_argument('--filetype', type=str, required=True, help="Give Either audio or video")
		parser.add_argument('--location', type=str, required=True, help="Location of file")
		parser.add_argument('--output', type=str, default='outputfile.srt', help="Name of Output file")
		args = parser.parse_args()
	except:
		print("An Error has occur...Please restart")



if __name__=="__main__":
	augument_function()
