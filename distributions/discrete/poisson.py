import numpy as np
from scipy.stats import poisson
import streamlit as st
from ..base import Distribution

class PoissonDistribution(Distribution):
    def get_parameters(self):
        self.lambda_ = st.slider('Rate parameter (λ)', 0.1, 20.0, 5.0, 0.1)
        return {'lambda_': self.lambda_}

    def plot(self, ax):
        x = np.arange(0, max(20, int(self.lambda_*3)))
        y = poisson.pmf(x, self.lambda_)
        ax.bar(x, y, alpha=0.8)
        ax.set_xlabel('Number of Events')
        ax.set_ylabel('Probability')

    def get_formula(self):
        return r'P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}'

    def get_properties(self):
        return """
        - Models number of events in fixed time/space interval
        - Events occur independently at constant rate
        - Mean = Variance = λ 
        - Support is k ∈ {0,1,2,...}
        - Limit of binomial as n→∞, p→0 with np=λ
        """
