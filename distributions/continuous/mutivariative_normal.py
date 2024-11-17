import numpy as np
from scipy.stats import multivariate_normal
import streamlit as st
from ..base import Distribution
import matplotlib.pyplot as plt

class MultivariateNormalDistribution(Distribution):
    def get_parameters(self):
        st.write('Mean Vector:')
        self.mean1 = st.slider('μ₁', -5.0, 5.0, 0.0, 0.1)
        self.mean2 = st.slider('μ₂', -5.0, 5.0, 0.0, 0.1)
        
        st.write('Covariance Matrix:')
        self.var1 = st.slider('σ₁²', 0.1, 5.0, 1.0, 0.1)
        self.var2 = st.slider('σ₂²', 0.1, 5.0, 1.0, 0.1)
        self.corr = st.slider('Correlation ρ', -1.0, 1.0, 0.0)
        
        self.cov12 = self.corr * np.sqrt(self.var1 * self.var2)
        self.cov_matrix = np.array([[self.var1, self.cov12], [self.cov12, self.var2]])
        
        return {
            'mean': [self.mean1, self.mean2],
            'cov': self.cov_matrix
        }

    def plot(self, ax):
        x, y = np.mgrid[-5:5:.01, -5:5:.01]
        pos = np.dstack((x, y))
        mean = [self.mean1, self.mean2]
        rv = multivariate_normal(mean, self.cov_matrix)
        z = rv.pdf(pos)
        contour = ax.contourf(x, y, z, levels=20, cmap='viridis')
        plt.colorbar(contour, label='Probability Density')
        ax.set_xlabel('X₁')
        ax.set_ylabel('X₂')

    def get_formula(self):
        return r'f(x) = \frac{1}{2\pi|\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)\right)'

    def get_properties(self, st):
        st.write("""
        The **Multivariate Normal Distribution** is a generalization of the univariate normal distribution to multiple dimensions.
        It is characterized by two parameters:
        - **μ (mean vector)**: determines the center of the distribution
        - **Σ (covariance matrix)**: determines the shape, spread and orientation of the distribution
        
        Key Properties:
        - **Generalizes univariate normal to multiple dimensions**
        - **Characterized by mean vector and covariance matrix**
        - **Elliptical contours of constant density**
        - **Marginal and conditional distributions are normal**
        - **Linear combinations are normally distributed**
        
        The probability density function (PDF) is given by:
        """)
        
        st.latex(r'f(x) = \frac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)\right)')
        
        st.write("""
        where:
        - **x** is an n-dimensional vector
        - **μ** is the mean vector
        - **Σ** is the covariance matrix
        - **|Σ|** is the determinant of Σ
        
        The cumulative distribution function (CDF) does not have a closed form for n>1, but can be expressed as:
        """)
        
        st.latex(r'F(x) = \int_{-\infty}^{x_1}\cdots\int_{-\infty}^{x_n} f(t_1,\ldots,t_n)dt_1\cdots dt_n')
        
        st.write("""
        Important links:
        - [**Maximum Likelihood Estimation**](https://en.wikipedia.org/wiki/Multivariate_normal_distribution#Maximum_likelihood_estimation)
        - [**Properties**](https://en.wikipedia.org/wiki/Multivariate_normal_distribution#Properties)
        - [**Applications**](https://en.wikipedia.org/wiki/Multivariate_normal_distribution#Applications)
        """)