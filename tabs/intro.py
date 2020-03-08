from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Introduction

This web app enables users to enter various combinations of effects and flavors for over 2,300 marijuana strains and returns five recommended stains meeting the users criteria.

#### Dataset

The dataset used for the app is from the Cannabis Strains Marijuana Dataset from LiamLarsen in Kaggle.  It contains 2,350 strains of marijuana.  Each strain has a combination of effects and flavors (among other features) that are used in the app.  There are 16 unique effects and 50 unique flavors.

""")]
