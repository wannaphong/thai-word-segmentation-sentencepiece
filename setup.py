# -*- coding: utf-8 -*-
from setuptools import setup,find_packages
requirements = [
	'sentencepiece'
]
test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pythaipiece',
    version='0.1',
    description="thai word segmentation using sentencepiece.",
    author='Wannaphong Phatthiyaphaibun',
    author_email='wannaphong@kkumail.com',
    url='https://github.com/wannaphongcom/thai-word-segmentation-sentencepiece',
    packages=find_packages(),
    package_data={'pythaipiece':['thai1.model','thai1.vocab','thai2.model','thai2.vocab','thai3.model','thai3.vocab']},
    include_package_data=True,
    install_requires=requirements,
    license='Apache Software License 2.0',
    zip_safe=False,
    #keywords='pythainlp',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Thai',
        'Topic :: Text Processing :: Linguistic',
        'Programming Language :: Python :: Implementation']
)
