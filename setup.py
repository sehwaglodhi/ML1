from setuptools import find_packages ,setup
from typing import List
hypen_e_dot='-e .'

def get_requirement(file_path:str)->List[str]:
    '''this fuction will return the list of requirement'''
    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirement]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='sehwag',
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt')

)