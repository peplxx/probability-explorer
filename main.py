import streamlit as st
from distributions.continuous import *
from distributions.discrete import *
from ui.sidebar import Sidebar
import matplotlib.pyplot as plt
import numpy as np
from experiments.manager import ExperimentManager


class ProbabilityExplorer:
    def __init__(self):
        st.set_page_config(
            page_title="Probability Explorer",
            page_icon="🌐",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        st.markdown("""
            <style>
            .stMarkdown, .stText, .stNumber {
                font-size: 18px;
            }
            .stTitle {
                font-size: 42px !important;
            }
            .stMarkdown h2 {
                font-size: 32px;
            }
            .sidebar .stMarkdown {
                font-size: 16px;
            }
            </style>
        """, unsafe_allow_html=True)
        
        st.title("🌐 Probability Explorer")
        self.formula_col, self.plot_col, self.properties_col = st.columns([1, 1, 1])
        self.distributions = {
            'Normal': NormalDistribution(),
            'Multivariate Normal': MultivariateNormalDistribution(),
            'Chi-squared': ChiSquaredDistribution(),
            'Uniform': UniformDistribution(),
            'Poisson': PoissonDistribution(),
            'Binomial': BinomialDistribution(),
            'Multinomial': MultinomialDistribution(),
            'Exponential': ExponentialDistribution(),
            'Geometric': GeometricDistribution(),
            'Bernoulli': BernoulliDistribution(),
            'Cauchy': CauchyDistribution(),
            'Gamma': GammaDistribution(),
            'Hypergeometric': HypergeometricDistribution(),
            'UniformDiscrete': UniformDiscreteDistribution(),
        }
        self.experiment_manager = ExperimentManager()
        
        
    def run(self):
        page = Sidebar.setup()
        
        if page == "Experiments":
            self.show_experiments_page()
            return
            
        if page == "About":
            self.show_about_page()
            return
            
        if page not in ["Continuous Distributions", "Discrete Distributions"]:
            return
            
        with st.sidebar:
            dist_type = Sidebar.get_distribution_selector(
                "Continuous" if page == "Continuous Distributions" else "Discrete"
            )
            distribution = self.distributions[dist_type]
            
            st.markdown("---")
            auto_update = st.checkbox('Auto-update plot', value=True)
            
        with self.formula_col:
            params = distribution.get_parameters()
        if auto_update or st.sidebar.button('Calculate Distribution'):
            try:
                self.display_distribution(distribution, params)
            except RuntimeError as e:
                st.error("Error plotting distribution: " + str(e))
                
    def show_experiments_page(self):
        with st.sidebar:
            experiment = st.selectbox(
                "Choose an experiment:",
                self.experiment_manager.get_experiment_names()
            )
        
        self.experiment_manager.run_experiment(experiment)

    def show_about_page(self):
        st.header("About project:")
        
        st.markdown("""
        ```
        Project Information
        
        This is an interactive web application for exploring and visualizing probability distributions.        
        It provides intuitive interfaces for understanding both continuous and discrete probability distributions through 
        interactive plots and mathematical formulas.
        
        Built with:
        - Streamlit
        - NumPy
        - SciPy
        - Matplotlib
        
        Melnikov Sergey | https://github.com/peplxx/probability-explorer
        ```
        """)
        
    def display_distribution(self, distribution, params):
        with self.formula_col:
            st.write('Distribution Formula:')
            st.latex(distribution.get_formula())
            st.write('Key Parameters:')
            st.write(params)
        with self.plot_col:
            st.write('Distribution Plot:')
            fig, ax = plt.subplots()
            plot = distribution.plot(ax)
            if plot is not None:
                plt.colorbar(plot, label='Probability Density')
            st.pyplot(fig)
            st.success(icon="🔥", body="Distribution calculated!")
        with self.properties_col:
            distribution.get_properties(st)

if __name__ == "__main__":
    app = ProbabilityExplorer()
    app.run()