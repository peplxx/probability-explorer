from abc import ABC, abstractmethod
import streamlit as st

class Distribution(ABC):
    @abstractmethod
    def get_parameters(self):
        """Get distribution parameters from user input"""
        pass
    
    @abstractmethod
    def plot(self, ax):
        """Plot the distribution"""
        pass
    
    @abstractmethod
    def get_formula(self):
        """Return LaTeX formula for the distribution"""
        pass
    
    @abstractmethod
    def get_properties(self):
        """Return distribution properties"""
        pass