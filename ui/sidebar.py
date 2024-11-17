import streamlit as st

class Sidebar:
    @staticmethod
    def setup():
        with st.sidebar:
            st.header("🧭 Navigation")
            page = st.radio(
                "",
                ["Continuous Distributions", "Discrete Distributions", "Experiments", "About"],
                format_func=lambda x: f"{'📈' if x=='Continuous Distributions' else '📊' if x=='Discrete Distributions' else '🎲' if x=='Random Variables' else '🧪' if x=='Experiments' else '👤'} {x}"
            )
            
            st.markdown("---")
            return page

    @staticmethod
    def get_distribution_selector(distribution_type):
        if distribution_type == "Continuous":
            return st.selectbox(
                'Select distribution type',
                ['Multivariate Normal', 'Normal', 'Chi-squared','Exponential', 'Cauchy', 'Uniform', 'Gamma'],
                format_func=lambda x: f"{x} Distribution"
            )
        elif distribution_type == "Discrete":
            return st.selectbox(
                'Select distribution type',
                ['Multinomial', 'Poisson', 'Binomial', 'Geometric', 'Bernoulli', 'Hypergeometric', 'UniformDiscrete'],
                format_func=lambda x: f"{x} Distribution"
            )