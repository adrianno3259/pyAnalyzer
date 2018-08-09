import argparse
import os
import timeit


class AnalyzerParser:

	def __init__(self):
		
		self._parser = argparse.ArgumentParser()
		
		self._parser.add_argument("-p", help='sets the target program')
		self._parser.add_argument("-n", help='number of times the program will be executed', type=int)
		self._parser.add_argument("-v", "--verbosity", help='set log verbosity', type=int)
		self._parser.add_argument("-i", help='inputs')
		self._parser.add_argument("-a", "--save-average", help='set a file to save the average execution time')
		

	def get_args(self):

		return self._parser.parse_args()

def main():

	parser = AnalyzerParser()
	args = parser.get_args()

	print(args.i)

	number_of_runs = 5
	command = 'import os\nos.system("./'
		
	if(not args.p):
		print("Error: no program name detected")
		exit(1)
	else:
		command += args.p + '")'

	if(args.n):
		number_of_runs = args.n

	execution_time = timeit.timeit(command, setup="import os", number=number_of_runs)

	print("Finished execution...")
	print("Number of program runs: " + str(number_of_runs))
	print("Average elapsed time: " + str(execution_time / number_of_runs))

if __name__ == '__main__':
	main()