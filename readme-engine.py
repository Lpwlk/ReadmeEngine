#!/usr/bin/env python

# Base imports
from rich.console import Console
from rich.theme import Theme
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.table import Table
from rich.box import ROUNDED
from rich.rule import Rule
from rich import inspect
# Debug imports
from rich.traceback import install

# Customizable styles - ReadmeEngine code semantic improvement concerning cli ouput generation
interactive_run_theme = Theme(
    inherit = False,
    styles = {
    'prompt.choices': 'italic blue',
    'prompt.default': 'blink bold yellow',
    'stitle': 'italic blue',
    'escape': 'red',
    'default': '',
    }
)
section_edit_theme = Theme(
    inherit = False,
    styles = {
    'prompt.choices': 'italic green',
    'prompt.default': 'blink bold yellow',
    'stitle': 'italic blue',
    'escape': 'orange1',
    'default': '',
    }
)
content_creation_theme = Theme(
    inherit = False,
    styles = {
    'prompt.choices': 'italic yellow',
    'prompt.default': 'blink bold yellow',
    'default': '',
    'stitle': 'italic blue',
    'escape': 'yellow',
    }
)

# Overriding base styles - Adjusting default rich theme styles for complete control over cli interface aspect & custom styles switch

base_theme = Theme(
    styles = {
    # default overrides
    'repr.number': 'bold not italic green',
    # custom themes
    'escape': 'default',
    'stitle': 'italic blue',
    }
)

console = Console(
    theme = base_theme,
    record = True,
    width = 120,
)

console.print('''
  ┌───────────────────────────────────────────────────────────────────────────
  │   ______               _                _____            _            
  │   | ___ \\             | |              |  ___|          (_)           
  │   | |_/ /___  __ _  __| |_ __ ___   ___| |__ _ __   __ _ _ _ __   ___ 
  │   |    // _ \/ _` |/ _` | '_ ` _ \ / _ |  __| '_ \ / _` | | '_ \ / _ \\
  │   | |\\ |  __| (_| | (_| | | | | | |  __| |__| | | | (_| | | | | |  __/
  │   \\_| \_\___|\__,_|\__,_|_| |_| |_|\___\____|_| |_|\__, |_|_| |_|\___|
  │                                                     __/ |             
  │                                                    |___/              
  │                                                                                                                         
  │ Open-source software, initially designed for personnal use in the GitHub
  │ profile Lpwlk (https://github.com/Lpwlk) repositories.
                                                        ''', style = 'blue', highlight = False)


def dbgGenSvg(inp, cl: bool = False, outfile: str | None = None):
    '''dbgGenSvg Debug functionnality for svg user input generation.

    Args:
        inp (_type_): input value from user
        cl (bool, optional): Clear flag for the previous command line. Defaults to False.
        
    Note: Desired behaviour would depend on the clear flag value.
    > cl = False: ghost print of input after prompt and go to next line
    > cl = True:  ghost print of input after prompt, clears prompt and go to next line
    '''
    if outfile is None: outfile = 'cli_outputs/output.svg'
    console.print(inp)
    print('\033[A\033[K', end = '')
    if cl:
        print('\033[A\033[K', end = '')
    console.save_svg(outfile, clear =  False)

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

def switch_context_theme(context = dict):
    for key, val in context.styles.items():
        if key in base_theme.styles.keys():
            base_theme.styles[key] = val
            
# Markdown rendering

def pulsing_bar() -> str:
    return center('\t<img src="https://github.com/Lpwlk/Lpwlk/blob/main/assets/pulsing-bar.gif?raw=true">&nbsp;', html = True)

def samp(content: str) -> str:
    return '\n<samp>\n' + content + '\n</samp>\n'

def center(content: str, html: bool = False) -> str:
    if not html: content = '\n' + content + '\n'
    return '\n<div align="center">\n' + content + '\n</div>\n\n'

def underline(content: str) -> str:
    return '<u>' + content + '</u>'

def italic(content: str) -> str:
    return '<i>' + content + '</i>'

