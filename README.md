# ChatView App 🗨️

## 📜 Overview
ChatView is a chat analysis application that leverages advanced natural language processing (NLP) techniques to analyze WhatsApp conversation data. As digital communication continues to expand, understanding the emotional and thematic content of chats has become essential for users wanting to gain insights into their interactions. ChatView aims to assist users—whether researchers, journalists, or everyday communicators—in uncovering patterns and sentiments within their conversations, thereby fostering informed communication.

## 📁 Dataset
The dataset consists of user-provided WhatsApp chat logs exported in .txt format. Each file contains message exchanges with timestamps, participants, and message content, enabling comprehensive sentiment analysis and keyword extraction.

## View the application here
https://chatviewapp.streamlit.app/


## 🔧 Dependencies
Ensure the following dependencies are installed:

1. **TensorFlow**: Deep learning framework.
2. **Keras**: Simplifies building neural networks.
3. **Scikit-Learn**: For ensemble learning methods and model evaluation.
4. **NLTK Toolkit**: For text preprocessing and tokenization.
5. **Streamlit**: Web application framework for creating interactive dashboards.
6. **Pandas**: Data manipulation and analysis library.
7. **Matplotlib & Seaborn**: For data visualization.

```bash
pip install tensorflow keras scikit-learn nltk streamlit pandas matplotlib seaborn
```
## 🚀 Project Setup and Execution

To set up and run the ChatView application, follow these detailed steps:

### 1. Clone the Repository

Start by cloning the ChatView repository to your local machine. Open your terminal and execute the following command:

```bash
git clone https://github.com/jayanthpotluri5513/ChatViewApp.git
```

This command creates a copy of the repository in your current directory. Alternatively, you can download the repository as a ZIP file and extract it to your preferred location.

## 2. Navigate to the Project Directory
Once cloned, navigate into the project directory using:

```bash
cd ChatViewApp
```
## 3. Install Dependencies
Ensure you have Python and pip installed on your system. Install the required dependencies for the project using the following command:

``` bash
pip install tensorflow keras scikit-learn nltk streamlit pandas matplotlib seaborn
```
This command installs all necessary libraries for running the ChatView application. Make sure to install these dependencies in a virtual environment to avoid conflicts with other projects. You can create a virtual environment using:

```bash
python -m venv venv
```
And activate it with:

For Windows:

```bash
venv\Scripts\activate
```
For macOS/Linux:

```bash
source venv/bin/activate
```
## 4. Prepare Your Data
Before running the application, ensure you have your WhatsApp chat data ready. The application accepts .txt files exported from WhatsApp. Place your chat files in the data directory within the ChatView project folder.

## 5. Run the Project Using Streamlit
With the dependencies installed and your data in place, you can now launch the ChatView application. Execute the following command in the terminal:

```bash
streamlit run app.py
```
This command starts the Streamlit server, and you should see output indicating that the application is running. By default, it opens in your web browser at `http://localhost:8501`.

## 6. Interacting with the Application
Once the application is running, you can interact with it through the web interface:
**Upload Chat Data**: Use the upload feature to load your WhatsApp chat files.
**View Insights**: Explore sentiment analysis results and visualizations based on your chats.
**Download Results**: Export charts and insights for further analysis or sharing.
## 7. Stopping the Application
To stop the Streamlit application, return to the terminal where it’s running and press `Ctrl + C`. This will terminate the server.

## 🏗️ Instructions to Run

Streamlit
Open your terminal and execute the following commands:

```bash
cd ~/Desktop/"Your Project Directory"
streamlit run app.py
```

## 🖥️ Tech Stack

### **Frameworks**
- **TensorFlow**: An open-source framework for building and training machine learning models.
- **Keras**: A high-level API for neural networks, simplifying model creation on top of TensorFlow.
- **Streamlit**: A framework for creating interactive web applications for data science projects.

### **Model Architecture**
- **Natural Language Processing (NLP)**: Techniques used for text analysis, including sentiment analysis and keyword extraction.

### **Text Preprocessing**
- **NLTK**: A library for natural language processing, offering tools for text processing tasks.

