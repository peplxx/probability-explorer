import streamlit as st

class Sidebar:
    @staticmethod
    def setup():
        with st.sidebar:
            st.header("📊 Navigation")
            page = st.radio(
                "",
                ["Continuous Distributions", "Discrete Distributions", "Random Variables"],
                format_func=lambda x: f"{'📈' if x=='Continuous Distributions' else '📊' if x=='Discrete Distributions' else '🎲'} {x}"
            )
            
            st.markdown("---")
            return page

    @staticmethod
    def get_distribution_selector(distribution_type):
        if distribution_type == "Continuous":
            return st.selectbox(
                'Select distribution type',
                ['Multivariate Normal', 'Normal', 'Chi-squared', 'Uniform'],
                format_func=lambda x: f"{x} Distribution"
            )
        else:
            return st.selectbox(
                'Select distribution type',
                ['Multinomial', 'Poisson', 'Binomial'],
                format_func=lambda x: f"{x} Distribution"
            )