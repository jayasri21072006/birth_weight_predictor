# 👶 Birth Weight Prediction Web App

A Flask-based Machine Learning web application that predicts a baby's birth weight based on maternal health and pregnancy details.

The model was trained using regression and predicts birth weight in ounces, which is converted to grams and kilograms for user-friendly output.

---

## 🚀 Features

- User-friendly web interface
- Accepts metric input (cm, kg)
- Automatically converts units internally
- Predicts birth weight using trained ML model
- Displays output in:
  - Grams
  - Kilograms
- Form values persist after prediction
- Clean and responsive UI

---

## 🧠 Input Features

| Feature     | Description |
|------------|------------|
| Gestation  | Total pregnancy duration in days |
| Parity     | Number of previous live births |
| Age        | Mother's age (years) |
| Height     | Mother's height (cm) |
| Weight     | Mother's weight (kg) |
| Smoke      | 0 = No, 1 = Yes |

---

## 📊 Model Details

- Type: Regression Model
- Target: Baby Birth Weight
- Original Output Unit: Ounces
- Converted Output: Grams & Kilograms

---

## 📁 Project Structure


project/
│
├── app.py
├── model.pkl
├── README.md
└── templates/
└── index.html


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd project
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Requirements
pip install flask pandas scikit-learn
4️⃣ Run Application
python app.py

Then open:

http://127.0.0.1:5000/
🔄 Unit Conversion Logic
Input Conversion

Height: cm → inches

Weight: kg → pounds

Output Conversion

Ounces → grams

Grams → kilograms

🎯 Example Output

Predicted Birth Weight:

3200 grams

3.20 kg

📌 Future Improvements

Add input validation

Add BMI auto-calculation

Deploy to cloud (Render / Railway / Azure)

Add REST API endpoint

Add model evaluation metrics display

👨‍💻 Author T.jayasri 

Developed using:

Python

Flask

Pandas

Scikit-learn

📄 License

This project is for educational purposes.


---

