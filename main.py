import streamlit as st
from distributions.continuous import *
from distributions.discrete import *
from ui.sidebar import Sidebar
import matplotlib.pyplot as plt


class ProbabilityExplorer:
    def __init__(self):
        st.set_page_config(
            page_title="Probability Explorer",
            page_icon="📊",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        st.title("Probability Explorer")
        self.formula_col, self.plot_col, self.properties_col = st.columns([1, 1, 1])
        self.distributions = {
            'Normal': NormalDistribution(),
            'Multivariate Normal': MultivariateNormalDistribution(),
            'Chi-squared': ChiSquaredDistribution(),
            'Uniform': UniformDistribution(),
            'Poisson': PoissonDistribution(),
            'Binomial': BinomialDistribution(),
            'Multinomial': MultinomialDistribution(),
        }
        
    def run(self):
        page = Sidebar.setup()
        
        if page == "Random Variables":
            self.show_random_variables_page()
            return
            
        with st.sidebar:
            dist_type = Sidebar.get_distribution_selector(
                "Continuous" if page == "Continuous Distributions" else "Discrete"
            )
            st.markdown("---")
            st.write("Distribution Parameters:")
            distribution = self.distributions[dist_type]
            params = distribution.get_parameters()
            
            st.markdown("---")
            auto_update = st.checkbox('Auto-update plot', value=True)
        
        if auto_update or st.sidebar.button('Calculate Distribution'):
            try:
                self.display_distribution(distribution, params)
            except RuntimeError as e:
                st.error("Error plotting distribution: " + str(e))
    
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
            st.write('Properties:')
            st.write(distribution.get_properties())

    def show_random_variables_page(self):
        # Implementation of random variables page
        pass

if __name__ == "__main__":
    app = ProbabilityExplorer()
    app.run()