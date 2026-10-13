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

df = df-df.mean()

st.write('''## After mean-centring''')
st.scatter_chart(df.iloc[:5000], x="pixel1", y="label")

c = (df.T@df)/len(df)-df.mean()@df.mean().T

lam,v = np.linalg.eigh(c)

idx = np.argsort(lam)[::-1]
lam = lam[idx]
v = v[:, idx]

w = v[:,:2]
x = df@w

fig, ax = plt.subplots()

scatter = ax.scatter(x.iloc[:,0], x.iloc[:,1], c = df["label"], s=1, alpha=0.5, cmap="tab10")

ax.set_title("MNIST Data visulization")
fig.colorbar(scatter, ax=ax, label="digital")

st.pyplot(fig)
plt.close(fig)
