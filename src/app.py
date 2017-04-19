

import uuid

from flask import Flask, render_template, request
from src.models.content import  Content
from src.common.database import Database

app = Flask(__name__) #__main__
app.secret_key = str(uuid.uuid4().hex)


@app.before_first_request
def database_initialize():
    Database.initialize()


@app.route('/') #www.mysite.com/api/
def hello_method():
    return render_template('query.html')



@app.route('/query', methods = ['POST'])  #www/mysite.com/query
def query():
    query_text = request.form['query_text']

    #send this query_text to the spark ....
    #let it process..
    #gather back the result in a form of list named "content"



    return render_template(result_page.html, query_text = query_text, contents = contents )






if __name__ == '__main__':
    app.run()



