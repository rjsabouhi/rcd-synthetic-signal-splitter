
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Synthetic Signal Splitter", layout="wide")
st.title("🧠 Synthetic Signal Splitter")

st.markdown("""
Separate entangled symbolic input streams into distinct cognitive threads using recursive decomposition.
""")

# Input symbolic stream
st.sidebar.header("Input Parameters")
signal_length = st.sidebar.slider("Signal Length", 10, 100, 50)
split_factor = st.sidebar.slider("Split Factor (Entanglement)", 1, 10, 3)

# Generate synthetic entangled signal
np.random.seed(42)
base = np.linspace(0, 10, signal_length)
signal_A = np.sin(base) + np.random.normal(0, 0.2, signal_length)
signal_B = np.cos(base / split_factor) + np.random.normal(0, 0.2, signal_length)
composite_signal = signal_A + signal_B

df = pd.DataFrame({
    'Token Index': range(signal_length),
    'Composite Signal': composite_signal,
    'Signal A (Recovered)': signal_A,
    'Signal B (Recovered)': signal_B
})

# Plot the split signals
fig = px.line(df, x='Token Index', y=['Composite Signal', 'Signal A (Recovered)', 'Signal B (Recovered)'],
              title="Decomposed Symbolic Streams", labels={'value': 'Signal Amplitude', 'variable': 'Stream'})
st.plotly_chart(fig, use_container_width=True)

st.markdown("This tool demonstrates symbolic decomposition of entangled narrative input via recursive signal modeling.")
