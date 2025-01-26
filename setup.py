import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
__version__ = "0.1.0"

REPONAME = "Brain_Tumor"
AUTHOR_USERNAME = "ShreyasKulkarni19"
SRC_DIR = "cnCLassifier"
AUTHOR_EMAIL = "skulkarni.sk.18@gmail"

setuptools.setup(
    name=REPONAME,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A tool for classifying brain MRI images using Convolutional Neural Networks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPONAME}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPONAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)