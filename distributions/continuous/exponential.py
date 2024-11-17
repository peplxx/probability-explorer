import numpy as np
from scipy.stats import expon
import streamlit as st
from ..base import Distribution

class ExponentialDistribution(Distribution):
    def get_parameters(self):
        self.rate = st.slider('Rate parameter (λ)', 0.1, 5.0, 1.0, 0.1)
        return {'rate': self.rate}

    def plot(self, ax):
        x = np.linspace(0, 5/self.rate, 200)
        y = self.rate * np.exp(-self.rate * x)
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('Probability Density')

    def get_formula(self):
        return r'f(x) = \lambda e^{-\lambda x}'

    def get_properties(self, st):
        st.write("""
        The **Exponential Distribution** is a continuous probability distribution that describes the time between events in a Poisson point process.
        It is characterized by one parameter:
        - **λ (rate parameter)**: determines the rate of decay
        
        Key Properties:
        - **Support is x ≥ 0** (non-negative values only)
        - **Mean = 1/λ**
        - **Variance = 1/λ²**
        - **Memoryless property**: P(X > s + t | X > s) = P(X > t)
        - **Maximum entropy** distribution for a given mean
        
        The probability density function (PDF) is given by:
        """)
        
        st.latex(r'f(x) = \lambda e^{-\lambda x} \text{ for } x \geq 0')
        
        st.write("""
        The cumulative distribution function (CDF) is:
        """)
        
        st.latex(r'F(x) = 1 - e^{-\lambda x} \text{ for } x \geq 0')
        
        st.write("""
        Common applications:
        - **Lifetime/survival analysis**
        - **Time between events**
        - **Reliability engineering**
        - **Queueing theory**
        
        Important links:
        - [**Properties**](https://en.wikipedia.org/wiki/Exponential_distribution#Properties)
        - [**Applications**](https://en.wikipedia.org/wiki/Exponential_distribution#Applications)
        - [**Relationship to other distributions**](https://en.wikipedia.org/wiki/Exponential_distribution#Related_distributions)
        """)
