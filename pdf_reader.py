from rake_nltk import Rake
import PyPDF2

def getKeywords(job):  
    r = Rake(max_length=2) # Uses stopwords for english from NLTK, and all puntuation characters.0
    r.extract_keywords_from_text(job)
    K = r.get_ranked_phrases()[:7]
    return K

f = open('AmazonSDE_Desc.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(f)
fob = pdfReader.getPage(0) 
job = fob.extractText()
#job = request.form['input_text'] #Get text from html
K = getKeywords(job)
print(K)