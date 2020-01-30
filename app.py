from rake_nltk import Rake
from flask import Flask, render_template, request #Used to render .html templates

def getKeywords(job):
    r = Rake(max_length=2) # Uses stopwords for english from NLTK, and all puntuation characters.0
    r.extract_keywords_from_text(job)
    K = r.get_ranked_phrases()[:7]
    return K

@app.route('/templates', methods=['POST'])
def original_text_form():
	#title = "Summarizer"
	job = request.form['input_text'] #Get text from html
	K = getKeywords(job)
	return render_template("index.html", job = job, K = K)

@app.route('/')
def homepage():
	#title = "Text Summarizer"
	return render_template("index.html")
	
if __name__ == "__main__":
	app.debug = True
	app.run()