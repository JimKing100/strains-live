from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### About

Marijuana is used for both medical and recreational purposes in the U.S. The two main strains, indica and sativa, have been joined with newer hybrid strains.  Each strain has a unique combination of effects and flavors.  In general, indica strains provide a sense of relaxation and euphoria while sativas provide a sense of energy and alertness.  Hybrids can combine effects of both indica and sativa.

Indica strains are often used for medical purposes because of their ability to reduce inflammation and provide temporary relief from pain.  Examples of popular indica strains are Northern Lights, Bubble Kush, Pineapple Kush and Pineapple Chunk.

Sativa strains are often favorites of recreational users due to their uplifting and energetic high they provide.  Medically, they are often used to treat certain mental conditions such depression, anxiety and bipolar disorder.  Examples of popular sativa strains are Jack Herer, Candyland, Island Sweet Skunk and Green Crack.

Hybrid strains are the result of crossing indica and sativa and popular strains include Lemon Diesel, OG Kush, THC Bomb, Sunset Sherbet, Blue Dream, Pineapple express and Sour Grape.
""")]
