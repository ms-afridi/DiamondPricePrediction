from setuptools import find_packages, setup
from typing import List

#HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirements]
        
        # if HYPEN_E_DOT in requirements:
        #     requirements.remove(HYPEN_E_DOT)
        # return requirements


setup(
    name='Diamond Price Prediction',
    version='0.0.1',
    author='Afridi',
    author_email='shaim5938@gmail.com',
    #install_requires = ['pandas','numpy'],
    install_requires = get_requirements('D:\\Diamond price prediction\\requirments.txt'),
    packages=find_packages()
)