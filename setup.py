from os.path import abspath, dirname, join
from setuptools import find_packages, setup

this_dir = abspath(dirname(__file__))
with open(join(this_dir, "README.md"), encoding="utf-8") as file:
    long_description = file.read()


setup(
    name="promptcli",
    python_requires=">3.5",
    options={"bdist_wheel": {"universal": "1"}},
    version="0.0.2",
    description="A command line application to help wrap the OpenAI ChatGPT api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raiyanyahya/prompt",
    author="Raiyan Yahya",
    license="MIT",
    author_email="raiyanyahyadeveloper@gmail.com",
    keywords=["cli", "developer tools", "productivity", "openai", "chatgpt"],
    packages=find_packages(),
    install_requires=["click==8.1.3", "openai==0.27.0", "rich==13.3.1"],
    entry_points={"console_scripts": ["prompt=prompt.cli:cli"]},
)
