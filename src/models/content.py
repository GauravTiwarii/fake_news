
import uuid
import datetime



class Content(object):
    def __init__(self,text, _id=None):
        self.text =  text
        self._id = uuid.uuid4().hex if _id is None else _id


    def new_query(self):
        text  = input("Enter text: ")
        date  = input("Enter post date or leave blank for today ( in format ddmmyyyy)")
        if date == '':
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date,"%d%m%y")


        ##take this query to the spark and send back
            ##the result.......



    def json(self):

        return {
            {
                '_id':id,
                'headline':headline
                'content': contents[0]
                'date': datetime.datetime.utcnow()
            },
            {
                '_id': id,
                'headline': headline
                'content': contents[1]
                'date': datetime.datetime.utcnow()
            },
            {
                '_id': id,
                'headline': headline
                'content': contentss[2]
                'date': datetime.datetime.utcnow()
            },
            {
                '_id': id,
                'headline': headline
                'content': contents[3]
                'date': datetime.datetime.utcnow()
            },
            {
                '_id': id,
                'headline': headline
                'content': contentss[4]
                'date': datetime.datetime.utcnow()
            },
            {
                '_id': id,
                'headline': headline
                'content': contents[5]
                'date': datetime.datetime.utcnow()
            },
            {
                '_id': id,
                'headline': headline
                'content': contents[6]
                'date': datetime.datetime.utcnow()
            }
        }


