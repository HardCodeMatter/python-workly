from setuptools import setup


setup(
    name='workly',
    version='0.1.0',
    description='Web platform for job search.',
    author='Dmytro Klymovets',
    scripts=[
        'app/main.py',
    ],
    install_requires=[
        'SQLAlchemy==2.0.22',
        'streamlit==1.28.0',
    ],
)