def details(console: Console = Console()) -> str:
    summary = Prompt.ask('Enter foldable section header text', default = 'Foldable section', show_default = False, console = console)
    default_open = Confirm.ask('Enter yes for default open', default = False)
    detail_content = []
    try:
        while True:
            cmd = Prompt.ask(
                prompt=f'Detail content creation command', 
                choices = ['p', 't', 'd', 'l', 'b', 'c', 'i', 'pb'], 
                show_choices = True, 
                console = console
            )
            dbgGenSvg(cmd, cl = True)
            match cmd:
                case 'p':
                    new_content = mdparagraph()
                    console.print(f'Paragraph created in detail content')
                case 't':
                    table_title = Prompt.ask(f'Enter Table title', default = 'Table title', show_default = False, console = console)
                    dbgGenSvg(table_title, cl = True)
                    table_width = IntPrompt.ask(f'Enter table width in column', default = 3, show_default = False, console = console)
                    dbgGenSvg(table_width, cl = True)
                    table_height = IntPrompt.ask(f'Enter table height in rows', default = 2, show_default = False, console = console)
                    dbgGenSvg(table_height, cl = True)
                    new_content = mdtable(table_title, table_width, table_height)
                    console.print(f'Table with size {table_width}x{table_height} created in detail content')
                case 'l':
                    new_content = mdlist()
                    console.print(f'List created in detail content')
                case 'd':
                    new_content = details()
                    console.print(f'Detail item created in detail content')
                case 'b':
                    new_content = blockquote()
                    console.print(f'Blockquote created in detail content')
                case 'c':
                    new_content = codeblock()
                    console.print(f'Codeblock created in detail content')
                case 'i':
                    img_link = Prompt.ask(f'Paste image URL', default = 'https://i.kym-cdn.com/photos/images/original/001/688/970/a72.jpg', show_default = False, console = console)
                    dbgGenSvg(img_link, cl = True)
                    img_width = IntPrompt.ask(f'Enter image width', default = 200, show_default = False, console = console)
                    dbgGenSvg(img_width, cl = True)
                    img_title = Prompt.ask(f'Enter image title', default = 'Dogwifhat is goated', show_default = False, console = console)
                    dbgGenSvg(img_title, cl = True)
                    new_content = imagefmt(img_link, img_width, img_title)
                    console.print(f'Image created using {img_width}px width in detail content')
                case 'pb':
                    new_content = pulsing_bar()
                    console.print(f'Pulsing bar separator created in detail content')
            detail_content.append(f'  {new_content}')
    except KeyboardInterrupt:
        print('')
        
    content = f'<details{default_open*' open=true'}>\n\n  <summary>\n\n ##### {summary}\n\n  </summary>\n\n'
    for item in detail_content: content += f'{item}\n\n'
    return content + '</details>'

def mdparagraph():
    text = Prompt.ask(f'Enter paragraph content', default = 'Empty paragraph', show_default = False, console = console)
    dbgGenSvg(text, cl = False)
    return text

def blockquote() -> str:
    content = '\n'
    try:
        while True:
            bq_item = Prompt.ask('Enter new blockquote line (Ctrl+C to end blockquote)', default = 'Fast, good, cheap: pick any two.', show_default = False, console = console)
            dbgGenSvg(bq_item, cl = True)
            content += '> ' + bq_item+ '\n> \n'
    except KeyboardInterrupt:
        print('')
        return content[:-3]

def codeblock(content: str = None) -> str:
    if content:
        return '```' + content + '```'
    else:
        content = '\n'
        try:
            while True:
                cb_item = Prompt.ask('Enter new codeblock line (Ctrl+C to end codeblock)', default = 'sudo rm -rf /*', show_default = False, console = console)
                dbgGenSvg(cb_item, cl = True)
                content += cb_item + '\n'
        except KeyboardInterrupt:
            print('')
            content = '```' + content + '```'
            return content
    
