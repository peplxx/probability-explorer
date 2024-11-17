import numpy as np
import matplotlib.pyplot as plt
from ..base import Experiment
import streamlit as st

class RandomWalkExperiment(Experiment):
    def run(self):
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            num_steps = st.slider("Number of steps", 1, 1000, 100)
            num_walks = st.slider("Number of walks", 1, 100, 10)
            
            # Generate random walks
            steps = np.random.choice([-1, 1], size=(num_walks, num_steps))
            walks = np.cumsum(steps, axis=1)
            
            # Calculate statistics
            final_positions = walks[:, -1]
            mean_position = np.mean(final_positions)
            std_position = np.std(final_positions)
            
            st.metric("Mean Final Position", f"{mean_position:.2f}")
            st.metric("Standard Deviation", f"{std_position:.2f}")
            
        with col2:
            fig, ax = plt.subplots()
            time_points = np.arange(num_steps)
            for walk in walks:
                ax.plot(time_points, walk, alpha=0.5)
            ax.set_xlabel('Time Steps')
            ax.set_ylabel('Position')
            ax.set_title(f'Random Walks (n={num_walks})')
            st.pyplot(fig)
            
        with col3:
            st.write("Random Walk Properties:")
            st.write("""
            - Each step is independent
            - Equal probability of +1 or -1 step
            - Expected final position = 0
            - Variance grows with number of steps
            - Distance from origin ~ √n steps
            """)
            st.markdown("📚 **Learn More:** [Random Walk](https://en.wikipedia.org/wiki/Random_walk)")
    
    def get_description(self) -> str:
        return "Simulate random walks and observe their statistical properties"
