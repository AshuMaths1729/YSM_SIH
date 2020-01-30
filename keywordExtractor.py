
# example text
text = "Compatibility of systems of linear constraints over the set of natural numbers. \
    Criteria of compatibility of a system of linear Diophantine equations, strict inequations, \
        and nonstrict inequations are considered. Upper bounds for components of a minimal set of \
            solutions and algorithms of construction of minimal generating sets of solutions for all\
                 types of systems are given. These criteria and the corresponding algorithms for \
                     constructing a minimal supporting set of solutions can be used in solving all the \
                         considered types systems and systems of mixed types."


job = "Amazon teams in India work on complex business challenges to innovate and create efficient \
    solutions that enable various Amazon businesses, including Amazon websites across the world as \
        well as support Payments, Transportation, and Digital products and services like the Kindle \
            family of tablets, e-readers and the store. We are proud to have some of the finest talent \
                and strong leaders with proven experience working to make Amazon the Earth’s most \
                    customer-centric company. At a strategic level, our development team will be \
                        instrumental in shaping the product direction and will be actively involved \
                            in defining key product features that impact the business. We are looking\
                                 for a passionate, hard-working, and talented Software Development Engineer\
                                      who can build innovative and mission critical system software applications \
                                          and tools. You will have an enormous opportunity to make a large impact \
                                              on the design, architecture, and development of consumer products. \
                                                  You will be responsible for delivery and support of large-scale,\
                                                       multi-tiered, distributed software applications and tools. \
                                                           Responsibilities Include Ability to design and code right \
                                                               solutions starting with broadly defined problems.\
                                                                   Drive best practices and engineering excellence.\
                                                                       Work with other team members to develop the architecture and \
                                                                           design of new and current systems. Work in an agile environment \
                                                                               to deliver high quality software."
"""
import spacy
import pytextrank

# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")

# add PyTextRank to the spaCy pipeline
tr = pytextrank.TextRank()
nlp.add_pipe(tr.PipelineComponent, last=True)

doc = nlp(job)

# examine the top-ranked phrases in the document
for p in doc._.phrases:
    #print("{:.4f} {:5d}  {}".format(p.rank, p.count, p.text))
    print(p.chunks[0])
    break

# summarize the document based on the top 15 phrases, 
# yielding the top 5 sentences...
for sent in doc._.textrank.summary():
    print(sent)
    break

"""
job2 = "Application maintenance and support experience (2+ years)\
 Basic knowledge on IoT e2e flow\
 Programming knowledge in Cloud technologies and Web development\
 Ability to understand Integration platforms and work with API\
 Ability to work in a Devops model with tools\
 Basic knowledge on Data Analytics\
 Good communication and collaboration skills\
 Fluent English (oral and written)\
 Preferable an Engineer with Computer science or Information technology Background\
 Willingness to operate in a 24/7 support team"



def getKeywords(job):
    from rake_nltk import Rake

    r = Rake(max_length=2) # Uses stopwords for english from NLTK, and all puntuation characters.

    r.extract_keywords_from_text(job)

    K = r.get_ranked_phrases()[:7]
    return K

K = getKeywords(job2)
print(K)