def mdlist(type: str | None = None, content: list[str] | None = None) -> str:
    list, list_index = '', 0
    list_head = '\n- '
    if not type:
        list_type = Prompt.ask('Enter u/o/t for un/ordered/tickable list (Ctrl+C to end list)', choices = ['u', 'o', 't'], default = 'u', show_default = False, console = console)
        dbgGenSvg(list_type, cl = False)
    if list_type == 't':
        list_head += '[ ] '
    if not content:
        try:
            while True:
                list_index += 1
                if list_type == 'o': list_head = f'\n{list_index}. '
                list_item = Prompt.ask(f'Enter list item n°{list_index} (Ctrl+C to end list)', default = f'List item n°{list_index}', show_default = False, console = console)
                dbgGenSvg(list_item, cl = True)
                list += list_head + list_item
        except KeyboardInterrupt:
            print('')
    else:
        for list_item in content:
            if list_type == 'o': list_head = f'\n{content.index(list_item)}. '
            list += list_head + list_item
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
    if level > 3: content = '\u27A4 ' + content
    return ' '.join(['#'*(level-1), '&nbsp;&nbsp;'*(level-2), content]) + '\n\n'

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
    help.add_row('mv', 	'Move selected section to targeted parent section')
    help.add_row('sw',  'Swap selected sections if they share the same parent')
    help.add_row('rm',  'Remove selected target section (default to last section created)')
    help.add_row('tree','Prints root tree section structure')
    help.add_row('list','Prints sections list under root')
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
	help.add_row('rn', 	'Update section title (default to section index)')
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
    help.add_row('p', 	'Create paragraph')
    help.add_row('t', 	'Create custom shape table')
    help.add_row('d',   'Create a foldable section with new elements until KeyboardInterrupt')
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
        self.title = self.init_title(title)
        self.subsections = []
        self.content = self.format_content(content)
    
    def init_title(self, title: str | None):
        if not title:
            title = Prompt.ask(prompt=f'Enter section title', default=self.default_title, show_default=True, console=console)
            dbgGenSvg(title)
        return title
    
    def format_content(self, content) -> list[str] | str | None:
        if isinstance(content, list):
            return content
        elif isinstance(content, str):
            return [content]
        elif content == None:
            return []
        else: 
            console.print(f'Error: Wrong content type for section init ({type(content)}), content list cleared', style = 'red')
            return []

    def add_section(self, subsection, verbose: bool = True):
        if isinstance(subsection, Section):
            self.subsections.append(subsection)
            if verbose: console.print(f'Section [stitle]{subsection.title}[/stitle] created in [stitle]{self.title}[/stitle]')
        else:
            console.print('Error: Sections.add_section method argument must be a Section object', style = 'red')
        
        
    def list_subsections(self, recursive_slist: list | None = None, prefix: str = '', increment: str = '  ', print: bool = False):
        if recursive_slist is None: recursive_slist = []
        if print:
            recursive_slist.append((self, prefix))
            for subsection in self.subsections:
                subsection.list_subsections(recursive_slist, increment + prefix, print = True)
        else:
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
        
        
    def add_content(self, content: str | None = None, index: int | None = None):
        if index is None: index = len(self.content)
        if content:
            self.content.insert(index, content)
        else:
            cmd = Prompt.ask(
                prompt=f'Section [stitle]{self.title}[/stitle] content creation command', 
                choices = ['p', 't', 'd', 'l', 'b', 'c', 'i', 'pb', 'h', 'q'], 
                show_choices = True, 
                console = console
            )
            dbgGenSvg(cmd)
            match cmd:
                case 'p':
                    self.content.insert(index, mdparagraph())
                    console.print(f'Paragraph created in section [stitle]{self.title}[/stitle]')
                case 't':
                    table_title = Prompt.ask(f'Enter Table title', default = 'Table title', show_default = False, console = console)
                    dbgGenSvg(table_title, cl = True)
                    table_width = IntPrompt.ask(f'Enter table width in column', default = 3, show_default = False, console = console)
                    dbgGenSvg(table_width, cl = True)
                    table_height = IntPrompt.ask(f'Enter table height in rows', default = 2, show_default = False, console = console)
                    dbgGenSvg(table_height, cl = True)
                    self.content.insert(index, mdtable(table_title, table_width, table_height))
                    console.print(f'Table with size {table_width}x{table_height} created in section [stitle]{self.title}[/stitle]')
                case 'l':
                    self.content.insert(index, mdlist())
                    console.print(f'List created in section [stitle]{self.title}[/stitle]')
                case 'd':
                    self.content.insert(index, details(console = console))
                    console.print(f'Detail item created in section [stitle]{self.title}[/stitle]')
                case 'b':
                    self.content.insert(index, blockquote())
                    console.print(f'Blockquote created in section [stitle]{self.title}[/stitle]')
                case 'c':
                    self.content.insert(index, codeblock())
                    console.print(f'Codeblock created in section [stitle]{self.title}[/stitle]')
                case 'i':
                    img_link = Prompt.ask(f'Paste image URL', default = 'https://i.kym-cdn.com/photos/images/original/001/688/970/a72.jpg', show_default = False, console = console)
                    dbgGenSvg(img_link, cl = True)
                    img_width = IntPrompt.ask(f'Enter image width', default = 200, show_default = False, console = console)
                    dbgGenSvg(img_width, cl = True)
                    img_title = Prompt.ask(f'Enter image title', default = 'Dogwifhat is goated', show_default = False, console = console)
                    dbgGenSvg(img_title, cl = True)
                    self.content.insert(index, imagefmt(img_link, img_width, img_title))
                    console.print(f'Image created using {img_width}px width in section [stitle]{self.title}[/stitle]')
                case 'pb':
                    self.content.insert(index, pulsing_bar())
                    console.print(f'Pulsing bar separator created in section [stitle]{self.title}[/stitle]')
                case 'h':
                    content_creation_mode_help()
                case 'q':
                    console.print(f'Exiting [stitle]{self.title}[/stitle] content creation operation', style = 'escape')
                    switch_context_theme(section_edit_theme)
                    return True
                
            
    def move_content(self):
        target = self.select_content('Select first target content index to swap', len(self.content))
        if target == None:
            console.print('Error: no content created', style = 'red')
            return None
        swap = self.select_content('Select second target content index to swap', len(self.content) - 1)
        self.content[target-1], self.content[swap-1] = self.content[swap-1], self.content[target-1]
        console.print(f'Content index {target} swapped with index {swap}')


    def remove_content(self, content_index: int | None = None):
        if content_index: target = content_index
        else: target = self.select_content('Select target content index to be removed', len(self.content))
        if target == None:
            console.print('Error: no content created', style = 'red')
            return None
        del self.content[target-1]
        console.print(f'Content [stitle]n°{target}[/stitle] removed from section instance [stitle]{self.title}[/stitle]')
        
        
    def select_content(self, prompt_text: str, default_index: int = 0):
        if self.content == []:
            return None
        target_index = IntPrompt.ask(
            prompt= prompt_text, 
            choices = [str(i+1) for i in range(len(self.content))], show_choices = True, 
            default = default_index, show_default = True,
            console = console
        )
        dbgGenSvg(target_index, cl = False)
        return target_index
    
    
    def update_content(self, content_index: int | None = None):
        if content_index: target = content_index
        else: target = self.select_content('Select target content index to be updated', len(self.content))
        if target == None:
            console.print('Error: no content created', style = 'red')
            return None
        del self.content[target-1]
        try:
            self.add_content(index = target-1)
            console.print(f'Content with index {target} has been updated in section {self.title}')
        except KeyboardInterrupt:
            console.print('\n[underline bold]KeyboardInterrupt[/underline bold] > Content update operation aborted', style = 'escape')
    
    
    def update_title(self):
        old_title = self.title
        self.title = Prompt.ask(
            prompt = f'Enter new section title', 
            default = self.default_title, show_default = True, 
            console = console
        )
        dbgGenSvg(self.title, cl = False)
        console.print(f'Section title [stitle]{old_title}[/stitle] changed to [stitle]{self.title}[/stitle]')

