import os
import sys
import subprocess
from collections import defaultdict
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from colorama import Fore, init
import random
import time

from utils.report_generator import generate_report
from utils.util import clean_domain_input

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from config import settings

init(autoreset=True)
console = Console()

if sys.version_info < (3, 0):
    print("This script requires Python 3.")
    sys.exit(1)

VERSION = "1.1"
AUTHOR = "BenCoding"

tools = [
    # DNS Tools
    {'name': 'DNS Over HTTPS', 'script': 'dns_over_https.py', 'section': 'DNS Tools'},
    {'name': 'DNS Records', 'script': 'dns_records.py', 'section': 'DNS Tools'},
    {'name': 'DNSSEC Check', 'script': 'dnssec.py', 'section': 'DNS Tools'},
    {'name': 'TXT Records', 'script': 'txt_records.py', 'section': 'DNS Tools'},
    {'name': 'WHOIS Lookup', 'script': 'whois_lookup.py', 'section': 'DNS Tools'},
    {'name': 'Zone Transfer', 'script': 'zonetransfer.py', 'section': 'DNS Tools'},

    # Domain and IP Information
    {'name': 'Domain Info', 'script': 'domain_info.py', 'section': 'Domain and IP Information'},
    {'name': 'IP Info', 'script': 'ip_info.py', 'section': 'Domain and IP Information'},

    # Server and Network Tools
    {'name': 'Associated Hosts', 'script': 'associated_hosts.py', 'section': 'Server and Network Tools'},
    {'name': 'Server Info', 'script': 'server_info.py', 'section': 'Server and Network Tools'},
    {'name': 'Server Location', 'script': 'server_location.py', 'section': 'Server and Network Tools'},
    {'name': 'Traceroute', 'script': 'traceroute.py', 'section': 'Server and Network Tools'},

    # Web Application Analysis
    {'name': 'Archive History', 'script': 'archive_history.py', 'section': 'Web Application Analysis'},
    {'name': 'Broken Links Detection', 'script': 'broken_links.py', 'section': 'Web Application Analysis'},
    {'name': 'CMS Detection', 'script': 'cms_detection.py', 'section': 'Web Application Analysis'},
    {'name': 'Cookies Analyzer', 'script': 'cookies.py', 'section': 'Web Application Analysis'},
    {'name': 'Content Discovery', 'script': 'content_discovery.py', 'section': 'Web Application Analysis'},
    {'name': 'Crawler', 'script': 'crawler.py', 'section': 'Web Application Analysis'},
    {'name': 'Robots.txt Analyzer', 'script': 'crawl_rules.py', 'section': 'Web Application Analysis'},
    {'name': 'Directory Finder', 'script': 'directory_finder.py', 'section': 'Web Application Analysis'},
    {'name': 'Email Harvesting', 'script': 'email_harvester.py', 'section': 'Web Application Analysis'},
    {'name': 'Sitemap Parsing', 'script': 'sitemap.py', 'section': 'Web Application Analysis'},
    {'name': 'Technology Stack Detection', 'script': 'technology_stack.py', 'section': 'Web Application Analysis'},
    {'name': 'Third-Party Integrations', 'script': 'third_party_integrations.py', 'section': 'Web Application Analysis'},

    # Security & Threat Intelligence
    {'name': 'Certificate Authority Recon', 'script': 'certificate_authority_recon.py', 'section': 'Security & Threat Intelligence'},
    {'name': 'Exposed Environment Files Checker', 'script': 'exposed_env_files.py', 'section': 'Security & Threat Intelligence'},
    {'name': 'HTTP Headers', 'script': 'http_headers.py', 'section': 'Security & Threat Intelligence'},
    {'name': 'HTTP Security Features', 'script': 'http_security.py', 'section': 'Security & Threat Intelligence'},
    {'name': 'Shodan Reconnaissance', 'script': 'shodan.py', 'section': 'Security & Threat Intelligence'},
    {'name': 'SSL Labs Report', 'script': 'ssl_labs_report.py', 'section': 'Security & Threat Intelligence'},
    {'name': 'Subdomain Enumeration', 'script': 'subdomain_enum.py', 'section': 'Security & Threat Intelligence'},
    {'name': 'Subdomain Takeover', 'script': 'subdomain_takeover.py', 'section': 'Security & Threat Intelligence'},
]
number_of_modules = len([tool for tool in tools if tool['script'] and tool['section'] not in ['Run All Scripts', 'Special Mode']])

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    ascii_art = f"""
( ___ )-----------------------------------( ___ )
 |   |                                     |   | 
 |   |   _   _ _____ _     ___ ___  ____   |   | 
 |   |  | | | | ____| |   |_ _/ _ \/ ___|  |   | 
 |   |  | |_| |  _| | |    | | | | \___ \  |   | 
 |   |  |  _  | |___| |___ | | |_| |___) | |   | 
 |   |  |_| |_|_____|_____|___\___/|____/  |   | 
 |   |                                     |   | 
 |___|                                     |___| 
(_____)-----------------------------------(_____)                              
    """
    lines = ascii_art.strip("\n").split("\n")
    colors = ["red","white","blue"]
    colored_lines = []
    for line in lines:
        color = random.choice(colors)
        colored_lines.append(f"[bold {color}]{line}[/bold {color}]")
        time.sleep(0.05)
    colored_ascii_art = "\n".join(colored_lines)
    description = f"""
[bold cyan]Audit WEB Tool[/bold cyan]

Version: [bold green]{VERSION}[/bold green]    Modules: [bold yellow]{number_of_modules}[/bold yellow]    Coded by: [bold magenta]{AUTHOR}[/bold magenta]
    """.strip()
    combined_text = f"{colored_ascii_art}\n{description}"
    panel_color = random.choice(colors)
    console.print(Panel(combined_text, border_style=panel_color, padding=(1, 4)), justify="center")

