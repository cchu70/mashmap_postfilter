# Main script to test the performance of mappers on simulated errors on the reference


import sys
import subprocess


def main():

	# Input files


	GAGE_A = sys.argv[1]
	GAGE_B= sys.argv[2]
	GAGE_A_reads= sys.argv[3]
	GAGE_B_reads= sys.argv[4]

	which_to_error= sys.argv[5]
	which_not_to_error= sys.argv[6]

	error_rate_start = flaot(sys.argv[7])
	error_rate_end = float(sys.argv[8])
	error_rate_step = float(sys.argv[9])

	iterations= int(sys.argv[10])
	
	prefix= sys.argv[11]


	script = sys.argv[12]


	e = error_rate_start
	while e < error_rate_end:
		subprocess.Popen(["/bin/bash", script, GAGE_A, GAGE_B, which_to_error, which_not_to_error, e, iterations, GAGE_A_reads, GAGE_B_reads, prefix])
		e += error_rate_step
	#####









if __name__ == "__main__": main()