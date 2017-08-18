import os
# import os.path

class Ph_weather(object):
	path = "D:\TDD_Challenge\TDD_Assignment"
	fname ="port-harcourt-weather.txt"
	"""docstring for ClassName"""
	def filePath(self, fname):

		if os.path.isfile(fname):
		    print fname
		else:
		    print "no such file"

	def tempDiff(self, fname):
		with open(fname) as newfile:
			next(newfile)
			next(newfile)
			dayKey = []
			dailyTempDiff = []
			for line in file:
				#print line
				splitted_line = line.split()
				
				#if isinstance(splitted_line[0]): #		
				#print splitted_line[0], splitted_line[1], splitted_line[2]
				try:
					dayKey.append(int(splitted_line[0]))
				
					try: 									#to catch error

						dailyHigh = int(splitted_line[1]) #to cast to integer
						dailyLow = int(splitted_line[2])
						#print int(splitted_line[0])

					except:									#to pass command to the next line
						pass
				except:
					pass
				dailyTempDiff.append(dailyHigh - dailyLow) #to subtract dailylow from dailyHigh and save it inside dailyTempSpread				
		weatherDict = dict (zip(dayKey, dailyTempDiff))
			
		print weatherDict

		tempDiff()