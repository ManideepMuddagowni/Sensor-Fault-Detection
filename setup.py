from setuptools import find_packages,setup
from typing import List


# create a function to install the requirements.txt file

def get_requirements()->List[str]:

    '''
    This function returns the list of requirements
    '''

    requirement_list:List[str]=[]
    return requirement_list
    
setup(
        name='sensor',
        version='0.0.1',
        author='Manideep Muddagowni',
        author_email='muddagownimanideep@gmail.com',
        packages=find_packages(),
        install_requires=get_requirements(),
    )

