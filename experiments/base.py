from abc import ABC, abstractmethod
import streamlit as st

class Experiment(ABC):
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @property
    def name(self) -> str:
        return self.__class__.__name__.replace('Experiment', '')