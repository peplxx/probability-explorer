import numpy as np
from scipy.stats import chi2
import streamlit as st
from ..base import Distribution

class ChiSquaredDistribution(Distribution):
    def get_parameters(self):
        self.df = st.slider('Degrees of freedom', 1, 30, 1)
        return {'df': self.df}

    def plot(self, ax):
        x = np.linspace(0, max(30, self.df*3), 200)
        y = chi2.pdf(x, self.df)
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('Probability Density')

    def get_formula(self):
        return r'f(x) = \frac{1}{2^{k/2}\Gamma(k/2)}x^{k/2-1}e^{-x/2}'

    def get_properties(self):
        return """
        - Support is x > 0 
        - Mean equals degrees of freedom (k)
        - Variance equals 2k
        - Right-skewed distribution
        - Sum of k squared standard normal variables
        """
