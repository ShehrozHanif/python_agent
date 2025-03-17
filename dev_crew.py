from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import LLM
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


llm1 = LLM(model = "gemini/gemini-2.0-flash", api_key=api_key)
llm2 = LLM(model = "gemini/gemini-1.5-flash", api_key=api_key)



@CrewBase
class DevCrew:
    """Dev Crew"""


    agents_config = "src/python_agent/config/agents.yaml"
    tasks_config = "src/python_agent/config/tasks.yaml"

    @agent
    def junior_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["junior_developer"],
            llm = llm1
        )
    @agent
    def senior_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_developer"],
            llm= llm2
        )

    @task
    def write_code(self) -> Task:
        return Task(
            config=self.tasks_config["write_code"],
        )
    @task
    def review_code(self) -> Task:
        return Task(
            config=self.tasks_config["review_code"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
    










import streamlit as st

# Custom CSS to disable default browser suggestions
custom_css = """
<style>
    input[type='text'] {
        autocomplete: off !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.title("Welcome to Shehroz Hanif's Agentic World")
st.title("Python Code Generator")

# Custom suggestions for problem statements
suggestions = [
    "Write a Python function to reverse a string.",
    "Create a calculator using Python.",
    "Generate Fibonacci sequence using recursion.",
    "Build a to-do list application using Python.",
    "Sort a list of numbers in ascending order."
]

# Text input where users can type freely
user_input = st.text_input("Enter the problem statement:", "")

# Display suggestions only when the input field is focused
if "show_suggestions" not in st.session_state:
    st.session_state.show_suggestions = False

def toggle_suggestions():
    st.session_state.show_suggestions = True

def select_suggestion(suggestion):
    st.session_state.user_input = suggestion
    st.session_state.show_suggestions = False

if user_input == "":
    toggle_suggestions()

if st.session_state.show_suggestions:
    st.write("### Suggestions:")
    for suggestion in suggestions:
        if st.button(suggestion):
            select_suggestion(suggestion)

if st.button("Generate Code"):
    if user_input.strip():
        response = DevCrew().crew().kickoff(inputs={"problem": user_input})
        if response:
            st.code(response, language='python')

            # Save the response as a file
            file_name = "response.py"
            with open(file_name, "w") as f:
                f.write(str(response))

            # Provide download button
            with open(file_name, "rb") as f:
                st.download_button(label="Download Generated Code",
                                   data=f,
                                   file_name=file_name,
                                   mime="text/x-python")
        else:
            st.error("No response generated. Please try again.")
    else:
        st.warning("Please enter a problem statement before generating code.")













# st.title("Welcome to Shehroz Hanif's Agentic World")
# st.title("Python Code Generator")
# user_input = st.text_input("Enter the problem statement:", "" )


# if st.button("Generate Code"):
#     if user_input.strip():
#         response = DevCrew().crew().kickoff(inputs={"problem": user_input})
#         if response:
#             st.code(response, language='python')

#             # Save the response as a file
#             file_name = "response.py"
#             with open(file_name, "w") as f:
#                 f.write(str(response))

#             # Provide download button
#             with open(file_name, "rb") as f:
#                 st.download_button(label="Download Generated Code",
#                                    data=f,
#                                    file_name=file_name,
#                                    mime="text/x-python")
#         else:
#             st.error("No response generated. Please try again.")
#     else:
#         st.warning("Please enter a problem statement before generating code.")    