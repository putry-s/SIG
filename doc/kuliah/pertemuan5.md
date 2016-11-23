MEMBUAT DATA GEOSPASIAL
MENBACA DATA
<img src="../../img/gis.jpg" width="200" height="400">
<p align="center">
<br>
Membaca menggunakan library pyshp. Kita akan membuat file baru bernama anu.shp beserta anu.dbf
<br>
Langkah-langkah :
<br>
1.	Import shape file
<br>
2.	Instansiasi writer method.
<br>
Sf=shapefile.writer(param)
<br>
<br>
<br>
Dimana param adalah pilih :
<br>
Shapetype = 1
<br>
Shapetype = 3
<br>
Shapetype = 5
<br>
3.	Sama seperti rend kita
<br>
Lakukan metode dbf dan shp 
<br>
<br>
SHP
Untuk menmbahkan record tambahan tergantung typenya.
<br>
1.Sf.point (x,y)
<br>
3.sf.line (parts {x,y},{z,w},…}).
<br>
6.sf.line (parts{x,y},{z,w},…}).
<br>
<br>
Dbf
<br>
1.	Membuat atribut terlebih dahulu, menambahkan record. 
<br>
Contoh :
<br>
Sf.field(‘Namafield’,’C’,’40’) 
<br>
Dimana C adalah character, srtinya nama atribut, nama field dengan 40 karakter.
<br>
2.	Untuk menmbahkan record 
<br>
Sf.record(‘Bandung’,’sarajida’)
<br>
Selesai maka simpan 
<br>
Sf.save(‘namafield.shp’)
<br>
<br>
<br>
Contoh script membuat shapefile.shp
<br>
<br>
Masuk phyton
<br>
<br>
<br>
<img src="../../1a/gis.jpg" width="200" height="400">
<p align="center">
EDITING
<br>
Sf.shapefile.editor (param)
<br>
Dimana param d=nama/letak file.
<br>
Contoh :
<br>
Sf.shapefile.editor(shapefile=’warteg.shp’)
<br>
<br>
Operasi
<br>
Shp
<br>
<br>
Sf.poly()
<br>
Sf.line()
<br>
Sf.point()
<br>
<br>
Sf.delete(n) 
<br>
Dimna n adalah baris ke n dari table 
<br>
<br>
Dbf
<br>
Sf.record()
<br>
Sf.save(‘namafile’)
<br>

