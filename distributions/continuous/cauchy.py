import numpy as np
from scipy.stats import cauchy
import streamlit as st
from ..base import Distribution

class CauchyDistribution(Distribution):
    def get_parameters(self):
        self.loc = st.slider('Location (x₀)', -10.0, 10.0, 0.0, 0.1)
        self.scale = st.slider('Scale (γ)', 0.1, 10.0, 1.0, 0.1)
        return {'loc': self.loc, 'scale': self.scale}

    def plot(self, ax):
        x = np.linspace(self.loc - 10*self.scale, self.loc + 10*self.scale, 1000)
        y = cauchy.pdf(x, loc=self.loc, scale=self.scale)
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('Probability Density')

    def get_formula(self):
        return r'f(x) = \frac{1}{\pi\gamma[1 + (\frac{x-x_0}{\gamma})^2]}'

    def get_properties(self, st):
        st.write("""
        The **Cauchy Distribution** is a continuous probability distribution that describes the ratio of two normally distributed variables. 
        It is characterized by two parameters:
        - **x₀ (location)**: the peak of the distribution
        - **γ (scale)**: controls the width/spread
        
        Key Properties:
        - **Support**: x ∈ (-∞,∞)
        - **Mean**: undefined (does not exist)
        - **Variance**: undefined (does not exist)
        - **Heavy-tailed** distribution
        - **Stable distribution**
        
        The probability density function (PDF) is given by:
        """)
        
        st.latex(r'f(x) = \frac{1}{\pi\gamma[1 + (\frac{x-x_0}{\gamma})^2]}')
        
        st.write("""
        Common applications:
        - **Physics**: describing resonance behavior
        - **Engineering**: modeling noise in communication systems
        - **Finance**: modeling price fluctuations
        - **Statistics**: as a pathological example in estimation theory
        
        Important links:
        - [**Properties**](https://en.wikipedia.org/wiki/Cauchy_distribution#Properties)
        - [**Applications**](https://en.wikipedia.org/wiki/Cauchy_distribution#Occurrence_and_applications)
        - [**Relationship to other distributions**](https://en.wikipedia.org/wiki/Cauchy_distribution#Related_distributions)
        """)
