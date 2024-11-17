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

    def get_properties(self, st):
        st.write("""
        The **Chi-squared distribution** is a continuous probability distribution that is commonly used in statistical inference.
        It is characterized by one parameter:
        - **k (degrees of freedom)**: determines the shape of the distribution
        
        Key Properties:
        - **Support is x > 0** (non-negative values only)
        - **Mean equals degrees of freedom (k)**
        - **Variance equals 2k**
        - **Right-skewed distribution**
        - **Sum of k squared standard normal variables**
        
        The probability density function (PDF) is given by:
        """)
        
        st.latex(r'f(x) = \frac{1}{2^{k/2}\Gamma(k/2)}x^{k/2-1}e^{-x/2}')
        
        st.write("""
        Common applications include:
        - **Goodness-of-fit tests**
        - **Testing independence in contingency tables**
        - **Confidence intervals for population variance**
        - **Component in other distributions** (e.g., F-distribution)
        
        Important links:
        - [**Properties**](https://en.wikipedia.org/wiki/Chi-square_distribution#Properties)
        - [**Applications**](https://en.wikipedia.org/wiki/Chi-square_distribution#Applications)
        """)
