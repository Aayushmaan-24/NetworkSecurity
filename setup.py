from setuptools import setup, find_packages
from typing import List

def get_requirements():
    
    """
    This function returns a list of requirements for this project
    """
    requirements = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found")
    
    return requirements

#print(get_requirements())


setup(
    
    name="NetworkSecurity",
    version="0.0.1",
    author="Aayushmaan",
    author_email="aayushmaan.chakraborty@gmail.com",
    install_requires= get_requirements(),
    packages=find_packages()
    
)