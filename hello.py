import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import math
from scipy.stats import multivariate_normal
st.title("Probability Explorer")

# Create two columns for layout
left_col, right_col = st.columns([1, 2])

with left_col:
    # Add interactive elements for probability exploration
    # Select distribution type
    dist_type = st.selectbox(
        'Select probability distribution',
        ['Multivariate Normal', 'Binomial', 'Normal', 'Poisson', 'Uniform']
    )
    st.write(f'Selected distribution: {dist_type}')

    # Parameters based on distribution type
    if dist_type == 'Multivariate Normal':
        st.write('Mean Vector:')
        mean1 = st.slider('μ₁', -5.0, 5.0, 0.0, 0.1)
        mean2 = st.slider('μ₂', -5.0, 5.0, 0.0, 0.1)
        
        st.write('Covariance Matrix:')
        var1 = st.slider('σ₁²', 0.1, 5.0, 1.0, 0.1)
        var2 = st.slider('σ₂²', 0.1, 5.0, 1.0, 0.1)
        corr = st.slider('Correlation ρ', -1.0, 1.0, 0.0, 0.1)
        
        # Calculate covariance from correlation
        cov12 = corr * np.sqrt(var1 * var2)
        
        # Display covariance matrix
        cov_matrix = np.array([[var1, cov12], [cov12, var2]])
        st.write("Covariance Matrix:")
        st.write(cov_matrix)
        
    elif dist_type == 'Normal':
        mean = st.slider('Mean', -10.0, 10.0, 0.0, 0.1)
        std = st.slider('Standard deviation', 0.1, 5.0, 1.0, 0.1)
        st.write(f'Mean: {mean}, Standard deviation: {std}')
    elif dist_type == 'Uniform':
        a = st.slider('Lower bound (a)', -10.0, 10.0, 0.0, 0.1)
        b = st.slider('Upper bound (b)', -10.0, 10.0, 1.0, 0.1)
        if b <= a:
            st.error('Upper bound must be greater than lower bound')
            b = a + 0.1
    else:
        # Slider for probability value
        probability = st.slider('Select a probability value', 0.0, 1.0, 0.5, 0.1)
        st.write(f'Selected probability: {probability}')

        # Number of trials input
        trials = st.number_input('Number of trials', min_value=1, value=100)
        st.write(f'Number of trials: {trials}')

    # Add auto-update toggle
    auto_update = st.checkbox('Auto-update plot', value=True)

    # Set confidence level
    confidence = 0.95

def calculate_and_plot():
    # Add these lines at the start of the function to access the variables
    global mean, std, probability, trials, a, b, mean1, mean2, var1, var2, cov12
    
    with right_col:
        st.write('Calculating probability distribution...')
        
        # Display formula based on distribution type
        if dist_type == 'Multivariate Normal':
            st.latex(r'f(x) = \frac{1}{2\pi|\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)\right)')
        elif dist_type == 'Normal':
            st.latex(r'f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}')
        elif dist_type == 'Binomial':
            st.latex(r'P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}')
        elif dist_type == 'Poisson':
            st.latex(r'P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}')
        elif dist_type == 'Uniform':
            st.latex(r'f(x) = \frac{1}{b-a} \text{ for } a \leq x \leq b')
        
        # Create figure
        fig, ax = plt.subplots()
        
        # Generate data based on selected distribution
        if dist_type == 'Multivariate Normal':
            # Create grid of points
            x, y = np.mgrid[-5:5:.01, -5:5:.01]
            pos = np.dstack((x, y))
            
            # Define distribution parameters
            mean = [mean1, mean2]
            cov = [[var1, cov12], [cov12, var2]]
            
            # Create multivariate normal distribution
            rv = multivariate_normal(mean, cov)
            
            # Calculate pdf
            z = rv.pdf(pos)
            
            # Create contour plot
            plt.contourf(x, y, z, levels=20, cmap='viridis')
            plt.colorbar(label='Probability Density')
            
            ax.set_xlabel('X₁')
            ax.set_ylabel('X₂')
            
        elif dist_type == 'Normal':
            x = np.linspace(mean - 4*std, mean + 4*std, 100)
            y = np.exp(-((x - mean)**2)/(2*std**2))/(std*np.sqrt(2*np.pi))
            ax.plot(x, y)
        elif dist_type == 'Binomial':
            x = np.arange(0, trials + 1)
            y = [scipy.special.comb(trials, k) * (probability**k) * ((1-probability)**(trials-k)) for k in x]
            ax.plot(x, y)
        elif dist_type == 'Poisson':
            x = np.arange(0, trials + 1)
            y = [(probability**k * np.exp(-probability))/math.factorial(k) for k in x]
            ax.plot(x, y)
        elif dist_type == 'Uniform':
            x = np.linspace(a - 0.5, b + 0.5, 100)
            y = np.where((x >= a) & (x <= b), 1/(b-a), 0)
            ax.plot(x, y)

        ax.set_title(f'{dist_type} Distribution')
        ax.grid(True)
        
        # Display plot in Streamlit
        st.pyplot(fig)
        st.success(icon="🔥", body="Distribution calculated!")

# Calculate either on button press or automatically based on toggle
if auto_update:
    calculate_and_plot()
else:
    with left_col:
        if st.button('Calculate Distribution'):
            calculate_and_plot()
