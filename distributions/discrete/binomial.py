import numpy as np
from scipy.stats import binom
import streamlit as st
from ..base import Distribution

class BinomialDistribution(Distribution):
    def get_parameters(self):
        self.n = st.slider('Number of trials (n)', 1, 100, 10)
        self.p = st.slider('Probability of success (p)', 0.0, 1.0, 0.5, 0.01)
        return {'n': self.n, 'p': self.p}

    def plot(self, ax):
        x = np.arange(0, self.n + 1)
        y = binom.pmf(x, self.n, self.p)
        ax.bar(x, y, alpha=0.8)
        ax.set_xlabel('Number of Successes')
        ax.set_ylabel('Probability')

    def get_formula(self):
        return r'P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}'

    def get_properties(self):
        return """
        - Models number of successes in n independent trials
        - Each trial has probability p of success
        - Mean = np
        - Variance = np(1-p)
        - Support is k ∈ {0,1,...,n}
        """
