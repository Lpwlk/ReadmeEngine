#!/usr/bin/env python

# Base imports
from rich.console import Console
from rich.theme import Theme
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.table import Table
from rich.rule import Rule
from rich import inspect
# Debug imports
from rich.traceback import install
from rich.box import ROUNDED
import sys, os, webbrowser
install()
debug = (sys.argv[1] == '-d') if len(sys.argv)>1 else False

# Customizable styles - ReadmeEngine code semantic improvement concerning cli ouput generation
interactive_run_theme = Theme(
    inherit = False,
    styles = {
    'prompt.choices': 'italic blue',
    'prompt.default': 'blink bold yellow',
    # '': '',
    }
)
section_edit_theme = Theme(
    inherit = False,
    styles = {
    'prompt.choices': 'italic green',
    'prompt.default': 'blink bold yellow',
    # '': '',
    }
)
content_creation_theme = Theme(
    inherit = False,
    styles = {
    'prompt.choices': 'italic yellow',
    'prompt.default': 'blink bold yellow',
    # '': '',
    }
)

# Overriding base styles - Adjusting default rich theme styles for complete control over cli interface aspect
base_theme = Theme(
    styles = {
    'escape_color_content_creation' : 'bright_yellow',
    'escape_color_section_edit'     : 'orange1',
    'escape_color_interactive_run'  : 'red',
    'scolor'                        : 'default',
    'secolor'                       : 'default',
    'sacolor'                       : 'default',
    'sstyle'                        : 'default underline',
    }
)

console = Console(
    theme = base_theme,
    record = True,
)
def dbgGenSvg(inp):
    console.print(inp)
    print ('\033[1A\033[K', end='')

inspect(console, console = console)

def display_theme(context: dict):
    table = Table(
        width = 120,
        box = ROUNDED
    )
    table.add_column('Item')
    table.add_column('Value')
    for key, val in context.styles.items():
        table.add_row(key, repr(val))
    console.print(table)
    
display_theme(interactive_run_theme)
display_theme(section_edit_theme)
display_theme(content_creation_theme)

def switch_context_theme(context = dict):
    for key, val in context.styles.items():
        if key in base_theme.styles.keys():
            base_theme.styles[key] = val
            
# Markdown rendering

def pulsing_bar() -> str:
    return center('\t<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif?raw=true">', html = True)

def samp(content: str) -> str:
    return '\n<samp>\n' + content + '\n</samp>\n'

def center(content: str, html: bool = False) -> str:
    if not html: content = '\n' + content + '\n'
    return '\n<div align="center">\n' + content + '\n</div>\n\n'

def underline(content: str) -> str:
    return '<u>' + content + '</u>'

def italic(content: str) -> str:
    return '<i>' + content + '</i>'

def details(content: str, summary: str) -> str: # NOT IMPLEMENTED YET
    return f'<details>\n\n  <summary>\n\n  ##### {summary}*\n\n  </summary>\n\n{content}\n\n</details>'

def mdparagraph():
    text = Prompt.ask(f'[sacolor]Enter paragraph content[/sacolor]', default = 'Empty paragraph', show_default = False, console = console)
    if debug: dbgGenSvg(text)
    return text

def blockquote() -> str:
    content = '\n'
    try:
        while True:
            bq_item = Prompt.ask(f'[sacolor]Enter new blockquote line (Ctrl+C to end blockquote)[/sacolor]', default = 'Fast, good, cheap: pick any two.', show_default = False, console = console) + '\n> \n'
            if debug: dbgGenSvg(bq_item)
            content += '> ' + bq_item
    except KeyboardInterrupt:
        print('')
        return content[:-3]

def codeblock() -> str:
    content = '\n'
    try:
        while True:
            cb_item = Prompt.ask(f'[sacolor]Enter new codeblock line (Ctrl+C to end codeblock)[/sacolor]', default = 'sudo rm -rf /*', show_default = False, console = console)
            if debug: dbgGenSvg(cb_item)
            content += cb_item + '\n'
    except KeyboardInterrupt:
        print('')
        content = '```' + content + '```'
        return content
    
