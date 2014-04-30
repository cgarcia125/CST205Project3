#!/anaconda/bin/python

# the line above needs to be there for the code to work with the right version of python on my machine

'''
Claudia Garcia
CST 205
Project 3
Gif generator with GUI
'''

# import needed libraries
from moviepy.editor import *

# regular takes a video and produces a gif
# t1 = initial time and t2 = final time
# t1 & t2 cant be more than 5 seconds apart
def regular(Video, t1, t2, size, gifName):
	VideoFileClip(Video).\
	subclip(t1,t2).\
	resize(size).\
	to_gif(gifName, fps = 15, program = 'ffmpeg')
	
#freeze will take a snapshot of the left half of a clip and
#allow the other half to move in the produced gif	
def freeze(Video, t1, t2, size, speed, snap, frames, gifName):
	bow = VideoFileClip(Video).\
	subclip(t1, t2).\
	speedx(speed).\
	resize(size)
	
	#cuts it in half, freezing the left half only
	snapshot = bow.\
	crop(x2 = bow.w/2).\
	to_ImageClip(snap).\
	set_duration(bow.duration)
	
	CompositeVideoClip([bow, snapshot]).\
	to_gif(gifName, fps = frames, program = 'ffmpeg')
	
#time_symetrize is necessary for videoTS
def time_symetrize(clip):
	return concatenate([clip, clip.fx( vfx.time_mirror)])

#produced gif clip plays once backwards and once forwards
def videoTS(Video,t1, t2, size, gifName):
	VideoFileClip(Video).\
	subclip(t1, t2).\
	resize(size).\
	fx(time_symetrize).\
	to_gif(gifName, fps = 15, program = 'ffmpeg')

# gif will fade into the next play
def loopOne(Video,t1, t2, speed, size, gifName, frames):
	spark = VideoFileClip(Video).\
	subclip(t1, t2).\
	speedx(speed).\
	resize(size)
	
	d = spark.duration
	spark = spark.crossfadein(d/2)
	
	CompositeVideoClip([spark, spark.set_start(d/2), spark.set_start(d)]).\
	subclip(d/2, 3*d/2).\
	to_gif(gifName, fps = frames, program = 'ffmpeg')
	
# snapshot of first frame and play it at the end of the gif	
def loopTwo(Video, t1, t2, gifName):
	boo = VideoFileClip(Video).\
	subclip(t1, t2)
	
	d = boo.duration
	snapshot = boo.to_ImageClip().\
	set_duration(d/6).\
	crossfadein(d/6).\
	set_start(5*d/6)
	
	CompositeVideoClip([carry, snapshot]).\
	to_gif(gifName, fps = boo.frames, program = 'ffmpeg')

# crops a gif	
def cropping():
    VideoFileClip(Video, size, left, right, gifName).\
    subclip(t1,t2).\
	resize(size).\
    crop(x1=left,x2=right).\
	to_gif(gifName, fps = None, program = 'ffmpeg')
		
def main():
	#Unit testing
	regular("./BeautyAndTheBeast.mp4",50, 52, .5, "regular_test.gif")
	freeze("./BeautyAndTheBeast.mp4",75,77 , .5, 1, 0.2, 20, "freeze_test.gif")
	videoTS("./BeautyAndTheBeast.mp4",160, 162, .5,"TS_test.gif")
	loopOne("./BeautyAndTheBeast.mp4", 200, 204, .5, .5, "loopOne_test.gif", 15)
	#loopTwo("./BeautyAndTheBeast.mp4", 222, 224, "loopTwo_test.gif")
	
main()