import webbrowser

def open_website(url):
    webbrowser.open(url)

if __name__ == "__main__":
    website_url = input("Enter the URL of the website you want to open: ")
    open_website(website_url)