################################################################################################################################################################

class Markdown:
    def __init__(self, filename: str | None = None):
        '''Markdown generator object - Can be used in interactive mode using the run method as well as using methods directly inside a script.

        Args:
            filename (str | None, optional): Filename to be used to generate markdown output. Defaults to None.
        '''
        self.filename = filename if filename else 'MARKDOWN'
        self.root = Section(title = 'root')
        self.toc = True
        self.header = self.generate_header()
        self.footer = self.generate_footer()
            
            
    def write_markdown(self, filename: str | None = None, verbose: bool = False) -> None:
        if not filename: filename = self.filename
        if self.toc: self.update_toc()
        content = self.header + self.root.recursive_generation(level = 1) + self.footer
        with open(f'{filename}.md', 'w') as f:
            f.write(content)
        if verbose: console.print(Rule(f'Templated generated @ {self.filename}.md', style = 'green'))
            
    def tree_sections(self, section: Section = None, prefix: str = '', is_last: bool = True, index: bool = True, branchsize: int = 1):
        if section == None:
            section = self.root
            console.print(Rule(f'Current [stitle]{section.title}[/stitle]\'s subsections tree'), width = 70)
        if index:
            index = f"{self.get_section_index(section, new=False)[:-1]} "
        else:
            index = ''
        if section.title is self.root.title: 
            nprefix = index = ''
        elif is_last:
            nprefix = f'└{'─' * branchsize} '
        else:
            nprefix = f'├{'─' * branchsize} '
        console.print(prefix, nprefix, f'{index}{section.title}', sep = '')
        if not is_last:
            prefix += f'│{' ' * (branchsize + 1)}'
        else:
            prefix += ' ' * branchsize
        for i, child in enumerate(section.subsections):
            is_last = (i == len(section.subsections)-1)
            self.tree_sections(child, prefix, is_last)
            
        
    def list_sections(self, section: Section = None, index: bool = True, prefix: str = '→ ', increment: str = '  '):
        if section == None:
            section = self.root
        console.print(Rule(f'Current [stitle]{section.title}[/stitle]\'s subsections list'), width = 70)
        for subsection, prefix in section.list_subsections(prefix = prefix, increment = increment, print = True):
            if index: sindex = self.get_section_index(subsection, new = False)[:-1] + ' '
            console.print(f'{prefix}{sindex}{subsection.title}')
            
            
    def get_parent(self, target: Section, root: Section = None):
        if root == None: root = self.root
        for child in root.subsections:
            if child == target:
                return root
            parent = self.get_parent(target, child)
            if parent is not None:
                return parent
        return None
        
        
    def get_section_index(self, target: Section, index: str = None, new: bool = True) -> str:
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
            
            
    def select_section(self, prompt_text: str, root_include: bool = True, default_index: int = 0) -> Section | None:
        sections_list = [section for section in self.root.list_subsections()]
        if root_include is False:
            del sections_list[0]
        if len(sections_list) >= 1:
            target = Prompt.ask(
                prompt = f'[scolor]{prompt_text}[/scolor]', 
                choices = [section.title.lower() for section in sections_list], show_choices = True, 
                default = sections_list[default_index].title.lower(), show_default = True,
                console = console
            )
            dbgGenSvg(target, cl = False)
            for section in sections_list:
                if section.title.lower() == target.lower(): return section
        else: return None
            
            
    def add_section(self, section: Section | None = None, target: Section | None = None) -> None:
        if section is None:
            if target is None:
                target = self.select_section('Select parent session title')
            target.add_section(Section(default_title = self.get_section_index(target)))
        else:
            self.root.add_section(section)
            
            
    def move_sections(self, target: Section | None = None, new_parent: Section | None = None):
        target = self.select_section('Select target section to be moved', root_include = False)
        parent = self.get_parent(target)
        parent.subsections.remove(target)
        if new_parent is None:
            new_parent = self.select_section('Select new parent section', default_index = 0)
        new_parent.subsections.append(target)
        console.print(f'Section {target.title} moved into {new_parent.title}')
            

    def swap_sections(self, target: Section | None = None, swap_target: Section | None = None):
        target = self.select_section('Select first section to be swapped', root_include = False)
        swap_target = self.select_section('Select first section to be swapped', root_include = False)
        target_parent = self.get_parent(target)
        swap_parent = self.get_parent(swap_target)
        if target_parent == swap_parent:
            target_index = target_parent.subsections.index(target)
            swap_index = target_parent.subsections.index(swap_target)
            target_parent.subsections[target_index], target_parent.subsections[swap_index] = target_parent.subsections[swap_index], target_parent.subsections[target_index]
            console.print(f'Section [stitle]{target.title}[/stitle] swapped with section [stitle]{swap_target.title}[/stitle]')
        else:
            console.print('Error, selected targets are not in the same parent section', style = 'red')
            

    def remove_section(self, target: Section = None):
        if target is None:
            target = self.select_section('Select section to be removed', root_include = False)
        if target is not None:
            target_parent = self.get_parent(target)
            target_parent.subsections.remove(target)
            console.print(f'Section [stitle]{target.title}[/stitle] removed from [stitle]{target_parent.title}[/stitle]')
        else:
            console.print(f'Error: No sections created under root section [stitle]{self.root.title}[/stitle]', style = 'red')
    
    # Header methods 
    
    def generate_header(self) -> None:
        if False:
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

    def update_toc(self) -> None:
        toc = self.recursive_tocline(self.root)
        for index, content in enumerate(self.root.content):
            if 'Table of Contents' in content:
                self.root.content[index] = toc

    def recursive_tocline(self, child: Section, toc: str = '## Table of Contents\n\n', level = 0) -> str:
        for section in child.subsections:
            toc += f'{'&nbsp;&nbsp;&nbsp;'*level}{self.get_section_index(section, new = False)[:-1]} - [{section.title}](#{section.title.replace(' ', '-')})  \n'
            toc = self.recursive_tocline(section, toc, level + 1)
        return toc
    
    # Footer methods
    
    def generate_footer(self) -> bool:
        default_rbglink = '![Alt](https://repobeats.axiom.co/api/embed/99c19ed191ab42775bc9297d8af467ccc608f2e7.svg "Repobeats analytics image")'
        if False:
            return f'\n{pulsing_bar()}\n{rbgmdlink(default_rbglink)}\n{signature}'
        else:
            if Confirm.ask('Add [bold]RepoBeats analytics[/bold] in footer ?', default = True, show_default=False):
                rbglink = Prompt.ask('> Enter [bold]RepoBeats md link[/bold] (https://repobeats.axiom.co/)', default = default_rbglink, show_default = False, console = console)
                if not rbglink.endswith('"Repobeats analytics image")'):
                    console.print('Not a valid RepoBeats API link, using default one')
                return f'\n{pulsing_bar()}\n{rbgmdlink(rbglink)}\n{signature}'
            else:
                return f'\n{pulsing_bar()}\n{signature}'

  
    def generate_template(self, template: str | None = None) -> None:
        sdict = {
            'desc': Section('Description', ['Repository project description including project typical usecase, available features and links to any reference visitors might be unfamiliar with.']),
            'inst': Section('Installation', ['Installation guide for each tool included in the repository.']),
            'uses': Section('Usage', ['Details about different usecases of the repository tools using text, image(s) and/or gif(s).', imagefmt('https://i.kym-cdn.com/photos/images/original/001/688/970/a72.jpg', 200, 'Dogwifhat is goated')]),
            'exam': Section('Examples', ['Examples of executions & results for the previous described usecases.']),
            'rdmp': Section('Roadmap', ['Developement goals as well as current planned or achieved milestones list']),
            'lcns': Section('License', ['For open source projects, say how it is licensed.']),
            'auth': Section('Authors', ['The repo has been created by [Author] and maintained by [Author]. Feel free to contact [Author] via email or creating a GitHub issue for any repo-related support request.']),
        }
        sdict['inst'].add_section(Section('Prerequisites', ['Required software (Python version, specific dependencies).']), verbose=False)
        sdict['inst'].add_section(Section('Instructions', ['Detailed steps to install the project on any machine.']), verbose=False)
        sdict['uses'].add_section(Section('Basic Usage', ['Basic usage examples.']), verbose=False)
        sdict['uses'].add_section(Section('Configuration', ['Configuration options.']), verbose=False)
        sdict['uses'].add_section(Section('Command-Line Interface', ['How to use the CLI (if applicable).']), verbose=False)
        sdict['rdmp'].add_section(Section('Milestones', [center(mdtable('Past & future patches', 2, 6))]), verbose=False)
        sdict['exam'].add_section(Section('Mode 1', ['How to execute the example scripts in mode 1']), verbose=False)
        sdict['exam'].add_section(Section('Mode 2', ['How to execute the example scripts in mode 2']), verbose=False)
        
        if template: cmd = template
        else:
            cmd = Prompt.ask(
                prompt = f'Enter template type to call for {self.root.title}',
                choices = ['d', 'm'], show_choices = True,
                default = 'd', show_default = False,
                console = console
            )
            dbgGenSvg(cmd, cl = False)
        match cmd:
            case 'd':
                template_name = 'Default'
                self.root.subsections = [sdict[key] for key in ['desc', 'inst', 'uses', 'exam', 'rdmp', 'lcns', 'auth']]
            case 'm':
                template_name = 'Minimal'
                self.root.subsections = [sdict[key] for key in ['desc', 'inst', 'uses', 'lcns']]
        console.print(f'{template_name} template generated: overriding current root sections for the following structure ...')
        self.tree_sections()
        
        
    def edit_section(self) -> None:
        target = self.select_section('Select target session to edit', default_index = -1)
        switch_context_theme(section_edit_theme)
        try:
            while(True):
                cmd = Prompt.ask(
                    prompt = f'Section [stitle]{target.title}[/stitle] edit command', 
                    choices = ['a', 'mv', 'rm', 'rn', 'up', 'tree', 'list', 'i', 'h', 'q'], 
                    show_choices = True,
                    console = console,
                )
                dbgGenSvg(cmd, cl = False)
                match cmd:
                    case 'a':
                        try:
                            switch_context_theme(content_creation_theme)
                            while True:
                                if target.add_content():
                                    break
                                else:
                                    self.write_markdown(verbose = False)
                        except KeyboardInterrupt:
                            console.print('\n[underline bold]KeyboardInterrupt[/underline bold] > Content creation operation aborted', style = 'escape')
                            switch_context_theme(section_edit_theme)
    
                    case 'mv':
                        target.move_content()
                    case 'rm':
                        target.remove_content()
                    case 'rn':
                        target.update_title()
                    case 'up':
                        target.update_content()
                    case 'tree':
                        console.print(Rule(f'Current [stitle]{target.title}[/stitle]\'s subsections tree'), width = 70)
                        self.tree_sections(target)
                    case 'list':
                        self.list_sections(target)
                    case 'i':
                        inspect(target, methods = True, console = console)
                    case 'h':
                        section_edit_mode_help()
                    case 'q':
                        console.print(f'Exiting [stitle]{target.title}[/stitle] edit operation', style = 'escape')
                        switch_context_theme(interactive_run_theme)
                        break
                self.write_markdown(verbose = False)
        except KeyboardInterrupt:
            console.print('\n[underline bold]KeyboardInterrupt[/underline bold] > Section edit operation aborted', style = 'escape')
            switch_context_theme(interactive_run_theme)
            
            
    def run(self):
        self.write_markdown(verbose = False)
        while True:
            switch_context_theme(interactive_run_theme)
            try:
                cmd = Prompt.ask(
                    prompt = f'[scolor]Sections management command[/scolor]', 
                    choices = ['a', 'e', 'mv', 'sw', 'rm', 'tree', 'list', 'temp', 'i', 'h', 'q'], 
                    show_choices = True, 
                    console = console
                )
                dbgGenSvg(cmd, cl = False)
                match cmd:
                    case 'a':
                        self.add_section()
                    case 'mv':
                        self.move_sections()
                    case 'sw':
                        self.swap_sections()
                    case 'rm':
                        self.remove_section()
                    case 'e':
                        self.edit_section()
                    case 'tree':
                        self.tree_sections()
                    case 'list':
                        self.list_sections()
                    case 'temp':
                        self.generate_template()
                    case 'i':
                        inspect(self, methods = True, console = console)
                        dbgGenSvg(inp = '')
                    case 'h':
                        interactive_run_mode_help()
                    case 'q':
                        console.print(f'Exiting interactive {self.filename} generation')
                        self.write_markdown(self.filename, verbose = True)
                        break
                self.write_markdown(self.filename)
            except KeyboardInterrupt:
                console.print(f'\n[underline bold]KeyboardInterrupt[/underline bold] > Interactive run operation aborted', style = 'escape')
