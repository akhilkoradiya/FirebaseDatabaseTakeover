from setuptools import setup

readme = """# Firebase Database Takeover (FDT)

[![MIT License](https://img.shields.io/badge/License-MIT-green)](https://github.com/akhilkoradiya/FirebaseDatabaseTakeover/blob/main/LICENSE)
[![YouTube Channel](https://img.shields.io/badge/YouTube-Subscribe-red)](https://www.youtube.com/@hackerno21)
[![Twitter Follow](https://img.shields.io/twitter/follow/mytwitterhandle?label=Follow%20on%20Twitter&style=social)](https://twitter.com/akhilkoradiya21)
[![LinkedIn Connect](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://in.linkedin.com/in/akhil-koradiya-2722a51a0)
[![GitHub Follow](https://img.shields.io/github/followers/mygithubusername?label=Follow%20on%20GitHub&style=social)](https://github.com/akhilkoradiya)

FDT stands for Firebase Database Takeover, an automation tool used to assess the vulnerability of Firebase databases for potential exploitation. Firebase Database Takeover is a Python script specifically developed for this purpose. By analyzing the given Firebase database URL, the script determines whether it is susceptible to a takeover. In the event of a vulnerability, the script empowers attackers to inject custom data into the database, offering them an option to exploit it. Additionally, the script provides a proof-of-concept URL as evidence of the exploit.

<p align="center">
  <br>
  <a href="https://ko-fi.com/akhilkoradiya">
    <img src="https://github.com/appcraftstudio/buymeacoffee/raw/master/Images/snapshot-bmc-button.png" width="300">
  </a>
</p>

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Author](#author)

## Introduction
Firebase Database Takeover is a powerful Python script designed to assess the vulnerability of Firebase database URLs and provide an option for exploiting the discovered vulnerabilities. Firebase is a widely-used Backend-as-a-Service (BaaS) platform that offers real-time database services to developers, making it an attractive choice for app development. However, misconfigurations in Firebase databases can lead to unauthorized access, data leaks, and potential data breaches.

This tool aims to assist developers and security enthusiasts in identifying potential security risks associated with Firebase databases. It checks the provided Firebase URL for vulnerabilities and informs users if the database is exposed to takeover attacks. In case of a vulnerable database, the script offers the option to add data to the database, showcasing the potential impact of a takeover.

With its straightforward and interactive interface, the Firebase Database Takeover tool empowers users to understand the importance of securing their Firebase databases effectively. By responsibly using this tool, developers can proactively protect their applications from unauthorized access and ensure the confidentiality of sensitive information stored in Firebase databases.

## Features

- Add data to a Firebase database with ease.
- Validate Firebase URL and email format before making requests.
- Simple and intuitive command-line interface.

## Requirements

To use the script provided in this repository, you need to have the following dependencies installed:

- **Python 3.x:** The script is written in Python, so you must have Python 3.x installed on your system.
- **argparse:** This library is required for handling command-line arguments in the script. Install it using the following command: ```pip install argparse```
- **requests:** The requests library is necessary to make HTTP requests and interact with URLs. Install it using the following command: ```pip install requests```
- **colorama:** The colorama library is used for colored terminal output. Install it using the following command: ```pip install colorama```

## Installation

To use FDT, you need to have Python installed on your system. Follow these steps to install and use FDT:

```
pip install FirebaseDatabaseTakeover
```

## Usage

```
fdt <add_your_firebase_database_url>
``` 

## Disclaimer
This script is intended for educational and testing purposes only. The author is not responsible for any misuse or damage caused by the usage of this script. Use it at your own risk.

## License
This project is licensed under the [MIT License](https://github.com/akhilkoradiya/FirebaseDatabaseTakeover/blob/main/LICENSE).

## Author

Firebase Database Takeover is developed by **Akhil Koradiya.**

Follow me on:

- YouTube: https://www.youtube.com/@hackerno21
- GitHub: https://github.com/akhilkoradiya
- Twitter: https://twitter.com/akhilkoradiya21
- Linkedin: https://in.linkedin.com/in/akhil-koradiya-2722a51a0
"""

setup(
    name="FirebaseDatabaseTakeover",
    version="1.0.1",
    author="Akhil Koradiya",
    author_email="akhil.koradiya.21@gmail.com",
    description="Firebase Database Takeover tool",
    long_description=readme,
    long_description_content_type='text/markdown',
    py_modules=["fdt.__main__"],
    install_requires=[
        "requests",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "fdt = fdt.__main__:main",
        ],
    },
)
