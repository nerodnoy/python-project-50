<div align="center">

![Image alt](https://github.com/nerodnoy/python-project-50/blob/main/kandinsky-download-1690797048402.png)
<h1>Difference Generator</h1>

Find the difference between two files.

![Actions Status](https://github.com/nerodnoy/python-project-50/workflows/hexlet-check/badge.svg)  [![main](https://github.com/nerodnoy/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/nerodnoy/python-project-50/actions/workflows/main.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/0e19e094594cd2be67e5/maintainability)](https://codeclimate.com/github/nerodnoy/python-project-50/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/0e19e094594cd2be67e5/test_coverage)](https://codeclimate.com/github/nerodnoy/python-project-50/test_coverage)

<a href="#about">About</a> •
<a href="#installation">Installation</a> •
<a href="#usage">Usage</a> •
<a href="#demonstration">Demonstration</a> •
<a href="#requirements">Requirements</a>

</div>

## About

Difference Generator is a tool that determines the difference between two data structures.


The difference is based on how the files have changed relative to each other, the keys are rendered in alphabetical
order.

> Sidenote: This project was created by [Hexlet.io](https://hexlet.io) student as a part of
> a ["Python Developer"](https://ru.hexlet.io/programs/python) learning course.

### Supported formats

- JSON
- YAML

### Various output formats

- Plain text
- Structured text
- JSON

## Installation

To use this package you need to clone repository to your device:

    git clone https://github.com/nerodnoy/python-project-50.git

Switch to package's directory:

    cd python-project-50

Use [poetry](https://python-poetry.org/docs/) and pip to install the package:

    poetry build  
    python3 -m pip install --user dist/*.whl

## Usage

Difference Generator can be used as an **external library** or as **CLI tool**.

### As an external library

    from gendiff import generate_diff  
    diff = generate_diff(file_path1, file_path2, file_format)

### As CLI tool

    gendiff [-f file_format] file_path1 file_path2

or

    gendiff [--format file_format] file_path1 file_path2

## Demonstration

### *Stylish format*

Comparison of 2 simple files:

--- Asciinema of gendiff simple_file1.json simple_file2.json

Comparison of 2 nested files:

--- Asciinema of gendiff nested_file1.json nested_file2.json

### *Plain format*

Comparison of 2 simple files:

--- Asciinema of gendiff --format plain simple_file1.json simple_file2.json

Comparison of 2 nested files:

--- Asciinema of gendiff --format plain nested_file1.json nested_file2.json

### *JSON format*

Comparison of 2 simple files:

--- Asciinema of gendiff --format json simple_file1.json simple_file2.json

Comparison of 2 nested files:

--- Asciinema of gendiff --format json nested_file1.json nested_file2.json

> Note: If there is no specific format provided when using the package, default output format is *Stylish*.

## Requirements

Python = "^3.10"  
PyYAML = "^6.0"
