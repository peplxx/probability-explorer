import numpy as np
from scipy.stats import multivariate_normal, chi2
import streamlit as st
from ..base import Distribution

class NormalDistribution(Distribution):
    def get_parameters(self):
        self.mean = st.slider('Mean', -10.0, 10.0, 0.0, 0.1)
        self.std = st.slider('Standard deviation', 0.1, 5.0, 1.0, 0.1)
        return {'mean': self.mean, 'std': self.std}

    def plot(self, ax):
        x = np.linspace(self.mean - 4*self.std, self.mean + 4*self.std, 100)
        y = np.exp(-((x - self.mean)**2)/(2*self.std**2))/(self.std*np.sqrt(2*np.pi))
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('Probability Density')

    def get_formula(self):
        return r'f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}'

    def get_properties(self):
        return """
        - Symmetric about mean
        - 68-95-99.7 rule applies
        - Bell-shaped curve
        - Infinite support
        """