def display_table():
    table = Table(box=box.SIMPLE_HEAD)

    sections = ['DNS Tools', 'Domain and IP Information', 'Server and Network Tools', 
                'Web Application Analysis', 'Security & Threat Intelligence']

    table.add_column("🌐 DNS Tools", justify="left", style="red", no_wrap=True)
    table.add_column("🖥️ Domain and IP Information", justify="left", style="yellow", no_wrap=True)
    table.add_column("🔧 Server and Network Tools", justify="left", style="cyan", no_wrap=True)
    table.add_column("🌐 Web Application Analysis", justify="left", style="green", no_wrap=True)
    table.add_column("🛡️ Security & Threat Intelligence", justify="left", style="magenta", no_wrap=True)

    tools_by_section = defaultdict(list)
    for tool in tools:
        if tool['section'] in sections:
            tools_by_section[tool['section']].append(f"{tool['name']}")
    
    max_tools = max(len(tools_by_section[section]) for section in sections)
    
    for idx in range(max_tools):
        row = []
        for section in sections:
            if idx < len(tools_by_section[section]):
                row.append(f"  {tools_by_section[section][idx]}  ") 
            else:
                row.append("  ")
        table.add_row(*row)

    console.print(table)

def execute_script(script_name, target):
    script_path = os.path.join("modules", script_name)
    if os.path.isfile(script_path):
        try:
            with console.status(f"[bold green]Running {script_name}...[/bold green]", spinner="dots"):
                process = subprocess.Popen(
                    [sys.executable, script_path, target],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )
                for line in iter(process.stdout.readline, ''):
                    if line:
                        console.print(line.strip())
                process.stdout.close()
                process.wait()
        except Exception as e:
            console.print(f"[!] Error running {script_name}: {e}", style="bold red")
    else:
        console.print(f"Script {script_name} not found.", style="bold red")

def audit_mode():
    clear_screen()
    logo()
    display_table()
    console.print("\n[bold red][*] Running AUDIT MODE - Executing All Modules [/bold red]\n")
    selected_modules = [tool for tool in tools if tool['script']]
    domain = input("Enter the target domain or URL: ")
    for tool in selected_modules:
        execute_script(tool['script'], domain)
        time.sleep(3)

def main():
    audit_mode()

if __name__ == "__main__":
    main()