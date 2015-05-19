import unittest
from Crowdmap import Crowdmap

class FindProjTests(unittest.TestCase):
	def setUp(self):
		self.crowdmap= Crowdmap(["I met Or A. at Chabad house Bangkok","We found Or A. R.I.P at Langtang valley","Missing Cowboy"])

	def test_get_all_posts_for_missing_name(self):
		posts = self.crowdmap.get_all_posts_for("Joe")
		self.assertEquals([],posts)
	
	def test_get_all_posts_for_name(self):
		self.assertEquals(["I met Or A. at Chabad house Bangkok","We found Or A. R.I.P at Langtang valley"],posts)
		
		
if __name__ == '__main__':
	unittest.main()

