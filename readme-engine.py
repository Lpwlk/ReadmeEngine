from rich.prompt import Prompt, IntPrompt, Confirm
from rich.console import Console
from rich.table import Table
from rich.rule import Rule
console = Console(log_path = False, highlight = False)

pulsingbar = '\t<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif?raw=true">'
repobeats = '<p align="center">\n\n![RepoBeats generator](https://repobeats.axiom.co/api/embed/a9dcf7a67c680871d7836e0dc87e7950c946c8b4.svg "Repobeats analytics image")\n'

def samp(content: str) -> str:
    return '<samp>\n\n' + content + '</samp>\n\n'

def center(content: str) -> str:
    return '<p align="center">\n' + content + '\n</p>'

def underline(content: str) -> str:
    return '<u>' + content + '</u>'

def details(content: str, summary: str) -> str:
    return f'<details>\n\n  <summary>\n\n  ##### {summary}*\n\n  </summary>\n\n{content}\n\n</details>'

def blockquote(content: str) -> str:
    return '> ' + content 

def codeblock(content: str) -> str:
    return '```\n' + content + '```'

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
            
### Generator subclasses
    
class Section:
    def __init__(self, template: str = None, index: int = 0):
        self.index = index
        self.title = self.get_section_title(template)
        self.contents = []
    
    def get_section_title(self, template) -> str:
        if template != None:
            return template
        
        return Prompt.ask(prompt='Enter section title', default=f'Section n°{self.index+1}', show_default=False, console=console)
    
    def select_content(self):
        if self.contents == []:
            return None
        target_index = IntPrompt.ask(
            prompt = 'Enter content index', 
            choices = [str(i+1) for i in range(len(self.contents))], 
            show_choices = True, 
            default = len(self.contents),
            show_default = False,
            console = console
        )
        return target_index
        
    def add_content(self, parent):
        console.log('Entering content creation menu', style = 'bold')
        while(True):
            ctype = Prompt.ask(
                prompt = 'Enter content type to add', 
                choices = ['p', 't', 'i', 'b', 'pb', 'h', 'q'], 
                show_choices = True, 
                default = len(self.contents)+1,
                show_default = False,
                console = console
            )
            match ctype:
                case 'p':
                    new_content = Prompt.ask('Enter paragraph content', default = 'Empty paragraph', show_default = False)
                    console.log(f'Paragraph created in section [italic]{self.title}[/italic]', style = 'bold')
                case 't':
                    table_title = Prompt.ask('Enter Table title', default = 'Table title', show_default = False)
                    table_width = IntPrompt.ask('Enter table width in column', default = 3, show_default = False)
                    table_height = IntPrompt.ask('Enter table height in rows', default = 2, show_default = False)
                    new_content = mdtable(table_title, table_width, table_height)
                    console.log(f'Table with size {table_width}x{table_height} created in section [italic]{self.title}[/italic]', style = 'bold')
                case 'i':
                    link = Prompt.ask('Paste image URL', default = 'https://i.kym-cdn.com/photos/images/original/001/688/970/a72.jpg', show_default = False)
                    img_width = IntPrompt.ask('Enter image width', default = 200, show_default = False)
                    img_title = Prompt.ask('Enter image title', default = 'Dogwifhat is goated', show_default = False)
                    new_content = imagefmt(link, img_width, img_title)
                    console.log(f'Image created using {img_width}px width in section [italic]{self.title}[/italic]', style = 'bold')
                case 'b':
                    blockquoted_text = Prompt.ask('Enter blockquote content', default = 'Blockquoted text', show_default = False)
                    new_content = blockquote(blockquoted_text)
                    console.log(f'Blockquote created in section [italic]{self.title}[/italic]', style = 'bold')
                case 'pb':
                    new_content = center(pulsingbar)
                    console.log(f'Pulsing bar separator created in section [italic]{self.title}[/italic]', style = 'bold')
                case 'h':
                    self.add_content_help()
                case 'q':
                    console.log('Exiting content creation menu', style = 'bold')
                    break
            self.contents.append(new_content)
            parent.generate_content()
    
    def move_content(self):
        console.log('Select target content index')
        target = self.select_content()
        if target == None:
            console.print('Error: no content created', style = 'red')
            return None
        console.log('Select swap content index')
        swap = self.select_content()
        self.contents[target-1], self.contents[swap-1] = self.contents[swap-1], self.contents[target-1]
        console.log(f'Content index {target} swapped with index {swap}', style = 'bold')
    
    def remove_content(self):
        target = self.select_content()
        console.log(f'Content with index {target} removed from section instance [italic]{target.title}[/italic]', style = 'bold')
        del self.contents[target]
    
    def generate_section_content(self):
        section_content = mdheader(self.title, 3)
        for content in self.contents:
            section_content += content + '\n\n'
        return section_content
    
    def add_content_help(self) -> None:
        help = Table(title=Rule('Section edit menu help utility', style = 'white'), title_justify = 'left', border_style='white', min_width = 80)
        help.add_column('Command', style='yellow', header_style='bold yellow')
        help.add_column('Description', style='yellow', header_style='bold yellow')
        help.add_row('cmd', 'Edit function')
        help.add_row('cmd', 'Edit function')
        help.add_row('cmd', 'Edit function')
        help.add_row('cmd', 'Edit function')
        help.add_row('q', 'Exit from edit to sections management menu')
        console.print(help)

class Header:
    def __init__(self):
        self.repo_name = self.get_repo_name()
        self.dotoc = self.assert_toc()
        self.contents = []

    def get_repo_name(self) -> str:
        return Prompt.ask(prompt='Enter repo name', default=f'Repository name', show_default=False, console=console)
    
    def assert_toc(self) -> str | None:        
        if Confirm.ask('Add Table of Content in header ?'): return True
        else: return False
    
    def generate_header_content(self):
        header_content = mdheader(self.repo_name, 1) + '\n\n'
        for content in self.contents:
            header_content += content + '\n\n'
        return header_content
    
