from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(fiel_path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''

    get_requirements=[]
    with open(fiel_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup (
    name='mlproject',
    version='0.0.1',
    author='Sanbaj',
    author_email='sanbajansari01@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)