import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        episode = request.form["episodio"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(episode),
            temperature=0.6,
            max_tokens=2500
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(episode):
    return f"Summarize the episode '{episode}' of the podcast 'Mi Mejor Versión con Isa Garcia' in Spanish. Then list the key sections of the podcast. Each section should include the minute and second that they start. List each section in a newline."
