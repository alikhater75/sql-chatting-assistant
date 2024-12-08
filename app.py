import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_openai import ChatOpenAI
from langchain import hub
import os
from typing_extensions import Annotated, TypedDict
from langgraph.graph import START, StateGraph
from dotenv import load_dotenv
load_dotenv()

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize the database connection and model
db = SQLDatabase.from_uri("sqlite:///consumption.db")  # Ensure this path is correct
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Load the SQL query prompt from LangChain hub
query_prompt_template = hub.pull("langchain-ai/sql-query-system-prompt")

# Define the state and query output
class State(TypedDict):
    question: str
    query: str
    result: str
    answer: str

class QueryOutput(TypedDict):
    query: Annotated[str, ..., "Syntactically valid SQL query."]

# Define the steps for the workflow
def write_query(state: State):
    """Generate SQL query to fetch information."""
    prompt = query_prompt_template.invoke(
        {
            "dialect": db.dialect,
            "top_k": 10,
            "table_info": db.get_table_info(),
            "input": state["question"],
        }
    )
    structured_llm = llm.with_structured_output(QueryOutput)
    result = structured_llm.invoke(prompt)
    return {"query": result["query"]}

def execute_query(state: State):
    """Execute SQL query."""
    execute_query_tool = QuerySQLDataBaseTool(db=db)
    return {"result": execute_query_tool.invoke(state["query"])}

def generate_answer(state: State):
    """Answer question using retrieved information as context."""
    prompt = (
        "Given the following user question, corresponding SQL query, "
        "and SQL result, answer the user question.\n\n"
        f'Question: {state["question"]}\n'
        f'SQL Query: {state["query"]}\n'
        f'SQL Result: {state["result"]}'
    )
    response = llm.invoke(prompt)
    return {"answer": response.content}

# Define the state graph for the LangGraph processing
graph_builder = StateGraph(State).add_sequence(
    [write_query, execute_query, generate_answer]
)
graph_builder.add_edge(START, "write_query")
graph = graph_builder.compile()

def get_answer(question: str) -> str:
    """
    Takes a user question as input and returns a natural language answer generated 
    by the application, which queries a SQL database to retrieve relevant data.

    Parameters:
    - question (str): The user question to be answered.

    Returns:
    - str: The generated natural language answer to the question.
    """
    # Use the LangGraph graph.invoke method to process the input question
    # The result is fetched in streaming mode to provide updates, and the final answer is extracted
    answer = graph.invoke({"question": question}, stream_mode="updates")[-1]["generate_answer"]["answer"]
    return answer

# Streamlit app interface
st.title("SQL Query and Answer Generator")

# Input question from user
user_question = st.text_input("Ask a question about your data:")

if user_question:
    with st.spinner("Processing your question..."):
        # Get the final answer
        final_answer = get_answer(user_question)
        
        # Display the results
        st.subheader("Generated Answer")
        st.write(final_answer)


