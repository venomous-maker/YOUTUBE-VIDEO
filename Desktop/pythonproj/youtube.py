#!/usr/bin/python3
import pytube, time, os
from pytube import YouTube
print("Download Youtube videos!")
link = input("Enter the video link: ")
# pass the link to youtube for video details

yt = YouTube(link)
class youtube():
	def video_det():
		#Title of video
		print("Title: ",yt.title)
		print("Number of views: ",yt.views)#Number of views of video
		print("Length of video: ",yt.length,"seconds")#Length of the video
		print("Description: ",yt.description)#Description of video
		print("Ratings: ",yt.rating)# Rating
		
	def all_str():
		streams= yt.streams # Streams
		for tr1 in streams:
			i_str = str(tr1)
			print(i_str)
			time.sleep(0.1)
	
	def aud_str():
		a_str = yt.streams.filter(only_audio=True)
		for audio in a_str:
			aud = str(audio)
			print(aud)
			time.sleep(0.1)
	
	def vid_str():
		v_str = yt.streams.filter(only_video=True)
		for video in v_str:
			vid = str(video)
			print(vid)
			time.sleep(0.1)
	
	def prog_str():
		# progressive streams
		prog = yt.streams.filter(progressive=True)
		for pr in prog:
			s_prog = str(pr)
			print(s_prog)
			time.sleep(0.1)
	def downbytag():
		tag = input("Enter the itag for the video quality you want: ")
		maind = yt.streams.get_by_itag(tag)
		location = "/home/venom/Desktop/pythonproj"
		os.sytem("chmod +x *")
		print("Downloading ...")
		maind.download()
		maind.download(location)
		print("Download finished")
		
	def down_h():
		# high resolution videos
		high = yt.streams.get_highest_resolution()
		location = "~/home/venom/Desktop/pythonproj"
		os.sytem("chmod +x *")
		print("Downloading ...")
		high.download()
		high.download(location)
		print("Download finished.")
def menu():
	n = input(f'''
CHOOSE ONE OF THE FOLLOWING:
	1. CHECK VIDEO DETAILS.
	2. CHECK ALL VIDEO STREAMS.
	3. CHECK AUDIO STREAMS.
	4. CHECK VIDEO STREAMS.
	5. DOWNLOAD VIDEO BY ITAGS.
	6. DOWNLOAD THE HIGHEST VIDEO QUALITY.
	: ''')
	if n == '1':
		youtube.video_det()
	elif n == '2':
		youtube.all_str()
	elif n == '3':
		youtube.aud_str()
	elif n == '4':
		youtube.vid_str()
	elif n == '5':
		youtube.downbytag()
	elif n == '6':
		youtube.down_h()
	else:
		os.system("clear")
		print("Download Youtube videos!")
		print(f"Enter the video link: {link}")
		print('Invalid input try again')
		menu()
menu()
