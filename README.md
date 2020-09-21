# theia

:construction: This project is in beta!

Cut out houses from satellite imagery.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)][1]

## Table of Contents

-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Initial setup](#initial-setup)
    -   [Running the notebook](#running-the-notebook)
-   [Contributing](#contributing)
-   [Versioning](#versioning)
-   [Authors](#authors)
-   [License](#license)
-   [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

If you would just like to play around with the model without downloading
anything to your machine, you can open this notebook in Google Colab
(Note that a Google account is required to run the notebook):
[Open in Google Colab][1]

### Prerequisites

You will need python3 and pip3 installed on your machine. You can install it
from the official website https://www.python.org/.

To install pytorch with CUDA support, conda is recommended. An installation
guide is available in the conda docs:
https://docs.conda.io/projects/conda/en/latest/user-guide/install/

To be able to view und run the example notebooks on your machine, jupyter is
required. An installation guide can be found on their website:
https://jupyter.org/install

### Initial setup

A step by step series of examples that tell you how to get the project up and
running.

Clone the git repository

```bash
git clone https://github.com/intelligenerator/theia.git
cd theia/
git submodule init
git submodule update
git config submodule.recurse true
```

Next, Download the xView2 dataset into the `data/` folder.

Create your conda virtual environment

```bash
conda create --name torch
conda activate torch
```

Next, installed the required packages. This may vary based on your system
hardware and requirements. Read more about pytorch installation:
https://pytorch.org/get-started/locally/

```bash
conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
```

To exit the virtual environment run

```bash
conda deactivate
```

Happy coding!

### Running the notebook

To run the provided notebook on your machine, make sure you have jupyter
installed.

First, create a jupyter kernel for your conda environment:

```bash
pip install --user ipykernel
python -m ipykernel install --user --name=torch
```

Then, open jupyter lab:

```bash
jupyter lab
```

> **Important:**
> Make sure you use the kernel you created above. After opening the notebook,
> navigate to `Kernel` > `Change Kernel...` in the UI and select `torch` from
> the dropdown.
> See this blog post for more info:
> https://janakiev.com/blog/jupyter-virtual-envs/

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct, and
the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the [tags on this repository](https://github.com/intelligenerator/theia/tags).

## Authors

The Intelligenerator Group - [intelligenerator](https://github.com/intelligenerator)

See also the list of
[contributors](https://github.com/intelligenerator/theia/contributors)
who participated in this project.

## License

This project is licensed under the MIT License - see the
[LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

-   [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/pdf/1505.04597.pdf) - Initial research paper
-   [numpy gitignore](https://github.com/numpy/numpy/blob/master/.gitignore) -
    Gitignore inspiration
-   [github python gitignore template](https://github.com/github/gitignore/blob/master/Python.gitignore) - The gitignore template
-   [python3 tutorial](https://docs.python.org/3/tutorial/venv.html) - Guide and
    explanations
-   [Contributor Covenant](https://www.contributor-covenant.org/) - Code of Conduct

[1]: http://colab.research.google.com/github/intelligenerator/theia/blob/master
