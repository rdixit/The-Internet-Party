from libraries.requests import requests
from tornado.web import RequestHandler as r
import random
import logging

#todo resize all post images in GIMP to same size.
#Use a sprite to cut up all the images. 
#Later: do something fun with the images. Like a rubic's cube or something. 



class Test(r):
	def get(self):
		context = {}
		self.render("basic/test.html", **context)


class Home(r):
	def get(self):

		titles = [
			"rohan", 
			"CNS", 
			"schizoType", 
			"del.icio.us"
		]
		
		urls = [
			"/", 
			"https://github.com/rdixit/The-Cybernetic-Sutra", 
			"/schizo_robot", 
			"http://delicious.com/rd108"
		]
		
		contents = [
			"""Rohan is a human who lives on planet Earth <span class="amp">&amp;</span> and loves you.""", 
			"The Cybernetic Sutra is a short e-book (currently in progress) that explores networks, neuroscience and nirvanva.", 
			"schizoType is a project to automatically suggest pharmaceutical interventions to schizophrenic patients based on their symptoms and history.", 
			"delicious.com is a digital bookmarking service I use a lot. Here's a link to check mine out." 
		]
		
		images = ["http://m3.licdn.com/mpr/pub/image-6wzyKOGe_tEUmEj9KzdOfu-kvpnDhkNKHQwZ0T3evRUwhUv66wzZ_hfevZ9YhC32FVZp/rohan-dixit.jpg", "static/images/cns.png", "static/images/sr.jpg", "static/images/blue_brain.jpg" ]

		context = { 
			"titles": titles,
			"urls": urls,
			"images": images,
			"contents": contents,
		 }
		self.render("basic/homepage.html", **context)



class SchizoRobot(r):
	def get(self):
		context = {}
		self.render("basic/schizo_robot.html", **context)


class PageNotFound(r):
	def get(self):
		context = {}
		self.render("basic/404_not_found.html", **context)
