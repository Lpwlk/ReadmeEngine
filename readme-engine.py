from rich.prompt import Prompt, IntPrompt, Confirm
from rich.console import Console
from rich.table import Table
from rich.rule import Rule

console = Console(log_path = False, highlight = False)

default_repo_name = 'Lpwlk'
default_dobadges = True
default_gh_username = 'Lpwlk'
default_dopybadges = True
default_pypi_pckgname = 'pwlk'
default_rbglink = '![RepoBeats analytics image](https://repobeats.axiom.co/api/embed/99c19ed191ab42775bc9297d8af467ccc608f2e7.svg "Repobeats analytics image")'

# CLI aspects

def sections_management_prompt(style: str = 'bold blue') -> str:
    return f'[{style}]Sections management command[/{style}]'

def section_edit_prompt(section: str, style: str = 'bold magenta') -> str:
    return f'[{style}]Section {section} edit command[/{style}]'

def section_add_prompt(section: str, style: str = 'bold yellow') -> str:
    return f'[{style}]Section {section} add command[/{style}]'

# Markdown rendering

def pulsing_bar() -> str:
    return center('\t<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif?raw=true">')

def samp(content: str) -> str:
    return '\n<samp>\n' + content + '\n</samp>\n'

def center(content: str) -> str:
    return '\n<div align="center">\n' + content + '\n</div>\n'

def underline(content: str) -> str:
    return '<u>' + content + '</u>'

def details(content: str, summary: str) -> str:
    return f'<details>\n\n  <summary>\n\n  ##### {summary}*\n\n  </summary>\n\n{content}\n\n</details>'

def blockquote(content: str) -> str:
    return '> ' + content 

def codeblock(content: str) -> str:
    return '```\n' + content + '\n```'

def mdlist() -> str:
    list, listindex = '', 0
    listhead = '\n - '
    ordered = Prompt.ask('Enter \'y\' for ordered list', default = False)
    try:
        while True:
            listindex += 1
            if ordered: 
                listhead = f'\n {listindex}. '
            list += listhead + Prompt.ask(f'Enter list item n°{listindex}', default = f'List item n°{listindex}', show_default = False)
    except KeyboardInterrupt:
        return list
    
def mdtable(title: str, width: int, height: int) -> str:
    mdtable = title
    mdtable += '\n' + '|  Column  ' * width + '|\n'
    mdtable += '|----------' * width + '|\n'
    mdtable += ('|          ' * width + '|\n') * height
    return mdtable
 
def imagefmt(link: str, img_width: int, img_title: str) -> str:
    return center(underline(img_title)) + '\n' + center(f'\t<img width = "{img_width}" src="{link}">')

def mdheader(content: str, level: int):
    return '#' * level + ' ' + content + '\n\n'

def tocline(section_title: str):
    return f'**[{section_title}](#{section_title.replace(' ', '-')})**<br>\n\n'

def rbgmdlink(mdlink: str) -> str:
    return center('\n<br>\n\n' + mdlink + '\n')

signature = center(samp('\n###### Mardown generated using readme-engine <a href ="https://github.com/Lpwlk/ReadmeEngine">Project\'s repo</a>\n'))

# CLI help utilities
    
def content_add_help() -> None:
    help = Table(title=Rule('Main menu help utility', style = 'white'), border_style='yellow', min_width = 80)
    help.add_column('Command', style='yellow', header_style='bold yellow')
    help.add_column('Description', style='yellow', header_style='bold yellow')
    help.add_row('p',  'Add paragraph')
    help.add_row('t',  'Add empty table')
    help.add_row('l',  'Add list until KeyboardInterurpt')
    help.add_row('b',  'Add blockquote')
    help.add_row('c',  'Add codeblock')
    help.add_row('i',  'Add image from URL')
    help.add_row('pb', 'Add green pulsingbar')
    help.add_row('h',  'Display add content menu')
    help.add_row('q',  'Exit from add content to edit content menu')
    console.print(help)
    
