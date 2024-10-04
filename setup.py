from setuptools import find_packages, setup

setup(
    name="cq_dagster_embedded",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
)