class Footer:
    def __init__(self, contents):
        self.contents = contents
       
    def generate_footer_content(self):
        footer_content = ''
        for content in self.contents:
            footer_content += content + '\n\n'
        return footer_content

# Generator class

class Readme:
    def __init__(self):
        self.header: Header = Header()
        self.footer: Footer = Footer([center(pulsingbar), center(repobeats)])
        self.content: str = ''
        self.outfile: str = './OUTFILE.md'
        self.sections: list = []
        self.generate_content()
        
    def select_section(self):
        if self.sections == []:
            return None
        target = Prompt.ask(
            prompt = 'Enter section title', 
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
        console.log(f'Section [italic]{self.sections[-1].title}[/italic] created in readme instance', style = 'yellow')
        
    def move_section(self):
        console.log('Select target section')
        target = self.select_section()
        if target == None:
            console.print('Error: no section created', style = 'red')
            return None
        console.log('Select swap section')
        swap = self.select_section()
        t_index, s_index = self.sections.index(target), self.sections.index(swap)
        self.sections[t_index], self.sections[s_index] = self.sections[s_index], self.sections[t_index]
        console.log(f'Section [italic]{target.title}[/italic] swapped with [italic]{swap.title}[/italic]')
        self.generate_content()
        
    def remove_section(self):
        target = self.select_section()
        self.sections = [section for section in self.sections if section != target]
        self.generate_content()
        console.log(f'Section [italic]{target.title}[/italic] removed from readme instance')
        
    def edit_section(self):
        target = self.select_section()
        if target == None:
            console.print('Error: no section created ', style = 'red')
            return None
        console.log(f'Entering [italic]{target.title}[/italic] edit menu', style = 'bold blue')
        while(True):
            cmd = Prompt.ask(
                prompt = f'[italic]{target.title}[/italic] edit command', 
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
                    self.content_edit_help()
                case 'q':
                    console.log(f'Exiting [italic]{target.title}[/italic] edit menu', style = 'bold blue')
                    break
            self.generate_content()
        
    def manage_sections(self):
        console.log('Entering sections management menu', style = 'bold yellow')
        while(True):
            cmd = Prompt.ask(
                prompt = 'Section management command', 
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
                    self.sections_menu_help()
                case 'q':
                    console.log('Exiting sections management menu', style = 'bold yellow')
                    break
                
    def run(self):
        console.log('Entering readme generator main menu', style = 'bold green')
        while(True):
            cmd = Prompt.ask(
                prompt = 'Main command',
                choices = ['s', 'h', 'q'],
                show_choices = True,
                console = console,
            )
            match cmd:
                case 's':
                    self.manage_sections()
                case 'h':
                    self.main_menu_help()
                case 'q':
                    console.log('Closing readme generator instance', style = 'bold green')
                    break
                
    def generate_content(self):
        if self.header.dotoc: self.header.contents = [self.make_toc()]
        self.content = self.header.generate_header_content()
        for section in self.sections:
            self.content += section.generate_section_content()
        self.content += self.footer.generate_footer_content()
        
        with open(self.outfile, 'w') as f:
            f.write(self.content)
        # console.print(f'README.md template generated - {self.outfile}', style = ')
        
    def make_toc(self) -> str:
        toc = mdheader('Table of Contents', 3)
        for section in self.sections:
            toc += tocline(section.title)
        return toc
    
    def content_edit_help(self) -> None:
        help = Table(title=Rule('Section edit menu help utility', style = 'white'), title_justify = 'left', border_style='white', min_width = 80)
        help.add_column('Command', style='yellow', header_style='bold yellow')
        help.add_column('Description', style='yellow', header_style='bold yellow')
        help.add_row('cmd', 'Edit function')
        help.add_row('cmd', 'Edit function')
        help.add_row('cmd', 'Edit function')
        help.add_row('cmd', 'Edit function')
        help.add_row('q', 'Exit from edit to sections management menu')
        console.print(help)
        
    def sections_menu_help(self) -> None:
        help = Table(title=Rule('Sections management help utility', style = 'white'), border_style='white', min_width = 80)
        help.add_column('Command', style='yellow', header_style='bold yellow')
        help.add_column('Description', style='yellow', header_style='bold yellow')
        help.add_row('a',  'Add section')
        help.add_row('mv', 'Move section')
        help.add_row('rm', 'Remove section')
        help.add_row('h',  'Display section management menu help')
        help.add_row('e',  'Enter section edit menu')
        help.add_row('q',  'Exit from sections management to main menu')
        console.print(help)
        
    def main_menu_help(self) -> None:
        help = Table(title=Rule('Main menu help utility', style = 'white'), title_justify = 'left', border_style='white', min_width = 80)
        help.add_column('Command', style='yellow', header_style='bold yellow')
        help.add_column('Description', style='yellow', header_style='bold yellow')
        help.add_row('s', 'Open section management menu')
        help.add_row('h',  'Display main menu help')
        help.add_row('q',  'Exit readme generator instance')
        console.print(help)


generator = Readme()

generator.run()

# description = Section('Description')
# description.contents=['Description of the repo']
# generator.sections.append(description)
# generator.sections.append(Section('Install'))
# generator.sections.append(Section('Usage'))
# generator.sections.append(Section('Developement'))
# generator.sections.append(Section('References'))
# generator.sections.append(Section('Author'))
# generator.sections.append(Section('License'))
# generator.generate_content()