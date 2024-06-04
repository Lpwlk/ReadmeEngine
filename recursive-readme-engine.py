#!/usr/bin/env python

# Base imports
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.console import Console
from rich.table import Table
from rich.rule import Rule
import rich
import copy
# Debug imports
from rich import inspect
from rich.traceback import install
import os

console = Console(highlight = True)
install(console = console)

default_repo_name = 'RepoName'
default_dobadges = True
default_gh_username = 'Lpwlk'
default_dopybadges = True
default_pypi_pckgname = 'PackageName'
default_rbglink = '![Repobeats analytics svg](https://repobeats.axiom.co/api/embed/a9dcf7a67c680871d7836e0dc87e7950c946c8b4.svg "Repobeats analytics image")'

scolor = 'white'
secolor = 'white'
sacolor = 'white'

sstyle = 'italic blue'

# ![GitHub License](https://img.shields.io/github/license/Lpwlk/ReadmeEngine 'Github repo license')
# [![Lpwlk - GH profile](https://img.shields.io/static/v1?label=Lpwlk&message=Author&color=blue&logo=github)](https://github.com/Lpwlk 'Go to GitHub profile page')
# ![GitHub Tag](https://img.shields.io/github/v/tag/Lpwlk/ReadmeEngine?label=Version)
# <!-- ![GitHub Release](https://img.shields.io/github/v/release/Lpwlk/ReadmeEngine) -->

# ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/readme-engine?label=PyVersion 'Supported PyVersion from PyPi package')
# [![PyPI - Version](https://img.shields.io/pypi/v/readme-engine?label=PyPi)](https://pypi.org/project/readme-engine 'Pypi package version')
# [![PyPI - Downloads](https://img.shields.io/pypi/dm/readme-engine?label=Downloads)](https://pypi.org/project/readme-engine 'Pypi package monthly downloads')

# Markdown rendering

def pulsing_bar() -> str:
    return center('\t<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif?raw=true">')

def samp(content: str) -> str:
    return '\n<samp>\n' + content + '\n</samp>\n'

def center(content: str) -> str:
    return '\n<div align="center">\n' + content + '\n</div>\n'

def underline(content: str) -> str:
    return '<u>' + content + '</u>'

def italic(content: str) -> str:
    return '<i>' + content + '</i>'

def details(content: str, summary: str) -> str: # NOT IMPLEMENTED YET
    return f'<details>\n\n  <summary>\n\n  ##### {summary}*\n\n  </summary>\n\n{content}\n\n</details>'

def mdparagraph():
    return Prompt.ask(f'[{sacolor}]Enter paragraph content[/{sacolor}]', default = 'Empty paragraph', show_default = False)

def blockquote() -> str:
    content = '\n'
    try:
        while True:
            content += '> ' + Prompt.ask(f'[{sacolor}]Enter new blockquote line (Ctrl+C to end blockquote)[/{sacolor}]', default = 'Fast, good, cheap: pick any two.', show_default = False) + '\n> \n'
    except KeyboardInterrupt:
        print('')
        return content[:-3]

def codeblock() -> str:
    content = '\n'
    try:
        while True:
            content += Prompt.ask(f'[{sacolor}]Enter new codeblock line (Ctrl+C to end codeblock)[/{sacolor}]', default = 'sudo rm -rf /*', show_default = False) + '\n'
    except KeyboardInterrupt:
        print('')
        content = '```' + content + '```'
        return content
    
def mdlist() -> str:
    list, list_index = '', 0
    list_head = '\n- '
    list_type = Prompt.ask(f'[{sacolor}]Enter u/o/t for un/ordered/tickable list (Ctrl+C to end list)[/{sacolor}]', choices = ['u', 'o', 't'], default = 'u', show_default=False)
    if list_type == 2:
        list_head += '[ ] '
    try:
        while True:
            list_index += 1
            if list_type == 1: list_head = f'\n{list_index}. '
            list += list_head + Prompt.ask(f'[{sacolor}]Enter list item n°{list_index} (Ctrl+C to end list)[/{sacolor}]', default = f'List item n°{list_index}', show_default = False)
    except KeyboardInterrupt:
        print('')
        return list
    
