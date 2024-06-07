# ReadmeEngine




<div align="center">

![GitHub License](https://img.shields.io/github/license/Lpwlk/ReadmeEngine "Github repo license")
[![Lpwlk - GH profile](https://img.shields.io/static/v1?label=Lpwlk&message=profile&color=blue&logo=github)](https://github.com/Lpwlk "Go to GitHub profile page")
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/readme-engine "Supported Python version from PyPi package")
[![PyPI - Version](https://img.shields.io/pypi/v/readme-engine)](https://pypi.org/project/readme-engine "Pypi package version")
[![PyPI - Downloads](https://img.shields.io/pypi/dm/readme-engine)](https://pypi.org/project/readme-engine "Pypi package monthly downloads")

</div>


### Table of Contents

**[Description](#Description)**<br>

**[Installation](#Installation)**<br>

**[Usage](#Usage)**<br>

**[Roadmap](#Roadmap)**<br>

<div align="center">
	<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif?raw=true">
</div>


### Description

This Python tool has been designed to generate (flavoured) markdown files for GitHub repositories. It includes basic badges and RepoBeats generation options as well as auto Table of content generation.

It is currently in developpement and its CLI interface is based of the rich Python library tools.

### Installation

To install the tool on your machine (Windows/MacOS/Linux), run the following command

```
pip install readme-engine
```

### Usage

The tool is designed using a tree structure for sections and section's contents. Every element (Section or content) can me moved/edited or removed using commands and help utilities are available for every menu.

### Roadmap

- [x] Update .gitignore & clean repo before next commit
- [ ] Implementation of InlinePrompts for sections-dependant commands (using format: >'a title' to add section foo instead of >'a' >'title')
- [ ] Full command coverage test w/ .svg output generation for CLI rendering validation alongside
- [ ] Add block-comments under major methods of both Markdown & Section objects
- [ ] Define clear styles names for each contexts & specific elements
- [ ] Include/update styles in every console outputs

<div align="center">
	<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif?raw=true">
</div>



<div align="center">

<br>

![Alt](https://repobeats.axiom.co/api/embed/99c19ed191ab42775bc9297d8af467ccc608f2e7.svg "Repobeats analytics image")

</div>



<div align="center">

<samp>

###### Mardown generated using readme-engine <a href ="https://github.com/Lpwlk/ReadmeEngine">Project's repo</a>

</samp>

</div>


