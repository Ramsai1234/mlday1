from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ="-e ."
def get_reqiurements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    
    '''

    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

        requirements = [req.replace("\n","") for req in requirements] 


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements



setup(
    Name ="aiml",
    Version ="0.0.1",
    Author ="Ramsai",
    AuthorMail ="Ponugotiramsai@gmail.com",
    packages =find_packages(),
    install_equires=get_reqiurements('requirements.txt')
)


