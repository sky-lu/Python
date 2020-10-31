class Book:
    bookId = 0
    def __init__(self,title = None, author = None, editor = None, price = 0.0):
        self.title = title
        self.author = author
        self.editor = editor
        self.price = price
        Book.bookId += 1
    
    @property
    def getTitle(self):
        return self.title
    
    @property
    def getAuthor(self):
        return self.author
    
    @property
    def getEditor(self):
        return self.editor
    
    @property
    def getPrice(self):
        return self.price
    
    @property
    def getBookId(self):
        return self.bookId

    @getPrice.setter
    def setPrice(self, newPrice):
        if newPrice > 0:
            self.price = newPrice
        else:
            self.price = 0.0
    
    def __str__(self):
        return f"Book id : {self.bookId} \tBook name : {self.title} \tAuthor name : {self.author} \tPrice : {self.price}"

    

