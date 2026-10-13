import pandas as pd
import numpy as np
import streamlit as st
import kagglehub
from pathlib import Path
import os

path = kagglehub.dataset_download("zalando-research/fashionmnist", path="fashion-mnist_train.csv")
print(path)
print(os.path.getsize(path) / (1024 * 1024), "MB")

st.write(path)
st.write(os.path.getsize(path))
