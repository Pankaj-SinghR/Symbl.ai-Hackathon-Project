# Symbl.ai-Hackathon-Project
#### Subtitle Generator for audio/video file using python sdk of Symbl.ai
##### Install python libraries
```
$ pip install symbl
$ pip install argparse
```
##### Create a symbl.conf file and add your API credential.
```
$ touch symbl.conf
```
##### Add API_ID and API_KEY in the _symbl.conf_
```
[credentials]
app_id='YOUR_API_ID'
app_secret='YOUR_API_KEY'
```
##### Clone this github repo
```
$ git clone https://github.com/PankajSingh1010/Symbl.ai-Hackathon-Project.git
```
##### Add symbl.conf file in Symbl.ai-Hackathon-Project directory
```
$ mv symbl.conf ./Symbl.ai-Hackathon-Project
$ cd Symbl.ai-Hackathon-Project
$ ls
sampleVideo.mp4  subtitleGenerator.py  symbl.conf
$ chmod +x subtitleGenerator.py
```
#### ***Lets try to create subtitle file for sampleVideo.mp4***
##### Print Usage
```
$ ./subtitleGenerator.py -h
usage: subtitleGenerator.py [-h] --filetype FILETYPE --locate LOCATE [--output OUTPUT]

Subtite Generator Using Symbl.ai

optional arguments:
  -h, --help           show this help message and exit
  --filetype FILETYPE  Give file type audio/video
  --locate LOCATE      Locate file
  --output OUTPUT      Name of Output file
```
##### Pass arguments to the files
> filetype : give audio or video

> locate : location of your audio/video file

> output : give name to output file with .srt extension
```
$ ./subtitleGenerator.py --filetype video --locate ./sampleVideo.mp4 --output subtitle.srt
Filetype --> video
File location --> ./sampleVideo.mp4
Outputfile name --> subtitle.srt
Your Subtitle File Is Generating
Please Wait This Might Take A While.....


Task Complete..Subtitle File Has Been Created
$ ls
sampleVideo.mp4  subtitleGenerator.py  subtitle.srt  symbl.conf
```
> subtitle.srt

#### Now you can add subtitle.srt file to the video :-)
#### [video]()