def mdtable(title: str, width: int, height: int) -> str:
    mdtable = title
    mdtable += '\n' + '|  Column  ' * width + '|\n'
    mdtable += '|----------' * width + '|\n'
    mdtable += ('|          ' * width + '|\n') * height
    return mdtable
 
def imagefmt(link: str, img_width: int, img_title: str) -> str:
    return center(underline(italic(img_title))) + '\n' + center(f'\t<img width = "{img_width}" src="{link}">')

def mdheader(content: str, level: int):
    return '#' * (level-1) + ' ' + content + '\n\n'

def tocline(section_title: str):
    return f'- [{section_title}](#{section_title.replace(' ', '-')})  \n'

def rbgmdlink(mdlink: str) -> str:
    return center('\n<br>\n\n' + mdlink + '\n')

signature = center(samp('\n###### Mardown file generated using <a href ="https://github.com/Lpwlk/ReadmeEngine">readme-engine</a>\n'))

def main_help():
    help = Table(
        title = Rule('Main help', style = 'yellow'),
        box = rich.box.ROUNDED,
        min_width = 100,
        )
    help.add_column('Command', style='', header_style='bold yellow')
    help.add_column('Associated client methods description', style='', header_style='bold yellow')
    help.add_row('a',       'Add section to selected parent one (default to root)')
    help.add_row('e',       'Edit selected target section (default to last section created)')
    help.add_row('mv',      'Move selected section to targeted parent section (default to _ & _)')
    help.add_row('rm',      'Remove selected target section (default to last section created)')
    help.add_row('tree',    'Prints root section tree structure', end_section=True)
    help.add_row('h',       'Prints interractive run cmd help')
    help.add_row('q',       'Exits interractive run mode')
    console.print(help)
    
def section_edit_help() -> None:
    help = Table(
        title = Rule('Section edit help', style = 'yellow'),
        box = rich.box.ROUNDED,
        min_width = 100,
        )
    help.add_column('Command', style='', header_style='yellow')
    help.add_column('Associated client methods description', style='', header_style='yellow')
    help.add_row('a',       'Prints section edit cmd help')
    help.add_row('mv',       'Prints section edit cmd help')
    help.add_row('rm',       'Prints section edit cmd help')
    help.add_row('',       'Prints section edit cmd help')
    help.add_row('h',       'Prints section edit cmd help')
    help.add_row('q',       'Exits section edit mode')
    help.add_row('tree',    'Prints current section tree structure')
    console.print(help)
    
def content_creation_help():
    help = Table(
        title = Rule('Content_creation', style = 'yellow'),
        box = rich.box.ROUNDED,
        min_width = 100,
        )
    help.add_column('Command', style='', header_style='bold yellow')
    help.add_column('Associated client methods description', style='', header_style='bold yellow')
    help.add_row('h',       'Prints section content creation cmd help')
    help.add_row('q',       'Exits section content creation mode')
    console.print(help)

################################################################################################################################################################

