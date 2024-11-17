from typing import Dict, Type
from .base import Experiment
from .coin_flip import CoinFlipExperiment
import streamlit as st

class ExperimentManager:
    def __init__(self):
        self.experiments: Dict[str, Type[Experiment]] = {
            'Coin Flip': CoinFlipExperiment(),
        }
    
    def get_experiment_names(self):
        return list(self.experiments.keys())
    
    def run_experiment(self, name: str):
        if name not in self.experiments:
            raise ValueError(f"Unknown experiment: {name}")
        
        experiment = self.experiments[name]
        st.header(name)
        st.markdown(experiment.get_description())
        experiment.run()
