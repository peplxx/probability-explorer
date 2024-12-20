import numpy as np
from scipy.stats import multinomial
import streamlit as st
from ..base import Distribution
import matplotlib.pyplot as plt

class MultinomialDistribution(Distribution):
    def get_parameters(self):
        st.write('Parameters:')
        self.n = st.slider('Number of trials (n)', 1, 100, 10)
        
        # Get probabilities for k=3 categories
        st.write('Probabilities (must sum to 1):')
        self.p1 = st.slider('p₁', 0.0, 1.0, 0.33, 0.01)
        self.p2 = st.slider('p₂', 0.0, 1.0, 0.33, 0.01)
        self.p3 = min(1.0 - self.p1 - self.p2, 1.0)
        st.write(f'p₃ = {self.p3:.2f}')
        
        return {
            'n': self.n,
            'p': [self.p1, self.p2, self.p3]
        }

    def plot(self, ax):
        # Create grid of possible outcomes
        x = np.arange(0, self.n + 1)
        y = np.arange(0, self.n + 1)
        X, Y = np.meshgrid(x, y)
        
        # Calculate probabilities where Z = n - X - Y
        Z = self.n - X - Y
        probs = np.zeros_like(X, dtype=float)
        
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                if Z[i,j] >= 0 and X[i,j] + Y[i,j] <= self.n:
                    probs[i,j] = multinomial.pmf([X[i,j], Y[i,j], Z[i,j]], 
                                               self.n, 
                                               [self.p1, self.p2, self.p3])
                    
        # Plot as heatmap
        contour = ax.contourf(X, Y, probs, levels=20, cmap='viridis')
        plt.colorbar(contour, label='Probability')
        ax.set_xlabel('X₁ (Category 1)')
        ax.set_ylabel('X₂ (Category 2)')

    def get_formula(self):
        return r'P(X_1=k_1,...,X_m=k_m) = \frac{n!}{k_1!...k_m!}p_1^{k_1}...p_m^{k_m}'

    def get_properties(self, st):
        st.write("""
        The **Multinomial Distribution** is a generalization of the binomial distribution to multiple categories.
        It is characterized by two parameters:
        - **n (number of trials)**: total number of independent experiments
        - **p₁,...,pₘ (probabilities)**: probability of each category, must sum to 1
        
        Key Properties:
        - **Support**: k₁,...,kₘ ≥ 0 with Σkᵢ = n
        - **Mean of category i**: npᵢ
        - **Variance of category i**: npᵢ(1-pᵢ)
        - **Covariance between categories i,j**: -npᵢpⱼ
        - **Independent trials** (no memory between trials)
        
        The probability mass function (PMF) is given by:
        """)
        
        st.latex(r'P(X_1=k_1,...,X_m=k_m) = \frac{n!}{k_1!...k_m!}p_1^{k_1}...p_m^{k_m}')
        
        st.write("""
        Common applications:
        - **Genetic studies** (allele frequencies)
        - **Market research** (consumer preferences)
        - **Natural language processing** (word frequencies)
        - **Political science** (voting patterns)
        
        Important links:
        - [**Properties**](https://en.wikipedia.org/wiki/Multinomial_distribution#Properties)
        - [**Applications**](https://en.wikipedia.org/wiki/Multinomial_distribution#Examples)
        """)
