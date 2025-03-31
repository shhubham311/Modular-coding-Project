from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = 'Modular-coding-Project'
PROJECT_VERSION = '0.0.1'
DESCRIPTION = 'A Machine Learning modular coding project for demonstration purposes .'
AUTHOR_NAME = 'Shubham Kumar'
AUTHOR_EMAIL = 'shubham31103@gmail.com'

REQUIREMENTS_FILE_NAME = 'requirements.txt'

def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

        if '-e .' in requirement_list:
            requirement_list.remove('-e .')

        return requirement_list

setup(name=PROJECT_NAME,
      version=PROJECT_VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires= get_requirements_list()
)