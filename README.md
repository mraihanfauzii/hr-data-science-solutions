# Proyek Analisis Attrition Karyawan – PT Jaya Jaya Maju

## Business Understanding

PT Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Perusahaan ini memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri dan saat ini sedang menghadapi suatu masalah yaitu tingginya attrition (turnover karyawan) yang berdampak negatif pada kinerja perusahaan. Tingginya tingkat pengunduran diri karyawan menyebabkan kehilangan tenaga kerja berpengalaman, peningkatan biaya rekrutmen/pelatihan, serta potensi menurunnya moral dan produktivitas tim. Manajemen menyadari bahwa diperlukan langkah proaktif untuk memahami pola attrition dan faktor-faktor penyebabnya, agar dapat merumuskan strategi efektif dalam mempertahankan karyawan berharga.

### Permasalahan Bisnis

Permasalahan bisnis utama yang hendak diselesaikan adalah menurunkan tingkat attrition karyawan yang tinggi di PT Jaya Jaya Maju. Beberapa pertanyaan utama yang ingin dijawab meliputi:

* Siapa saja kelompok karyawan yang paling rentan meninggalkan perusahaan? (berdasarkan usia, status pernikahan, jabatan, departemen, dll.)
* Faktor-faktor apa yang paling berpengaruh terhadap keputusan karyawan untuk keluar (lembur, gaji, masa kerja, dan sebagainya)?
* Apakah dapat dibangun model prediksi sederhana untuk mengidentifikasi karyawan berisiko tinggi attrition sehingga dapat dilakukan intervensi dini?
* Tindakan apa yang dapat diambil perusahaan (terutama oleh HR dan manajemen) untuk meningkatkan retensi karyawan ke depannya?

### Cakupan Proyek

Cakupan proyek ini meliputi analisis menyeluruh terhadap data historis karyawan PT Jaya Jaya Maju guna mengidentifikasi pola attrition dan faktor-faktor penyebabnya, pembuatan dashboard bisnis interaktif sebagai alat monitoring dan insight, pembangunan model machine learning sederhana untuk memprediksi attrition, serta rekomendasi tindakan strategis. Secara spesifik, langkah-langkah proyek mencakup:

* Data understanding & preparation: Mengumpulkan dan membersihkan data HR (profil demografi, data ketenagakerjaan, riwayat kerja, dan penanda apakah karyawan keluar atau tetap).
* Exploratory data analysis(Univariate & Multivariate): Mengolah data untuk menemukan hubungan antara variabel (usia, gender, departemen, jabatan, lembur, pendapatan, masa kerja, dll.) dengan status attrition.
* Business dashboard development: Membuat dashboard yang menyajikan metrik attrition dan visualisasi penting untuk membantu pemangku kepentingan memahami kondisi secara cepat.
* *Modeling*: Membangun model prediksi sederhana untuk mengidentifikasi kemungkinan attrition berdasarkan faktor-faktor tertentu.
* Evaluation & insight: Mengevaluasi hasil analisis dan model, menginterpretasikan temuan utama.
* Recommendations: Menyusun rekomendasi action items bagi manajemen HR untuk menekan attrition.

Batasan proyek: Analisis difokuskan pada data internal perusahaan Jaya Jaya Maju saja (belum mencakup benchmarking eksternal). Implementasi program retensi di luar lingkup proyek (tugas tim manajemen), sementara proyek ini fokus pada penyediaan insight data-driven.

### Persiapan

Sumber data: Dataset HR karyawan PT Jaya Jaya Maju [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).

Data terdiri dari 1.470 entri karyawan dengan 35 fitur, mencakup informasi demografis, jabatan, kepuasan kerja, kinerja, dan kolom target *Attrition* (0 = bertahan, 1 = keluar). Contoh fitur: `Age` (usia), `Department` (departemen), `JobRole` (jabatan), `MaritalStatus` (status pernikahan), `MonthlyIncome` (gaji bulanan), `OverTime` (lembur), `YearsAtCompany` (masa kerja di perusahaan), `YearsInCurrentRole` (masa dalam jabatan saat ini), dll.

Setup environment: Proyek dianalisis menggunakan bahasa Python dalam lingkungan Jupyter Notebook. Untuk mengaksesnya :

* Setup conda environment:

    ```
    conda create --name datascience-human-resources python==3.11.12
    ```
* Install requirements:
    ```
    pip install -r requirements.txt
    ```
