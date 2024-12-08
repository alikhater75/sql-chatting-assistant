
# SQL Chatting Assistant

This project is a **natural language question-answering system** that generates and executes SQL queries to retrieve data from a relational database. Using **Large Language Models (LLMs)** and modern frameworks like **LangChain**, the assistant answers user questions with human-readable responses.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [How to Run](#how-to-run)
7. [Usage](#usage)
8. [Exploratory Data Analysis](#exploratory-data-analysis)
9. [Future Improvements](#future-improvements)

---

## Overview

The SQL Chatting Assistant combines **natural language processing** and **SQL execution** to interact with relational databases. The system takes user questions as input, translates them into SQL queries, retrieves relevant data, and generates human-readable responses.

---

## Features

- **Natural Language Understanding**: Converts user questions into SQL queries.
- **SQL Query Execution**: Executes queries using SQLite.
- **Answer Synthesis**: Converts SQL results into readable answers.
- **Streamlit UI**: A clean user interface for interacting with the assistant.
- **Exploratory Data Analysis (EDA)**: A pipeline for structured data analysis.

---

## Project Structure

```
project/
│
├── app.py                     # Streamlit app to generate answers
├── requirements.txt           # Project dependencies
├── build_and_evaluate_SQL_chatting_assistant.ipynb  # Notebook for SQL model building and evaluation
├── EDA.ipynb                  # Notebook for data exploration and analysis
├── chatting assistant documentation.pdf   # Detailed project documentation
└── README.md                  # This file
```

---

## Requirements

The project uses the following libraries and tools:

```txt
streamlit
langchain
langchain-community
langchain-openai
python-dotenv
sqlalchemy
pandas
matplotlib
numpy
pymongo
openai
```

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/sql-chatting-assistant.git
   cd sql-chatting-assistant
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```

4. **Prepare your database**:
   - Add your SQLite database file `consumption.db` in the project directory.
   - Ensure it contains the necessary tables and data.

---

## How to Run

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will launch a user interface where you can input questions about your data.

---

## Usage

1. **Input**: Ask a natural language question like:
   ```
   What is the total revenue for 2023?
   ```

2. **Processing**:
   - The assistant generates an SQL query using the OpenAI GPT-4 model.
   - Executes the query on the database.

3. **Output**:
   - Returns the human-readable answer:
     ```
     The total revenue for 2023 is $1,500,000.
     ```

---

## Exploratory Data Analysis

For data exploration, the `EDA.ipynb` notebook provides visualizations and insights into your structured data:
- Missing values analysis
- Trends analysis (e.g., revenue per year)
- Visualizations using `matplotlib` and `pandas`

---

## Future Improvements

- **Support for other databases** (PostgreSQL, MySQL)
- **Advanced query validation** for more complex SQL generation
- **Scalability enhancements** to handle larger datasets
- **Predictive analytics** using machine learning models

---

## Documentation

Refer to the [chatting assistant documentation](./chatting%20assistant%20documentation.pdf) for detailed insights into the project approach, methodologies, and algorithms.


