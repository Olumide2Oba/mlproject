from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path) -> List[str]:
    '''
    this function will return the list of requiremnts
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Olumide',
    author_email='olumide2obanla@gmail.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn']
)