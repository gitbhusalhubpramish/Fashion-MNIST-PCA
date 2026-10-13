import pandas as pd
import numpy as np
import streamlit as st
import kagglehub
from pathlib import Path

path = kagglehub.dataset_download("zalando-research/fashionmnist", path="fashion-mnist_train.csv")
print(path)
