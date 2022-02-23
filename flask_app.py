from flask import Flask
from drone_db_ops import droneDB
from flask import request
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the drone database. Fly as high as you want!'

#dronedb = droneDB('host.docker.internal', 'root', 'Unbxd@123', 'drone_info')
host = os.environ.get('DB_URL') 
user = os.environ.get("MYSQL_USER")
pwd = os.environ.get("MYSQL_PASSWORD")
db_name = 'drone_info'
dronedb = droneDB(host, user, pwd, db_name)
#dronedb = droneDB('localhost', 'root', 'Unbxd@123', 'drone_info')
#dronedb = droneDB('host.docker.internal', 'root', 'Unbxd@123', 'drone_info')

'''

curl --header "Content-Type: application/json" --request GET --data '{}' http://127.0.0.1:5000/get_db_details
'''
@app.route('/get_db_details', methods=["GET"])
def f_get_db_details():
    return dronedb.get_db_details()


'''
curl --header "Content-Type: application/json" --request GET --data '{"tablename":"domain"}' http://127.0.0.1:5000/desc_table
'''
@app.route('/desc_table', methods=["GET"])
def f_desc_table():
    request_data = request.get_json()
    tablename = request_data['tablename']
    return dronedb.desc_table(tablename)


'''
curl --header "Content-Type: application/json" --request PUT --data '{"auto_feat_ID":200, "name":"dfdsfh", "description":"djhfdkshf"}' http://127.0.0.1:5000/insert_into_automation_features
'''
@app.route('/insert_into_automation_features', methods=['PUT'])
def f_insert_into_automation_features():
    request_data = request.get_json()
    auto_feat_ID = request_data['auto_feat_ID']
    name = request_data['name']
    description = request_data['description']
    return dronedb.insert_into_automation_features(auto_feat_ID, name, description)


'''
curl --header "Content-Type: application/json" --request PUT --data '{"company_id":200, "name":"dfdsfh"}' http://127.0.0.1:5000/insert_into_company
'''
@app.route('/insert_into_company', methods=['PUT'])
def f_insert_into_company():
    request_data = request.get_json()
    company_id = request_data['company_id']
    name = request_data['name']
    return dronedb.insert_into_company(company_id, name)


'''
curl --header "Content-Type: application/json" --request PUT --data '{"country_id":200, "name":"dfdsfh"}' http://127.0.0.1:5000/insert_into_country
'''
@app.route('/insert_into_country', methods=['PUT'])
def f_insert_into_country():
    request_data = request.get_json()
    country_id = request_data['country_id']
    name = request_data['name']
    return dronedb.insert_into_country(country_id, name)


'''

curl --header "Content-Type: application/json" --request PUT --data '{"algo_ID":200, "name":"dfdsfh"}' http://127.0.0.1:5000/insert_into_cv_algorithm
'''
@app.route('/insert_into_cv_algorithm', methods=['PUT'])
def f_insert_into_cv_algorithm():
    request_data = request.get_json()
    algo_ID = request_data['algo_ID']
    name = request_data['name']
    return dronedb.insert_into_cv_algorithm(algo_ID, name)


'''
curl --header "Content-Type: application/json" --request PUT --data '{"domain_ID":200, "name":"dfdsfh"}' http://127.0.0.1:5000/insert_into_domain
'''
@app.route('/insert_into_domain', methods=['PUT'])
def f_insert_into_domain():
    request_data = request.get_json()
    domain_ID = request_data['domain_ID']
    name = request_data['name']
    return dronedb.insert_into_domain(domain_ID, name)


'''
curl --header "Content-Type: application/json" --request PUT --data '{"ID":200, "name":"dfdsfh", "company_id":1, "height":1, "users": "sfdds", "license": 0, "training": 0, "price":0, "weight_in_kg":0, "country_of_operation_ID":1, "domain_ID":1, "usecase":"werr", "wingspan":0}' http://127.0.0.1:5000/insert_into_drone_models
'''
@app.route('/insert_into_drone_models', methods=['PUT'])
def f_insert_into_drone_models():
    request_data = request.get_json()
    ID = request_data['ID']
    name = request_data['name']
    company_id = request_data['company_id']
    height = request_data['height']
    users = request_data['users']
    license = request_data['license']
    training = request_data['training']
    price = request_data['price']
    weight_in_kg = request_data['weight_in_kg']
    country_of_operation_ID = request_data['country_of_operation_ID']
    domain_ID = request_data['domain_ID']
    usecase = request_data['usecase']
    wingspan = request_data['wingspan']
    return dronedb.insert_into_drone_models(ID, name, company_id, height, users, license, training, price, weight_in_kg, country_of_operation_ID, domain_ID, usecase, wingspan)


'''
curl --header "Content-Type: application/json" --request PUT --data '{"drone_ID":200, "auto_feat_ID":1}' http://127.0.0.1:5000/insert_into_pair_drone_automation_feature
'''
@app.route('/insert_into_pair_drone_automation_feature', methods=['PUT'])
def f_insert_into_pair_drone_automation_feature():
    request_data = request.get_json()
    drone_ID = request_data['drone_ID']
    auto_feat_ID = request_data['auto_feat_ID']
    return dronedb.insert_into_pair_drone_automation_feature(drone_ID, auto_feat_ID)


'''
curl --header "Content-Type: application/json" --request PUT --data '{"drone_ID":200, "country_id":1}' http://127.0.0.1:5000/insert_into_pair_drone_country
'''
@app.route('/insert_into_pair_drone_country', methods=['PUT'])
def f_insert_into_pair_drone_country():
    request_data = request.get_json()
    drone_ID = request_data['drone_ID']
    country_id = request_data['country_id']
    return dronedb.insert_into_pair_drone_country(drone_ID, country_id)


