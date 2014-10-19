import os
import fileinput
import sys

os.listdir(path) = "/users/xjcasper/desktop/msgst_2015/fall/TGIS_501/labs/lab_3/data/text_files"
filename = open("text_files", "a")

for filename in os.listdir(path):
	if filename.endswith(".text"):
		newname = filename.replace(".text", ".txt")
		os.rename(filename, "file_"+newname)
	elif filename.endswith(".rtf"):
		newname = filename.replace(".rtf", ".txt")
		os.rename(filename, "file_"+newname)
	else:
		newname = filename
		os.rename(filename, "file_"+newname)

print filename.lower()