def content_edit_help() -> None:
    help = Table(title=Rule('Section edit menu help utility', style = 'white'), border_style='magenta', min_width = 80)
    help.add_column('Command', style='', header_style='bold')
    help.add_column('Description', style='', header_style='bold')
    help.add_row('a',  'Add content to section')
    help.add_row('rm', 'Remove content from section')
    help.add_row('mv', 'Swap contents in section')
    help.add_row('h',  'Display session edit menu help')
    help.add_row('q',  'Exit from session edit to session management menu')
    console.print(help)
    
def sections_management_help() -> None:
    help = Table(title=Rule('Sections management help utility', style = 'white'), border_style='blue', min_width = 80)
    help.add_column('Command', style='', header_style='bold')
    help.add_column('Description', style='', header_style='bold')
    help.add_row('e',  'Section edit menu')
    help.add_row('a',  'Add section')
    help.add_row('rm', 'Remove section')
    help.add_row('mv', 'Swap sections')
    help.add_row('h',  'Display sections management menu help')
    help.add_row('q',  'Exit generator instance')
    console.print(help)

### Generators objects 
    
class Section:
    def __init__(self, index: int = 0):
        self.index = index
        self.title = Prompt.ask(prompt='[bright_blue]Enter section title[/bright_blue]', default=f'Section {self.index+1}', show_default=False, console=console)
        self.contents = []
    
    def select_content(self, keyword: str):
        if self.contents == []:
            return None
        target_index = IntPrompt.ask(
            prompt = f'[bright_blue]Enter {keyword} index[/bright_blue]', 
            choices = [str(i+1) for i in range(len(self.contents))], 
            show_choices = True, 
            default = len(self.contents),
            show_default = False,
            console = console
        )
        return target_index
        
    def add_content(self, parent):
        while(True):
            ctype = Prompt.ask(
                prompt = section_add_prompt(self.title), 
                choices = ['p', 't', 'l', 'b', 'c', 'i', 'pb', 'h', 'q'], 
                show_choices = True, 
                default = len(self.contents)+1,
                show_default = False,
                console = console
            )
            match ctype:
                case 'p':
                    self.contents.append(Prompt.ask('[yellow]Enter paragraph content[/yellow]', default = 'Empty paragraph', show_default = False))
                    console.log(f'Paragraph created in section [italic]{self.title}[/italic]', style = 'yellow')
                case 't':
                    table_title = Prompt.ask('[yellow]Enter Table title[/yellow]', default = 'Table title', show_default = False)
                    table_width = IntPrompt.ask('[yellow]Enter table width in column[/yellow]', default = 3, show_default = False)
                    table_height = IntPrompt.ask('[yellow]Enter table height in rows[/yellow]', default = 2, show_default = False)
                    self.contents.append(mdtable(table_title, table_width, table_height))
                    console.log(f'Table with size {table_width}x{table_height} created in section [italic]{self.title}[/italic]', style = 'yellow')
                case 'l':
                    self.contents.append(mdlist())
                    console.log(f'List created in section [italic]{self.title}[/italic]', style = 'yellow')
                case 'b':
                    blockquoted_text = Prompt.ask('Enter blockquote content', default = 'Blockquoted text', show_default = False)
                    self.contents.append(blockquote(blockquoted_text))
                    console.log(f'Blockquote created in section [italic]{self.title}[/italic]', style = 'yellow')
                case 'c':
                    codeblock_text = Prompt.ask('Enter codeblock content', default = 'sudo rm -rf /*', show_default = False)
                    self.contents.append(codeblock(codeblock_text))
                    console.log(f'Codeblock created in section [italic]{self.title}[/italic]', style = 'yellow')
                case 'i':
                    img_link = Prompt.ask('[yellow]Paste image URL[/yellow]', default = 'https://i.kym-cdn.com/photos/images/original/001/688/970/a72.jpg', show_default = False)
                    img_width = IntPrompt.ask('[yellow]Enter image width[/yellow]', default = 200, show_default = False)
                    img_title = Prompt.ask('[yellow]Enter image title[/yellow]', default = 'Dogwifhat is goated', show_default = False)
                    self.contents.append(imagefmt(img_link, img_width, img_title))
                    console.log(f'Image created using {img_width}px width in section [italic]{self.title}[/italic]', style = 'yellow')
                case 'pb':
                    self.contents.append(pulsing_bar())
                    console.log(f'Pulsing bar separator created in section [italic]{self.title}[/italic]', style = 'yellow')
                        
                case 'h':
                    content_add_help()
                case 'q':
                    break
            parent.generate_content()
    
    def move_content(self):
        target = self.select_content('target')
        if target == None:
            console.print('Error: no content created', style = 'red')
            return None
        swap = self.select_content('swap')
        self.contents[target-1], self.contents[swap-1] = self.contents[swap-1], self.contents[target-1]
        console.log(f'Content index {target} swapped with index {swap}', style = 'yellow')
    
    def remove_content(self):
        target = self.select_content('rm')
        if target == None:
            console.print('Error: no content created', style = 'red')
            return None
        console.log(f'Content with index {target} removed from section instance [italic]{target.title}[/italic]', style = 'yellow')
        del self.contents[target]
    
    def generate_section_content(self):
        section_content = mdheader(self.title, 3)
        for content in self.contents:
            section_content += content + '\n\n'
        return section_content

