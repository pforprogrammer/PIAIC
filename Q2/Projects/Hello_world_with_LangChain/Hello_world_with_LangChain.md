
# Project Overview: **Hello World with LangChain and Google Gemini**

This project integrates **LangChain** and **Google Gemini AI** to create a conversational AI application. The application takes user queries and provides AI-generated responses using LangChain's prompt-based chaining capabilities.

---

## Key Components of the Notebook

### 1. **Installing Dependencies**
```python
!pip install -qU langchain-google-genai langchain
```
- **What it does**: Installs the necessary libraries:
  - **`langchain-google-genai`**: Enables integration with Google Gemini AI.
  - **`langchain`**: A framework for building AI-powered applications using language models.

- **Why it's important**: These libraries provide the tools required to interact with Google Gemini AI and manage AI prompts effectively.

---

### 2. **Importing Libraries**
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
```
- **What it does**:
  - **`ChatGoogleGenerativeAI`**: Facilitates interaction with Google Gemini AI.
  - **`LLMChain`**: Manages the chaining of prompts and AI responses.
  - **`PromptTemplate`**: Enables the creation of customizable prompts for AI queries.

- **Why it's important**: These components are the backbone of the application's interaction with AI, ensuring structured and meaningful responses.

---

### 3. **Initializing the Gemini API Client**
```python
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
```
- **What it does**: Retrieves the API key required to access Google Gemini AI.

- **How it works**:
  - The key is stored securely and accessed using `userdata.get()`.
  - This is essential for authentication when making API calls to Google Gemini.

- **Why it's important**: Without a valid API key, the application cannot interact with Google Gemini AI.

---

### 4. **Defining the LangChain Prompt Template**
```python
TEMPLATE = """
You are an advanced AI assistant using Google Gemini AI.
Answer user queries concisely, clearly, and effectively.

User Query: {query}

Your Response:
"""
prompt_template = PromptTemplate(input_variables=["query"], template=TEMPLATE)
```
- **What it does**:
  - Creates a structured prompt for LangChain.
  - Uses `{query}` as a placeholder for dynamic user inputs.

- **Why it's important**: This template ensures that the AI understands the user's query context and responds appropriately.

---

### 5. **Creating a LangChain Client**
```python
client: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0.2,
    google_api_key=GOOGLE_API_KEY
)
```
- **What it does**:
  - Initializes the LangChain client with Google Gemini AI.
  - Specifies:
    - **Model**: `gemini-2.0-flash-exp`.
    - **Temperature**: Controls response creativity (lower = more focused).
    - **API Key**: Authenticates requests.

- **Why it's important**: This client bridges the LangChain framework and Google Gemini AI.

---

### 6. **Setting up the LangChain LLMChain**
```python
chain = LLMChain(llm=client, prompt=prompt_template)
```
- **What it does**:
  - Combines the LangChain client and the prompt template.
  - Manages the process of sending queries and receiving responses.

- **Why it's important**: Simplifies the workflow for generating AI-powered responses.

---

### 7. **Defining Helper Functions**
#### 1. **Generate Response with Chain**
```python
def generate_response_with_chain(user_query):
    response = chain.invoke({"query": user_query})
    return response['text']
```
- **What it does**: Sends the user's query to the AI and retrieves the response.

- **How it works**:
  - Passes the query as input to the LangChain chain.
  - Extracts and returns the AI's textual response.

---

#### 2. **Display AI Response**
```python
def display_response(response):
    print("\n===== AI Response =====")
    print(response)
```
- **What it does**: Displays the AI's response in a readable format.

---

### 8. **Main Program Execution**
```python
def main():
    print("Welcome to the Hello Gemini Project!")
    print("This application uses Google Gemini AI with LangChain for advanced capabilities.")
    print("Type 'exit' to quit the program.\n")

    while True:
        user_query = input("Enter your query: ").strip()
        if user_query.lower() == "exit":
            print("Thank you for using the Hello Gemini Project. Goodbye!")
            break

        ai_response = generate_response_with_chain(user_query)
        display_response(ai_response)
```
- **What it does**:
  - Runs the main application loop.
  - Prompts the user for input and handles the conversation flow.
  - Ends the program if the user types "exit".

---

## Example Execution
1. **User Input**: `who is imran khan`
2. **AI Response**:
   ```
   Imran Khan is a Pakistani politician and former cricketer who served as the 22nd Prime Minister of Pakistan from 2018 to 2022. He founded the political party Pakistan Tehreek-e-Insaf (PTI).
   ```

---

## Summary
This notebook demonstrates how to:
- Install and configure LangChain and Google Gemini AI.
- Create structured prompts for natural language processing.
- Build a conversational AI application using Python.
