from flask import Flask
from drone_db_ops import droneDB

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the drone database. Fly as high as you want!'

#Add proper parameters for routing insert and delete URLs

dronedb = droneDB('localhost', 'root', 'Unbxd@123', 'drone_info')
app.add_url_rule('/get_db_details', 'get_db_details', dronedb.get_db_details)
app.add_url_rule('/desc_table/<tablename>', 'desc_table', dronedb.desc_table)
#app.add_url_rule('/insert_records/<tablename>/<val_tuple>', 'insert_records', dronedb.insert_records) #change type to int for tuple elements
app.add_url_rule('/display_entries/<tablename>', 'display_entries', dronedb.display_entries)
#app.add_url_rule('/delete_rows/<tablename>/<condition>', 'delete_rows', dronedb.delete_rows)

if(__name__ == '__main__'):
    app.run(debug=True)
