# 📄 **README.md for Forebet Analytics Project**

---

# ⚡ **Forebet Analytics - Football Match Prediction Parser** ⚡

Welcome to **Forebet Analytics**, a Python-powered web scraping and data analysis tool designed to extract and analyze football match predictions from **[Forebet](https://www.forebet.com/)**. The script identifies matches where:
- **Both Teams to Score (BTTS): No**  
- **Total Goals: Under 2.5**  
- **Predicted Probability: Greater than 60%**  

The result? A refined list of matches that fit these criteria, giving you valuable insights for betting or statistical analysis. 🚀⚽

---

## 🚀 **Key Features**  
- 🌐 **Automated web scraping** using `Selenium` and `BeautifulSoup`  
- 📊 **Data analysis** of football matches based on user-defined conditions  
- 🏆 **Filtered predictions** where both teams are unlikely to score and total goals are expected to be under 2.5  
- ⚡ **Easy execution** with a single Python script  
- 💾 **Results saved** automatically in `mix_file/result.txt`  

---

## ⚙️ **Technologies Used**  
- 🐍 Python 3.x  
- 🕸 `Selenium` — for browser automation and dynamic content scraping  
- 🍲 `BeautifulSoup` — for parsing HTML content  
- 📝 Other Python standard libraries for data manipulation  

---

## 💾 **Installation & Setup**  

### 1⃣ **Clone the repository:**  
```bash
git clone https://github.com/morf-1-3/forebet_analytics.git
cd forebet_analytics
```

### 2⃣ **Install required libraries:**  
Make sure you have Python installed. Then, install the dependencies:
```bash
pip install selenium beautifulsoup4
```

### 3⃣ **Set up WebDriver:**  
- Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome).  
- Ensure that the WebDriver executable is in your system's PATH or update the path in the script accordingly.

---

## ⚡ **Usage**  

### 🏃 **Run the main script:**
1. Open `main.py` located in the project root directory.  
2. Define the match dates you're interested in using a **Python dictionary** format, for example:
   ```python
   dates = {
            "2": [day for day in range(16,17)]
        }
   ```  
3. Execute the script:
   ```bash
   python main.py
   ```

### 📝 **Result Output:**  
- After execution, the filtered list of matches will be saved in:
   ```plaintext
   mix_file/result.txt
   ```  
- The results will include matches that meet the conditions:  
   - ✅ BTTS: No  
   - ✅ Under 2.5 goals  
   - ✅ Probability > 60%

---

## 🌍 **How It Works**  
1⃣ The script uses **Selenium** to dynamically load Forebet pages.  
2⃣ **BeautifulSoup** parses the HTML, extracting data related to the matches.  
3⃣ It filters matches based on predefined conditions:
   - Both teams not scoring.
   - Less than 2.5 total goals.
   - Probability threshold over 60%.  
4⃣ Generates a final list of suitable matches and saves them in `result.txt`.

---


```

---

## 📑 **Example Output (`result.txt`):**
```
Team: Deportivo Madryn vs Racing de Cordoba, Probability: 63, Prediction: Under, Scores: None, IsSuccess: None
Team: Artesanos Metepec vs Deportivo Yautepec, Probability: 97, Prediction: Under, Scores: None, IsSuccess: None
Team: Zitacuaro vs Pioneros de Cancún, Probability: 72, Prediction: Under, Scores: None, IsSuccess: None
Team: Jaguares de Córdoba vs Orsomarso SC, Probability: 82, Prediction: Under, Scores: None, IsSuccess: None
Team: Sport Sinop vs Academia, Probability: 63, Prediction: Under, Scores: None, IsSuccess: None
Team: Gualan vs AFF Guatemala, Probability: 78, Prediction: Under, Scores: None, IsSuccess: None
Team: Macará vs Orense SC, Probability: 65, Prediction: Under, Scores: None, IsSuccess: None
Team: Malacateco vs Deportivo Guastatoya, Probability: 72, Prediction: Under, Scores: None, IsSuccess: None
Team: Atlético Central Córdoba vs Córdoba CF B, Probability: 80, Prediction: Under, Scores: None, IsSuccess: None
Team: Los Cabos United vs Mexicali FC, Probability: 62, Prediction: Under, Scores: None, IsSuccess: None ...
```

---

## 🏀 **Contributing**  
If you have ideas to improve this project or want to add more predictive capabilities — feel free to fork and submit a pull request. 💪✨

---

## 🛡 **Disclaimer**  
- This project is for **educational purposes** only.  
- **Forebet** is a trademark of its respective owners.  
- Always ensure responsible usage and comply with website terms.

---

## 🏆 **Author**    
📩 GitHub: [morf-1-3](https://github.com/morf-1-3)  

---

💬 **Happy Analyzing & Best of Luck with Your Predictions!** ⚽✨

