import numpy as np
from scipy.stats import randint
import streamlit as st
from ..base import Distribution

class UniformDiscreteDistribution(Distribution):
    def get_parameters(self):
        st.write('Distribution Parameters:')
        self.low = st.slider('Low (a)', -10, 10, 0)
        self.high = st.slider('High (b)', self.low + 1, 20, 10)
        
        return {
            'low': self.low,
            'high': self.high
        }

    def plot(self, ax):
        x = np.arange(self.low, self.high + 1)
        rv = randint(self.low, self.high + 1)
        pmf = rv.pmf(x)
        ax.bar(x, pmf)
        ax.set_xlabel('Value')
        ax.set_ylabel('Probability')
        ax.set_title('Discrete Uniform Distribution')

    def get_formula(self):
        return r'P(X=k) = \frac{1}{b-a+1} \quad \text{for } k \in \{a,\ldots,b\}'

    def get_properties(self, st):
        st.write("""
        The **Discrete Uniform Distribution** models a random variable that can take on a finite number of equally likely values.
        
        Parameters:
        - **a**: Lower bound (inclusive)
        - **b**: Upper bound (inclusive)
        
        Key Properties:
        - **Support**: {a, a+1, ..., b}
        - **Mean**: (a + b)/2
        - **Variance**: ((b - a + 1)² - 1)/12
        
        The probability mass function (PMF) is given by:
        """)
        
        st.latex(r'P(X=k) = \frac{1}{b-a+1} \quad \text{for } k \in \{a,\ldots,b\}')
        
        st.write("""
        Applications:
        - Rolling a fair die
        - Random selection from a finite set
        - Simple random sampling
        - Basic randomization algorithms
        """)
