importshapefile
fbi = shapefile.Reader("E:\KULIAH\Semester 5\Sistem Informasi Geografis\Countries\ptry.shp")
shape = fbi.shapes()
print len (shapes)