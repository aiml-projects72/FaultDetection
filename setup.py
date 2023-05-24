from typing import List
from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."

def get_requirements(path:str)->List[str]:
    """
    Return list of requirements when path of file is passed 
    """
    requirements = []
    with open(path) as file_obj:
        requirements = [i.replace('\n','') for i in file_obj.readlines()]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

    

setup(name='DefectShodhak',
      version='1.0',
      description='This project is intended detect the defect in casting iron products just by uploading the images. It involves Machine Learning and Flask on the tech front',
      author='Prathmesh Choudhari',
      author_email='choudhariprathmesh001@gmail.com',
      url='https://iampratham29.herokuapp.com/',
      packages=find_packages(),
      install_requires = get_requirements('requirements.txt')
     )