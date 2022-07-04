# Saliency Evaluation
Python implementation for evaluating explanations presented in [On the (In)fidelity and Sensitivity for Explanations](https://arxiv.org/pdf/1901.09392.pdf) published in NeurIPS 2019 for evaluating any saliency explanations.

## Get Started
Run vis_mnist.ipynb to see examples of explanations in MNIST along with their sensitivity and infidelity.

## Acknowledgements
We build our visualization tools based on codes available in the following repositories:
1. https://github.com/PAIR-code/saliency
2. https://github.com/marcoancona/DeepExplain

## Installation
```bash
pip install -U "git+https://github.com/HeinrichAD/saliency_evaluation.git@master"
```

setup.py
```bash
...
install_requires=[
    ...
    "saliency_evaluation @ git+https://github.com/HeinrichAD/saliency_evaluation.git@master",
    ...
],
...
```

### Development
```bash
# create virtual environment
virtualenv -p $(which python3.7) .venv
# or
python -m venv .venv

# activate our virtual environment:
source .venv/bin/activate

# update pip (optional)
python -m pip install -U pip

# install
pip install -e .[dev]
```
