from setuptools import setup, find_packages
import silabel

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="silabel",
    version=silabel.__version__,
    author="Wira Dharma Kencana Putra",
    author_email="wiradharma_kencanaputra@yahoo.com",
    description="Silabel is a python package to syllabelize indonesian word",
    long_description=description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=['numpy'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Natural Language :: Indonesian"
    ],
    keywords="silabel syllable indonesian indonesia jcop nlp bahasa",
    url="https://github.com/WiraDKP/indonesian_syllabelizer"
)