# Projek-DL
# Sentiment Analysis Ulasan Aplikasi Honor of King (Google Play Store)

## 📌 Latar Belakang
Perkembangan teknologi digital dan internet telah mendorong pertumbuhan interaksi digital yang sangat pesat, terutama pada platform distribusi aplikasi mobile seperti Google Play Store. Ulasan yang ditinggalkan oleh pengguna mengandung opini dan evaluasi pengalaman nyata terhadap aplikasi yang digunakan, sehingga menjadi sumber data kualitatif penting untuk menilai kepuasan pengguna serta permasalahan yang dialami. Namun, volume ulasan yang sangat besar menyulitkan analisis manual karena memerlukan waktu, tenaga, serta konsistensi yang tinggi (Alfatah, 2024).

Dalam konteks aplikasi mobile populer seperti Honor of King, ribuan ulasan pengguna yang tersedia di Play Store memiliki ragam sentimen yang berbeda-beda — dari ulasan positif, netral, hingga negatif — yang mencerminkan persepsi pengguna terhadap kualitas pengalaman bermain dan fitur aplikasi itu sendiri. Variasi ini menunjukkan kompleksitas bahasa dan ekspresi dalam ulasan yang tidak mudah ditangani secara tradisional tanpa dukungan teknik otomatis (Dhendra & Utomo, 2025).

Untuk mengatasi permasalahan tersebut, analisis sentimen menjadi teknik komputasi utama dalam Natural Language Processing (NLP) yang bertujuan untuk mengklasifikasikan teks berdasarkan polaritas sentimen seperti positif, netral, dan negatif. Teknik ini telah digunakan secara luas dalam penelitian terbaru untuk menganalisis opini pengguna pada media sosial maupun ulasan aplikasi mobile, termasuk pendekatan berbasis LSTM dan Transformer yang menunjukkan kemampuan untuk menangkap konteks bahasa alami dengan lebih akurat dibandingkan metode klasik seperti Naïve Bayes atau SVM (Malasari & Ramli, 2025).

Dalam beberapa tahun terakhir, teknik deep learning dan model Transformer telah menunjukkan performa yang unggul dalam tugas analisis sentimen dan ekstraksi fitur konteks teks. Model seperti BERT dan turunannya, termasuk IndoBERT yang dilatih khusus untuk bahasa Indonesia, telah berhasil mengungguli pendekatan konvensional dalam klasifikasi ulasan berbahasa Indonesia dalam berbagai domain aplikasi digital. Penelitian benchmarking terbaru menunjukkan bahwa model ini memiliki akurasi dan F1-score yang lebih tinggi dibandingkan model Bi-LSTM dan model klasik lainnya (Dhendra & Utomo, 2025).

Berdasarkan latar belakang tersebut, proyek ini bertujuan untuk melakukan analisis sentimen ulasan pengguna aplikasi Ludo King yang diambil dari Google Play Store dengan fokus pada bahasa Indonesia. Proyek ini membandingkan performa beberapa model yaitu IndoBERT baseline, Bi-LSTM, dan IndoBERT yang dioptimasi, guna mengetahui model yang paling efektif dalam mengklasifikasikan sentimen ulasan pengguna. Hasil penelitian diharapkan dapat memberikan gambaran yang lebih komprehensif mengenai efektivitas penggunaan model deep learning dalam analisis sentimen berbahasa Indonesia serta kontribusi terhadap pengembangan sistem analisis opini otomatis di bidang industri perangkat lunak dan evaluasi aplikasi digital (Alfatah, 2024; Dhendra & Utomo, 2025).

---

## ⚙️ Pemrosesan Data

### 1. Pengambilan Data (Scraping)
Data ulasan diperoleh dari Google Play Store menggunakan library `google-play-scraper`. Parameter scraping yang digunakan:
- Aplikasi: Honor of King (`com.levelinfinite.sgameGlobal`)
- Bahasa: Indonesia
- Negara: Indonesia
- Jumlah data: ±10.000 ulasan terbaru

Data hasil scraping disimpan dalam format `.csv`.

### 2. Pelabelan Sentimen
Pelabelan sentimen dilakukan secara otomatis berdasarkan rating bintang:
- Rating 4–5 → Positif
- Rating 3 → Netral
- Rating 1–2 → Negatif

Pendekatan ini dikenal sebagai *weak labeling* karena label diturunkan dari rating pengguna.

### 3. Data Cleaning & Preprocessing
Tahapan preprocessing yang dilakukan meliputi:
- Menghapus mention, hashtag, URL, dan simbol
- Menghilangkan karakter berulang
- Menghapus angka dan tanda baca
- Mengubah teks menjadi huruf kecil (*lowercase*)

Hasil preprocessing digunakan sebagai input model.

---

## 🤖 Model

Pada proyek ini digunakan satu pendekatan model untuk analisis sentimen:
### 1. IndoBERT Optimized
- Model: `indobenchmark/indobert-base-p2`
- Epoch: 10
- Learning rate: 2e-5
- Split data: 90% data latih, 10% data uji

Model ini digunakan untuk mendapatkan performa terbaik melalui fine-tuning yang lebih optimal.

---

## 📊 Hasil

Evaluasi model dilakukan menggunakan metrik:
- Accuracy
- Precision
- Recall
- F1-Score

Hasil eksperimen menunjukkan bahwa:
- **Model IndoBERT Optimized memberikan performa terbaik**
- Model berbasis Transformer unggul dibandingkan Bi-LSTM dalam memahami konteks bahasa Indonesia
- Bi-LSTM tetap mampu melakukan klasifikasi sentimen namun dengan akurasi lebih rendah

---

## 📚 Sitasi
- Alfatah, D. (2024). Application of Transformer Model for Sentiment Detection on Indonesian Twitter Data. Jurnal Komputer, 2(2).

- Dhendra & Utomo, V. G. (2025). Benchmarking IndoBERT and Transformer Models for Sentiment Classification on Indonesian E-Government Service Reviews. Jurnal Transformatika, 23(1).

- Malasari, N. & Ramli, M. (2025). Analisis Sentimen Media Sosial Menggunakan Algoritma BERT dan LSTM. Journal of Computer Science and Information Technology.

- Widyananda et al. (2025). Machine Learning and Transformer-based Model for Sentiment Analysis of Indonesian E-Commerce Reviews. The Indonesian Journal of Computer Science.
  
- Google Play Scraper  
  https://github.com/JoMingyu/google-play-scraper

- IndoBERT  
  https://huggingface.co/indobenchmark/indobert-base-p2

- Hugging Face Transformers  
  https://huggingface.co/docs/transformers
