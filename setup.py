from setuptools import setup, find_packages

setup(
    name="dns_json",
    version="0.0.1",
    description="DNS over HTTPS with JSON Format",
    author="Michael Brux",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
