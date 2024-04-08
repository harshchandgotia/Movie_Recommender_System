# Movie_Recommender_System

This project introduces a Movie Recommendation System implemented using machine learning techniques and deployed on a website via the Streamlit library. The system utilizes a dataset containing 5000 movies, with attributes including overview, crew cast, and genres.

Key Components:

Data Preprocessing:
The dataset undergoes preprocessing to handle missing values and irrelevant features, ensuring data quality.
Text data is cleaned by removing punctuation, stop words, and converting text to lowercase for consistency.
The PorterStemmer technique is applied to address variations in words, enhancing the accuracy of text analysis.

Text Vectorization:
CountVectorizer is employed to transform textual features such as movie overviews into numerical representations.
Tokenization breaks down text into individual words, while counting calculates the frequency of each word.
The resulting matrix represents the occurrence of words in each movie's overview, facilitating similarity assessment.

Deployment using Streamlit:
The model is deployed on a website using Streamlit, allowing users to interactively explore movie recommendations.
