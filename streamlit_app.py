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

df = pd.read_csv(path)

st.write('''## Before mean-centring''')
st.scatter_chart(df.iloc[:5000], x="pixel1", y="label")

st.write('''## After mean-centring''')
st.scatter_chart(df.iloc[:5000], x="pixel1", y="label")

c = (df.T@df)/len(df)-df.mean()@df.mean().T

lam,v = np.linalg.eigh(c)

idx = np.argsort(lam)[::-1]
lam = lam[idx]
v = v[:, idx]