class Header:
    def __init__(self):
        self.repo_name = self.get_repo_name()
        self.gh_username = None
        self.pypi_pckgname = None
        self.dotoc = self.assert_toc()
        self.dobadges = self.assert_badges()
        self.badges = None
        self.contents = []

    def get_repo_name(self) -> str:
        return Prompt.ask(prompt='Enter repo name', default = default_repo_name, show_default = False, console = console)
    
    def assert_toc(self) -> bool:        
        if Confirm.ask('Add a Table of Contents in header ?', default = True, show_default = False): return True
        else: return False
    
    def assert_badges(self) -> bool:
        if Confirm.ask('Add Shields.io badges in header ?', default = default_dobadges, show_default = False): 
            self.gh_username = Prompt.ask('Enter you GitHub username', default = default_gh_username, show_default = False)
            if Confirm.ask('Add PyPi package badges in header ?', default = default_dopybadges, show_default = False):
                self.pypi_pckgname = Prompt.ask('Enter PyPi package name', default = default_pypi_pckgname, show_default = False)
            return True
        else: return False
    
    def generate_header_content(self):
        header_content = mdheader(self.repo_name, 1) + '\n\n'
        self.contents.append(pulsing_bar())
        for content in self.contents:
            header_content += content + '\n\n'
        return header_content
    
class Footer:
    def __init__(self):
        self.contents = []
        self.rbg_link = None
        self.dorbg = self.assert_rbg()
        
    def assert_rbg(self) -> bool:        
        if Confirm.ask('Add a RepoBeats element in footer ?', default = True): 
            self.rbg_link = Prompt.ask('Enter RepoBeats Generator full md link output (https://repobeats.axiom.co/)', default = default_rbglink, show_default = False)
            if not self.rbg_link.endswith('"Repobeats analytics image")'):
                console.print('Not a valid RepoBeats API link, using default one')
            return True
        else: return False
        
    def generate_footer_content(self):
        footer_content = ''
        for content in self.contents:
            footer_content += content + '\n\n'
        return footer_content

# Generator class