class Section:
    '''
    Recursive Section object
    '''
    def __init__(self, title: str = None, content: str | list[str] | None = None, default_title: str = 'Section'):
        self.default_title = default_title
        self.title = title if title else Prompt.ask(prompt=f'[{scolor}]Enter section title[/{scolor}]', default=self.default_title, show_default=False, console=console)
        self.content = [] if content is None else [content]
        self.subsections = []
        print(hex(id(self.content)))
        for sub in self.subsections:
            print(' > ', hex(id(sub.content)))

    def add_section(self, subsection):
        if isinstance(subsection, Section):
            self.subsections.append(subsection)
            console.print(f'Section [{sstyle}]{subsection.title}[/{sstyle}] created in [{sstyle}]{self.title}[/{sstyle}]')
        else:
            console.print('Error: Sections.add_section method argument must be a Section object', style = 'red')
        
    def list_subsections(self, recursive_slist: list | None = None):
        if recursive_slist is None: recursive_slist = []
        recursive_slist.append(self)
        for subsection in self.subsections:
            subsection.list_subsections(recursive_slist)
        return recursive_slist
        
    def get_self_index(self):
        self.parent.get_session_index(self, new = True)
        
    def generate_markdown(self, level):
        markdown = mdheader(self.title, 1+level)
        for content in self.content:
            print(f'{self} {self.title=} {self.content=}')
            markdown += f'{content}\n\n'
        return markdown
        
    def recursive_generation(self, level: int = 1, markdown: str = ''):
        markdown += self.generate_markdown(level)
        for subsection in self.subsections:
            markdown += subsection.recursive_generation(level + 1)
        return markdown
        
    def select_content(self, prompt_text: str):
        return None
        
    def add_content(self):
        # while(True):
        try:
            cmd = Prompt.ask(
                prompt = f'[{secolor}][{sstyle}]{self.title}[/{sstyle}] content creation command[/{secolor}]', 
                choices = ['p', 't', 'l', 'b', 'c', 'i', 'pb', 'h', 'q'], 
                show_choices = True, 
                default = 'h',
                show_default = False,
                console = console
            )
            match cmd:
                case 'p':
                    print(self.title)
                    self.content.append(mdparagraph())
                    console.print(f'Paragraph created in section [italic]{self.title}[/italic]', style = sacolor)
                case 't':
                    table_title = Prompt.ask(f'[{sacolor}]Enter Table title[/{sacolor}]', default = 'Table title', show_default = False)
                    table_width = IntPrompt.ask(f'[{sacolor}]Enter table width in column[/{sacolor}]', default = 3, show_default = False)
                    table_height = IntPrompt.ask(f'[{sacolor}]Enter table height in rows[/{sacolor}]', default = 2, show_default = False)
                    self.content.append(mdtable(table_title, table_width, table_height))
                    console.print(f'Table with size {table_width}x{table_height} created in section [italic]{self.title}[/italic]', style = sacolor)
                case 'l':
                    self.content.append(mdlist())
                    console.print(f'List created in section [italic]{self.title}[/italic]', style = sacolor)
                case 'b':
                    self.content.append(blockquote())
                    console.print(f'Blockquote created in section [italic]{self.title}[/italic]', style = sacolor)
                case 'c':
                    self.content.append(codeblock())
                    console.print(f'Codeblock created in section [italic]{self.title}[/italic]', style = sacolor)
                case 'i':
                    img_link = Prompt.ask(f'[{sacolor}]Paste image URL[/{sacolor}]', default = 'https://i.kym-cdn.com/photos/images/original/001/688/970/a72.jpg', show_default = False)
                    img_width = IntPrompt.ask(f'[{sacolor}]Enter image width[/{sacolor}]', default = 200, show_default = False)
                    img_title = Prompt.ask(f'[{sacolor}]Enter image title[/{sacolor}]', default = 'Dogwifhat is goated', show_default = False)
                    self.content.append(imagefmt(img_link, img_width, img_title))
                    console.print(f'Image created using {img_width}px width in section [italic]{self.title}[/italic]', style = sacolor)
                case 'pb':
                    if Confirm.ask(f'[{sacolor}]Add space after separator ?[/{sacolor}]', default = False, show_default = False):
                        self.content.append(pulsing_bar()+'<br>\n')
                    else: 
                        self.content.append(pulsing_bar())
                    console.print(f'Pulsing bar separator created in section [italic]{self.title}[/italic]', style = sacolor)
                    
                case 'h':
                    content_creation_help()
                case 'q':
                    console.print(f'Exiting [{sstyle}]{self.title}[/{sstyle}] content creation operation', style = sstyle)
                    # break
        except KeyboardInterrupt:
            console.print('\nSection edit operation aborted (q exits to main menu)', style = 'red')
    
    def move_content(self):
        return None
        
    def remove_content(self):
        self.content.remove(self.select_content())
    
    def update_title(self):
        old_title = self.title
        self.title = Prompt.ask(
            prompt=f'[{scolor}]Enter new section title[/{scolor}]', 
            default=self.default_title, show_default=True, 
            console=console
        )
        console.print(f'Title [{sstyle}]{old_title}[/{sstyle}] changed to [{sstyle}]{self.title}[/{sstyle}]')

