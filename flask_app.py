from flask import Flask
from drone_db_ops import droneDB

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the drone database. Fly as high as you want!'

dronedb = droneDB('localhost', 'root', 'Unbxd@123', 'drone_info')

app.add_url_rule('/get_db_details', 'get_db_details', dronedb.get_db_details)
app.add_url_rule('/desc_table/<tablename>', 'desc_table', dronedb.desc_table)

app.add_url_rule('/insert_into_automation_features/<int:arg_auto_feat_ID>/<string:arg_name>/<string:arg_description>', 'insert_into_automation_features', dronedb.insert_into_automation_features)
app.add_url_rule('/insert_into_company/<int:company_id>/<string:name>', 'insert_into_company', dronedb.insert_into_company)
app.add_url_rule('/insert_into_country/<int:country_id>/<string:name>', 'insert_into_country', dronedb.insert_into_country)
app.add_url_rule('/insert_into_cv_algorithm/<int:algo_ID>/<string:name>', 'insert_into_cv_algorithm', dronedb.insert_into_cv_algorithm)
app.add_url_rule('/insert_into_domain/<int:domain_ID>/<string:name>', 'insert_into_domain', dronedb.insert_into_domain)
# URL testing; http://127.0.0.1:5000/insert_into_drone_models/111/sdsfd/1/0/0/0/0/0/0/1/1/asds/0  (Coz we can't keep typing everytime... Its boring)
app.add_url_rule('/insert_into_drone_models/<int:ID>/<string:Name>/<int:company_id>/<int:height>/<string:users>/<int:licence>/<int:training>/<int:price>/<int:weight_in_kg>/<int:country_of_operation_ID>/<int:domain_ID>/<string:usecase>/<int:wingspan>', 'insert_into_drone_models', dronedb.insert_into_drone_models)
app.add_url_rule('/insert_into_pair_drone_automation_feature/<int:drone_ID>/<int:auto_feat_ID>', 'insert_into_pair_drone_automation_feature', dronedb.insert_into_pair_drone_automation_feature)
app.add_url_rule('/insert_into_pair_drone_country/<int:drone_ID>/<int:country_id>', 'insert_into_pair_drone_country', dronedb.insert_into_pair_drone_country)
app.add_url_rule('/insert_into_pair_drone_cv_algo/<int:drone_ID>/<int:cv_algo_ID>', 'insert_into_pair_drone_cv_algo', dronedb.insert_into_pair_drone_cv_algo)
app.add_url_rule('/insert_into_pair_drone_security_feature/<int:drone_ID>/<int:sec_feat_ID>', 'insert_into_pair_drone_security_feature', dronedb.insert_into_pair_drone_security_feature)
app.add_url_rule('/insert_into_security_features/<int:sec_feat_ID>/<string:name>/<string:decription>', 'insert_into_security_features', dronedb.insert_into_security_features)


app.add_url_rule('/display_entries/<tablename>', 'display_entries', dronedb.display_entries)
#DELETION
app.add_url_rule('/delete_rows/<tablename>/<condition>', 'delete_rows', dronedb.delete_rows)

if(__name__ == '__main__'):
    app.run(debug=True)
