import os
import sys
import re
from traceback import print_exc

import xbmc

import xbmcgui

import xbmcaddon

settings = xbmcaddon.Addon(id='script.module.torrent.ts')


addonDir = settings.getAddonInfo("path")
print addonDir
XBMC_SKIN  = xbmc.getSkinDir()


class xbmcguiWindowError(Exception):
	def __init__(self, winError=None):
		Exception.__init__(self, winError)

	  
class WTSEngine(xbmcgui.WindowXMLDialog):
	def __init__(self, *args, **kwargs):
		#xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)
		#self.doModal()
		self.progress=0
		
		pass
	def onInit(self):
		self.controls = {}
		try:
			self.getControls()
		except:
			print_exc()
		#self.close()
	def updater(self,progress,text1,text2):
		self.label = self.getControl(2004)
		self.label.setPercent(progress)
		self.label = self.getControl(2002)
		self.label.setLabel(text1)
		self.label = self.getControl(2003)
		self.label.setLabel(text2)
	def getControls(self):
		pass

	def onFocus(self, controlID):
		pass

	def onClick(self, controlID):
		print self.getControl(controlID).getLabel()
		pass
	def show1(self):
		self.label = self.getControl(2000)
		self.label.setVisible(True)
	def hide1(self):
		self.label = self.getControl(2000)
		self.label.setVisible(False)
	def onAction(self, action):
		pass

class dwprogress():
	def __init__(self, *args, **kwargs):
		self.ui = WTSEngine("DialogDownloadProgress.xml",addonDir)
		self.ui.show()
	def onInit(self):
		#self.ui = WTSEngine("DialogDownloadProgress.xml",addonDir)
		#self.ui.show()
		pass
	def show(self):
		self.ui.show1()
		pass
	def hide(self):
		self.ui.hide1()
		pass
	def updater(self,progress=0,text1='',text2=''):
		self.ui.updater(progress,text1,text2)
		#self.ui.update()
		pass
	def close(self):
		self.ui.close()