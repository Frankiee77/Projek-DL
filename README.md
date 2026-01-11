# Projek-DL
# Sentiment Analysis Ulasan Aplikasi Ludo King (Google Play Store)

## 📌 Latar Belakang
Perkembangan teknologi informasi dan komunikasi telah mendorong pertumbuhan aplikasi mobile secara signifikan. Platform distribusi aplikasi seperti Google Play Store memungkinkan pengguna untuk memberikan ulasan dan penilaian terhadap aplikasi yang mereka gunakan. Ulasan pengguna tersebut berisi opini, pengalaman, serta evaluasi terhadap kualitas aplikasi, sehingga dapat dimanfaatkan sebagai sumber informasi penting bagi pengembang dalam melakukan evaluasi dan peningkatan kualitas layanan aplikasi secara berkelanjutan (Liu, 2012).

Aplikasi Ludo King merupakan salah satu permainan mobile yang sangat populer di Indonesia dengan jumlah pengguna yang sangat besar. Tingginya jumlah pengguna tersebut menyebabkan aplikasi ini menerima ribuan hingga puluhan ribu ulasan yang memiliki variasi sentimen, mulai dari ulasan positif terkait keseruan permainan, ulasan netral, hingga ulasan negatif yang berisi keluhan seperti bug, gangguan sistem, maupun iklan yang berlebihan. Banyaknya jumlah ulasan tersebut membuat proses analisis sentimen secara manual menjadi tidak efisien, memakan waktu, dan rentan terhadap subjektivitas (Zhang et al., 2018).

Untuk mengatasi permasalahan tersebut, diperlukan suatu pendekatan otomatis yang mampu menganalisis opini pengguna dalam jumlah besar secara cepat dan akurat. Analisis sentimen merupakan salah satu cabang dari Natural Language Processing (NLP) yang bertujuan untuk mengidentifikasi dan mengklasifikasikan polaritas sentimen dalam teks ke dalam kategori tertentu, seperti positif, netral, dan negatif. Teknik analisis sentimen telah banyak diterapkan dalam berbagai bidang, termasuk analisis media sosial, evaluasi produk, serta pengukuran kepuasan pengguna aplikasi (Pang & Lee, 2008).

Seiring dengan perkembangan teknologi machine learning, metode deep learning semakin banyak digunakan dalam analisis sentimen karena kemampuannya dalam memahami konteks bahasa yang kompleks. Model Recurrent Neural Network (RNN), khususnya Bidirectional Long Short-Term Memory (Bi-LSTM), mampu memproses informasi teks dari dua arah sehingga lebih efektif dalam memahami hubungan antar kata dalam suatu kalimat (Hochreiter & Schmidhuber, 1997). Selain itu, model berbasis Transformer seperti BERT (Bidirectional Encoder Representations from Transformers) menunjukkan performa yang sangat unggul dalam berbagai tugas NLP karena mampu memahami konteks kalimat secara mendalam melalui mekanisme attention (Devlin et al., 2019).

Berdasarkan latar belakang tersebut, proyek ini bertujuan untuk melakukan analisis sentimen terhadap ulasan pengguna aplikasi Ludo King yang diambil dari Google Play Store dengan fokus pada bahasa Indonesia. Penelitian ini membandingkan performa beberapa pendekatan model, yaitu IndoBERT baseline, Bi-LSTM, dan IndoBERT yang dioptimasi, guna mengetahui model yang paling efektif dalam mengklasifikasikan sentimen ulasan pengguna. Diharapkan hasil dari proyek ini dapat memberikan gambaran mengenai efektivitas penerapan model deep learning dalam analisis sentimen berbahasa Indonesia serta menjadi referensi bagi penelitian dan pengembangan sistem analisis opini otomatis di masa mendatang (Wilie et al., 2020).

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
