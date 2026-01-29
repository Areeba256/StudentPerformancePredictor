from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''Reads the requirements from a file and returns them as a list.'''
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements=[req.replace("\n","").strip() for req in requirements]
        # Remove comments from each line
        requirements = [req.split('#')[0].strip() for req in requirements]
        # Remove empty strings and -e .
        requirements = [req for req in requirements if req and req != HYPHEN_E_DOT]
    return requirements

setup(
   
    name='performance_prediction',
    version='0.1.0',
    author='Areeba',
    author_email='areebasial515@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
   
)
