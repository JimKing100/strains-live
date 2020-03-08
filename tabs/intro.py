from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Introduction

This web app enables users to enter various combinations of effects and flavors for over 2,300 marijuana strains and returns five recommended stains meeting the users criteria.  Click on the Recommend tab to obtain recommendations.

#### Methodology

The effects and features for the 2,300+ marijuana strains are tokenized and vectorized using Term Frequency-Inverse Document Frequency (TF-IDF) to create a document-term matrix (dtm).  The dtm is then fit on a Nearest Neighbors model.  The model is then used to obtain the 5 closest matching strains based on the users selections of 5 effects and 3 flavors (8 features).

#### Dataset

The dataset used for the app is from the Cannabis Strains Marijuana Dataset from LiamLarsen in Kaggle.  It contains 2,350 strains of marijuana.  Each strain has a combination of effects and flavors (among other features) that are used in the app.  There are 16 unique effects and 50 unique flavors.

""")]
