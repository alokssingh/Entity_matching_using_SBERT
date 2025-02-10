# 🚀 Entity Matching using SBERT

## 📌 Project Overview
This project focuses on **Entity Matching** for **Barclays**, where farm names scraped from an open-source site are cleaned and matched using **Sentence-BERT (SBERT)**. The goal is to accurately link and standardize farm names by leveraging **state-of-the-art NLP techniques**.

```

## 📜 Methodology
1. **Data Collection**: Farm names were scraped from an open-source website.
2. **Data Cleaning**: Preprocessing techniques such as **removing duplicates, lowercasing, and special character removal**.
3. **SBERT Embeddings**: Convert text into meaningful vector representations.
4. **Entity Matching**: Use cosine similarity between embeddings to find the best match.
5. **Evaluation**: Check model accuracy and optimize thresholds for best performance.

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/alokssingh/Entity_matching_using_SBERT.git
cd Entity_matching_using_SBERT
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv env
source env/bin/activate  # On Mac/Linux
env\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

## 🏃 Running the Project

### 1️⃣ Data Cleaning
```sh
python scripts/data_cleaning.py
```

### 2️⃣ Entity Matching
```sh
python scripts/entity_matching.py
```

### 3️⃣ Main Pipeline Execution
```sh
python main.py
```

## 📊 Results & Performance
- Achieved **high accuracy** in entity matching using SBERT.
- Improved **data quality** by eliminating inconsistencies in farm names.
- Optimized **threshold selection** for similarity scoring.

## 📚 Dependencies
- Python 3.8+
- Transformers (Hugging Face)
- Sentence-BERT (SBERT)
- Pandas, NumPy, Scikit-learn
- Flask (optional for API integration)

## 🤝 Contributing
Feel free to submit a **pull request** or report an issue if you'd like to contribute!

## 🔗 References
- [Sentence-BERT Paper](https://arxiv.org/abs/1908.10084)
- [Hugging Face Transformers](https://huggingface.co/)

## 📜 License
This project is licensed under the **MIT License**.

---

🔥 **Happy Coding!** 🔥
