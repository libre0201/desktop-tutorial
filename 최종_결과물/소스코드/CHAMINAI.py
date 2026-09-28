"""Backward-compatible Streamlit launcher.

Run:
    streamlit run CHAMINAI.py
"""
import streamlit as st
import os
os.environ.update(st.secrets)

from chaminai_app.app import main

if __name__ == "__main__":
    main()