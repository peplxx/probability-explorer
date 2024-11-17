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

    def get_properties(self, st):
        st.write("""
        The **Poisson Distribution** models the number of events occurring in a fixed interval of time or space.
        It is characterized by one parameter:
        - **λ (rate parameter)**: average number of events in the interval
        
        Key Properties:
        - **Support**: k ∈ {0,1,2,...}
        - **Mean = λ**
        - **Variance = λ**
        - **Events occur independently** at a constant rate
        - **No memory** between events
        
        The probability mass function (PMF) is given by:
        """)
        
        st.latex(r'P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}')
        
        st.write("""
        Common applications:
        - **Customer arrivals** at a service point
        - **Defects** in manufacturing
        - **Radioactive decay** events
        - **Network traffic** analysis
        
        Important links:
        - [**Properties**](https://en.wikipedia.org/wiki/Poisson_distribution#Properties)
        - [**Applications**](https://en.wikipedia.org/wiki/Poisson_distribution#Applications)
        - [**Relationship to other distributions**](https://en.wikipedia.org/wiki/Poisson_distribution#Related_distributions)
        """)
