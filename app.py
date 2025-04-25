from dotenv import load_dotenv
load_dotenv()   #loads all the environment variables
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

#configuring our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#main function
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('models/gemini-1.5-flash')
    response=model.generate_content([prompt[0],question])
    return response.text

#function to retrieve query from sql database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = ["""
You are an expert at converting English questions into clean and correct SQL queries.

The SQL database has one table named STUDENT with the following columns:
BU_ID (text), NAME (text), MAJOR (text), SUBJECT (text), MARKS (integer)

Important rules:
1. Always return **only** the SQL query.
2. Do **NOT** include code block syntax (no ```sql or ```)
3. Do **NOT** add comments or explanations.
4. The SQL should start with SELECT and end with a semicolon.
5. Always use correct column names exactly as described.

Examples:
Q: How many students are there?
A: SELECT COUNT(*) FROM STUDENT;

Q: Show names of students studying ARTIFICIAL INTELLIGENCE
A: SELECT NAME FROM STUDENT WHERE SUBJECT = 'ARTIFICIAL INTELLIGENCE';

Q: Get the average marks of all students.
A: SELECT AVG(MARKS) FROM STUDENT;

Q: List all students in the COMPUTER SCIENCE major.
A: SELECT * FROM STUDENT WHERE MAJOR = 'COMPUTER SCIENCE';
"""]

st.set_page_config(page_title="I Can Retrive Any SQL Query")
st.header("Gemini App For Convertin Text to SQL Query")
question=st.text_input("Input: ", key="input")
submit=st.button("Ask the Question")
if submit:
    response = get_gemini_response(question, prompt) 
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is: ")
    for row in data:
        print(row)
        st.header(row)

