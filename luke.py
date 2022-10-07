import sys

def main(text):
    relations = {'Darth Vader':'father', 
             'Leia':'sister', 
             'Han':'brother in law', 
             'R2D2':'droid', 
             'Rey':'Padawan', 
             'Tatooine':'homeworld'}

    
    if sys.argv[1] == 'Darth Vader':
        print("No, I am your father")
        
    else:
        print('Luke, I am your', relations[text])
  

(main(sys.argv[1]))