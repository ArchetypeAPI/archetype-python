from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="archetypesdk",
    version="1.0.16",
    description="Python bindings for Archetype. Archetype makes API monetization and usage based billing for APIs easy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArchetypeAPI/",
    author="Archetype",
    author_email="hello@archetype.dev",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=["requests", "Flask"],
    zip_safe=False,
)