from setuptools import setup, find_packages

with open("requirements.in") as fid:
    install_requires = fid.readlines()

setup(
    name="stack_capture",
    version="0.1.0",
    description=(
        "a tool for capturing images with a DLSR "
        "that can be used for focus stacking"
    ),
    author="Stefan Blaser",
    author_email="blaserstefan@hotmail.com",
    license="MIT",
    license_files=("LICENSE.md",),
    packages=find_packages(include=["app", "app.*"]),
    python_requires=">=3.12",
    install_requires=install_requires,
)