'''

curl --header "Content-Type: application/json" --request PUT --data '{"drone_ID":200, "cv_algo_ID":1}' http://127.0.0.1:5000/insert_into_pair_drone_cv_algo
'''
@app.route('/insert_into_pair_drone_cv_algo', methods=['PUT'])
def f_insert_into_pair_drone_cv_algo():
    request_data = request.get_json()
    drone_ID = request_data['drone_ID']
    cv_algo_ID = request_data['cv_algo_ID']
    return dronedb.insert_into_pair_drone_cv_algo(drone_ID, cv_algo_ID)


'''

curl --header "Content-Type: application/json" --request PUT --data '{"drone_ID":200, "sec_feat_ID":1}' http://127.0.0.1:5000/insert_into_pair_drone_security_feature
'''
@app.route('/insert_into_pair_drone_security_feature', methods=['PUT'])
def f_insert_into_pair_drone_security_feature():
    request_data = request.get_json()
    drone_ID = request_data['drone_ID']
    sec_feat_ID = request_data['sec_feat_ID']
    return dronedb.insert_into_pair_drone_security_feature(drone_ID, sec_feat_ID)


'''

curl --header "Content-Type: application/json" --request PUT --data '{"sec_feat_ID":200, "name":"skjdksjf", "decription":"dfdsffddsfdd"}' http://127.0.0.1:5000/insert_into_security_features
'''
@app.route('/insert_into_security_features', methods=['PUT'])
def f_insert_into_security_features():
    request_data = request.get_json()
    sec_feat_ID = request_data['sec_feat_ID']
    name = request_data['name']
    decription = request_data['decription']
    return dronedb.insert_into_security_features(sec_feat_ID, name, decription)


'''
curl --header "Content-Type: application/json" --request GET --data '{"tablename":"domain"}' http://127.0.0.1:5000/display_entries
'''
@app.route('/display_entries', methods=["GET"])
def f_display_entries():
    request_data = request.get_json()
    tablename = request_data['tablename']
    return dronedb.display_entries(tablename)


'''
curl --header "Content-Type: application/json" --request DELETE --data '{"tablename":"security_features", "condition": "sec_feat_ID=200"}' http://127.0.0.1:5000/delete_rows
'''
@app.route('/delete_rows', methods=["DELETE"])
def f_delete_rows():
    request_data = request.get_json()
    tablename = request_data['tablename']
    del_condition = request_data['condition']

    return dronedb.delete_rows(tablename, del_condition)


if(__name__ == '__main__'):
    app.run(host="0.0.0.0", debug=True)

#URL mapping without JSON
#app.add_url_rule('/get_db_details', 'get_db_details', dronedb.get_db_details, methods=['GET'])
#app.add_url_rule('/insert_into_automation_features/<int:arg_auto_feat_ID>/<string:arg_name>/<string:arg_description>', 'insert_into_automation_features', dronedb.insert_into_automation_features, methods=['POST'])
#app.add_url_rule('/insert_into_company/<int:company_id>/<string:name>', 'insert_into_company', dronedb.insert_into_company, methods=['POST'])
#app.add_url_rule('/insert_into_country/<int:country_id>/<string:name>', 'insert_into_country', dronedb.insert_into_country, methods=['POST'])
#app.add_url_rule('/insert_into_cv_algorithm/<int:algo_ID>/<string:name>', 'insert_into_cv_algorithm', dronedb.insert_into_cv_algorithm, methods=['POST'])
#app.add_url_rule('/insert_into_domain/<int:domain_ID>/<string:name>', 'insert_into_domain', dronedb.insert_into_domain, methods=['POST'])
# URL testing; http://127.0.0.1:5000/insert_into_drone_models/111/sdsfd/1/0/0/0/0/0/0/1/1/asds/0  (Coz we can't keep typing everytime... Its boring)
#app.add_url_rule('/insert_into_drone_models/<int:ID>/<string:Name>/<int:company_id>/<int:height>/<string:users>/<int:licence>/<int:training>/<int:price>/<int:weight_in_kg>/<int:country_of_operation_ID>/<int:domain_ID>/<string:usecase>/<int:wingspan>', 'insert_into_drone_models', dronedb.insert_into_drone_models, methods=['POST'])
#app.add_url_rule('/insert_into_pair_drone_automation_feature/<int:drone_ID>/<int:auto_feat_ID>', 'insert_into_pair_drone_automation_feature', dronedb.insert_into_pair_drone_automation_feature, methods=['POST'])
#app.add_url_rule('/insert_into_pair_drone_country/<int:drone_ID>/<int:country_id>', 'insert_into_pair_drone_country', dronedb.insert_into_pair_drone_country, methods=['POST'])
#app.add_url_rule('/insert_into_pair_drone_cv_algo/<int:drone_ID>/<int:cv_algo_ID>', 'insert_into_pair_drone_cv_algo', dronedb.insert_into_pair_drone_cv_algo, methods=['POST'])
#app.add_url_rule('/insert_into_pair_drone_security_feature/<int:drone_ID>/<int:sec_feat_ID>', 'insert_into_pair_drone_security_feature', dronedb.insert_into_pair_drone_security_feature, methods=['POST'])
#app.add_url_rule('/insert_into_security_features/<int:sec_feat_ID>/<string:name>/<string:decription>', 'insert_into_security_features', dronedb.insert_into_security_features, methods=['POST'])

#app.add_url_rule('/display_entries/<tablename>', 'display_entries', dronedb.display_entries, methods=['GET'])
#DELETION
#app.add_url_rule('/delete_rows/<tablename>/<condition>', 'delete_rows', dronedb.delete_rows, methods=['DELETE'])