################################################################################################################################################################

class Markdown:
    '''
    Markdown generator object based on root Section definition
    '''
    def __init__(self, filename: str | None = None):
        self.filename = filename if filename else 'RECURSIVE.md'
        self.root = Section(title = f'{self.filename}')
    
    def write_markdown(self, filename: str | None = None):
        if not filename: filename = self.filename
        content = self.root.recursive_generation(level = 1)
        with open(filename, 'w') as f:
            f.write(content)
            
    def sections_tree(self, section: Section = None, prefix: str = '', is_last: bool = True, index: bool = True):
        branchsize = 2
        if section == None: 
            section = self.root
            console.print(Rule('Current section tree', style = sstyle), width = 50)
        if section.title is self.filename: 
            nprefix = ''
        elif is_last: 
            nprefix = '└' + '─'*branchsize + ' '
        else: 
            nprefix = '├' + '─'*branchsize + ' '
        
        if index: index = f"[{sstyle}]{self.get_section_index(section, new=False)[:-1]}[/{sstyle}]{' ─ '*(not (section.title is self.filename))}"
        else: index = ''
        console.print(prefix, nprefix, f'{index}[{sstyle}]{section.title}[/{sstyle}]', sep = '')
        
        if not is_last: 
            prefix += '│' + ' '*(branchsize+1)
        elif section.title is self.filename: 
            prefix += ' '
        else: 
            prefix += ' '*(branchsize+2)
            
        for i, child in enumerate(section.subsections):
            is_last = (i == len(section.subsections)-1)
            self.sections_tree(child, prefix, is_last)


    def get_parent(self, target: Section, root: Section = None):
        if root == None: root = self.root
        for child in root.subsections:
            if child == target:
                return root
            parent = self.get_parent(target, child)
            if parent is not None:
                return parent
        return None
        
        
    def get_section_index(self, target: Section, index: str = None, new: bool = True):
        if index is None:
            if new: index = f'{1+len(target.subsections)}'
            else: index = ''
        parent = self.get_parent(target)
        if parent is None: 
            return f'{1+len(self.root.subsections)}'
        elif parent is self.root:
            return (f'{1+parent.subsections.index(target)}.' + index)
        else:
            index = f'{1+parent.subsections.index(target)}.' + index 
            return self.get_section_index(parent, index)
            
            
    def select_section(self, prompt_text: str, root_include: bool = True, default_index: int = 0):
        sections_list = [section for section in self.root.list_subsections()]
        if root_include is False:
            del sections_list[0]
        if len(sections_list) >= 1:
            target = Prompt.ask(
                prompt = f'[{scolor}]{prompt_text}[/{scolor}]', 
                choices = [section.title for section in sections_list], show_choices = True, 
                default = sections_list[default_index].title, show_default = True,
                console = console
            )
            for section in sections_list:
                if section.title == target:
                    return section
        else:
            return None
            
            
    def add_section(self, section: Section | None = None):
        if section is None:
            target = self.select_section('Select parent session title')
            target.add_section(Section(default_title = self.get_section_index(target)))
        else:
            self.root.add_section(section)
            
            
    def move_sections(self):
        target = self.select_section('Select target section to be moved')
        parent = self.get_parent(target)
        if parent is not None:
            self.remove_section(target)
            new_parent = self.select_section('Select new parent section')
            new_parent.add_section(target)
            console.print(f'Section [{sstyle}]{target.title}[/{sstyle}] moved into [{sstyle}]{new_parent.title}[/{sstyle}]')
        else:
            console.print(f'Error: Root section [{sstyle}]{target.title}[/{sstyle}] can\'t be moved', style = 'red')
            
            
    def remove_section(self, target: Section = None):
        if target is None:
            target = self.select_section('Select section to be removed', root_include = False)
        if target is not None:
            target_parent = self.get_parent(target)
            target_parent.subsections.remove(target)
            console.print(f'Section [{sstyle}]{target.title}[/{sstyle}] removed from [{sstyle}]{target_parent.title}[/{sstyle}]')
        else:
            console.print(f'Error: No sections created under root section [{sstyle}]{self.root.title}[/{sstyle}]', style = 'red')
            
            
    def edit_section(self):
        target = self.select_section('Select target session to edit', default_index = -1)
        try:
            while(True):
                cmd = Prompt.ask(
                    prompt = f'[{secolor}][{sstyle}]{target.title}[/{sstyle}] edit command[/{secolor}]', 
                    choices = ['a', 'mv', 'rn', 'rm', 'h', 'q'], 
                    show_choices = True,
                    console = console,
                )
                match cmd:
                    case 'a':
                        target.add_content()
                    case 'mv':
                        target.move_content()
                    case 'rm':
                        target.remove_content()
                    case 'rn':
                        target.update_title()
                    case 'h':
                        section_edit_help()
                    case 'q':
                        console.print(f'Exiting [{sstyle}]{target.title}[/{sstyle}] edit operation', style = 'blue')
                        break
                self.write_markdown()
        except KeyboardInterrupt:
            console.print('\n[underline bold]KeyboardInterrupt[/underline bold] > Section edit operation aborted (q exits to main menu)', style = 'red')

            
    def run(self):
        try: # remember to switch increment w/ while loop to prevent from exiting script via Ctrl+C (q cmd for this instead)
            while True:
                cmd = Prompt.ask(
                    prompt = f'[{scolor}]Sections management command[/{scolor}]', 
                    choices = ['a', 'e', 'mv', 'rm', 'tree', 'h', 'q'], 
                    show_choices = True, 
                    console = console
                )
                match cmd:
                    case 'a':
                        self.add_section()
                    case 'mv':
                        self.move_sections()
                    case 'rm':
                        self.remove_section()
                    case 'e':
                        self.edit_section()
                    case 'tree':
                        self.sections_tree()
                    case 'h':
                        main_help()
                    case 'q':
                        console.print(f'Exiting interactive {self.filename} generation', style = 'blue')
                        break
                self.write_markdown(self.filename)
        except KeyboardInterrupt: # remember to switch increment w/ while loop 
            console.print(f'\n[underline bold]KeyboardInterrupt[/underline bold] > Exiting interactive {self.filename} generation', style = 'red')


