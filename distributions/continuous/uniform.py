import numpy as np
import streamlit as st
from ..base import Distribution

class UniformDistribution(Distribution):
    def get_parameters(self):
        self.a = st.slider('Lower bound (a)', -10.0, 10.0, 0.0, 0.1)
        self.b = st.slider('Upper bound (b)', -10.0, 10.0, 1.0, 0.1)
        if self.b <= self.a:
            st.error('Upper bound must be greater than lower bound')
            self.b = self.a + 0.1
        return {'a': self.a, 'b': self.b}

    def plot(self, ax):
        x = np.linspace(self.a - 0.5, self.b + 0.5, 100)
        y = np.where((x >= self.a) & (x <= self.b), 1/(self.b-self.a), 0)
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('Probability Density')

    def get_formula(self):
        return r'f(x) = \frac{1}{b-a} \text{ for } a \leq x \leq b'

    def get_properties(self, st):
        st.write("""
        The **Uniform Distribution** is the simplest continuous probability distribution.
        It is characterized by two parameters:
        - **a (lower bound)**: minimum value of the interval
        - **b (upper bound)**: maximum value of the interval
        
        Key Properties:
        - **Constant probability density** of 1/(b-a) over interval [a,b]
        - **Zero probability density** outside interval [a,b]
        - **Mean = (a+b)/2**
        - **Variance = (b-a)²/12**
        - **Maximum entropy** continuous distribution for a bounded interval
        - **All points in interval are equally likely**
        
        The probability density function (PDF) is given by:
        """)
        
        st.latex(r'f(x) = \begin{cases} \frac{1}{b-a} & \text{for } a \leq x \leq b \\ 0 & \text{otherwise} \end{cases}')
        
        st.write("""
        The cumulative distribution function (CDF) is:
        """)
        
        st.latex(r'F(x) = \begin{cases} 0 & \text{for } x < a \\ \frac{x-a}{b-a} & \text{for } a \leq x \leq b \\ 1 & \text{for } x > b \end{cases}')
        
        st.write("""
        Common applications:
        - **Random number generation**
        - **Prior distribution in Bayesian inference**
        - **Modeling random errors**
        - **Simple random sampling**
        
        Important links:
        - [**Properties**](https://en.wikipedia.org/wiki/Continuous_uniform_distribution#Properties)
        - [**Applications**](https://en.wikipedia.org/wiki/Continuous_uniform_distribution#Applications)
        - [**Relationship to other distributions**](https://en.wikipedia.org/wiki/Continuous_uniform_distribution#Related_distributions)
        """)
