import numpy as np
import matplotlib.pyplot as plt
from ..base import Experiment
import streamlit as st

class MarkovChainExperiment(Experiment):
    def run(self):
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            num_steps = st.slider("Number of steps", 10, 1000, 100)
            
            # Define transition matrix
            states = ['A', 'B', 'C']
            transition_matrix = np.array([
                [0.7, 0.2, 0.1],  # A -> A,B,C
                [0.3, 0.5, 0.2],  # B -> A,B,C 
                [0.2, 0.3, 0.5]   # C -> A,B,C
            ])
            
            # Simulate Markov chain
            current_state = 0  # Start in state A
            states_history = [current_state]
            
            for _ in range(num_steps):
                current_state = np.random.choice(3, p=transition_matrix[current_state])
                states_history.append(current_state)
            
            # Calculate state frequencies
            unique, counts = np.unique(states_history, return_counts=True)
            frequencies = dict(zip(states, counts / len(states_history)))
            
            for state, freq in frequencies.items():
                st.metric(f"State {state} Frequency", f"{freq:.3f}")
            
        with col2:
            fig, ax = plt.subplots()
            ax.plot(range(len(states_history)), [states[s] for s in states_history])
            ax.set_xlabel('Time Steps')
            ax.set_ylabel('State')
            ax.set_title('Markov Chain State Transitions')
            st.pyplot(fig)
            
        with col3:
            st.write("Markov Chain Properties:")
            st.write("""
            - Memoryless process
            - Next state depends only on current state
            - Transition probabilities are fixed
            - Can reach steady state distribution
            - Used in:
                - Weather prediction
                - Natural language processing
                - Page rank algorithm
            """)
            st.markdown("📚 **Learn More:** [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain)")
    
    def get_description(self) -> str:
        return "Simulate a simple Markov chain and observe state transitions"