################################################################################################################################################################

if __name__ == '__main__':
    os.system('clear && printf "\\e[3J"\n')

    # Templated section

    console.print(Rule('Templated README.md generation test', style = 'bold green'), '\n')
    templated_outfile = 'TEMPLATED.md'

    md = Markdown(templated_outfile)

    console.print(Rule('Generating readme structure using [underline bold]hard-coded statements[/underline bold] ...', style = 'yellow'), width = 100)
    
    # md.add_section(Section('Introduction', 'This is the introduction.'))
    s1 = Section('Chapter 1')
    md.add_section(s1)
    s2 = Section('Chapter 2')
    md.add_section(s2)
    # md.add_section(Section('Conclusion', 'This is the conclusion.'))
    
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
    s2.add_section(s21)  

    md.write_markdown()
    
    console.print(Rule('Printing recursive section names as [underline bold]list[/underline bold] ...', style = 'yellow'), width = 100)
    for section in md.root.list_subsections():
        console.print(section.title)

    console.print(Rule('Printing recursive section names as [underline bold]tree[/underline bold] ...', style = 'yellow'), width = 100)
    md.sections_tree(index = True)

    console.print('\n', Rule(f'Templated README.md version generated @ {templated_outfile}', style = 'green'))

    ### Interactive section

    console.print('\n', Rule('Switching to interactive markdown generation test', style = 'blue'), '\n')

    interactive_outfile = 'INTERACTIVE.md'
    cli_md = Markdown(interactive_outfile)
    cli_md.run()

    console.print('\n', Rule(f'Interactive README.md version generated @ {interactive_outfile}!', style = 'blue'))