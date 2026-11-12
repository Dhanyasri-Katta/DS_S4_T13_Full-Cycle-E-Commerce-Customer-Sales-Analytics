import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')

print("----- Text Preprocessing -----")

text = "The movie was amazing, exciting, and full of action scenes!"

text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
tokens = word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_tokens = [
    word for word in tokens
    if word not in stop_words
]
print("Original Text:")
print("The movie was amazing, exciting, and full of action scenes!")
print("\nProcessed Tokens:")
print(filtered_tokens)
print("\n\n----- Content-Based Recommendation -----")

movies = pd.DataFrame({
    'Movie': [
        'Avengers',
        'Batman',
        'Superman',
        'Titanic',
        'Inception'
    ],    
    'Description': [
        'action superhero marvel fight',
        'dark superhero action detective',
        'superhero flying action hero',
        'romance ship love drama',
        'dream science fiction thriller'
    ]
})
print("Movie Dataset:")
print(movies)
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(movies['Description'])

similarity = cosine_similarity(tfidf_matrix)

movie_name = 'Batman'

movie_index = movies[movies['Movie'] == movie_name].index[0]

scores = list(enumerate(similarity[movie_index]))
sorted_scores = sorted(
    scores,
    key=lambda x: x[1],
    reverse=True
)
print("\nRecommended Movies for Batman:")
for i in sorted_scores[1:4]:
    print(movies.iloc[i[0]]['Movie'])
