# strains-live
Content-based Recommendation Using TF-IDF and k-NN

The contents include the following:

data - The data directory

- cannabis.csv - The Cannabis Strains dataset posted on Kaggle by LiamLarsen consisting of 2,350 unique cannabis strains.

model - The model directory

- dtm.pkl - The pickled document-term matrix
- tf.pkl - The pickled tf-idf vectorizer
- tf_knn.ipynb - The Jupyter notebook containing the TF-IDF and k-NN code

tabs - The tabs directory

- about.py - The about tab Dash code
- intro.py - The intro tab Dash code
- recommend.py - The recommend tab Dash code and recommendation code

The main app

- Procfile - The Procfile for Heroku
- app.py - Initiates the Dash app
- index.py - The main Dash code with the layout and callback
- requirements.txt - The requirements.txt file for Heroku


