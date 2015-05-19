__author__ = 'liran'
class Crowdmap(object):
	def __init__(self, init_list):
		self.list = init_list
#		self.location_service = LocationService()

	def get_all_posts_for(self, name):
		return [post for post in self.list if post.find(name) != -1]