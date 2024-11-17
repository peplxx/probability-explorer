import numpy as np
import matplotlib.pyplot as plt
from ..base import Experiment
import streamlit as st

class CoinFlipExperiment(Experiment):
    def run(self):
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            num_flips = st.slider("Number of flips", 1, 10000, 100)
            flips = np.random.choice(['Heads', 'Tails'], size=num_flips)
            unique, counts = np.unique(flips, return_counts=True)
            probabilities = dict(zip(unique, counts/num_flips))
            st.metric("Heads Probability", f"{probabilities.get('Heads', 0):.3f}")
            st.metric("Tails Probability", f"{probabilities.get('Tails', 0):.3f}")
            
        with col2:
            fig, ax = plt.subplots()
            ax.bar(probabilities.keys(), probabilities.values())
            ax.set_ylabel('Probability')
            ax.set_title(f'Probability Distribution ({num_flips} flips)')
            st.pyplot(fig)
            
        with col3:
            st.write("Coin Flip Properties:")
            st.write("""
            - Each flip is independent
            - Probability of heads = 0.5
            - Probability of tails = 0.5
            - Expected value = 0.5
            - Variance = 0.25
            """)
            st.markdown("📚 **Learn More:** [Coin Flipping Probability](https://en.wikipedia.org/wiki/Coin_flipping#Physics)")
    
    def get_description(self) -> str:
        return "Simulate coin flips and observe probability distribution"
