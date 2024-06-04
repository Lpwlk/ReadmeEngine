from rich.prompt import Prompt, IntPrompt, Confirm
from rich.console import Console
from rich.table import Table
from rich.rule import Rule

console = Console(highlight = False)

default_repo_name = 'RepoName'
default_dobadges = True
default_gh_username = 'Lpwlk'
default_dopybadges = True
default_pypi_pckgname = 'PackageName'
default_rbglink = '![Repobeats analytics svg](https://repobeats.axiom.co/api/embed/a9dcf7a67c680871d7836e0dc87e7950c946c8b4.svg "Repobeats analytics image")'

scolor = 'magenta'
secolor = 'blue'
sacolor = 'yellow'

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
    return '#' * level + ' ' + content + '\n\n'

def tocline(section_title: str):
    return f'- [{section_title}](#{section_title.replace(' ', '-')})  \n'

def rbgmdlink(mdlink: str) -> str:
    return center('\n<br>\n\n' + mdlink + '\n')

signature = center(samp('\n###### Mardown file generated using <a href ="https://github.com/Lpwlk/ReadmeEngine">readme-engine</a>\n'))

# CLI help utilities
    
def content_add_help() -> None:
    help = Table(title=Rule('Main menu help utility', style = 'white'), border_style=sacolor, min_width = 80)
    help.add_column('Command', style=sacolor, header_style='bold')
    help.add_column('Description', style=sacolor, header_style='bold')
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
    help = Table(title=Rule('Section edit menu help utility', style = 'white'), border_style=secolor, min_width = 80)
    help.add_column('Command', style=secolor, header_style='bold')
    help.add_column('Description', style=secolor, header_style='bold')
    help.add_row('a',  'Add content to section')
    help.add_row('rm', 'Remove content from section')
    help.add_row('mv', 'Swap contents in section')
    help.add_row('h',  'Display session edit menu help')
    help.add_row('q',  'Exit from session edit to session management menu')
    console.print(help)
    
