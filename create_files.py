import os

#--------------------------------------
# Fiddle with this to suit
#--------------------------------------

#Base output directory
output_dir 	= "c:\\TESTMIGRATE\\"

#number for each iteration from array below
num_files 	= 1000000

# The set of tests to run - 
# Default is 1MB, 5MB, 10MB, 100MB, 1GB each x num_files
tests		= [1]

#--------------------------------------

def create_file(size, output_file):
	for _ in range (size):
		f = open(output_file, 'ab')
		print ("\t...pushing a random 1MB chunk into " + output_file)
		f.write(os.urandom(1048576))
		f.close()

#--------------------------------------

for test in tests:
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
	for _ in range(num_files):
		output_file = output_dir + "\\file_" + str(test) + str(_) + ".file"
		print "Creating: " + output_file
		create_file(test, output_file)

