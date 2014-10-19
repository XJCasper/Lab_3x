gis_file = open("GIS_is_the_best.txt",'r')
file_list = gis_file.read()

new_file = open("GIS_is_still_the_best.txt", "w+")

for word in file_list.split(" "):
    if word == "Science":
        word = "Systems"
        new_file.write(word + " ")
    elif word == "science":
        word = "systems"
        new_file.write(word + " ")
    else:
        new_file.write(word + " ")

gis_file.close()
new_file.close()
