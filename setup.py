from setuptools import setup


# read version file
# exec(open("src/version.py").read())
__version__ = "0.0.1-dev"


def readme():
    with open("README.md", "r") as f:
        return f.read()


extras_require = {
    "dev": [
        "ipykernel",
        "matplotlib",
        "scikit-image",
        "torchvision",
    ],
}

setup(
    name="saliency_evaluation",
    author="chihkuanyeh",
    author_email="chihkuanyeh@github.com",
    version=__version__,  # type: ignore # noqa F821
    description="Saliency Evaluation",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/HeinrichAD/saliency_evaluation",
    packages=["saliency_evaluation"],
    package_dir={
        "saliency_evaluation": "src/saliency_evaluation",
    },
    python_requires=">=3.7",
    install_requires=[  # TODO: add version numbers
        "numpy",
        "torch",
    ],
    extras_require=extras_require,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        # "License :: OSI Approved :: GNU General Public License",
        # "Topic :: Scientific/Engineering",
    ],
)
