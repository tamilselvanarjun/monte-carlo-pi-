from setuptools import setup, find_packages

setup(
    name='montecarlomodel',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your script might have
        # For this example, there are no additional dependencies
    ],
    entry_points={
        'console_scripts': [
            'montecarlomodel = montecarlo:monte_carlo_pi',  # Replace 'your_script_name' with the actual name of your script
        ],
    },
    author='Tamilselvan_Arjunan',
    author_email='nishantamil@gmail.com',
    description='Monte Carlo simulation to estimate the value of π',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/arjunlimat/montecarlomodel',  # Update with your GitHub repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
