
<div align="center">


#  ReadmeEngine




</div>


<div align="center">

![Open source](https://img.shields.io/badge/open-source-6894d4?logo=git&logoColor=6894d4)
![GitHub license](https://img.shields.io/github/license/Lpwlk/ReadmeEngine?color=86c255 "Github repo license")
[![GitHub profile](https://img.shields.io/static/v1?label=Lpwlk&message=profile&color=6894d4&logo=github)](https://github.com/Lpwlk "Go to GitHub profile page")
[![GitHub tags](https://img.shields.io/github/v/tag/Lpwlk/ReadmeEngine?color=6894d4)](https://github.com/Lpwlk/ReadmeEngine/tags "Go to GitHub repo tags")
[![GitHub last release](https://img.shields.io/github/release-date/Lpwlk/ReadmeEngine?color=6894d4?label=Release)](https://github.com/{gh_username}/{repo_name} "Go to GitHub repo")
[![PyPI - Python version](https://img.shields.io/pypi/pyversions/readme-engine?color=6894fA)](https://pypi.org/project/readme-engine "Supported Python version from PyPi package")
[![PyPI - Package version](https://img.shields.io/pypi/v/readme-engine?color=eda547)](https://pypi.org/project/readme-engine "Pypi package version")
[![PyPI - Package downloads](https://img.shields.io/pypi/dm/readme-engine?color=76b645)](https://pypi.org/project/readme-engine "Pypi package monthly downloads")

</div>

## Table of Contents

1 - [Description](#Description)  
2 - [Installation](#Installation)  
&nbsp;&nbsp;&nbsp;2.1 - [Prerequisites](#Prerequisites)  
&nbsp;&nbsp;&nbsp;2.2 - [Instructions](#Instructions)  
&nbsp;&nbsp;&nbsp;2.3 - [Dependancies](#Dependancies)  
3 - [Usage](#Usage)  
&nbsp;&nbsp;&nbsp;3.1 - [Interactive mode](#Interactive-mode)  
&nbsp;&nbsp;&nbsp;3.2 - [Templating](#Templating)  
&nbsp;&nbsp;&nbsp;3.3 - [Best practices](#Best-practices)  
4 - [Tests](#Tests)  
5 - [Roadmap](#Roadmap)  
6 - [Contributing](#Contributing)  
7 - [License](#License)  



<div align="center">
	<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif?raw=true">
</div>



## &nbsp;&nbsp; Description

This Python tool has been designed to generate (flavoured) markdown files for GitHub repositories. It includes basic badges and RepoBeats generation options as well as multiple basic integrated methods to render markdown elements inside recursive section objects.

It can be useful to kickstart personal projects as it includes templating options via Mardown & Section objects methods calls.

Moreover, a wide range of flavoured markdown (GitHub Markdown) features are supported by the templated-compatible interactive mode commands. 

<div align="center">
	<img width = "500" src="https://github.com/Lpwlk/ReadmeEngine/blob/main/tests/hard-coded.svg">
</div>

> Note that some commands only generate a "base of content". Thus, generated content (example: custom-size table) may have to be updated after interactive mode.

## &nbsp;&nbsp; Installation

### &nbsp;&nbsp;&nbsp;&nbsp; Prerequisites

The package was written on Python 3.12 version but supported versions will be determined when the package will be released on PyPi. 

This section will be updated accordingly with the first PyPi realease.

### &nbsp;&nbsp;&nbsp;&nbsp; Instructions

To work with the tool on your machine and start templating with your own preferences, you can clone the repo or download the PyPi package using pip ...

Cloning the repository ...

```
git clone https://github.com/Lpwlk/ReadmeEngine.git
```

Downloading the PyPi package ...

```
pip install readme-engine
```

### &nbsp;&nbsp;&nbsp;&nbsp; Dependancies

The engine is built on top of the rich package for CLI rendering in interactive mode as well as for verbose features & tools provided by both python objects.

## &nbsp;&nbsp; Usage

The tool is designed using a tree structure for sections and section's contents. Every element (Section or content) can me moved/edited or removed using commands and help utilities are available withing every interactive menu & submenus.

### &nbsp;&nbsp;&nbsp;&nbsp; Interactive mode

The interactive mode can be started using the run method on Markdown object instance. It includes several submenus for header/footer generation as well as section structure & content management.

```
import readme-engine

md = Markdown()
md.run()
```

Every menu & submenu includes a help utility which describes every available commands.

<div align="center">
	<img width = "200" src="https://github.com/Lpwlk/ReadmeEngine/blob/main/tests/interactive-test-render.png">
</div>


### &nbsp;&nbsp;&nbsp;&nbsp; Templating

Templating consists of Markdown & Section objects recursive calls within a script to create various kinds of README.md structures with control on titles and contents.

Some methods still need to be updated to be fully available externally (some work only in interactive mode as they are not supposed to be very useful when it comes to template creation from outside the source-code).

However, some structure display methods such as tree_sections and list_sections are available for the typical usecase described in the next subsection (Best practices). Future commits will include some example scripts using all available methods for personal templating purposes.

### &nbsp;&nbsp;&nbsp;&nbsp; Best practices

The ideal use of this tool would be to design your own base template for some of your (future) projects and to call interactive mode on the templated object in order to automate your README.md redactions/updates (fast copy&paste of previous markdown content works well with interactive mode prompts).

```
import readme-engine

md = Markdown()
md.add_section(Section(title = 'Description', content = ['Project description.']))
md.add_section(Section(title = 'Installation'))
usage = Section('Usage')
usage.add_section(Section('Best practices'))
md.add_section(usage)

md.run() # Calling interactive mode on Markdown object to edit previous template
```

This methodology can be reproduced inside the 'temp' command in main interactive run menu with the default Markdown template. This command reinitialize the whole Markdown structure & content to create the selected default template.

## &nbsp;&nbsp; Tests

The /tests directory includes rich-generated .svg files of terminal output of the script in pure templating as well as pure interactive contexts with the corresponding generated markdown file.


> Future commits should include unit-tests for every methods references as available for templating in the Usage section.


## &nbsp;&nbsp; Roadmap


- [x] Update .gitignore & clean repo before next commit
- [x] Implementation of one-line prompts for section selects [canceled because not efficient]
- [x] Implement details tag option for foldable content creation in content creation mode
- [x] Full command coverage test w/ .svg output generation for CLI rendering validation alongside
- [ ] Add block-comments under major methods of both Markdown & Section objects
- [x] Define clear styles names for each contexts & specific elements
- [x] Include/update styles in every console outputs
- [ ] Define external methods availability for external templating use & update accordingly
- [ ] Reference every available methods for the end-user w/ descrition in Usage > Templating
- [ ] Write unit tests for every methods externally available in /tests


## &nbsp;&nbsp; Contributing

Pull requests are welcome. For major changes, please fell free to open an issue first to discuss what you would like to change and in which way you would like to to it.

## &nbsp;&nbsp; License

The project is currently published under MIT license which allows very flexible use for any kind of purposes and contributions.



<div align="center">
	<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif?raw=true">&nbsp;
</div>



<div align="center">


<br>

![Alt](https://repobeats.axiom.co/api/embed/99c19ed191ab42775bc9297d8af467ccc608f2e7.svg "Repobeats analytics image")


</div>



<div align="center">


<samp>

###### Mardown file generated using <a href ="https://github.com/Lpwlk/ReadmeEngine">readme-engine</a>

</samp>


</div>