### **Python Libraries**
- **NumPy**: For numerical operations and handling arrays.
- **Pandas**: For data manipulation and analysis using DataFrames.

### **Data Visualization**
- **Matplotlib**: A library for creating static, animated, and interactive visualizations.
- **Seaborn**: A statistical data visualization library built on Matplotlib, enhancing plot aesthetics.

### **Additional Libraries**
- **TextBlob**: For simple NLP tasks, including sentiment analysis.
- **VADER**: Specialized for sentiment analysis, effective on social media texts.

### **Development Tools**
- **Jupyter Notebook**: For interactive code execution and data visualization.
- **Google Colab**: A cloud-based platform for running Python code and machine learning experiments.

### **Deployment**
- **Heroku/Streamlit Sharing**: Platforms for deploying Streamlit applications to a live environment.

## 🔍 Step-by-Step Process

Here’s a complete breakdown of the project flow:

### 1. Data Collection and Loading

- **Data Import**: Users upload WhatsApp chat data in .txt format through the app interface.
- **Loading**: The application reads and structures the data for analysis, converting it into a suitable format for processing.

### 2. Data Preprocessing

- **Cleaning**: 
  - Remove unwanted characters, punctuation, and stop words using NLTK’s stopwords list.
  - Normalize text by converting it to lowercase to ensure consistency.

- **Tokenization**: 
  - Split the text into individual tokens (words) to prepare for analysis.
  - Utilize NLTK’s `word_tokenize` function for efficient tokenization.

- **Vectorization**: 
  - Transform the cleaned text into numerical vectors, using word embeddings (such as Word2Vec or GloVe) for contextual representation.
  - Create a matrix representation of the tokens to facilitate further analysis.

### 3. Sentiment Analysis

- **Sentiment Extraction**: 
  - Apply NLP algorithms to determine the emotional tone of conversations (positive, negative, neutral).
  - Utilize sentiment analysis libraries like VADER or TextBlob to classify sentiments accurately.

- **Keyword Extraction**: 
  - Identify key terms and phrases within the chat data, highlighting important discussion points.
  - Implement techniques such as TF-IDF or RAKE for effective keyword extraction.

### 4. Data Visualization

- **Summary Statistics**: 
  - Display total messages, unique users, and interaction trends in an easy-to-understand format.
  - Provide insights on user engagement over time.

- **Charts and Graphs**: 
  - Visualize sentiment trends and keyword frequencies over time using libraries like Matplotlib and Seaborn.
  - Create interactive plots that allow users to explore data dynamically.

### 5. User Interaction

- **Filtering and Searching**: 
  - Users can filter chats by date, participant, or sentiment for focused analysis.
  - Implement search functionalities to help users find specific discussions or keywords easily.

- **Exporting Results**: 
  - Provide the ability to download visualizations and insights for further review in various formats (e.g., PNG, PDF).
  - Enable users to save their analysis for offline access.

### 6. Model Evaluation (Optional)

- While the main focus is on interactive analysis, implement techniques to validate sentiment accuracy and extraction quality.
- Use cross-validation or hold-out testing to evaluate the performance of sentiment classification models.

## 📊 Results and Visualization

The application provides real-time insights into WhatsApp chats, showcasing:

- **Sentiment Analysis Results**: Overall sentiment distribution visualized through pie charts or bar graphs.
- **Keyword Frequency Charts**: Visual representation of frequently used terms, highlighting trends in conversation topics.
- **User Interaction Metrics**: Statistics on messaging activity, such as the number of messages per user and the most active participants.

## Live deployed link
https://chatviewapp.streamlit.app/


## 📜 License
[MIT](https://choosealicense.com/licenses/mit/)

## 🤖 About Me:
I'm Srijayanth Potluri, an aspiring data analyst with a strong interest in machine learning, deep learning, and NLP technologies. This project exemplifies my commitment to harnessing advanced algorithms for insightful communication analysis, combating misinformation, and promoting meaningful digital interactions.

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/srijayanth-potluri-437519259/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/SrijayanthP)


