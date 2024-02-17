from setuptools import setup, find_packages

setup(
    name='monte_carlo_pi',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your script might have
        # For this example, there are no additional dependencies
    ],
    entry_points={
        'console_scripts': [
            'monte_carlo_pi = montecarlo:monte_carlo_pi',  # Replace 'your_script_name' with the actual name of your script
        ],
    },
    author='Tamilselvan_Arjunan',
    author_email='nishantamil@gmail.com',
    description='Monte Carlo simulation to estimate the value of π',
    url='https://github.com/arjunlimat/monte_carlo_pi',  # Update with your GitHub repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
