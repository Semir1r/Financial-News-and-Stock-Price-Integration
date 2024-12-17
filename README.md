Nova Financial Solutions - Predictive Analytics Project
Table of Contents
Introduction
Task 1: Git and GitHub
Task 2: Quantitative Analysis using PyNance and TA-Lib
Task 3: Correlation between News and Stock Movement
Getting Started
Folder Structure
KPIs and Requirements
Contributing
License
Introduction
Nova Financial Solutions aims to enhance its predictive analytics capabilities to significantly boost financial forecasting accuracy and operational efficiency. This project focuses on analyzing financial news sentiment and its correlation with stock price movements. It involves setting up a Python environment, using Git for version control, implementing CI/CD practices, and performing exploratory and quantitative data analysis.

Task 1: Git and GitHub
Objectives:
Dev Environment Setup: Establish a Python environment and GitHub repository.
Git Version Control: Utilize Git for version control.
CI/CD: Implement continuous integration and continuous deployment practices.
Tasks:
Create a GitHub repository to host all the code for this week.
Set up a Python environment.
Create at least one new branch called "task-1" for ongoing development.
Commit your work at least three times a day with descriptive commit messages.
Perform Exploratory Data Analysis (EDA):
Descriptive Statistics:
Obtain basic statistics for textual lengths (like headline length).
Count the number of articles per publisher.
Analyze publication dates for trends.
Text Analysis (Sentiment Analysis & Topic Modeling):
Perform sentiment analysis on headlines.
Use NLP to identify common keywords or phrases.
Time Series Analysis:
Analyze publication frequency over time.
Identify spikes in article publications related to market events.
Publisher Analysis:
Identify the most active publishers.
If email addresses are used as publisher names, extract unique domains.
Suggested Folder Structure:
markdown
Copy code
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
Task 2: Quantitative Analysis using PyNance and TA-Lib
Objectives:
Use additional finance data.
Apply technical indicators to stock price data.
Visualize data to understand the impact of indicators on stock prices.
Tasks:
Merge necessary branches from task-1 into the main branch using a Pull Request (PR).
Create at least one new branch called "task-2" for ongoing development.
Prepare your data by loading stock price data into a pandas DataFrame.
Apply TA-Lib indicators such as moving averages, RSI, and MACD.
Use PyNance for financial metrics.
Visualize data to show the impact of different indicators on stock price movements.
KPIs:
Proactivity to self-learn - sharing references.
Accuracy of indicators.
Completeness of data analysis.
Task 3: Correlation between News and Stock Movement
Objectives:
Align dates between news and stock datasets.
Perform sentiment analysis on news headlines.
Calculate stock movements and analyze their correlation with news sentiment.
Tasks:
Merge necessary branches from task-2 into the main branch using a Pull Request (PR).
Create at least one new branch called "task-3" for ongoing development.
Normalize dates to align news and stock datasets.
Perform sentiment analysis using NLP tools like nltk, TextBlob.
Calculate daily stock returns.
Compute correlation between sentiment scores and stock returns.
KPIs:
Proactivity to self-learn - sharing references.
Sentiment analysis accuracy.
Correlation strength.
Getting Started
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/predictive-analytics-project.git
cd predictive-analytics-project
Set up the Python environment:

bash
Copy code
pip install -r requirements.txt
Initialize Git:

bash
Copy code
git init
git branch task-1
git branch task-2
git branch task-3
Folder Structure
The project follows a structured folder layout to maintain organization and ease of access:

markdown
Copy code
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
.vscode/: VSCode settings for development environment.
.github/: GitHub workflows for CI/CD.
src/: Main source code.
notebooks/: Jupyter notebooks for analysis.
tests/: Unit tests for validation.
scripts/: Utility scripts.
KPIs and Requirements
Dev Environment Setup: Ensure a clean setup with all dependencies.
Relevant skill in the area demonstrated: Perform tasks with attention to detail and efficiency.
Proactivity to self-learn: Share references and document your learning.
Accuracy of indicators: Verify calculations and analysis.
Completeness of data analysis: Ensure thoroughness in data preparation, analysis, and visualization.
Contributing
Feel free to fork this repository and contribute! Please ensure to:

Create a new branch for each task.
Commit regularly with descriptive messages.
Open a Pull Request when you have completed your changes.
License
This project is licensed under the MIT License. See the LICENSE file for more information.