import webbrowser
from colorama import init, Fore, Style

# Initialize colorama to support colored text on Windows
init()

def open_website(url):
    webbrowser.open(url)

def fancy_print(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL)

if __name__ == "__main__":
    fancy_print("Welcome to Fancy Website Opener!", Fore.CYAN)
    fancy_print("-" * 40, Fore.YELLOW)
    website_url = input(Fore.GREEN + "Enter the URL of the website you want to open: ")
    fancy_print("-" * 40, Fore.YELLOW)
    fancy_print("Opening website...", Fore.MAGENTA)
    open_website(website_url)
