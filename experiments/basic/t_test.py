import numpy as np
import matplotlib.pyplot as plt
from ..base import Experiment
import streamlit as st
from scipy import stats

class TTestExperiment(Experiment):
    def run(self):
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            sample_size = st.slider("Sample size", 10, 1000, 100)
            effect_size = st.slider("Effect size", 0.0, 2.0, 0.5)
            
            # Generate two samples
            sample1 = np.random.normal(0, 1, sample_size)
            sample2 = np.random.normal(effect_size, 1, sample_size)
            
            # Perform t-test
            t_stat, p_value = stats.ttest_ind(sample1, sample2)
            
            st.metric("t-statistic", f"{t_stat:.4f}")
            st.metric("p-value", f"{p_value:.4f}")
            st.metric("Significant?", "Yes" if p_value < 0.05 else "No")
            
        with col2:
            fig, ax = plt.subplots()
            ax.hist(sample1, bins=30, alpha=0.5, label='Sample 1')
            ax.hist(sample2, bins=30, alpha=0.5, label='Sample 2')
            ax.axvline(np.mean(sample1), color='blue', linestyle='--')
            ax.axvline(np.mean(sample2), color='orange', linestyle='--')
            ax.set_xlabel('Value')
            ax.set_ylabel('Frequency')
            ax.set_title('Sample Distributions')
            ax.legend()
            st.pyplot(fig)
            
        with col3:
            st.write("T-Test Properties:")
            st.write("""
            - Tests difference between means
            - Assumes normal distribution
            - Null hypothesis: means are equal
            - p < 0.05 suggests significant difference
            - Effect size impacts test power
            """)
            st.markdown("📚 **Learn More:** [Student's t-test](https://en.wikipedia.org/wiki/Student%27s_t-test)")
    
    def get_description(self) -> str:
        return "Demonstrate Student's t-test for comparing two samples"