* Setup metabase:
    ```
    docker pull metabase/metabase:v0.46.4
    docker run -p 3000:3000 --name metabase metabase/metabase
    ```
    Akses metabase pada http://localhost:3000/setup dan lakukan setup.
* Setup database (supabase):

    * Buat akun dan login https://supabase.com/dashboard/sign-in.
    * Buat project
    * Copy URI pada database setting
    * Kirim dataset menggunakan sqlalchemy 
    ```python
    from sqlalchemy import create_engine
 
    URL = "DATABASE_URL"
    
    engine = create_engine(URL)
    df.to_sql('orders', engine)
    ```

## Business Dashboard

Untuk memudahkan pemantauan dan komunikasi insight, telah dibuat business dashboard interaktif yang menampilkan metrik attrition karyawan dan visualisasi penting. Dashboard ini dirancang agar tim HR dan manajemen dapat secara cepat mengidentifikasi pola attrition menurut berbagai dimensi dan melakukan *drill-down* pada area yang membutuhkan perhatian.

<img src="https://raw.githubusercontent.com/mraihanfauzii/hr-data-science-solutions/main/images/mraihanfauzi-dashboard.png" width="500">

Dengan adanya business dashboard ini, diharapkan tim HR dapat memantau kesehatan organisasi secara berkelanjutan, mengidentifikasi tren attrition secara dini, dan mengevaluasi efektifitas kebijakan HR (seperti perubahan aturan lembur atau program kesejahteraan) melalui data real-time.

## Conclusion

Berdasarkan analisis data karyawan PT Jaya Jaya Maju, dapat disimpulkan beberapa temuan utama terkait attrition dan faktor-faktor yang memengaruhinya:

* Tingkat Attrition Keseluruhan: Perusahaan mengalami attrition sebesar \~16% selama periode data. Angka ini termasuk tinggi dan menjadi indikasi perlunya perbaikan strategi retensi. 

<img src="https://raw.githubusercontent.com/mraihanfauzii/hr-data-science-solutions/main/images/attrition_by_age_group.png" width="500">

* Pengaruh Usia: Karyawan berusia 25-34 rentan meninggalkan perusahaan dengan attrition tertinggi. Kemudian yang terbanyak ke 2 ada di rentang 35-44 kemudian rentang <25 lalu rentang 45-54 lalu 55+. Karyawan yang lebih tua yaitu berusia 35+ cenderung lebih stabil bertahan begitupun dengan rentang 25 kebawah. Hal ini mungkin disebabkan oleh karyawan pada rentang 25-34 yang menginginkan kenaikan karir di tempat lain, sedangkan karyawan senior lebih menetap dan karyawan muda yaitu <25 ingin mencari pengalaman terlebihi dahulu.

<img src="https://raw.githubusercontent.com/mraihanfauzii/hr-data-science-solutions/main/images/multivariate_marital_status.png" width="500">

* Status Pernikahan: Karyawan lajang memiliki proporsi turnover paling besar jika dibandingkan dengan persentasenya dengan yang menetap bila dibandingkan dengan karyawan yang bercerai dan yang telah menikah. Ini selaras dengan profil usia – banyak karyawan lajang yang lebih muda dan mobile. Implikasinya, status pernikahan (yang berkaitan dengan tanggung jawab keluarga dan kebutuhan stabilitas) berhubungan dengan loyalitas karyawan.

<img src="https://raw.githubusercontent.com/mraihanfauzii/hr-data-science-solutions/main/images/multivariate_overtime.png" width="500">

* Beban Kerja (Lembur): Overtime (lembur) muncul sebagai salah satu faktor kunci attrition. Data menunjukkan karyawan yang sering lembur jauh lebih mungkin keluar jika dibandingkan dengan yang tidak overtime. Kelebihan jam kerja yang berlebihan dapat menyebabkan burnout atau ketidakpuasan work-life balance, mendorong karyawan mencari pekerjaan dengan kondisi lebih baik. Fakta ini menggarisbawahi pentingnya keseimbangan kerja-kehidupan bagi retensi.

<img src="https://raw.githubusercontent.com/mraihanfauzii/hr-data-science-solutions/main/images/multivariate_job_role.png" width="500">

