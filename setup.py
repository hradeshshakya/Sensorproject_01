# conda activate venv/

from setuptools import find_packages,setup
from typing import List




HYPHE_E_DOT = '-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if HYPHE_E_DOT in requirements:
        requirements.remove(HYPHE_E_DOT)
    return requirements   

setup(
    name = 'Fault Detection',
    version = '0.0.1',
    author = 'Hradesh',
    author_mail = 'kushwaha.prem234@gmail.com',
    install_requirements = get_requirements('requirements.txt'),
    packages = find_packages()
    )