################################################################################################################################################################

if __name__ == '__main__':    
    install(show_locals = True, width = 120)
    debug = True
    # display_theme(interactive_run_theme)
    # display_theme(section_edit_theme)
    # display_theme(content_creation_theme)
    
#     console.print(Rule('Templated README.md generation test', style = 'bold green'))
#     md = Markdown('tests/'+outfile)
#     md.add_section(Section('Introduction', 'This is the introduction.'))
#     s1 = Section('Chapter 1')
#     md.add_section(s1)
#     s2 = Section('Chapter 2')
#     md.add_section(s2)
#     md.add_section(Section('Conclusion', 'This is the conclusion.'))
#     s11 = Section('Chapter 1.1', 'Content of chapter 1.1.')
#     s11.add_section(Section('Chapter 1.1.1', 'Content of chapter 1.1.1.'))
#     s11.add_section(Section('Chapter 1.1.2', ['Here is a sample of code that can be used to generate custom templates without editing the source code.', 'You may add content in sections instances as second argument in list or using the add_content method and built-in markdown parsers.']))
#     s1.add_section(s11)
#     s1.add_section(Section('Chapter 1.2', 'Content of chapter 1.2.'))
#     s11.add_content(codeblock(
# '''
# md = Markdown('tests/'+outfile)
# md.add_section(Section('Introduction', 'This is the introduction.'))
# s1 = Section('Chapter 1')
# md.add_section(s1)
# s2 = Section('Chapter 2')
# md.add_section(s2)
# md.add_section(Section('Conclusion', 'This is the conclusion.'))
# s11 = Section('Chapter 1.1', 'Content of chapter 1.1.')
# s11.add_section(Section('Chapter 1.1.1', 'Content of chapter 1.1.1.'))
# s11.add_section(Section('Chapter 1.1.2', ['Content of chapter 1.1.2.', '2nd Content of chapter 1.1.2.']))
# s1.add_section(s11)
# s1.add_section(Section('Chapter 1.2', 'Content of chapter 1.2.'))
# s21 = Section('Chapter 2.1', 'Content of chapter 2.1.')  
# s211 = Section('Chapter 2.1.1', 'Content of chapter 2.1.1.')
# s21.add_section(s211)
# s2111 = Section('Chapter 2.1.1.1', 'Content of chapter 2.1.1.1.')
# s211.add_section(s2111)
# s211.add_content(s211.add_content(codeblock([this_code]))
# s2.add_section(s21)  
# md.tree_sections(index = True)
# md.write_markdown()
# '''))
#     md.tree_sections(index = True)
#     md.write_markdown()
    
    cli_md = Markdown()
    cli_md.run()
    
    console.save_svg('cli_outputs/output.svg', clear = False)
    
# webbrowser.open(f'file://{os.path.abspath('cli_outputs/output.svg')}')
