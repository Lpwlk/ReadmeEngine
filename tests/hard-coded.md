
<div align="center">


#  ReadmeEngine




</div>


<div align="center">

![GitHub license](https://img.shields.io/github/license/Lpwlk/ReadmeEngine "Github repo license")
[![GitHub profile](https://img.shields.io/static/v1?label=Lpwlk&message=profile&color=blue&logo=github)](https://github.com/Lpwlk "Go to GitHub profile page")
[![GitHub tags](https://img.shields.io/github/v/tag/Lpwlk/ReadmeEngine?label=Version)](https://github.com/Lpwlk/ReadmeEngine/tags "Go to GitHub repo tags")
[![PyPI - Python version](https://img.shields.io/pypi/pyversions/pwlk)](https://pypi.org/project/pwlk "Supported Python version from PyPi package")
[![PyPI - Package version](https://img.shields.io/pypi/v/pwlk)](https://pypi.org/project/pwlk "Pypi package version")
[![PyPI - Package downloads](https://img.shields.io/pypi/dm/pwlk)](https://pypi.org/project/pwlk "Pypi package monthly downloads")

</div>

## Table of Contents

1 - [Introduction](#Introduction)  
2 - [Chapter 1](#Chapter-1)  
&nbsp;&nbsp;&nbsp;2.1 - [Chapter 1.1](#Chapter-1.1)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.1 - [Chapter 1.1.1](#Chapter-1.1.1)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.2 - [Chapter 1.1.2](#Chapter-1.1.2)  
&nbsp;&nbsp;&nbsp;2.2 - [Chapter 1.2](#Chapter-1.2)  
3 - [Chapter 2](#Chapter-2)  
4 - [Conclusion](#Conclusion)  



<div align="center">
	<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif?raw=true">
</div>



## &nbsp;&nbsp; Introduction

This is the introduction.

## &nbsp;&nbsp; Chapter 1

### &nbsp;&nbsp;&nbsp;&nbsp; ➤ Chapter 1.1

Content of chapter 1.1.

```
md = Markdown('tests/'+outfile)
md.add_section(Section('Introduction', 'This is the introduction.'))
s1 = Section('Chapter 1')
md.add_section(s1)
s2 = Section('Chapter 2')
md.add_section(s2)
md.add_section(Section('Conclusion', 'This is the conclusion.'))
s11 = Section('Chapter 1.1', 'Content of chapter 1.1.')
s11.add_section(Section('Chapter 1.1.1', 'Content of chapter 1.1.1.'))
s11.add_section(Section('Chapter 1.1.2', ['Content of chapter 1.1.2.', '2nd Content of chapter 1.1.2.']))
s1.add_section(s11)
s1.add_section(Section('Chapter 1.2', 'Content of chapter 1.2.'))
s21 = Section('Chapter 2.1', 'Content of chapter 2.1.')  
s211 = Section('Chapter 2.1.1', 'Content of chapter 2.1.1.')
s21.add_section(s211)
s2111 = Section('Chapter 2.1.1.1', 'Content of chapter 2.1.1.1.')
s211.add_section(s2111)
s211.add_content(s211.add_content(codeblock([this_code]))
s2.add_section(s21)  
md.tree_sections(index = True)
md.write_markdown()
```

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ➤ Chapter 1.1.1

Content of chapter 1.1.1.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ➤ Chapter 1.1.2

Here is a sample of code that can be used to generate custom templates without editing the source code.

You may add content in sections instances as second argument in list or using the add_content method and built-in markdown parsers.

### &nbsp;&nbsp;&nbsp;&nbsp; ➤ Chapter 1.2

Content of chapter 1.2.

## &nbsp;&nbsp; Chapter 2

## &nbsp;&nbsp; Conclusion

This is the conclusion.



<div align="center">
	<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif?raw=true">
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

