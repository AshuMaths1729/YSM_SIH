# User-Job/Course Similarity
# Content-based Filtering
# Using Semantic Similarity

from rake_nltk import Rake
import spacy
nlp = spacy.load("en_core_web_md")

"""
Keywords will be found for each course before finding similarity and then,
These associated keywords will be used to find similarity.
"""

def getKeywords(txt):
    """
    Returns top 6 keywords of maximum length 2 associated with a
    given text.
    """
    r = Rake(max_length=2)
    r.extract_keywords_from_text(txt)
    K = r.get_ranked_phrases()[:6]
    return K


### For Job
job_desc = "Application maintenance and support experience (2+ years)\
    Basic knowledge on IoT e2e flow\
    Programming knowledge in Cloud technologies and Web development\
    Ability to understand Integration platforms and work with API\
    Ability to work in a Devops model with tools\
    Basic knowledge on Data Analytics\
    Good communication and collaboration skills\
    Fluent English (oral and written)\
    Preferable an Engineer with Computer science or Information technology Background\
    Willingness to operate in a 24/7 support team"
jobKeys = getKeywords(job_desc)
jobKeys = ','.join(jobKeys)
job = nlp(jobKeys)
skills = nlp("Coding, Data Analytics, Python, Web Development, English")
sj = skills.similarity(job)
print(sj)



### For Course
course_desc = "Introduction to Computation and Programming using Python"
crsKeys = getKeywords(course_desc)
crsKeys = ','.join(crsKeys)
course = nlp(crsKeys)
skills = nlp("Coding, Data Analytics, Python, Web Development, English")
sc = skills.similarity(course)
print(sc)



"""
Similarly for a large set of jobs and courses,
Two recommendation lists will be calculated each for jobs and courses.
These will be calculated as follows:
1. The similarities will be calculated for each course/job keywords with the
    user skillset keywords (extracted from his resum/profile).
2. The similarities would be ranked and the top 10 (or as required) jobs/courses
    would be displayed.


As soon as the job-seeker's profile would be created and resume will be uploaded.
The keywords will be extracted from the profile/resume.
Now, the web crawler will fetch relevant courses on the basis of skillsets mentioned by the job-seeker.
These courses will be ranked by the recommendation engine.
Then, the courses will be displayed.
Same will be performed with jobs, with a difference that jobs will be fetched from the job database.

"""