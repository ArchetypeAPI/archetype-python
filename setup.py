from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="archetypesdk",
    version="1.0.6",
    description="Python implementation for Archetype. Archetype provides packages that automatically handles API user auth and an SDK for managing your APIs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArchetypeAPI/",
    author="Archetype",
    author_email="dev@archetype.dev",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["requests", "Flask"],
    zip_safe=False,
)