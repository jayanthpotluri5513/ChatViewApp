# ChatView App 🗨️

## 📜 Overview
ChatView is a chat analysis application that leverages advanced natural language processing (NLP) techniques to analyze WhatsApp conversation data. As digital communication continues to expand, understanding the emotional and thematic content of chats has become essential for users wanting to gain insights into their interactions. ChatView aims to assist users—whether researchers, journalists, or everyday communicators—in uncovering patterns and sentiments within their conversations, thereby fostering informed communication.

## 📁 Dataset
The dataset consists of user-provided WhatsApp chat logs exported in .txt format. Each file contains message exchanges with timestamps, participants, and message content, enabling comprehensive sentiment analysis and keyword extraction.

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
This command starts the Streamlit server, and you should see output indicating that the application is running. By default, it opens in your web browser at http://localhost:8501.

## 6. Interacting with the Application
Once the application is running, you can interact with it through the web interface:

**Upload Chat Data**: Use the upload feature to load your WhatsApp chat files.
**View Insights**: Explore sentiment analysis results and visualizations based on your chats.
**Download Results**: Export charts and insights for further analysis or sharing.
## 7. Stopping the Application
To stop the Streamlit application, return to the terminal where it’s running and press Ctrl + C. This will terminate the server.