def mdlist() -> str:
    list, list_index = '', 0
    list_head = '\n- '
    list_type = Prompt.ask(f'[sacolor]Enter u/o/t for un/ordered/tickable list (Ctrl+C to end list)[/sacolor]', choices = ['u', 'o', 't'], default = 'u', show_default = False, console = console)
    if debug: dbgGenSvg(list_type)
    if list_type == 't':
        list_head += '[ ] '
    try:
        while True:
            list_index += 1
            if list_type == 'o': list_head = f'\n{list_index}. '
            list_item = Prompt.ask(f'[sacolor]Enter list item n°{list_index} (Ctrl+C to end list)[/sacolor]', default = f'List item n°{list_index}', show_default = False, console = console)
            if debug: dbgGenSvg(list_item)
            list += list_head + list_item
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
    return center('\t'+underline(italic(img_title)), html = True) + center(f'\t<img width = "{img_width}" src="{link}">', html = True)

def mdheader(content: str, level: int):
    return '#' * (level-1) + '&nbsp;&nbsp;'*(level-2) + ' '*(level-1) + content + '\n\n'

def rbgmdlink(mdlink: str) -> str:
    return center('\n<br>\n\n' + mdlink + '\n')

signature = center(samp('\n###### Mardown file generated using <a href ="https://github.com/Lpwlk/ReadmeEngine">readme-engine</a>\n'))

def interactive_run_mode_help() -> None:
	help = Table(
		title = Rule('Interactive run help', style = 'yellow'),
		box = ROUNDED, min_width = 100,
	)
	help.add_column('Command', style='', header_style='bold yellow')
	help.add_column('Description', style='', header_style='bold yellow')
	help.add_row('a', 	'Add section to target parent (defaut to root)')
	help.add_row('e', 	'Edit selected target section (default to last section created)')
	help.add_row('mv', 	'Move selected section to targeted parent section (default to _ & _)')
	help.add_row('rm', 	'Remove selected target section (default to last section created)')
	help.add_row('tree','Prints root section tree structure')
	help.add_row('temp','Load one of the available templates into root (default to generic template)', end_section = True)
	help.add_row('i', 	'Inspect Markdown object')
	help.add_row('h', 	'Print interactive run mode help utility')
	help.add_row('q',	'Exit from interactive run mode')
	console.print(help)

def section_edit_mode_help() -> None:
	help = Table(
		title = Rule('Section edit help', style = 'yellow'),
		box = ROUNDED, min_width = 100,
	)
	help.add_column('Command', style='', header_style='bold yellow')
	help.add_column('Description', style='', header_style='bold yellow')
	help.add_row('a', 	'Add section content (content creation mode)')
	help.add_row('mv', 	'Swap section contents using index inputs (default to 2 last contents)')
	help.add_row('rm', 	'Remove section content using index input (default to last content)')
	help.add_row('rm', 	'Rename section (default to section index)')
	help.add_row('up', 	'Update section content using index input (default to last content)', end_section = True)
	help.add_row('i', 	'Inspect targeted object')
	help.add_row('h', 	'Prints section edit mode help utility')
	help.add_row('q',	'Exit from section edit mode to interactive run mode')
	console.print(help)

def content_creation_mode_help() -> None:
	help = Table(
		title = Rule('Content creation help', style = 'yellow'),
		box = ROUNDED, min_width = 100,
	)
	help.add_column('Command', style='', header_style='bold yellow')
	help.add_column('Description', style='', header_style='bold yellow')
	help.add_row('a', 	'Create paragraph')
	help.add_row('t', 	'Create custom shape table')
	help.add_row('l', 	'Create custom list type until KeyboardInterrupt (un/ordered/tickable)')
	help.add_row('b', 	'Create blockquote lines until KeyboardInterrupt')
	help.add_row('c', 	'Create codeblock lines until KeyboardInterrupt')
	help.add_row('i', 	'Create custom image based on link, title and width')
	help.add_row('pb', 	'Create pulsing bar separator', end_section = True)
	help.add_row('h', 	'Prints content creation mode help')
	help.add_row('q',	'Exit from content creation mode to section edit mode')
	console.print(help)

