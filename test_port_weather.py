import unittest
from port_weather import Ph_weather

class PhWeatherTest(unittest.TestCase):
	# filename = Ph_weather()
	"""docstring for pordt weather unit tests"""


	def setup(self, filename):
		self.filename = ph_weather()
		pass


	def test_filePath(self, filename):
		filename = ph_weather()
		self.assertTrue(os.path.filename)
		pass

	def test_fileOpen(self, filename):
		with open(filename) as fname:
			self.open_content(fname)
			self.assertRaise(self.open, fname, "port-harcourt-weather.txt", msg='File is open!')
			pass


	def test_dayKey_is_integer(self, filename):
		filename = ph_weather()
		dayKey = filename.tempDiff("port-harcourt-weather.txt")
		self.assertIsInstance(dayKey, int)
		pass




if __name__ == '__main__':
    unittest.main()
		
		