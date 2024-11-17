import numpy as np
import matplotlib.pyplot as plt
from ..base import Experiment
import streamlit as st

class MonteCarloExperiment(Experiment):
    def run(self):
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            num_points = st.slider("Number of points", 100, 10000, 1000)
            x = np.random.uniform(-1, 1, num_points)
            y = np.random.uniform(-1, 1, num_points)
            distances = np.sqrt(x**2 + y**2)
            inside_circle = distances <= 1
            pi_estimate = 4 * np.sum(inside_circle) / num_points
            st.metric("π Estimate", f"{pi_estimate:.6f}")
            st.metric("Actual π", f"{np.pi:.6f}")
            st.metric("Error", f"{abs(pi_estimate - np.pi):.6f}")
            
        with col2:
            fig, ax = plt.subplots()
            ax.scatter(x[inside_circle], y[inside_circle], c='blue', label='Inside')
            ax.scatter(x[~inside_circle], y[~inside_circle], c='red', label='Outside')
            ax.set_aspect('equal')
            ax.legend()
            st.pyplot(fig)
            
        with col3:
            st.write("Monte Carlo Method Properties:")
            st.write("""
            - Uses random sampling to estimate π
            - Area of circle = πr²
            - Area of square = (2r)²
            - Ratio = π/4
            - Accuracy improves with more points
            """)
            st.markdown("📚 **Learn More:** [Monte Carlo Methods](https://en.wikipedia.org/wiki/Monte_Carlo_method)")
    
    def get_description(self) -> str:
        return "Estimate π using Monte Carlo simulation"