################################################################################################################################################################

class Section:
    def __init__(self, title: str = None, content: str | list[str] | None = None, default_title: str = 'Section'):
        '''Section object - recursive implementation of markdown sections designed to be used in Markdown object methods.
        
        Args:
            title (str, optional): Prompt generated title if no title is passed as argument. Defaults to None.
            content (str | list[str] | None, optional): Initialized as empty list if no content or list of contents passed as arguments. Defaults to None.
            default_title (str, optional): Default title for title prompt in interractive mode or if no title is passed as arguments . Defaults to 'Section'.
        '''
        self.default_title = default_title
        self.title = title if title else Prompt.ask(prompt=f'[scolor]Enter section title[/scolor]', default=self.default_title, show_default=False, console=console)
        if debug: dbgGenSvg(self.title)
        self.subsections = []
        self.content = self.format_content(content)
        
    def format_content(self, content) -> list[str] | str | None:
        if isinstance(content, list):
            return content
        elif isinstance(content, str):
            return [content]
        elif content == None:
            return []
        else: 
            console.print(f'Error: Wrong section init content type ({type(content)}), content list cleared', style = 'red')
            return []

    def add_section(self, subsection):
        if isinstance(subsection, Section):
            self.subsections.append(subsection)
            console.print(f'Section [sstyle]{subsection.title}[/sstyle] created in [sstyle]{self.title}[/sstyle]')
        else:
            console.print('Error: Sections.add_section method argument must be a Section object', style = 'red')
        
    def list_subsections(self, recursive_slist: list | None = None):
        if recursive_slist is None: recursive_slist = []
        recursive_slist.append(self)
        for subsection in self.subsections:
            subsection.list_subsections(recursive_slist)
        return recursive_slist
    
    def generate_markdown(self, level):
        if level > 1:
            markdown = mdheader(self.title, 1+level)
        else:
            markdown = ''
        for content in self.content:
            markdown += f'{content}\n\n'
        return markdown

    def recursive_generation(self, level: int = 1, markdown: str = ''):
        markdown += self.generate_markdown(level)
        for subsection in self.subsections:
            markdown += subsection.recursive_generation(level + 1)
        return markdown
        
    def add_content(self):
        cmd = Prompt.ask(
            prompt=f'[secolor][sstyle]{self.title}[/sstyle] content creation command[/secolor]', 
            choices = ['p', 't', 'l', 'b', 'c', 'i', 'pb', 'h', 'q'], 
            show_choices = True, 
            console = console
        )
        if debug: dbgGenSvg(cmd)
        match cmd:
            case 'p':
                self.content.append(mdparagraph())
                console.print(f'Paragraph created in section [italic]{self.title}[/italic]', style = 'sacolor')
            case 't':
                table_title = Prompt.ask(f'[sacolor]Enter Table title[/sacolor]', default = 'Table title', show_default = False, console = console)
                if debug: dbgGenSvg(table_title)
                table_width = IntPrompt.ask(f'[sacolor]Enter table width in column[/sacolor]', default = 3, show_default = False, console = console)
                if debug: dbgGenSvg(table_width)
                table_height = IntPrompt.ask(f'[sacolor]Enter table height in rows[/sacolor]', default = 2, show_default = False, console = console)
                if debug: dbgGenSvg(table_height)
                self.content.append(mdtable(table_title, table_width, table_height))
                console.print(f'Table with size {table_width}x{table_height} created in section [italic]{self.title}[/italic]', style = 'sacolor')
            case 'l':
                self.content.append(mdlist())
                console.print(f'List created in section [italic]{self.title}[/italic]', style = 'sacolor')
            case 'b':
                self.content.append(blockquote())
                console.print(f'Blockquote created in section [italic]{self.title}[/italic]', style = 'sacolor')
            case 'c':
                self.content.append(codeblock())
                console.print(f'Codeblock created in section [italic]{self.title}[/italic]', style = 'sacolor')
            case 'i':
                img_link = Prompt.ask(f'[sacolor]Paste image URL[/sacolor]', default = 'https://i.kym-cdn.com/photos/images/original/001/688/970/a72.jpg', show_default = False, console = console)
                if debug: dbgGenSvg(img_link)
                img_width = IntPrompt.ask(f'[sacolor]Enter image width[/sacolor]', default = 200, show_default = False, console = console)
                if debug: dbgGenSvg(img_width)
                img_title = Prompt.ask(f'[sacolor]Enter image title[/sacolor]', default = 'Dogwifhat is goated', show_default = False, console = console)
                if debug: dbgGenSvg(img_title)
                self.content.append(imagefmt(img_link, img_width, img_title))
                console.print(f'Image created using {img_width}px width in section [italic]{self.title}[/italic]', style = 'sacolor')
            case 'pb':
                self.content.append(pulsing_bar())
                console.print(f'Pulsing bar separator created in section [italic]{self.title}[/italic]', style = 'sacolor')
            case 'h':
                content_creation_mode_help()
            case 'q':
                console.print(f'Exiting [sstyle]{self.title}[/sstyle] content creation operation', style = 'sstyle')
                return True

    def move_content(self):
        target = self.select_content('Select first target content index to swap', 0)
        if target == None:
            console.print('Error: no content created', style = 'red')
            return None
        swap = self.select_content('Select second target content index to swap', -1)
        self.content[target-1], self.content[swap-1] = self.content[swap-1], self.content[target-1]
        console.print(f'Content index {target} swapped with index {swap}', style = 'secolor')

    def remove_content(self):
        target = self.select_content('Select target to be removed', )
        if target == None:
            console.print('Error: no content created', style = 'red')
            return None
        del self.content[target-1]
        console.print(f'Content with index {target} removed from section instance [italic]{self.title}[/italic]', style = 'secolor')
        
    def select_content(self, prompt_text: str, default_index: int = 0):
        if self.content == []:
            return None
        target_index = IntPrompt.ask(
            prompt= prompt_text, 
            choices = [str(i+1) for i in range(len(self.content))], show_choices = True, 
            default = default_index, show_default = True,
            console = console
        )
        if debug: dbgGenSvg(target_index)
        return target_index
    
    def update_title(self):
        old_title = self.title
        self.title = Prompt.ask(
            prompt = f'[scolor]Enter new section title[/scolor]', 
            default = self.default_title, show_default = True, 
            console = console
        )
        if debug: dbgGenSvg(self.title)
        console.print(f'Title [sstyle]{old_title}[/sstyle] changed to [sstyle]{self.title}[/sstyle]')

