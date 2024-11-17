import numpy as np
import matplotlib.pyplot as plt
from ..base import Experiment
import streamlit as st

class DiceExperiment(Experiment):
    def run(self):
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            num_rolls = st.slider("Number of rolls", 1, 10000, 100)
            num_dice = st.slider("Number of dice", 1, 4, 1)
            rolls = np.sum(np.random.randint(1, 7, size=(num_rolls, num_dice)), axis=1)
            unique, counts = np.unique(rolls, return_counts=True)
            probabilities = dict(zip(unique, counts/num_rolls))
            
            expected_value = np.mean(rolls)
            variance = np.var(rolls)
            st.metric("Expected Value", f"{expected_value:.2f}")
            st.metric("Variance", f"{variance:.2f}")
            
        with col2:
            fig, ax = plt.subplots()
            ax.bar(probabilities.keys(), probabilities.values())
            ax.set_xlabel('Sum of Dice')
            ax.set_ylabel('Probability')
            ax.set_title(f'Probability Distribution ({num_rolls} rolls, {num_dice} dice)')
            st.pyplot(fig)
            
        with col3:
            st.write("Dice Roll Properties:")
            st.write(f"""
            - Each die has 6 faces (1-6)
            - Each roll is independent
            - For {num_dice} dice:
                - Min sum: {num_dice}
                - Max sum: {6*num_dice}
                - Theoretical E[X]: {3.5*num_dice:.1f}
                - Theoretical Var[X]: {(35/12)*num_dice:.2f}
            """)
            st.markdown("📚 **Learn More:** [Dice Probability](https://en.wikipedia.org/wiki/Dice#Probability)")
    
    def get_description(self) -> str:
        return "Simulate dice rolls and observe probability distributions"
