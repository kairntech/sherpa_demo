import streamlit as st
from sherpa_streamlit import visualize

default_text = """This is a sample text.
With two lines.
"""
visualize(default_text,
          favorite_only=False,
          show_connection=False,
          project_selector_title="Select demo",
          annotator_selector_title="Select variant",
          sidebar_title="KAIRNTECH Sherpa",
          sidebar_description="Customizable Sherpa demonstration")
