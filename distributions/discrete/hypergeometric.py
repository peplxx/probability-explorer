import numpy as np
from scipy.stats import hypergeom
import streamlit as st
from ..base import Distribution
import matplotlib.pyplot as plt

class HypergeometricDistribution(Distribution):
    def get_parameters(self):
        st.write('Population Parameters:')
        self.N = st.slider('N (population size)', 1, 100, 50)
        self.K = st.slider('K (number of success states)', 0, self.N, 20)
        self.n = st.slider('n (number of draws)', 0, self.N, 10)
        
        return {
            'N': self.N,
            'K': self.K, 
            'n': self.n
        }

    def plot(self, ax):
        x = np.arange(0, min(self.n, self.K) + 1)
        rv = hypergeom(self.N, self.K, self.n)
        pmf = rv.pmf(x)
        ax.bar(x, pmf)
        ax.set_xlabel('Number of Successes')
        ax.set_ylabel('Probability')
        ax.set_title('Hypergeometric Distribution')

    def get_formula(self):
        return r'P(X=k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}'

    def get_properties(self, st):
        st.write("""
        The **Hypergeometric Distribution** models the probability of obtaining k successes in n draws without replacement from a population of size N containing K successes.
        
        Parameters:
        - **N**: Population size
        - **K**: Number of success states in the population
        - **n**: Number of draws
        - **k**: Number of observed successes
        
        Key Properties:
        - **Support**: max(0, n-(N-K)) ≤ k ≤ min(n, K)
        - **Mean**: n(K/N)
        - **Variance**: n(K/N)(1-K/N)((N-n)/(N-1))
        
        The probability mass function (PMF) is given by:
        """)
        
        st.latex(r'P(X=k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}')
        
        st.write("""
        Applications:
        - Quality control sampling
        - Random sampling in finite populations
        - Card drawing problems
        - Population sampling
        """)
 