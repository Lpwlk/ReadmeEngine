import os
import rich 
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.markdown import Markdown
from rich.table import Table
from rich.rule import Rule
console = Console(log_path = False)

'''
panel = Panel("txt", style="")
layout = Layout()
layout.split_row(panel)
console.print(layout)
'''

SAMPDIV = ['<samp>\n\n', '</samp>\n\n']
CENTERDIV = ['<p align="center">\n', '\n</p>']
PULSING_BAR = CENTERDIV[0] + '\t<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif">' + CENTERDIV[1]
REPOBEATS = CENTERDIV[0] + '\n![RepoBeats generator](https://repobeats.axiom.co/api/embed/a9dcf7a67c680871d7836e0dc87e7950c946c8b4.svg "Repobeats analytics image")\n' + CENTERDIV[1]

### Generator subclasses

class Header:
    def __init__(self):
        self.repo_name = self.get_repo_name()
        self.contents = []
       
    def get_repo_name(self) -> str:
        return Prompt.ask(prompt='Enter repo name', default=f'Repository name', show_default=False, console=console)
    
    def generate_header_content(self):
        header_content = '# ' + self.repo_name + '\n\n'
        for content in self.contents:
            header_content += content + '\n\n'
        return header_content
    
class Section:
    def __init__(self, index: int):
        self.index = index
        self.title = self.get_section_title()
        self.contents = []
        self.samp = True
    
    def get_section_title(self) -> str:
        return Prompt.ask(prompt='Enter section title', default=f'Section n°{self.index+1}', show_default=False, console=console)
    
    def generate_section_content(self):
        section_content = '### ' + self.title + '\n\n'
        for content in self.contents:
            section_content += content + '\n\n'
        if self.samp: section_content = SAMPDIV[0] + section_content + SAMPDIV[1]
        return section_content
        
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
        self.footer: Footer = Footer([PULSING_BAR, REPOBEATS])
        self.content: str = ''
        self.outfile: str = './OUTFILE.md'
        self.sections: list = []
        self.generate_content()
        self.run()
        
    def add_section(self):
        self.sections.append(Section(len(self.sections)))
        self.generate_content()

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
        console.log(f'Section {target.title} swapped with {swap.title}')
        self.generate_content()
        
    def remove_section(self):
        target = self.select_section()
        console.log(f'Section [italic]{target.title}[/italic] removed from readme instance')
        self.sections = [section for section in self.sections if section != target]
        self.generate_content()
        
    def edit_section(self):
        target = self.select_section()
        if target == None:
            console.print('Error: no section created ', style = 'red')
            return None
        console.log(f'Entering [italic]{target.title}[/italic] edit menu', style = 'bold blue')
        while(True):
            cmd = Prompt.ask(
                prompt = f'[italic]{target.title}[/italic] edit command', 
                choices = ['a', 'h', 'q'], 
                show_choices = True,
                console = console,
            )
            match cmd:
                    case 'a':
                        pass
                    case 'h':
                        self.section_edit_help()
                    case 'q':
                        console.log(f'Exiting session [italic]{target.title}[/italic] edit menu', style = 'bold blue')
                        break
        self.generate_content()
        
    def manage_sections(self):
        console.log('Entering sections management menu', style = 'bold yellow')
        while(True):
            
            if 0: 
                console.print('List of sections for debug')
                for section in self.sections: rich.inspect(section)
            
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
        self.content = self.header.generate_header_content()
        for section in self.sections:
            self.content += section.generate_section_content()
        self.content += self.footer.generate_footer_content()
        
        with open(self.outfile, 'w') as f:
            f.write(self.content)
        # console.print(f'README.md template generated - {self.outfile}', style = '')
    
    def select_section(self):
        if self.sections == []:
            return None
        target = Prompt.ask(
            prompt = "Enter section's title", 
            choices = [section.title for section in self.sections], 
            show_choices = True, 
            default = self.sections[-1].title,
            show_default = False,
            console = console
        )
        return [section for section in self.sections if section.title == target][0]

    def section_edit_help(self) -> None:
        help = Table(title=Rule("Section edit menu help utility", style = 'white'), title_justify = "left", border_style="white", min_width = 80)
        help.add_column("Command", style="yellow", header_style="bold yellow")
        help.add_column("Description", style="yellow", header_style="bold yellow")
        help.add_row("'cmd'", "Edit function")
        help.add_row("'cmd'", "Edit function")
        help.add_row("'cmd'", "Edit function")
        help.add_row("'cmd'", "Edit function")
        help.add_row("'q'", "Exit from edit to sections management menu")
        console.print(help)
        
    def sections_menu_help(self) -> None:
        help = Table(title=Rule("Sections management help utility", style = 'white'), border_style="white", min_width = 80)
        help.add_column("Command", style="yellow", header_style="bold yellow")
        help.add_column("Description", style="yellow", header_style="bold yellow")
        help.add_row("'a'",  "Add section")
        help.add_row("'mv'", "Move section")
        help.add_row("'rm'", "Remove section")
        help.add_row("'h'",  "Display section management menu help")
        help.add_row("'e'",  "Enter section edit menu")
        help.add_row("'q'",  "Exit from sections management to main menu")
        console.print(help)
        
    def main_menu_help(self) -> None:
        help = Table(title=Rule("Main menu help utility", style = 'white'), title_justify = "left", border_style="white", min_width = 80)
        help.add_column("Command", style="yellow", header_style="bold yellow")
        help.add_column("Description", style="yellow", header_style="bold yellow")
        help.add_row("'s'", "Open section management menu")
        help.add_row("'h'",  "Display main menu help")
        help.add_row("'q'",  "Exit readme generator instance")
        console.print(help)
        
generator = Readme()