* Peran/Jabatan: Terdapat disparitas attrition signifikan antar Job Role. Peran di lini penjualan mengalami attrition tertinggi khususnya Sales Representative yang turnover-nya \~40%. Peran teknis level junior seperti Laboratory Technician juga cukup tinggi attrition-nya. Sebaliknya, jabatan manajerial dan spesialis senior (Manager, Director) memiliki attrition sangat rendah. Hal ini menandakan bahwa level jabatan dan mungkin jenjang karir/penghargaan berbeda antar peran. Posisi entry-level atau frontline mungkin kurang puas dengan prospek karir atau beban target, sehingga lebih mudah keluar dibanding posisi senior yang sudah mapan.

<img src="https://raw.githubusercontent.com/mraihanfauzii/hr-data-science-solutions/main/images/multivariate_department.png" width="500">

* Departemen: Sejalan dengan temuan jabatan, Departemen Sales (yang berisi banyak Sales Rep/Sales Exec) menyumbang proporsi terbesar dari karyawan keluar. Departemen R\&D mempunyai attrition mendekati rata-rata (masih perlu perhatian namun tidak setinggi Sales), sementara Departemen HR walau kecil, menunjukkan persentase attrition yang tidak bisa diabaikan. Ini mengindikasikan perlunya fokus perbaikan terutama pada unit Sales, diikuti R\&D, untuk menurunkan angka turnover.

<img src="https://raw.githubusercontent.com/mraihanfauzii/hr-data-science-solutions/main/images/attrition_by_years_at_company.png" width="500">

* Masa Kerja (Years at Company): Puncak attrition terjadi di kelompok “2–5 tahun” dengan total sekitar 65 karyawan yang keluar. Kelompok “<2 tahun” menempati urutan kedua, sekitar 55 karyawan, menunjukkan angka churn yang masih sangat tinggi di masa orientasi dan early-career. Setelah itu semakin lama bekerja diperusahaan maka tingkat attritionnya semakin rendah. Risiko keluar paling tinggi terjadi di fase 0–5 tahun, terutama antara tahun ke-2 hingga ke-5. Program retensi dan engagement paling efektifnya difokuskan pada karyawan baru dan mereka di early-career (0–5 tahun) untuk menurunkan angka attrition.

<img src="https://raw.githubusercontent.com/mraihanfauzii/hr-data-science-solutions/main/images/attrition_by_monthly_income.png" width="500">

* Pendapatan: Tingkat pendapatan memiliki korelasi terbalik dengan attrition. Karyawan berpenghasilan rendah (misal termasuk 20% terbawah secara gaji) lebih sering keluar, kemungkinan karena faktor finansial – baik merasa gaji kurang kompetitif maupun mendapatkan tawaran lebih tinggi di luar. Sebaliknya, karyawan dengan gaji lebih tinggi cenderung bertahan. Ini memberi sinyal bahwa kebijakan kompensasi dan benefit yang adil sangat krusial untuk retensi, terutama bagi staf level junior.

* Model Prediksi Attrition: Sebagai bagian dari proyek, telah dibangun sebuah model machine learning sederhana untuk memprediksi kemungkinan attrition seorang karyawan. Model Regresi Logistik yang dilatih berhasil mencapai akurasi sekitar 84% dalam mengklasifikasikan apakah karyawan akan keluar atau bertahan. Meskipun peningkatannya marginal, model ini memberikan insight fitur-fitur terpenting yang berkontribusi pada attrition. Faktor “OverTime” muncul sebagai variabel prediktor terkuat, diikuti oleh YearsAtCompany, Age, dan JobRole tertentu sebagai faktor penting. Artinya, model menegaskan temuan analisis: pola lembur, masa kerja, usia, dan jenis pekerjaan karyawan dapat digunakan untuk mengidentifikasi siapa yang berisiko tinggi. Model ini dapat dikembangkan lebih lanjut untuk membantu HR melakukan deteksi dini (early warning) karyawan berisiko, sehingga intervensi dapat dilakukan sebelum mereka memutuskan resign.

Secara keseluruhan, proyek analisis ini berhasil mengungkap bahwa attrition karyawan dipengaruhi oleh kombinasi faktor demografis, pekerjaan, dan lingkungan kerja. Tidak ada satu penyebab tunggal – melainkan interaksi beberapa hal seperti kelompok usia muda yang banyak lembur dalam peran tertentu dengan gaji rendah akan sangat rawan meninggalkan perusahaan. Insight dari data ini memberikan dasar yang kuat bagi manajemen untuk merancang strategi retensi yang lebih tepat sasaran.

### Rekomendasi Action Items

