# Bike Rent Analysis ✨

## Question and Answer
1. Kapan musim dengan jumlah penyewaan sepeda tertinggi?
   Musim penyewaan sepeda tertinggi secara keseluruhan berada pada musim summer, dimana pada musim tersebut juga merupakan musim dengan feeling temprature rataan tertinggi
2. Bagaimana faktor lingkungan yang mempengaruhi jumlah penyewaan sepeda bulanan?
   Faktor lingkungan mempengaruhi jumlah penyewaan sepeda bulanan lewat pengaruh feeling tempraturenya, diamana dengan kenaikan feeling temprature membuat penyewaan sepeda akan meningkat, begitupun sebaliknya.
3. Bagaimana pengkategorian jumlah penyewaan sepeda bulanan akibat pengaruh faktor lingkungan?
   Pengkategorian jumlah penyewaan bulanan akibat pengaruh faktor lingkungan (feeling temprature), menghasilkan bulan berkategori penyewaan rendah di awal tahun (Jun, Feb), Bulan berkategori penyewaan sedang di      awal-tengah tahun dan akhir tahun (Mar, Apr, Nov, Des), serta bulan berkategori penyewaan tinggi di pertengahan tahun (Mei, Jun, Jul, Agu, Sep, Okt)
4. Bagaimana perbandingan jumlah penyewaan musiman sepeda di hari kerja dan hari libur untuk kedua jenis user?
   Secara keseluruhan jumlah penyewaan sepeda pada hari kerja selalu lebih tinggi dari pada hari non-kerja di tiap musimnya. Pada hari-hari kerja total penyewa sepeda untuk registered user sebesar 86.8% dan
   casual user sebesar 13.2%. Sedangkan untuk hari non-kerja (hari libur dan weekend), untuk registered user sebesar 68.3% dan casual user sebesar 31.7%. Hal ini menunjukan dominansi penyewa merupakan registered
   user yang menyewa sepeda terutama pada hari-hari kerja, dan sebagiannya akan tidak melakukan penyewaan pada hari libur.

## Setup environment
```
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

## Run steamlit app
```
streamlit run stremlit_bike_rent.py
or
python -m streamlit run stremlit_bike_rent.py
```
## tautan untuk dashboard steamlit app
https://bike-rent-app-badqhwkvcyre5ejwb8zlvo.streamlit.app/

![Alt text](image.png)
![Alt text](image-1.png)
