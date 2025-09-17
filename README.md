# 📊 CORD-19 Research Dataset Assignment  

This project is part of my **Frameworks Assignment**. It focuses on analyzing the **CORD-19 metadata dataset** (COVID-19 research papers) and building a simple **Streamlit app** to display insights.  

---

## 🚀 Features
- Load and clean real-world data (`metadata.csv` from the CORD-19 dataset).  
- Explore and visualize research publications over time.  
- Identify top journals publishing COVID-19 papers.  
- Generate word frequency insights from paper titles.  
- Interactive **Streamlit app** for data exploration.  

---

## 📂 Repository Structure
CORD19_Assignment/
│
├── analysis.ipynb # Jupyter Notebook for exploration
├── analysis.py # Python script for data analysis
├── app.py # Streamlit application
├── requirements.txt # Required Python libraries
├── .gitignore # Ensures large files (metadata.csv) are ignored
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Installation & Setup

Follow these steps to set up and run the project:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/Frameworks_Assignment.git
cd Frameworks_Assignment
2️⃣ Download the dataset
Go to the Kaggle dataset:
👉 CORD-19 Research Challenge (Kaggle)

Download the ZIP file and extract it.

Copy the file metadata.csv into the project folder (same directory as analysis.py and app.py).

3️⃣ Install dependencies
Make sure you have Python 3.7+ installed. Then install the required libraries:

bash
Copy code
pip install -r requirements.txt
4️⃣ Run the analysis script
Run the Python analysis file to check basic outputs and visualizations:

bash
Copy code
python analysis.py
5️⃣ Launch the Streamlit app
Start the interactive web app with:

bash
Copy code
streamlit run app.py
Once the app starts, you’ll see a link like:

nginx
Copy code
Local URL: http://localhost:8501
Network URL: http://192.168.xx.xx:8501
👉 Open the Local URL in your browser to interact with the app.

📊 Example Visualizations in the App
📅 Publications by year (bar chart)

📰 Top journals publishing COVID-19 research (bar chart)

☁️ Word frequency in paper titles (word cloud)

📦 Distribution of papers by source

✨ Learning Outcomes
By completing this project, I practiced:

Data loading and cleaning with pandas

Visualizations with matplotlib/seaborn

Building an interactive dashboard with Streamlit

Clear documentation and GitHub workflow

🙌 Notes
The dataset file (metadata.csv) is too large for GitHub, so it has been excluded.

Please download it manually from Kaggle before running the code.
