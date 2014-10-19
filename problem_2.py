gis_file = open ("GIS_is_the_best.txt",'r')
file_list = gis_file.read()

system_count = 0
science_count = 0
geographic_count = 0
information_count = 0
other_count = 0
total_words = 0

for word in file_list.split(' '):
	if word.lower() == 'systems':
		system_count += 1
	elif word.lower() == 'science':
		science_count += 1
	elif word.lower() == 'geographic':
		geographic_count += 1
	elif word.lower() == 'information':
		information_count += 1
	else:
		other_count += 1
		
print(system_count + science_count + geographic_count + information_count + other_count)
print(system_count)
print(science_count)
