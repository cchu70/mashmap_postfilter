# This script calculates the mapQ based on the same procedure as minimap2 (Heng Li), but uses the number of shared kmers
# mapQsck = 1 - f2/f1
# Where fi is the number of shared unique kemrs between a read and its alignment i. For each read, we only consider the first (f1) and second best (f2)
import sys
import os.path


class TopTwo:

	best = None
	second_best = None

	def add(self, align_data):
		if (best == None):
			self.best = align_data
		elif (align_data.greaterThan(best)):
			self.second_best = self.best
			self.best = align_data
		elif (align_data.greaterThan(second_best)):
			self.second_best = align_data
		#####
	#####

	def __init__(self, align_data_A, align_data_B=None):

		if (align_data_A.greaterThan(align_data_B)):
			self.best = align_data_A
			self.second_best = align_data_B
		else:
			self.best = align_data_B
			self.second_best = align_data_A
		#####
#####

class AlignData:
	sck_count = 0
	data = ""

	def __init__(self, data_string, sck_count):
		self.sck_count = sck_count
		self.data = data_string
	#####

	def greaterThan(self, align_data):
		if (align_data == None):
			return True
		else:
			return self.sck_count > align_data.sck_count 
		#####
	#####
#####



def main():

	# Get the file with the read, the alignment, original mapping score, and the number of shared unique kmers

	map_sck_counts = sys.argv[1]

	if (not os.path.isfile(map_sck_counts)):
		sys.stderr.write("%s does not exist" % map_sck_counts)
		assert false
	#####
	read_name_idx = int(sys.argv[2])
	sck_count_idx = int(sys.argv[3])

	# For each read, get the top two alignments if there are at least 2, else just take the only one

	alignments = {}

	for line in open(map_sck_counts, "r"):
		# Dictionary of reads maintains queue of the sck alignment scores for each read
		data = line.split()
		read_name = data[read_name_idx]
		sck_count = data[sck_count_idx]
		align_data = AlignData(data, sck_count)

		try:
			alignments[read_name].add(align_data)
		except:
			alignments[read_name] = TopTwo(align_data)
		#####
	#####

	for read_name in alignments:
		print(read_name)
		if (alignments[read_name].second_best):
			print("First best: " % alignments[read_name].best.sck_count)
			print("Second best: " % alignments[read_name].second_best.sck_count)







if __name__ == "__main__": main()