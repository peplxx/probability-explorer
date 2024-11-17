import numpy as np
from scipy.stats import geom
import streamlit as st
from ..base import Distribution

class GeometricDistribution(Distribution):
    def get_parameters(self):
        self.p = st.slider('Probability of success (p)', 0.01, 1.0, 0.5, 0.01)
        return {'p': self.p}

    def plot(self, ax):
        x = np.arange(1, min(20, int(5/self.p)))
        y = geom.pmf(x, self.p)
        ax.bar(x, y, alpha=0.8)
        ax.set_xlabel('Number of Trials Until Success')
        ax.set_ylabel('Probability')

    def get_formula(self):
        return r'P(X=k) = (1-p)^{k-1}p'

    def get_properties(self, st):
        st.write("""
        The **Geometric Distribution** models the number of trials needed to get the first success in a sequence of independent Bernoulli trials.
        It is characterized by one parameter:
        - **p (probability of success)**: probability of success on each trial
        
        Key Properties:
        - **Support**: k ∈ {1,2,3,...}
        - **Mean = 1/p**
        - **Variance = (1-p)/p²**
        - **Memoryless property**: P(X > s + t | X > s) = P(X > t)
        - **Independent trials** with fixed probability
        
        The probability mass function (PMF) is given by:
        """)
        
        st.latex(r'P(X=k) = (1-p)^{k-1}p')
        
        st.write("""
        Common applications:
        - **Quality control** (number of items inspected until finding a defect)
        - **Marketing** (number of attempts until first sale)
        - **Reliability** (number of trials until first failure)
        - **Game theory** (number of attempts until first win)
        
        Important links:
        - [**Properties**](https://en.wikipedia.org/wiki/Geometric_distribution#Properties)
        - [**Applications**](https://en.wikipedia.org/wiki/Geometric_distribution#Applications)
        - [**Relationship to other distributions**](https://en.wikipedia.org/wiki/Geometric_distribution#Related_distributions)
        """)
