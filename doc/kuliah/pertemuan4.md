<img src="../../img/gambar1.jpg" width="200" height="400">
<p align="center">
<br>
Retrieve data geospasial adalah meretrieve data vector
<br>
Data shape file => .shp
<br>
Operasi retrieve data menggunakan library phyton yang bernama py.shp
<br>
<br>
Shape file yang merupakan standar file
<br>
Vektor geospasila adalah data yang dikeluarkan secara resmi oleh ESRI
<br>
<img src="../../img/gambar2.jpg" width="200" height="400">
<p align="center">
<br>
Data Geometri adalah Data koordinat yang membentuk bangun datar/ruang diantaranya
<br>
1.	Point/titik, yang memiliki nomor standar [1]
<br>
2.	Line/polyline/garis, yang memiliki nomor standar [3] 
<br>
3.	Polygon, yang memiliki nomor standar [5]
<br>
Inilah yang dimaksud data shapefile oleh ESRI yang memiliki nomor standard 
<br>
<br>
Operasi Pengambilan Data
<br>
Library pyshp class shapefile
<br>
<br>
Cara membaca
<br>
1.	Buka/Baca 
<br>
2.  SF = Shapefile.reader (“btsnegara.shp”)
<img src="../../img/gambar3.jpg" width="200" height="400">
<p align="center">
<br>
<br>
Method SHp
<br>
Shapes()
<br>
Shape(n) , n adalah nomor record (bbox, parts, points, shapefile)
<br>
-	Bbox -> bording box, merupakan batas view peta 
<br>
<img src="../../img/gambar4.jpg" width="200" height="400">
<p align="center">
<br>
Koordinat A,B,C,D itu disebut bbox 
<br>
<br>
-	Part -> points ini bagian dari record lain/pecahan record
<br>
-	Points -> koordinat membentuk peta
<br>
-	Shap type -> jenis geometri dari points 
<br>
<br>
Method DBF
<br>
Fields -> nama field/colom
<br>
Record(n) -> n adalah nomor sequence record 
<br>
Records()
<br>
Membuat class pada retrieve
<br>
<img src="../../img/pertama.jpg" width="200" height="400">
<p align="center">
<br>
Menampilkan select negara 
<br>
<img src="../../img/kedua.jpg" width="200" height="400">
<p align="center">
<br>
