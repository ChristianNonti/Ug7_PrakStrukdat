class Browser:
    def __init__(self):
        self.history = []  
        self.current_url = None  
    
    def go(self, url):
        self.history.append(self.current_url)  
        self.current_url = url  
    
    def back(self):
        if len(self.history) > 0:
            self.current_url = self.history.pop()  
    
    def forward(self):
        if self.current_url is not None:
            self.history.append(self.current_url)  
            self.current_url = None  
            if len(self.history) > 0:
                self.current_url = self.history.pop()  
    
    def printAll(self):
        if self.current_url is not None:
            print(self.current_url, end=" ")
        for url in reversed(self.history):
            print(url, end=" ")

browser = Browser()

browser.go("https://google.com")
browser.go("https://ukdw.ac.id")
browser.go("https://facebook.com")
browser.back()  # output: https://ukdw.ac.id
browser.back()  # output: https://google.com
browser.forward()  # output: https://ukdw.ac.id
browser.go("https://twitter.com")
browser.printAll()  # output: https://google.com https://ukdw.ac.id https://twitter.com
