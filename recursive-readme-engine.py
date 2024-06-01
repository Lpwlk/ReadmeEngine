from rich.prompt import Prompt, IntPrompt, Confirm
from rich.console import Console
from rich.table import Table
from rich.rule import Rule
from rich import inspect
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

class Section:
    def __init__(self, title: str, content: str=None):
        self.title = title
        self.content = content if content else ""
        self.subsections = []

    def list_subsections(self):
        print(self.title)
        for subsection in self.subsections:
            subsection.list_subsections()
            
    def add_subsection(self, subsection):
        if isinstance(subsection, Section):
            self.subsections.append(subsection)

    def generate_markdown(self, level=1):
        markdown = f"{'#' * (1+level)} {self.title}\n\n"
        if self.content:
            markdown += f"{self.content}\n\n"
        for subsection in self.subsections:
            markdown += subsection.generate_markdown(level + 1)
        return markdown

class Document:
    def __init__(self, title):
        self.title = title
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    def generate_markdown(self):
        markdown = f"# {self.title}\n\n"
        for section in self.sections:
            markdown += section.generate_markdown(level=1)
        return markdown
    
    def list_sections(self):
        for section in self.sections:
            section.list_subsections()
                    
    def write_to_file(self, filename):
        content = self.generate_markdown()
        with open(filename, 'w') as f:
            f.write(content)



doc = Document("My Document")

intro = Section("Introduction", "This is the introduction.")
doc.add_section(intro)

ch1 = Section("Chapter 1")
ch1.add_subsection(Section("Section 1.1", "Content of section 1.1."))
ch12 = Section("Section 1.2")
ch12.add_subsection(Section("Subsection 1.2.1", "Content of subsection 1.2.1."))
ch12.add_subsection(Section("Subsection 1.2.2", "Content of subsection 1.2.2."))
ch1.add_subsection(ch12)
doc.add_section(ch1)

ch2 = Section("Chapter 2")
ch2.add_subsection(Section("Section 2.1", "Content of section 2.1."))
doc.add_section(ch2)

conclusion = Section("Conclusion", "This is the conclusion.")
doc.add_section(conclusion)

doc.list_sections()

doc.write_to_file("RECURSIVE.md")

