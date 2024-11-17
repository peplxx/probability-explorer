import numpy as np
import matplotlib.pyplot as plt
from ..base import Experiment
import streamlit as st

class CentralLimitExperiment(Experiment):
    def run(self):
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            num_samples = st.slider("Number of samples", 100, 10000, 1000)
            sample_size = st.slider("Sample size", 1, 100, 30)
            distribution = st.selectbox(
                "Distribution",
                ["Uniform", "Exponential", "Poisson"]
            )
            
            # Generate samples based on selected distribution
            if distribution == "Uniform":
                samples = np.random.uniform(0, 1, (num_samples, sample_size))
            elif distribution == "Exponential":
                samples = np.random.exponential(1, (num_samples, sample_size))
            else:  # Poisson
                samples = np.random.poisson(1, (num_samples, sample_size))
                
            # Calculate sample means
            sample_means = np.mean(samples, axis=1)
            
            # Calculate statistics
            population_mean = np.mean(sample_means)
            population_std = np.std(sample_means)
            
            st.metric("Sample Mean", f"{population_mean:.4f}")
            st.metric("Sample Standard Deviation", f"{population_std:.4f}")
            
        with col2:
            fig, ax = plt.subplots()
            ax.hist(sample_means, bins=30, density=True)
            ax.set_xlabel('Sample Mean')
            ax.set_ylabel('Density')
            ax.set_title(f'Distribution of Sample Means\n({distribution} Distribution)')
            st.pyplot(fig)
            
        with col3:
            st.write("Central Limit Theorem Properties:")
            st.write("""
            - Sample means approach normal distribution
            - True for any original distribution
            - Convergence improves with:
                - Larger sample sizes
                - More samples
            - Mean of sample means ≈ population mean
            - Standard error = σ/√n
            """)
            st.markdown("📚 **Learn More:** [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)")
    
    def get_description(self) -> str:
        return "Demonstrate the Central Limit Theorem with different distributions"
