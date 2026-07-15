import gradio as gr
import requests
import os

API_URL = "https://interview-backend-1-ia58.onrender.com/chat"
#API_URL="http://127.0.0.1:8000/generate"

def generate(language, category, difficulty, experience,
             company, role, count, answer_type):

    payload = {
        "language": language,   
        "category": category,
        "difficulty": difficulty,
        "experience": experience,
        "company": company,
        "role": role,
        "count": count,
        "answer_type": answer_type
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            return response.json()["result"]
        else:
            return response.text

    except Exception as e:
        return str(e)


demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Dropdown(
            ["Python", "Java", "C", "C++", "JavaScript", "SQL"],
            label="Programming Language",
            value="Python"
        ),

        gr.Dropdown(
            ["Technical", "HR", "Coding", "System Design", "Aptitude"],
            label="Interview Category",
            value="Technical"
        ),

        gr.Dropdown(
            ["Beginner", "Intermediate", "Advanced"],
            label="Difficulty",
            value="Beginner"
        ),

        gr.Dropdown(
            ["Fresher", "1-3 Years", "3-5 Years", "5+ Years"],
            label="Experience",
            value="Fresher"
        ),

        gr.Dropdown(
            ["Google", "Microsoft", "Amazon", "Infosys",
             "TCS", "Wipro", "Accenture", "Capgemini", "Deloitte"],
            label="Company",
            value="Google"
        ),

        gr.Textbox(
            label="Job Role",
            value="Python Developer"
        ),

        gr.Slider(
            minimum=5,
            maximum=20,
            step=5,
            value=10,
            label="Number of Questions"
        ),

        gr.Radio(
            ["Questions Only", "Questions + Answers"],
            value="Questions Only",
            label="Output Type"
        )
    ],

    outputs=gr.Textbox(
        lines=25,
        label="Interview Output"
    ),

    title="AI Interview Preparation Assistant",
    description="Generate interview questions using Gemini AI."
)
demo.launch()

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
