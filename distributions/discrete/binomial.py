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

    def get_properties(self, st):
        st.write("""
        The **Binomial Distribution** models the number of successes in a fixed number of independent trials.
        It is characterized by two parameters:
        - **n (number of trials)**: total number of independent experiments
        - **p (probability of success)**: probability of success on each trial
        
        Key Properties:
        - **Support**: k ∈ {0,1,...,n}
        - **Mean**: np
        - **Variance**: np(1-p)
        - **Independent trials** (no memory between trials)
        - **Fixed probability** of success for each trial
        
        The probability mass function (PMF) is given by:
        """)
        
        st.latex(r'P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}')
        
        st.write("""
        Common applications:
        - **Quality control** (number of defective items)
        - **Clinical trials** (number of successful treatments)
        - **Polling and surveys** (number of positive responses)
        - **Genetics** (inheritance patterns)
        
        Important links:
        - [**Properties**](https://en.wikipedia.org/wiki/Binomial_distribution#Properties)
        - [**Applications**](https://en.wikipedia.org/wiki/Binomial_distribution#Applications)
        - [**Relationship to other distributions**](https://en.wikipedia.org/wiki/Binomial_distribution#Related_distributions)
        """)
