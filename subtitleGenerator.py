#!/bin/python

try:	
	import argparse
	import symbl
	parser = argparse.ArgumentParser(description="Subtite Generator Using Symbl.ai")

	parser.add_argument('--filetype', type=str, required=True, help="Give file type audio/video")
	parser.add_argument('--locate', type=str, required=True, help="Locate file")
	parser.add_argument('--output', type=str, default='outputfile.srt', help="Name of Output file")
	args = parser.parse_args()
		
except ModuleNotFoundError as err:
	print(err)
	exit()
except Exception as e:
	print(e)
	print("An Error has occur...Please try again")
	exit()


def generate_conversation_object(file_type, location):
	
	if(file_type=="Audio"):
		try:
			print("Your Subtitle File Is Generating")
			print("Please Wait This Might Take A While...")
			conv_object = symbl.Audio.process_file(file_path=location)
			return conv_object
		except Exception as e:
			print(e)
			print("Something went wrong please check the file and try again")
			exit()
	else:
		try:
			print("Your Subtitle File Is Generating")
			print("Please Wait This Might Take A While.....")
			conv_object = symbl.Video.process_file(file_path=location)
			return conv_object
		except Exception as e:
			print(e)
			print("Something went wrong please check the file and try again")
			exit()

def main():	
	file_type = args.filetype
	location = args.locate
	output_filename = args.output
	print(file_type,location,output_filename)
	
	filetype_list = ['audio','video','Audio','Video']
	if(file_type in filetype_list):
		conversation_object = generate_conversation_object(file_type.capitalize(), location)
	else:
		print("filetype is not audio/video")
		exit()
		
	print(conversation_object.get_messages().messages[0].text)
	print(conversation_object.get_messages().messages[0].start_time.time())
	print(conversation_object.get_messages().messages[0].end_time.time())
			 
	
	
		


if __name__=="__main__":
	main()