class Readme:
    def __init__(self):
        self.header: Header = Header()
        self.footer: Footer = Footer()
        self.content: str = ''
        self.outfile: str = './OUTPUT.md'
        self.sections: list = []
        self.generate_content()
        
    def select_section(self, keyword: str):
        if self.sections == []:
            return None
        target = Prompt.ask(
            prompt = f'Enter {keyword} section title', 
            choices = [section.title for section in self.sections], 
            show_choices = True, 
            default = self.sections[-1].title,
            show_default = False,
            console = console
        )
        return [section for section in self.sections if section.title == target][0]
    
    def add_section(self):
        self.sections.append(Section(index = len(self.sections)))
        self.generate_content()
        console.log(f'Section [italic]{self.sections[-1].title}[/italic] created in readme instance', style = 'blue')
        
    def move_section(self):
        target = self.select_section('target')
        if target == None:
            console.print('Error: no section created', style = 'red')
            return None
        swap = self.select_section('swap')
        t_index, s_index = self.sections.index(target), self.sections.index(swap)
        self.sections[t_index], self.sections[s_index] = self.sections[s_index], self.sections[t_index]
        console.log(f'Section [italic]{target.title}[/italic] swapped with [italic]{swap.title}[/italic]', style = 'blue')
        self.generate_content()
        
    def remove_section(self):
        target = self.select_section('rm')
        if target == None:
            console.print('Error: no section created', style = 'red')
            return None
        self.sections = [section for section in self.sections if section != target]
        self.generate_content()
        console.log(f'Section [italic]{target.title}[/italic] removed from readme instance', style = 'blue')
        
    def edit_section(self):
        target = self.select_section('target')
        if target == None:
            console.print('Error: no section created ', style = 'red')
            return None
        while(True):
            cmd = Prompt.ask(
                prompt = section_edit_prompt(target.title), 
                choices = ['a', 'mv', 'rm', 'h', 'q'], 
                show_choices = True,
                console = console,
            )
            match cmd:
                case 'a':
                    target.add_content(self)
                case 'mv':
                    target.move_content()
                case 'rm':
                    target.remove_content()
                case 'h':
                    content_edit_help()
                case 'q':
                    break
            self.generate_content()
        
    def run(self):
        while(True):
            cmd = Prompt.ask(
                prompt = sections_management_prompt(), 
                choices = ['a', 'e', 'mv', 'rm', 'h', 'q'], 
                show_choices = True, 
                console = console
            )
            match cmd:
                case 'a':
                    self.add_section()
                case 'e':
                    self.edit_section()
                case 'mv':
                    self.move_section()
                case 'rm':
                    self.remove_section()
                case 'h':
                    sections_management_help()
                case 'q':
                    break
                
    def generate_content(self):
        self.header.contents = []
        if self.header.dobadges: self.header.contents.append(self.make_badges())
        if self.header.dotoc: self.header.contents.append(self.make_toc())
        self.content = self.header.generate_header_content()
        for section in self.sections:
            self.content += section.generate_section_content()
        if self.footer.dorbg: self.footer.contents = [pulsing_bar(), rbgmdlink(self.footer.rbg_link), signature]
        else: self.footer.contents = [pulsing_bar(), rbgmdlink(self.footer.rbg_link), signature]
        self.content += self.footer.generate_footer_content()
        
        with open(self.outfile, 'w') as f:
            f.write(self.content)
        
    def make_toc(self) -> str:
        toc = mdheader('Table of Contents', 3)
        for section in self.sections:
            toc += tocline(section.title)
        return toc
    
    def make_badges(self) -> str:
        badges = f'\n![GitHub License](https://img.shields.io/github/license/{self.header.gh_username}/{self.header.repo_name} "Github repo license")\n'
        badges += f'[![{self.header.gh_username} - GH profile](https://img.shields.io/static/v1?label={self.header.gh_username}&message=profile&color=blue&logo=github)](https://github.com/{self.header.gh_username} "Go to GitHub profile page")\n'
        if self.header.pypi_pckgname is not None:
            badges += f'![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{self.header.pypi_pckgname} "Supported Python version from PyPi package")\n'
            badges += f'[![PyPI - Version](https://img.shields.io/pypi/v/{self.header.pypi_pckgname})](https://pypi.org/project/{self.header.pypi_pckgname} "Pypi package version")\n'
            badges += f'[![PyPI - Downloads](https://img.shields.io/pypi/dm/{self.header.pypi_pckgname})](https://pypi.org/project/{self.header.pypi_pckgname} "Pypi package monthly downloads")\n'
        return center(badges)

generator = Readme()

if __name__ == '__main__':   
    generator.run()