Berdasarkan temuan di atas, dapat direkomendasikan beberapa langkah tindakan bagi perusahaan PT Jaya Jaya Maju untuk menurunkan attrition dan meningkatkan retensi karyawan:

* Tingkatkan Keseimbangan Kerja-Kehidupan: Kurangi budaya lembur berlebihan. Manajemen dapat mengevaluasi beban kerja dan memastikan tenaga kerja cukup sehingga tugas lembur tidak terus-menerus dibebankan pada individu tertentu. Pertimbangkan kebijakan fleksibilitas jam kerja atau penambahan staf di divisi dengan beban tinggi (misalnya Sales) untuk mencegah burnout. Program wellness dan manajemen stres juga dapat membantu meningkatkan work-life balance.

* Program Onboarding dan Mentorship: Karena banyak karyawan keluar di masa 0-5 tahun kerja, perkuat proses onboarding agar karyawan baru merasa terintegrasi dan didukung. Tinjau kembali ekspektasi pekerjaan yang disampaikan saat rekrutmen agar sesuai realita, sehingga mengurangi risiko kekecewaan karyawan baru. Kemudian untuk karyawan rentang 2-5 tahun dapat dipertimbangkan untuk naik jabatan atau kenaikan gaji. 

* Pengembangan Karir dan Peluang Promosi: Untuk mencegah attrition di kalangan karyawan muda/lajang yang haus peningkatan karir, sediakan jalur karir yang jelas. Perusahaan bisa meningkatkan frekuensi pelatihan, program rotasi jabatan, atau percepatan promosi bagi yang berprestasi. Dengan melihat prospek karir internal yang baik, karyawan cenderung bertahan lebih lama daripada mencari peluang di luar.

* Tinjau Kebijakan Kompensasi: Lakukan review struktur gaji dan benefit, terutama bagi kelompok jabatan dan level junior yang pendapatannya relatif rendah. Pastikan gaji kompetitif dengan pasar untuk mengurangi dorongan pindah karena alasan finansial. Selain gaji, pertimbangkan peningkatan benefit lain (asuransi, bonus, penghargaan kinerja) yang dapat meningkatkan kepuasan karyawan secara keseluruhan.

* Intervensi pada Jabatan/Departemen Berisiko: Fokuskan upaya retensi pada peran dan unit dengan turnover tertinggi. Misalnya, untuk tim Sales, pertimbangkan perbaikan skema insentif atau beban target yang realistis, peningkatan dukungan penjualan, serta pembinaan karir agar peran ini lebih menarik sebagai pilihan jangka panjang. Untuk posisi Laboratory Technician atau staf teknis muda, mungkin diperlukan program peningkatan keterampilan atau alur promosi ke posisi lebih senior agar mereka melihat masa depan di perusahaan.

* Meningkatkan Keterikatan Karyawan (Engagement): Inisiatif engagement seperti survey kepuasan kerja rutin dan exit interview yang mendalam dapat membantu memahami alasan spesifik karyawan keluar. Gunakan masukan tersebut untuk melakukan perbaikan internal. Selain itu, kegiatan yang membangun kebersamaan (outing, team building) dan budaya kerja yang apresiatif akan meningkatkan loyalitas, terutama bagi karyawan lajang yang bisa mendapat sense of belonging lebih kuat di perusahaan.

* Penggunaan Analytics Berkelanjutan: Integrasikan model prediksi attrition ke dalam proses manajemen HR. Misalnya, buat sistem peringatan dini yang menandai karyawan dengan profil berisiko (sering lembur, kinerja bagus tapi gaji rendah, dll.) agar HR bisa melakukan retention talk atau menawarkan penyesuaian sebelum terlambat. Secara umum, manfaatkan dashboard dan data analytics secara berkelanjutan untuk memonitor tren attrition tiap kuartal. Evaluasi efektivitas tiap action item secara data-driven (misal, apakah setelah perbaikan kebijakan lembur, attrition menurun?).

Dengan melaksanakan langkah-langkah di atas secara konsisten, PT Jaya Jaya Maju diharapkan dapat menurunkan tingkat attrition karyawan secara signifikan. Hasil akhirnya adalah tenaga kerja yang lebih stabil, termotivasi, dan loyal, sehingga perusahaan dapat mempertahankan pengetahuan dan keahlian di internal, mengurangi biaya turnover, serta mendorong kinerja dan pertumbuhan bisnis jangka panjang.
