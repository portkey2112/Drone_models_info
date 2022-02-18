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


    def insert_records(self, tablename, val_tuple):
        query_str = f'INSERT INTO {tablename} VALUES '
        for i in range(len(val_tuple)):
            if(i == 0):
                query_str += str(val_tuple[i])
            else:
                query_str += ', ' + str(val_tuple[i])
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except:
            self.db.rollback()
            return f'Exception in inserting into table {tablename}!!'
        return f'Insertion operation complete into table {tablename}'

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
        except:
            self.db.rollback()
            return f'Exception in deletion from table {tablename}!'
        return f'Deletion DONE from table {tablename}'

#FOR TESTING
'''
drone_db = droneDB('localhost', 'root', 'Unbxd@123', 'drone_info')
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