def sections_management_help() -> None:
    help = Table(title=Rule('Sections management help utility', style = 'white'), border_style=scolor, min_width = 80)
    help.add_column('Command', style=scolor, header_style='bold')
    help.add_column('Description', style=scolor, header_style='bold')
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
        self.title = Prompt.ask(prompt=f'[{scolor}]Enter section title[/{scolor}]', default=f'Section {self.index+1}', show_default=False, console=console)
        self.contents = []
    
    def select_content(self, keyword: str):
        if self.contents == []:
            return None
        target_index = IntPrompt.ask(
            prompt = f'[{secolor}]Enter {keyword} index[/{secolor}]', 
            choices = [str(i+1) for i in range(len(self.contents))], 
            show_choices = True, 
            default = len(self.contents),
            show_default = True,
            console = console
        )
        return target_index
        
    def add_content(self, parent):
        while(True):
            try:
                print(len(self.contents)+1)
                ctype = Prompt.ask(
                    prompt = f'[{sacolor}][underline]{self.title}[/underline] add command[/{sacolor}]', 
                    choices = ['p', 't', 'l', 'b', 'c', 'i', 'pb', 'h', 'q'], 
                    show_choices = True, 
                    default = len(self.contents)+1,
                    show_default = True,
                    console = console
                )
                match ctype:
                    case 'p':
                        self.contents.append(Prompt.ask(f'[{sacolor}]Enter paragraph content[/{sacolor}]', default = 'Empty paragraph', show_default = False))
                        console.print(f'Paragraph created in section [italic]{self.title}[/italic]', style = sacolor)
                    case 't':
                        table_title = Prompt.ask(f'[{sacolor}]Enter Table title[/{sacolor}]', default = 'Table title', show_default = False)
                        table_width = IntPrompt.ask(f'[{sacolor}]Enter table width in column[/{sacolor}]', default = 3, show_default = False)
                        table_height = IntPrompt.ask(f'[{sacolor}]Enter table height in rows[/{sacolor}]', default = 2, show_default = False)
                        self.contents.append(mdtable(table_title, table_width, table_height))
                        console.print(f'Table with size {table_width}x{table_height} created in section [italic]{self.title}[/italic]', style = sacolor)
                    case 'l':
                        self.contents.append(mdlist())
                        console.print(f'List created in section [italic]{self.title}[/italic]', style = sacolor)
                    case 'b':
                        self.contents.append(blockquote())
                        console.print(f'Blockquote created in section [italic]{self.title}[/italic]', style = sacolor)
                    case 'c':
                        self.contents.append(codeblock())
                        console.print(f'Codeblock created in section [italic]{self.title}[/italic]', style = sacolor)
                    case 'i':
                        img_link = Prompt.ask(f'[{sacolor}]Paste image URL[/{sacolor}]', default = 'https://i.kym-cdn.com/photos/images/original/001/688/970/a72.jpg', show_default = False)
                        img_width = IntPrompt.ask(f'[{sacolor}]Enter image width[/{sacolor}]', default = 200, show_default = False)
                        img_title = Prompt.ask(f'[{sacolor}]Enter image title[/{sacolor}]', default = 'Dogwifhat is goated', show_default = False)
                        self.contents.append(imagefmt(img_link, img_width, img_title))
                        console.print(f'Image created using {img_width}px width in section [italic]{self.title}[/italic]', style = sacolor)
                    case 'pb':
                        if Confirm.ask(f'[{sacolor}]Add space after separator ?[/{sacolor}]', default = False, show_default = False):
                            self.contents.append(pulsing_bar()+'<br>\n')
                        else: 
                            self.contents.append(pulsing_bar())
                        console.print(f'Pulsing bar separator created in section [italic]{self.title}[/italic]', style = sacolor)
                        
                    case 'h':
                        content_add_help()
                    case 'q':
                        break
                parent.generate_content()
            except KeyboardInterrupt:
                print(''); console.print(f'Content add operation aborted (q exits to [underline]{self.title}[/underline] edit menu)', style = sacolor)

    def move_content(self):
        target = self.select_content('target')
        if target == None:
            console.print('Error: no content created', style = 'red')
            return None
        swap = self.select_content('swap')
        self.contents[target-1], self.contents[swap-1] = self.contents[swap-1], self.contents[target-1]
        console.print(f'Content index {target} swapped with index {swap}', style = secolor)
    
    def remove_content(self):
        target = self.select_content('rm')
        if target == None:
            console.print('Error: no content created', style = 'red')
            return None
        console.print(f'Content with index {target} removed from section instance [italic]{self.title}[/italic]', style = secolor)
        del self.contents[target-1]
    
    def change_title(self):
        old_title = self.title
        self.title = Prompt.ask(f'[{secolor}]Enter new section title to replace {self.title}[/{secolor}]')
        console.print(f'Section title changed from [underline]{old_title}[underline] to [underline]{self.title}[/underline]', style = secolor)
    
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
        return Prompt.ask(prompt='Enter [bold]GitHub repository name[/bold]', default = default_repo_name, show_default = False, console = console)
    
    def assert_toc(self) -> bool:        
        if Confirm.ask('Add [bold]Table of Contents[/bold] in header ?', default = True, show_default = False): return True
        else: return False
    
    def assert_badges(self) -> bool:
        if Confirm.ask('Add [bold]Shields.io badges[/bold] in header ?', default = default_dobadges, show_default = False):
            pybadges = Confirm.ask('Add [bold]pip-linked badges[/bold] in header ?', default = default_dopybadges, show_default = False)
            self.gh_username = Prompt.ask('> Enter [bold]GitHub username[/bold]', default = default_gh_username, show_default = False)
            if pybadges:
                self.pypi_pckgname = Prompt.ask('> Enter [bold]PyPi package name[/bold]', default = default_pypi_pckgname, show_default = False)
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
        if Confirm.ask('Add [bold]RepoBeats analytics[/bold] in footer ?', default = True, show_default=False): 
            self.rbg_link = Prompt.ask('> Enter [bold]RepoBeats md link[/bold] (https://repobeats.axiom.co/)', default = default_rbglink, show_default = False)
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
        # self.content: str = ''
        self.outfile: str = './OUTPUT.md'
        self.sections: list = []
        self.generate_content()
        
    def select_section(self, keyword: str):
        if self.sections == []:
            return None
        target = Prompt.ask(
            prompt = f'[{scolor}]Enter {keyword} section title[/{scolor}]', 
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
        console.print(f'Section [underline]{self.sections[-1].title}[/underline] created in readme instance', style = scolor)
        
    def move_sections(self):
        target = self.select_section('target')
        if target == None:
            console.print('Error: no section created', style = 'red')
            return None
        swap = self.select_section('swap')
        t_index, s_index = self.sections.index(target), self.sections.index(swap)
        self.sections[t_index], self.sections[s_index] = self.sections[s_index], self.sections[t_index]
        console.print(f'Section [underline]{target.title}[/underline] swapped with [italic]{swap.title}[/italic]', style = scolor)
        self.generate_content()
        
    def remove_section(self):
        target = self.select_section('rm')
        if target == None:
            console.print('Error: no section created', style = 'red')
            return None
        self.sections = [section for section in self.sections if section != target]
        self.generate_content()
        console.print(f'Section [underline]{target.title}[/underline] removed from readme instance', style = scolor)
        
    def edit_section(self):
        target = self.select_section('target')
        if target == None:
            console.print('Error: no section created ', style = 'red')
            return None
        while(True):
            try:
                cmd = Prompt.ask(
                    prompt = f'[{secolor}][underline]{target.title}[/underline] edit command[/{secolor}]', 
                    choices = ['a', 'mv', 'rn', 'rm', 'h', 'q'], 
                    show_choices = True,
                    console = console,
                )
                match cmd:
                    case 'a':
                        target.add_content(self)
                    case 'mv':
                        target.move_content()
                    case 'rn':
                        target.change_title()
                    case 'rm':
                        target.remove_content()
                    case 'h':
                        content_edit_help()
                    case 'q':
                        break
                self.generate_content()
            except KeyboardInterrupt:
                print(''); console.print('Section edit operation aborted (q exits to sections manager menu)', style = 'red')

        
    def run(self):
        while(True):
            try:
                cmd = Prompt.ask(
                    prompt = f'[{scolor}]Sections management command[/{scolor}]', 
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
                        self.move_sections()
                    case 'rm':
                        self.remove_section()
                    case 'h':
                        sections_management_help()
                    case 'q':
                        console.print(f'Output file has been successfuly generated: {self.outfile}', style = 'green')
                        break
            except KeyboardInterrupt:
                print(''); console.print('Sections management operation aborted (q to exit program)', style = 'red')

    def generate_content(self):
        
        self.header.contents = []
        if self.header.dobadges: 
            self.header.contents.append(self.make_badges())
        if self.header.dotoc: 
            self.header.contents.append(self.make_toc())
        self.content = self.header.generate_header_content()
        
        for section in self.sections:
            self.content += section.generate_section_content()
        
        if self.footer.dorbg: 
            self.footer.contents = [pulsing_bar(), rbgmdlink(self.footer.rbg_link), signature]
        else: 
            self.footer.contents = [pulsing_bar(), signature]
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