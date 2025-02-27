from setuptools import find_packages, setup

setup(
    name="dlimp",
    version="0.0.1",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "tensorflow",
        "tqdm",
        "tqdm-multiprocess",
        "pre-commit",
        "tensorflow_datasets",
    ],
)
