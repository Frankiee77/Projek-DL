# Projek-DL
# sentiment-analysis-ludo-king
# Sentiment Analysis Ulasan Aplikasi Ludo King (Google Play Store)

## 📌 Latar Belakang
Aplikasi mobile yang tersedia di Google Play Store menerima ribuan ulasan dari pengguna setiap harinya. Ulasan tersebut mencerminkan tingkat kepuasan pengguna serta menjadi sumber informasi penting bagi pengembang dalam meningkatkan kualitas aplikasi. Namun, jumlah ulasan yang sangat besar menyulitkan analisis secara manual.

Oleh karena itu, proyek ini bertujuan untuk melakukan **analisis sentimen otomatis** terhadap ulasan pengguna aplikasi **Ludo King** menggunakan teknik *Natural Language Processing (NLP)* dan *Deep Learning*. Analisis sentimen ini mengklasifikasikan ulasan ke dalam tiga kelas, yaitu **positif**, **netral**, dan **negatif**, guna mengetahui persepsi pengguna terhadap aplikasi tersebut.

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

Pada proyek ini digunakan tiga pendekatan model untuk analisis sentimen:

### 1. IndoBERT Baseline
- Model: `indobenchmark/indobert-base-p2`
- Epoch: 3
- Split data: 80% data latih, 20% data uji

### 2. Bidirectional LSTM (Bi-LSTM)
- Embedding Layer
- Dua lapisan Bi-LSTM
- Dropout untuk mencegah overfitting
- Dense layer dengan softmax
- Split data: 70% data latih, 30% data uji

### 3. IndoBERT Optimized
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
