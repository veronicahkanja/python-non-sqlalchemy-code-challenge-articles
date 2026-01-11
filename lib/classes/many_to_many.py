class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception ("Title must be between 5 and 50 characters")
        
        self.author = author
        self.magazine = magazine
        self._title = title 
        
        Article.all.append(self)

@property
def title(self):
   return self._title

@title.setter
def title(self, value):
    pass


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception ("Name must bee a non-empty string")
        self.name = name


    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
       return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
         return list({magazine.category for magazine in self.magazines()})

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
          raise Exception("Invalid magazine name")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Invalid category")
           
        self.name = name
        self.category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = []
        for author in self.contributors():
            count = len([a for a in self.articles() if a.author == author])
            if count > 2:
                authors.append(author)
                return authors