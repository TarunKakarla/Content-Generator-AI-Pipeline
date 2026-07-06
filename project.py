import os
from typing import TypedDict

from dotenv import load_dotenv
load_dotenv()

class pipelinestate(TypedDict):
    raw_input: str
    edited_text: str
    script_text: str
    final_output: str


print(os.getenv("OPENAI_API_KEY"))
print(os.getenv("MODEL_NAME"))
from langchain_openai import ChatOpenAI
model = os.getenv("MODEL_NAME")
print(model)
llm = ChatOpenAI(model_name=model, base_url= "http://localhost:3001/v1", temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))

def editor_node(state: pipelinestate) -> dict:
    """Stage 1: Cleans up grammar, remove tupos, and refines the tone."""

    prompt = ("You are a an expert editor. You will be given a text and your task is to clean up the grammar, remove typos, and refine the tone of the text. Please provide the edited version of the text. While keeping the core message intact, return only the edited text.\n\n"f"Text: \n{state['raw_input']}")
    response = llm.invoke(prompt)
    return {"edited_text": response.content.strip()}

def scriptwriter_node(state: pipelinestate) -> dict:
    """Stage 2: Converts the edited text into a script format."""

    prompt = ("You are a professional charismatic youtube scriptwriter. You will be given a text and your task is to convert it into a script format suitable for a youtube video. Please provide the script version of the text. Make it sound like a real person speaking passionately. While keeping the core message intact, return only the script text.\n\n"f"Text: \n{state['edited_text']}")
    response = llm.invoke(prompt)
    return {"script_text": response.content.strip()}

def translator_node(state: pipelinestate) -> dict:
    """Stage 3: Translates the script into Hinglish."""

    prompt = ("You are a professional expert content localizer for the indian market. You will be given a text and your task is to translate it into Hinglish. Conversion must feel very natural, flowing 'Hinglish. Do not simply translate or repeat the information.Alternating comfortably betwqeen Hindi and English. Please provide the translated version of the text. While keeping the core message intact, return only the translated text (return only the translated text in english(literature)).\n\n"f"Text: \n{state['script_text']}")
    response = llm.invoke(prompt)
    return {"final_output": response.content.strip()}

#States and nodes are ready now it's ready to create a graph, We have to use the edges to connect the nodes and create a graph. The graph will be used to run the pipeline.

from langgraph.graph import StateGraph, START, END

state_graph = StateGraph(pipelinestate)
state_graph.add_node("editor", editor_node)
state_graph.add_node("scriptwriter", scriptwriter_node)
state_graph.add_node("translator", translator_node)
state_graph.add_edge(START, "editor")
state_graph.add_edge("editor", "scriptwriter")
state_graph.add_edge("scriptwriter", "translator")      
state_graph.add_edge("translator", END)

#compile the graph to check for any errors
app = state_graph.compile()
p = input("Prompt : ")
res = app.invoke({"raw_input": p})
print("Your results are", res["final_output"])

