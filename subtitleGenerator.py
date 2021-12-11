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
			print("Something went wrong please enter the correct file and try again")
			exit()


def generate_output_file(conv_obj, output_filename):
	
	err_hour = int(conv_obj.get_messages().messages[0].start_time.hour) #these values are not part of file
	err_minute = int(conv_obj.get_messages().messages[0].start_time.minute) 
	err_second = int(conv_obj.get_messages().messages[0].start_time.second) 
	
	print(err_hour,err_minute,err_second)
	
	with open(output_filename, 'w') as f:
		sequence_number = 1
		for data in conv_obj.get_messages().messages:
			f.write(f'{str(sequence_number)}\n')
			s_hour = int(data.start_time.hour)
			e_hour = int(data.end_time.hour)
			
			s_minute = int(data.start_time.minute)
			e_minute = int(data.end_time.minute)
			
			s_second = int(data.start_time.second)
			e_second = int(data.end_time.second)
			
			f.write(f'{s_hour-err_hour}:{s_minute-err_minute}:{s_second-err_second} --> {e_hour-err_hour}:{e_minute-err_minute}:{e_second-err_second}\n')
			print(data.text)
			f.write(f'{data.text}\n\n')
			sequence_number += 1
			
		print("Take Complete..Subtitle File Is Created")

def main():	
	file_type = args.filetype
	location = args.locate
	output_filename = args.output
	print(file_type,location,output_filename)
	
	filetype_list = ['audio','video','Audio','Video']

	if(file_type in filetype_list):
		conversation_object = generate_conversation_object(file_type.capitalize(), location) #function call to create a conversation object
	else:
		print("filetype is not audio/video")
		exit()
		
	generate_output_file(conversation_object, output_filename) #function call to generate subtitle file	


if __name__=="__main__":
	main()
