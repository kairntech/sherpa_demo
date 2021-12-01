import streamlit as st
from sherpa_streamlit import visualize

default_text = """This is a sample text.
With two lines.
"""
visualize(default_text,
          favorite_only=True,
          sidebar_title="KAIRNTECH Sherpa",
          sidebar_description="Customizable Sherpa demonstration")
