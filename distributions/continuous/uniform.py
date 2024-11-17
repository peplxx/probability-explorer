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

    def get_properties(self):
        return """
        - Constant probability density over interval [a,b]
        - Mean = (a+b)/2
        - Variance = (b-a)²/12
        - Maximum entropy continuous distribution for interval [a,b]
        - All points in interval equally likely
        """