################################################################################################################################################################

class Markdown:
    def __init__(self, filename: str | None = None):
        '''Markdown generator object - Can be used in interactive mode using the run method as well as using methods directly inside a script.

        Args:
            filename (str | None, optional): Filename to be used to generate markdown output. Defaults to None.
        '''
        self.filename = filename if filename else 'RECURSIVE.md'
        self.root = Section(title = 'README.md')
        self.toc = True
        self.header = self.generate_header()
        self.footer = self.generate_footer()
            
    def write_markdown(self, filename: str | None = None) -> None:
        if not filename: filename = self.filename
        if self.toc: self.update_toc()
        content = self.header + self.root.recursive_generation(level = 1) + self.footer
        with open(filename, 'w') as f:
            f.write(content)
            
    def sections_tree(self, section: Section = None, prefix: str = '', is_last: bool = True, index: bool = True):
        branchsize = 2
        if section == None: 
            section = self.root
            console.print(Rule('Current section tree', style = 'sstyle'), width = 50)
        if section.title is self.root.title: 
            nprefix = ''
        elif is_last: 
            nprefix = f'└{'─'*branchsize} '
        else: 
            nprefix = f'├{'─'*branchsize} '
        if index: index = f"[sstyle]{self.get_section_index(section, new=False)[:-1]}[/sstyle] "
        else: index = ''
        console.print(prefix, nprefix, f'{index}[sstyle]{section.title}[/sstyle]', sep = '')
        if not is_last: 
            prefix += f'│{' '*(branchsize+1)}'
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
                prompt = f'[scolor]{prompt_text}[/scolor]', 
                choices = [section.title for section in sections_list], show_choices = True, 
                default = sections_list[default_index].title, show_default = False,
                console = console
            )
            if debug: dbgGenSvg(target)
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
            parent.subsections.remove(target)

            new_parent = self.select_section('Select new parent section')
            new_parent.subsections.append(target)
            console.print(f'Section [sstyle]{target.title}[/sstyle] moved into [sstyle]{new_parent.title}[/sstyle]')
        else:
            console.print(f'Error: Root section [sstyle]{target.title}[/sstyle] can\'t be moved', style = 'red')
            
            
    def remove_section(self, target: Section = None):
        if target is None:
            target = self.select_section('Select section to be removed', root_include = False)
        if target is not None:
            target_parent = self.get_parent(target)
            target_parent.subsections.remove(target)
            console.print(f'Section [sstyle]{target.title}[/sstyle] removed from [sstyle]{target_parent.title}[/sstyle]')
        else:
            console.print(f'Error: No sections created under root section [sstyle]{self.root.title}[/sstyle]', style = 'red')
    
    # Header methods 
                
    def make_badges(self, repo_name: str, gh_username: str, pypi_pckg: str) -> str:
        badges = [  
            f'![GitHub license](https://img.shields.io/github/license/{gh_username}/{repo_name} "Github repo license")',
            f'[![GitHub profile](https://img.shields.io/static/v1?label={gh_username}&message=profile&color=blue&logo=github)](https://github.com/{gh_username} "Go to GitHub profile page")',
            f'[![GitHub tags](https://img.shields.io/github/v/tag/{gh_username}/{repo_name}?label=Version)](https://github.com/{gh_username}/{repo_name}/tags "Go to GitHub repo tags")',
            f'[![PyPI - Python version](https://img.shields.io/pypi/pyversions/{pypi_pckg})](https://pypi.org/project/{pypi_pckg} "Supported Python version from PyPi package")',
            f'[![PyPI - Package version](https://img.shields.io/pypi/v/{pypi_pckg})](https://pypi.org/project/{pypi_pckg} "Pypi package version")',
            f'[![PyPI - Package downloads](https://img.shields.io/pypi/dm/{pypi_pckg})](https://pypi.org/project/{pypi_pckg} "Pypi package monthly downloads")',
        ]
        badge_array = ''
        for badge in badges: badge_array += badge + '\n'*(badge != badges[-1])
        return center(badge_array)

    def update_toc(self):
        toc = self.recursive_tocline(self.root)
        for index, content in enumerate(self.root.content):
            if 'Table of Contents' in content:
                self.root.content[index] = toc

    def recursive_tocline(self, child: Section, toc: str = '## Table of Contents\n\n', level = 0):
        for section in child.subsections:
            toc += f'{'&nbsp;&nbsp;&nbsp;'*level}{self.get_section_index(section, new = False)[:-1]} - [{section.title}](#{section.title.replace(' ', '-')})  \n'
            # toc += f'{'#'*(level+5)} {'&nbsp;&nbsp;'*level}{self.get_section_index(section, new = False)[:-1]} - [{section.title}](#{section.title.replace(' ', '-')})  \n'
            toc = self.recursive_tocline(section, toc, level + 1)
        return toc
    
    def generate_footer(self) -> bool:
        default_rbglink = '![Alt](https://repobeats.axiom.co/api/embed/99c19ed191ab42775bc9297d8af467ccc608f2e7.svg "Repobeats analytics image")'
        if debug:
            return f'\n{pulsing_bar()}\n{rbgmdlink(default_rbglink)}\n{signature}'
        else:
            if Confirm.ask('Add [bold]RepoBeats analytics[/bold] in footer ?', default = True, show_default=False):
                rbglink = Prompt.ask('> Enter [bold]RepoBeats md link[/bold] (https://repobeats.axiom.co/)', default = default_rbglink, show_default = False, console = console)
                if not rbglink.endswith('Repobeats analytics image'):
                    console.print('Not a valid RepoBeats API link, using default one')
                return f'\n{pulsing_bar()}\n{rbgmdlink(rbglink)}\n{signature}'
            else:
                return f'\n{pulsing_bar()}\n{signature}'

    def generate_header(self) -> None:
        if debug:
            header = center('\n'+mdheader('ReadmeEngine', 2)+'\n')
            header += self.make_badges('ReadmeEngine', 'Lpwlk', 'pwlk')
            self.toc = True
            self.root.content.append('Table of Contents')
            self.root.content.append(pulsing_bar())
        else:
            repo_name = Prompt.ask(prompt='Enter [bold]GitHub repository name[/bold]', default = 'ReadmeEngine', show_default = False, console = console)
            header = center('\n'+mdheader(repo_name, 2)+'\n')
            gh_username = Prompt.ask('> Enter [bold]GitHub username[/bold]', default = 'Lpwlk', show_default = False, console = console)
            pypi_pckg = Prompt.ask('> Enter [bold]PyPi package name[/bold]', default = 'pwlk', show_default = False, console = console)
            if Confirm.ask('Add [bold]Shields.io badges[/bold] in header ?', default = True, show_default = False, console = console):
                header += self.make_badges(repo_name, gh_username, pypi_pckg)
            if Confirm.ask('Add [bold]Table of Contents[/bold] in header ?', default = True, show_default = False, console = console):
                self.toc = True
                self.root.content.append('Table of Contents')
            self.root.content.append(pulsing_bar())
        return header
  
    def generate_template(self, template: str | None = None) -> None:
        cmd = Prompt.ask(
            prompt = f'Enter template type to call for [sstyle]{self.root.title}[sstyle]',
            choices = ['d', 'm'], show_choices = True,
            default = 'd', show_default = False,
            console = console
        )
        if debug: dbgGenSvg(cmd)
        match cmd:
            case 'd':
                template_name = 'Default'
                self.root.subsections = [
                    Section('Description', 	['Repository project description including project typical usecase, available features and links to any reference visitors might be unfamiliar with.']),
                    Section('Installation', ['Installation guide for each tool included in the repository.']),
                    Section('Usage', 		['Details and example of usage of the repository tools using text, image(s) and/or gif(s).', imagefmt('https://i.kym-cdn/photos/imags/original/001/688/970/a72.jpg', 200, 'Dogwifhat is goated')]),
                    Section('Roadmap', 		['Developement goals as well as current planned or achieved milestones', center(mdtable('Milestones', width = 3, height = 6))]),
                    Section('License', 		['For open source projects, say how it is licensed.']),
                    Section('Authors', 		['The repo has been created by [Author] and maintained by [Author]. Feel free to contact [Author] via email or creating a GitHub issue for any repo-related support request.']),
                ]
            case 'm':
                template_name = 'Minimal'
                self.root.subsections = [
                    Section('Description', 	['Repository project description including project typical usecase, available features and links to any reference visitors might be unfamiliar with.']),
                    Section('Installation', ['Installation guide for each tool included in the repository.']),
                    Section('Usage', 		['Details and example of usage of the repository tools using text, image(s) and/or gif(s).', imagefmt('https://i.kym-cdn/photos/imags/original/001/688/970/a72.jpg', 200, 'Dogwifhat is goated')]),
                    Section('License', 		['For open source projects, say how it is licensed.']),
                ]
        console.print(f'{template_name} template generated: overriding current root sections for the following structure ...')
        self.sections_tree()
    def edit_section(self):
        switch_context_theme(section_edit_theme)
        target = self.select_section('Select target session to edit', default_index = -1)
        try:
            while(True):
                cmd = Prompt.ask(
                    prompt = f'[secolor][sstyle]{target.title}[/sstyle] edit command[/secolor]', 
                    choices = ['a', 'mv', 'rm', 'rn', 'up', 'i', 'h', 'q'], 
                    show_choices = True,
                    console = console,
                )
                if debug: dbgGenSvg(cmd)
                match cmd:
                    case 'a':
                        try:
                            switch_context_theme(content_creation_theme)
                            while True:
                                if target.add_content():
                                    break
                                else:
                                    self.write_markdown()
                        except KeyboardInterrupt:
                            console.print('\n[underline bold]KeyboardInterrupt[/underline bold] > Content creation operation aborted (q exits to main menu)', style = 'escape_color_content_creation')
    
                    case 'mv':
                        target.move_content()
                    case 'rm':
                        target.remove_content()
                    case 'rn':
                        target.update_title()
                    case 'up':
                        target.update_content()
                    case 'i':
                        inspect(target, methods = True)
                    case 'h':
                        section_edit_mode_help()
                    case 'q':
                        console.print(f'Exiting [sstyle]{target.title}[/sstyle] edit operation', style = 'blue')
                        break
                self.write_markdown()
        except KeyboardInterrupt:
            console.print('\n[underline bold]KeyboardInterrupt[/underline bold] > Section edit operation aborted (q exits to main menu)', style = 'escape_color_section_edit')


    def run(self):
        self.write_markdown()
        try:
            switch_context_theme(interactive_run_theme)
            while True:
                cmd = Prompt.ask(
                    prompt = f'[scolor]Sections management command[/scolor]', 
                    choices = ['a', 'e', 'mv', 'rm', 'tree', 'temp', 'i', 'h', 'q'], 
                    show_choices = True, 
                    console = console
                )
                if debug: dbgGenSvg(cmd)

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
                    case 'temp':
                        self.generate_template()
                    case 'i':
                        inspect(self, methods = True)
                    case 'h':
                        interactive_run_mode_help()
                    case 'q':
                        console.print(f'Exiting interactive {self.filename} generation', style = 'blue')
                        break
                self.write_markdown(self.filename)
        except KeyboardInterrupt:
            console.print(f'\n[underline bold]KeyboardInterrupt[/underline bold] > Exiting interactive {self.filename} generation', style = 'escape_color_interactive_run')


################################################################################################################################################################

if __name__ == '__main__':
    # Templated section
    console.print(Rule('Templated README.md generation test', style = 'bold green'))
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

    console.print(Rule(f'Templated README.md version generated @ {templated_outfile}', style = 'green'))

    ### Interactive section

    console.print('\n', Rule('Switching to interactive markdown generation test', style = 'blue'))

    interactive_outfile = 'INTERACTIVE.md'
    cli_md = Markdown(interactive_outfile)
    cli_md.run()
    console.print('\n', Rule(f'Interactive README.md version generated @ {interactive_outfile}!', style = 'blue'))
    
    console.save_svg('cli_outputs/output.svg', clear =  False)
    console.save_text('cli_outputs/output.txt', clear =  False)
    console.save_html('cli_outputs/output.html', clear =  True)
    
# webbrowser.open(f'file://{os.path.abspath('cli_outputs/output.svg')}')
# webbrowser.open(f'file://{os.path.abspath('cli_outputs/output.html')}')
