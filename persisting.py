#adding data to our database

from models import User, Comment
#from sqlalchemy.orm import Session
#from connect import engine
from main import session

#session = Session(bind=engine)

User1= User(
    username= 'Jona',
    email_address='jona@gmail.com',
    comments=[
        Comment(text='Hello Dude'),
        Comment(text='murife run')
    ]
)

Paul= User(
    username= 'Paul',
    email_address='paul@gmail.com',
    comments= [
        Comment(text='Do it Dude'),
        Comment(text='I loveit here')
    ] 
)   

Cathy = User(
    username= 'cathy',
    email_address="cathy@sql.org",
)    


session.add_all([User1,Paul,Cathy])
session.commit()