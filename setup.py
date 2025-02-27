from setuptools import find_packages,setup

from typing import List

HYPHEN_E = '-e .'
def requir(file_path:str)->List[str]:
    v=[]
    with open(file_path) as file_names:
        v=file_names.readlines()
        v=[req.replace("\n","") for req in v]

        if HYPHEN_E in v:
            v.remove(HYPHEN_E)
    return v



# makes a package of yr ml model so it can be used as pip intall _name 
# for that setup the metadat of your package 
setup(
name ='End to End ML project',
version = '0.0.1',
author='Isha',
author_email = 'talkishhh22042000@gmail.com',
packages = find_packages(),
install_requires = requir('requirements.txt')
)
