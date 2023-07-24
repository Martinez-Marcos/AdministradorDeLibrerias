class Book:
    def __init__(selft, title, author, condition):
        selft.title = title
        selft.author = author
        selft.condition = condition
    
    @property    
    def title(selft):
        return selft.__title

    @title.setter     
    def title(selft, title):
        selft.__title = title
    
    @property 
    def author(selft):
        return selft.__author

    @author.setter    
    def author(selft, author):
        selft.__author =author 

    @property 
    def condition(selft):
        return selft.__condition

    @condition.setter  
    def condition(selft, condition):
        selft.__condition = condition
    
    def replacement(selft):
        if (selft.condition == "Bad"):
            return True
        else :
            return False