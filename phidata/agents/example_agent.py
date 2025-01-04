from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

prompt = "Book Writing"

agent.print_response(f'''
Generate a JSON object for a course with the following structure:
    "name": "string (the name of the course)",
    "topics": [
        {{
        "id": "number",
        "title": "string",
        "timeToComplete": "number" (in minutes),
        "url": "string (the link of the content)"
        }}
    ]
      The course name should be related to "{prompt}", and the topics array should include at least 10 items in sequential order. 
      Topics should be sourced from real content such as YouTube videos, blogs, websites, etc. 
      Do not make up links; provide original URLs, check the url if it exists.
      The url should be embeddable urls using iframe but you do not need to create embeddable urls, just provide normal urls.
      Do not add links from course websites such as Coursera, Udemy, edX, etc.
      The response should ONLY contain the valid JSON object (name of the course and the topics array) and no other text, explanations, or notes.
             ''')
                     