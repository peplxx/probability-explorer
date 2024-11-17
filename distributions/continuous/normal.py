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

    def get_properties(self, st):
        st.write("""
        The **Normal** (or **Gaussian**) distribution is one of the most important probability distributions in statistics. 
        It is characterized by two parameters:
        - **μ (mean)**: determines the center of the distribution
        - **σ (standard deviation)**: determines the spread/width of the distribution
        
        Key features:
        - **Symmetric bell-shaped curve centered at the mean**
        - **About 68% of data falls within 1 standard deviation of mean**
        - **About 95% of data falls within 2 standard deviations**
        - **About 99.7% of data falls within 3 standard deviations**
        
        The probability density function (PDF) gives the relative likelihood of a random variable taking on a specific value:
        """)
        
        st.latex(r'f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}')
        
        st.write("""
        The cumulative distribution function (CDF) gives the probability that a random variable takes a value less than or equal to x:
        """)
        
        st.latex(r'F(x) = \frac{1}{2}[1 + \text{erf}(\frac{x-\mu}{\sigma\sqrt{2}})]')
        
        st.write("""
        The normal distribution is extremely important because:
        - **It appears naturally in many phenomena** ([Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem))
        - **It is easy to work with mathematically**
        - **Many statistical methods assume** [normality](https://en.wikipedia.org/wiki/Normal_distribution#Normality_tests)
        - **It is the** [maximum entropy](https://en.wikipedia.org/wiki/Maximum_entropy_probability_distribution) **distribution for given mean and variance**
        """)
        return