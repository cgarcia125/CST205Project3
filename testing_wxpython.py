

#testing wxpython.py
#This is meant to test basic wxpython functions and make sure they are working

#!/anaconda/bin/python
import wx
'''
app = wx.App(False)# Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World")# A Frame is a top-level window.
frame.Show(True)# Show the frame.
app.MainLoop()
'''

class MyFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title = title, size = (200, 200))
		self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
		self.Show(True)
		
app = wx.App(False)
frame = MyFrame(None, 'Small editor')
app.MainLoop()
