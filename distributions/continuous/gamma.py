
import numpy as np
from scipy.stats import gamma
import streamlit as st
from ..base import Distribution
import matplotlib.pyplot as plt

class GammaDistribution(Distribution):
    def get_parameters(self):
        st.write('Shape and Scale Parameters:')
        self.alpha = st.slider('α (shape)', 0.1, 10.0, 2.0, 0.1)
        self.beta = st.slider('β (scale)', 0.1, 10.0, 1.0, 0.1)
        
        return {
            'alpha': self.alpha,
            'beta': self.beta
        }

    def plot(self, ax):
        x = np.linspace(0, 20, 1000)
        rv = gamma(self.alpha, scale=self.beta)
        y = rv.pdf(x)
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('Probability Density')
        ax.set_title('Gamma Distribution')

    def get_formula(self):
        return r'f(x;\alpha,\beta) = \frac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-x/\beta}'

    def get_properties(self, st):
        st.write("""
        The **Gamma Distribution** is a continuous probability distribution with two parameters:
        - **α (alpha)**: shape parameter
        - **β (beta)**: scale parameter
        
        Key Properties:
        - **Support**: x > 0
        - **Mean**: αβ
        - **Variance**: αβ²
        - **Skewness**: 2/√α
        - **Kurtosis**: 6/α + 3
        
        The probability density function (PDF) is given by:
        """)
        
        st.latex(r'f(x;\alpha,\beta) = \frac{1}{\Gamma(\alpha)\beta^\alpha}x^{\alpha-1}e^{-x/\beta}')
        
        st.write("""
        where:
        - **Γ(α)** is the gamma function
        - **x > 0** is the support
        - **α > 0** is the shape parameter
        - **β > 0** is the scale parameter
        
        Applications:
        - Modeling waiting times
        - Reliability analysis
        - Financial risk modeling
        - Rainfall amounts
        """)
