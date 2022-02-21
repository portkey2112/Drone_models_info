import mysql.connector

class droneDB():
    def __init__(self, host='localhost', user='root', password='Unbxd@123', database='drone_info'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.db.cursor()

    def get_db_details(self):
        res_str = ''
        res_str += f'DATABASE DETAILS\n'
        res_str += f'Database tech: mysql\n'
        res_str += f'Database name: {self.database}\n'
        try:
            self.cursor.execute('show tables;')
        except:
            res_str += f'Exception in showing tables!'
            return res_str
        result = self.cursor.fetchall()
        res_str += 'The list of tables:\n'
        res_str += '\n'.join([str(item) for item in result])
        return res_str
        '''
        print('Showing list of tables...')
        for x in result:
            print(x)
        print('DONE')
        '''

    def desc_table(self, tablename):
        query = f'desc {tablename}'
        try:
            self.cursor.execute(query)
        except:
            return f'ERROR in fetching description of {tablename}'
        result = self.cursor.fetchall()
        res_str = f'Showing description of table {tablename}'
        res_str += '\n'.join([str(item) for item in result])
        '''
        for x in result:
            print(x)
        '''
        return res_str

    def insert_into_automation_features(self, arg_auto_feat_ID, arg_name, arg_description):
        query_str = f'INSERT INTO automation_features VALUES ({arg_auto_feat_ID}, \'{arg_name}\', \'{arg_description}\')'
        print(query_str)
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in inserting into table automation_features !!, {str(e)}'
        return f'Insertion operation complete into table automation_features'

    def insert_into_company(self, company_id, name):
        query_str = f'INSERT INTO company VALUES ({company_id}, \'{name}\')'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in inserting into table company !!, {str(e)}'
        return f'Insertion operation complete into table company'

    def insert_into_country(self, country_id, name):
        query_str = f'INSERT INTO country VALUES ({country_id}, \'{name}\')'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in inserting into table country !!, {str(e)}'
        return f'Insertion operation complete into table country'

    def insert_into_cv_algorithm(self, algo_ID, name):
        query_str = f'INSERT INTO cv_algorithm VALUES ({algo_ID}, \'{name}\')'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in inserting into table cv_algorithm !!, {str(e)}'
        return f'Insertion operation complete into table cv_algorithm'

    def insert_into_domain(self, domain_ID, name):
        query_str = f'INSERT INTO domain VALUES ({domain_ID}, \'{name}\')'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in inserting into table domain !!, {str(e)}'
        return f'Insertion operation complete into table domain'

    def insert_into_drone_models(self, ID, Name, company_id, height,
    users, licence, training, price, weight_in_kg, country_of_operation_ID,
    domain_ID, usecase, wingspan):
        query_str = f'INSERT INTO drone_models VALUES ({ID}, \'{Name}\', {company_id}, {height}, \'{users}\', {licence}, {training}, {price}, {weight_in_kg}, {country_of_operation_ID}, {domain_ID},\'{usecase}\', {wingspan})'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in inserting into table drone_models !!, {str(e)}'
        return f'Insertion operation complete into table drone_models'

    def insert_into_pair_drone_automation_feature(self, drone_ID, auto_feat_ID):
        query_str = f'INSERT INTO pair_drone_automation_feature VALUES ({drone_ID}, {auto_feat_ID})'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in inserting into table pair_drone_automation_feature  !!, {str(e)}'
        return f'Insertion operation complete into table pair_drone_automation_feature'

    def insert_into_pair_drone_country(self, drone_ID, country_id):
        query_str = f'INSERT INTO pair_drone_country VALUES ({drone_ID}, {country_id})'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in inserting into table pair_drone_country  !!, {str(e)}'
        return f'Insertion operation complete into table pair_drone_country'

    def insert_into_pair_drone_cv_algo(self, drone_ID, cv_algo_ID):
        query_str = f'INSERT INTO pair_drone_cv_algo VALUES ({drone_ID}, {cv_algo_ID})'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in inserting into table pair_drone_cv_algo  !!, {str(e)}'
        return f'Insertion operation complete into table pair_drone_cv_algo'

    def insert_into_pair_drone_security_feature(self, drone_ID, sec_feat_ID):
        query_str = f'INSERT INTO pair_drone_security_feature VALUES ({drone_ID}, {sec_feat_ID})'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in inserting into table pair_drone_security_feature  !!, {str(e)}'
        return f'Insertion operation complete into table pair_drone_security_feature'

    def insert_into_security_features(self, sec_feat_ID, name, decription):
        query_str = f'INSERT INTO security_features VALUES ({sec_feat_ID}, \'{name}\', \'{decription}\')'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in inserting into table security_features  !!, {str(e)}'
        return f'Insertion operation complete into table security_features'

    def display_entries(self, tablename):
        query_str = f'SELECT * FROM {tablename}'
        try:
            self.cursor.execute(query_str);
        except:
            return f'Exception in displaying table {tablename}!'
        result = self.cursor.fetchall()
        res_str = f'Displaying entries of table {tablename}\n'
        res_str += '\n'.join(str(item) for item in result)
        '''
        for x in result:
            print(x)
        print('Displaying DONE')
        '''
        return res_str

    def delete_rows(self, tablename, condition):
        query_str = f'DELETE FROM {tablename} WHERE {condition}'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            return f'Exception in deletion from table {tablename}!, {str(e)}'
        return f'Deletion DONE from table {tablename}'

#FOR TESTING
'''
drone_db = droneDB('localhost', 'root', 'Unbxd@123', 'drone_info')
print(drone_db. insert_into_drone_models(111, 'dss2', 1, 1, 1, 0,0,0,0,1,1,'dd',0))
print(drone_db.delete_rows('drone_models', 'ID=111'))
print('TABLE DESCRIPTIONS')
print(drone_db.desc_table('country'))
print(drone_db.desc_table('company'))
print('DISPLAY ALL ENTRIES OF A TABLE')
print(drone_db.display_entries('security_features'))
print('INSERTIONS AND DELETION')
val_tuple = ((22, 'abc'), (33, 'xyz'))
print(drone_db.insert_records('country', val_tuple))
print(drone_db.delete_rows('country', 'country_ID=22'))
print(drone_db.delete_rows('country', 'country_ID=33'))
print(drone_db.get_db_details())
print(drone_db.display_entries('security_features'))
'''
