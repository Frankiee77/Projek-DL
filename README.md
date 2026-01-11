# Projek-DL
# Sentiment Analysis Ulasan Aplikasi Ludo King (Google Play Store)

## 📌 Latar Belakang
Perkembangan teknologi digital, khususnya pada sektor aplikasi mobile, mengalami peningkatan yang sangat pesat. Google Play Store sebagai salah satu platform distribusi aplikasi terbesar menyediakan ruang bagi pengguna untuk memberikan ulasan dan penilaian terhadap aplikasi yang mereka gunakan. Ulasan pengguna ini memiliki peran penting karena mencerminkan tingkat kepuasan, keluhan, serta harapan pengguna terhadap kualitas dan kinerja aplikasi.

Aplikasi Ludo King merupakan salah satu permainan mobile yang sangat populer di Indonesia dan telah diunduh oleh jutaan pengguna. Tingginya jumlah pengguna tersebut menyebabkan aplikasi ini menerima ribuan hingga puluhan ribu ulasan. Ulasan-ulasan ini mengandung opini yang beragam, mulai dari ulasan positif terkait keseruan permainan, ulasan netral, hingga ulasan negatif yang berkaitan dengan bug, iklan berlebihan, maupun performa aplikasi. Jumlah ulasan yang sangat besar membuat proses analisis sentimen secara manual menjadi tidak efisien dan membutuhkan waktu yang lama.

Oleh karena itu, diperlukan sebuah pendekatan otomatis untuk menganalisis sentimen ulasan pengguna. Analisis sentimen merupakan salah satu cabang dari Natural Language Processing (NLP) yang bertujuan untuk mengidentifikasi dan mengklasifikasikan opini atau emosi dalam teks ke dalam kategori tertentu, seperti positif, netral, dan negatif. Dengan analisis sentimen, pengembang aplikasi dapat memperoleh gambaran umum mengenai persepsi pengguna terhadap aplikasi secara cepat dan sistematis.

Dalam beberapa tahun terakhir, metode Deep Learning telah banyak digunakan untuk analisis sentimen karena kemampuannya dalam memahami konteks bahasa yang kompleks. Model berbasis Recurrent Neural Network (RNN) seperti Bidirectional Long Short-Term Memory (Bi-LSTM) mampu memproses urutan kata dengan mempertimbangkan konteks dari dua arah. Selain itu, perkembangan model Transformer seperti BERT (Bidirectional Encoder Representations from Transformers) menunjukkan performa yang sangat baik dalam berbagai tugas NLP, termasuk analisis sentimen, terutama ketika menggunakan model yang telah dilatih khusus untuk bahasa tertentu seperti IndoBERT.

Berdasarkan latar belakang tersebut, proyek ini bertujuan untuk melakukan analisis sentimen ulasan pengguna aplikasi Ludo King yang diambil dari Google Play Store menggunakan bahasa Indonesia. Proyek ini membandingkan beberapa pendekatan model, yaitu IndoBERT baseline, Bi-LSTM, dan IndoBERT yang dioptimasi, guna mengetahui model mana yang memberikan performa terbaik dalam mengklasifikasikan sentimen ulasan pengguna. Hasil dari penelitian ini diharapkan dapat memberikan gambaran mengenai efektivitas penggunaan model deep learning dalam analisis sentimen berbahasa Indonesia serta menjadi referensi bagi pengembangan sistem analisis opini otomatis di masa mendatang.

---

## ⚙️ Pemrosesan Data

### 1. Pengambilan Data (Scraping)
Data ulasan diperoleh dari Google Play Store menggunakan library `google-play-scraper`. Parameter scraping yang digunakan:
- Aplikasi: Ludo King (`com.ludo.king`)
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

- Google Play Scraper  
  https://github.com/JoMingyu/google-play-scraper

- IndoBERT  
  https://huggingface.co/indobenchmark/indobert-base-p2

- Devlin et al., 2019. *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.*

- Hugging Face Transformers  
  https://huggingface.co/docs/transformers
