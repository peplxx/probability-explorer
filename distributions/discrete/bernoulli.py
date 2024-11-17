import numpy as np
from scipy.stats import bernoulli
import streamlit as st
from ..base import Distribution

class BernoulliDistribution(Distribution):
    def get_parameters(self):
        self.p = st.slider('Probability of success (p)', 0.0, 1.0, 0.5, 0.01)
        return {'p': self.p}

    def plot(self, ax):
        x = np.array([0, 1])
        y = bernoulli.pmf(x, self.p)
        ax.bar(x, y, alpha=0.8)
        ax.set_xlabel('Outcome')
        ax.set_ylabel('Probability')

    def get_formula(self):
        return r'P(X=k) = p^k(1-p)^{1-k}, k \in \{0,1\}'

    def get_properties(self, st):
        st.write("""
        The **Bernoulli Distribution** models a single trial with two possible outcomes (success/failure).
        It is characterized by one parameter:
        - **p (probability of success)**: probability of success on the trial
        
        Key Properties:
        - **Support**: k ∈ {0,1}
        - **Mean**: p
        - **Variance**: p(1-p)
        - **Simplest discrete distribution**
        - **Special case** of Binomial with n=1
        
        The probability mass function (PMF) is given by:
        """)
        
        st.latex(r'P(X=k) = p^k(1-p)^{1-k}, k \in \{0,1\}')
        
        st.write("""
        Common applications:
        - **Coin flips** (heads/tails)
        - **Quality control** (pass/fail)
        - **Medical tests** (positive/negative)
        - **Binary outcomes** in any experiment
        
        Important links:
        - [**Properties**](https://en.wikipedia.org/wiki/Bernoulli_distribution#Properties)
        - [**Applications**](https://en.wikipedia.org/wiki/Bernoulli_distribution#Applications)
        - [**Relationship to other distributions**](https://en.wikipedia.org/wiki/Bernoulli_distribution#Related_distributions)
        """)
