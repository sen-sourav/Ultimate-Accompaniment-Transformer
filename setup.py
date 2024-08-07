from setuptools import setup, find_packages

setup(
    name="ultimate_accompaniment_transformer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'torch',
        'tqdm',
        'matplotlib',
        'scikit-learn',
        'torchsummary',
        'huggingface_hub',
        # Add any other dependencies
    ],
)
