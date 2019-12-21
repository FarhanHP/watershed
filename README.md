# WATERSHED : VINCENT-SOILLE ALGORITHM

Ini adalah bagian kecil dari implementasi Transformasi Immersion Watershed versi algoritma Vincent-Soille. Adapun bagian yang luput dari implementasi yang saya buat adalah, grayscale-pixels-nya tidak berdasarkan pada gambar nyata melainkan menggunakan numpy random list2d yang dianggap sebagai gambar dengan grayscale pixels.

Dalam implementasi yang saya buat, saya membut dua Class yaitu Pixel, dan ImageGrayscale. Pixel memiliki atribut seperti nilai grayscale, label, dan list yang berisi 8-Connectivity-Neighboring-Pixels, sedangkan ImageGrayscale memiliki atribut kumpulan pixel yang berbentuk list2d. Selain itu juga, dalam Class ImageGrayscale memiliki method yang bernama watershedVS yang bertugas memberikan label pada tiap pixel berdasarkan definisi Immersion Watershed. Setiap pixel yang masuk ke dalam basin diberi label "A, B, C, dst", sedangkan untuk pixel yang merupakan watershed diberi label "-".

Adapun penjelasan bagaimana method watershedVS bekerja adalah sebagai berikut:
  
  1.) Urutkan semua pixel berdasarkan nilai grayscale-nya dari yang terkecil sampai yang terbesar.
  
  2.) Tentukan nilai threshold yang merupakan nilai grayscale terkecil dari pixel yang ada.
  
  3.) Masukkan pixel yang nilai grayscale-nya sama dengan threshold ke dalam antrian FIFO.
  
  4.) Ambil(pop) pixel yang ada di dalam antrian :
         p <- antrian.pop().
         Q <- himpunan pixel tetangga dari p.
         tambahkan Q ke dalam antrian.
         pada setiap Q, periksa label masing-masing anggota Q:
            jika terdapat >1 jenis label basin, maka label p adalah watershed.
            jika terdapat 1 jenis label basin, maka label p adalah sama dengan label tersebut(p menjadi bagian suatu basin).
            jika terdapat 0 jenis label basin, maka label p adalah label basin yang baru (p menjadi basin baru).
  
  5.) Jika panjang antrian > 0 maka kembali ke step-4, sebaliknya maka lanjut ke step-6.
  
  6.) threshold <- threshold + 1.
  
  7.) jika nilai treshold <= nilai grayscale paling besar, maka kembali ke step-3. Jika sebaliknya, maka berhenti.
         
            
