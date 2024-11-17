import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import math
from scipy.stats import multivariate_normal, chi2

st.set_page_config(
    page_title="Probability Explorer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

class ProbabilityExplorer:
    def __init__(self):
        st.title("Probability Explorer")
        self.formula_col, self.plot_col, self.properties_col = st.columns([1, 1, 1])  # Three equal columns
        self.confidence = 0.95
        self.setup_ui()

    def setup_ui(self):
        with st.sidebar:
            st.header("📊 Navigation")
            self.page = st.radio(
                "",
                ["Continuous Distributions", "Discrete Distributions", "Random Variables"],
                format_func=lambda x: f"{'📈' if x=='Continuous Distributions' else '📊' if x=='Discrete Distributions' else '🎲'} {x}"
            )
            
            st.markdown("---")
            
            if self.page == "Continuous Distributions":
                st.subheader("📈 Continuous Distributions")
                self.dist_type = st.selectbox(
                    'Select distribution type',
                    ['Multivariate Normal', 'Normal', 'Chi-squared', 'Uniform'],
                    format_func=lambda x: f"{x} Distribution"
                )
            elif self.page == "Discrete Distributions":
                st.subheader("📊 Discrete Distributions")
                self.dist_type = st.selectbox(
                    'Select distribution type',
                    ['Poisson', 'Binomial'],
                    format_func=lambda x: f"{x} Distribution"
                )
            else:  # Random Variables page
                st.subheader("🎲 Random Variables")
                st.write("""
                Learn about fundamental concepts:
                - 📊 Expected Value
                - 📈 Variance
                - 📉 Standard Deviation
                - ∑ Moment Generating Functions
                """)
                return
            
            self.get_distribution_parameters()
            self.auto_update = st.checkbox('Auto-update plot', value=True)

    def get_distribution_parameters(self):
        if self.dist_type == 'Multivariate Normal':
            self.get_multivariate_normal_params()
        elif self.dist_type == 'Normal':
            self.get_normal_params()
        elif self.dist_type == 'Uniform':
            self.get_uniform_params()
        elif self.dist_type == 'Chi-squared':
            self.get_chi_squared_params()
        else:
            self.get_discrete_params()

    def get_multivariate_normal_params(self):
        st.write('Mean Vector:')
        self.mean1 = st.slider('μ₁', -5.0, 5.0, 0.0, 0.1)
        self.mean2 = st.slider('μ₂', -5.0, 5.0, 0.0, 0.1)
        
        st.write('Covariance Matrix:')
        self.var1 = st.slider('σ₁²', 0.1, 5.0, 1.0, 0.1)
        self.var2 = st.slider('σ₂²', 0.1, 5.0, 1.0, 0.1)
        self.corr = st.slider('Correlation ρ', -1.0, 1.0, 0.0)
        
        self.cov12 = self.corr * np.sqrt(self.var1 * self.var2)
        self.cov_matrix = np.array([[self.var1, self.cov12], [self.cov12, self.var2]])
        st.write("Covariance Matrix:")
        st.write(self.cov_matrix)

    def get_normal_params(self):
        self.mean = st.slider('Mean', -10.0, 10.0, 0.0, 0.1)
        self.std = st.slider('Standard deviation', 0.1, 5.0, 1.0, 0.1)
        st.write(f'Mean: {self.mean}, Standard deviation: {self.std}')

    def get_uniform_params(self):
        self.a = st.slider('Lower bound (a)', -10.0, 10.0, 0.0, 0.1)
        self.b = st.slider('Upper bound (b)', -10.0, 10.0, 1.0, 0.1)
        if self.b <= self.a:
            st.error('Upper bound must be greater than lower bound')
            self.b = self.a + 0.1

    def get_chi_squared_params(self):
        self.df = st.slider('Degrees of freedom', 1, 30, 1)
        st.write(f'Degrees of freedom: {self.df}')

    def get_discrete_params(self):
        self.probability = st.slider('Select a probability value', 0.0, 1.0, 0.5, 0.1)
        st.write(f'Selected probability: {self.probability}')
        self.trials = st.number_input('Number of trials', min_value=1, value=100)
        st.write(f'Number of trials: {self.trials}')

    def display_formula(self):
        formulas = {
            'Multivariate Normal': r'f(x) = \frac{1}{2\pi|\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)\right)',
            'Normal': r'f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}',
            'Binomial': r'P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}',
            'Poisson': r'P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}',
            'Uniform': r'f(x) = \frac{1}{b-a} \text{ for } a \leq x \leq b',
            'Chi-squared': r'f(x) = \frac{1}{2^{k/2}\Gamma(k/2)}x^{k/2-1}e^{-x/2}'
        }
        st.latex(formulas[self.dist_type])

    def plot_distribution(self):
        fig, ax = plt.subplots()  # Control figure size here
        
        if self.dist_type == 'Multivariate Normal':
            self.plot_multivariate_normal(ax)
        elif self.dist_type == 'Normal':
            self.plot_normal(ax)
        elif self.dist_type == 'Binomial':
            self.plot_binomial(ax)
        elif self.dist_type == 'Poisson':
            self.plot_poisson(ax)
        elif self.dist_type == 'Uniform':
            self.plot_uniform(ax)
        elif self.dist_type == 'Chi-squared':
            self.plot_chi_squared(ax)

        ax.set_title(f'{self.dist_type} Distribution')
        ax.grid(True)
        return fig

    def plot_multivariate_normal(self, ax):
        x, y = np.mgrid[-5:5:.01, -5:5:.01]
        pos = np.dstack((x, y))
        mean = [self.mean1, self.mean2]
        cov = [[self.var1, self.cov12], [self.cov12, self.var2]]
        rv = multivariate_normal(mean, cov)
        z = rv.pdf(pos)
        plt.contourf(x, y, z, levels=20, cmap='viridis')
        plt.colorbar(label='Probability Density')
        ax.set_xlabel('X₁')
        ax.set_ylabel('X₂')

    def plot_normal(self, ax):
        x = np.linspace(self.mean - 4*self.std, self.mean + 4*self.std, 100)
        y = np.exp(-((x - self.mean)**2)/(2*self.std**2))/(self.std*np.sqrt(2*np.pi))
        ax.plot(x, y)

    def plot_binomial(self, ax):
        x = np.arange(0, self.trials + 1)
        y = [scipy.special.comb(self.trials, k) * (self.probability**k) * 
             ((1-self.probability)**(self.trials-k)) for k in x]
        ax.plot(x, y)

    def plot_poisson(self, ax):
        x = np.arange(0, self.trials + 1)
        y = [(self.probability**k * np.exp(-self.probability))/math.factorial(k) for k in x]
        ax.plot(x, y)

    def plot_uniform(self, ax):
        x = np.linspace(self.a - 0.5, self.b + 0.5, 100)
        y = np.where((x >= self.a) & (x <= self.b), 1/(self.b-self.a), 0)
        ax.plot(x, y)

    def plot_chi_squared(self, ax):
        x = np.linspace(0, max(30, self.df*3), 200)
        y = chi2.pdf(x, self.df)
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('Probability Density')

    def calculate_and_plot(self):
        if self.page == "Random Variables":
            with self.formula_col:
                st.write("## Mathematical Definitions")
                st.latex(r"E[X] = \sum_{x} x \cdot P(X=x)")
                st.latex(r"Var(X) = E[(X - \mu)^2]")
                st.latex(r"\sigma = \sqrt{Var(X)}")
                st.latex(r"M_X(t) = E[e^{tX}]")
            
            with self.plot_col:
                st.write("## Visual Representation")
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/The_Normal_Distribution.svg/1200px-The_Normal_Distribution.svg.png")
            
            with self.properties_col:
                st.write("""
                ## Key Properties
                - Expected value is the center of mass
                - Variance measures spread from mean
                - Standard deviation is in same units as data
                - MGF uniquely determines distribution
                """)
        else:
            with self.formula_col:
                st.write('Distribution Formula:')
                self.display_formula()
                st.write('Key Parameters:')
                if self.dist_type == 'Normal':
                    st.write(f'μ = {self.mean}, σ = {self.std}')
                elif self.dist_type == 'Multivariate Normal':
                    st.write(f'Mean vector: μ = [{self.mean1}, {self.mean2}]')
                    st.write('Covariance matrix:')
                    st.write(self.cov_matrix)
            
            with self.plot_col:
                st.write('Distribution Plot:')
                fig = self.plot_distribution()
                st.pyplot(fig)
                st.success(icon="🔥", body="Distribution calculated!")

            with self.properties_col:
                st.write('Properties:')
                if self.dist_type == 'Normal':
                    st.write("""
                    - Symmetric about mean
                    - 68-95-99.7 rule applies
                    - Bell-shaped curve
                    - Infinite support
                    """)

    def run(self):
        if self.page != "Random Variables" and self.auto_update:
            self.calculate_and_plot()
        elif self.page != "Random Variables":
            with self.formula_col:
                if st.button('Calculate Distribution'):
                    self.calculate_and_plot()
        else:
            self.calculate_and_plot()

# Initialize and run the app
app = ProbabilityExplorer()
app.run()
