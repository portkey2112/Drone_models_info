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
        print('DATABASE DETAILS')
        print(f'Database tech: mysql')
        print(f'Database name: {self.database}')
        try:
            self.cursor.execute('show tables;')
        except:
            print('Exception in showing tables!')
            return
        result = self.cursor.fetchall()
        print('Showing list of tables...')
        for x in result:
            print(x)
        print('DONE')

    def desc_table(self, tablename):
        query = f'desc {tablename}'
        try:
            self.cursor.execute(query)
        except:
            print('ERROR!')
            return
        result = self.cursor.fetchall()
        print(f'Showing description of table {tablename}')
        for x in result:
            print(x)
        print('DONE')

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
            print('Exception in inserting!!')
            self.db.rollback()
            return
        print('Insertion operation complete')

    def display_entries(self, tablename):
        query_str = f'SELECT * FROM {tablename}'
        try:
            self.cursor.execute(query_str);
        except:
            print('Exception in displaying!')
        result = self.cursor.fetchall()
        for x in result:
            print(x)
        print('Displaying DONE')

    def delete_rows(self, tablename, condition):
        query_str = f'DELETE FROM {tablename} WHERE {condition}'
        try:
            self.cursor.execute(query_str)
            self.db.commit()
        except:
            print('Exception in deletion!')
            self.db.rollback()
            return
        print('Deletion DONE')

#FOR TESTING
'''
drone_db = droneDB('localhost', 'root', 'Unbxd@123', 'drone_info')

print('TABLE DESCRIPTIONS')
drone_db.desc_table('country')
drone_db.desc_table('company')

print('DISPLAY ALL ENTRIES OF A TABLE')
drone_db.display_entries('security_features')

print('INSERTIONS AND DELETION')
val_tuple = ((22, 'abc'), (33, 'xyz'))
drone_db.insert_records('country', val_tuple)
drone_db.delete_rows('country', 'country_ID=22')
drone_db.delete_rows('country', 'country_ID=33')

drone_db.get_db_details()
'''
