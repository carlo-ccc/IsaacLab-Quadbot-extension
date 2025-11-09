from setuptools import setup, find_packages

setup(
    name="isaaclab-quadbot-extension",
    version="0.1.0",
    description="Quadruped tasks extension for Isaac Lab",
    author="Your Name",
    license="Apache-2.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
)