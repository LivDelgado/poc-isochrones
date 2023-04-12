from typing import List, Tuple
import psycopg2
import os
from postgis.psycopg import register

class DatabaseConfig:
    def create_connection(self):
        connection = None

        # LOCAL CONFIGURATION - UNCOMMENT THIS TO RUN LOCALLY
        # os.environ["POSTGRES_HOST"] = "localhost"
        # os.environ["POSTGRES_PORT"] = "5432"
        # os.environ["POSTGRES_DB"] = "geospatial_test_db"
        # os.environ["POSTGRES_USER"] = "root"
        # os.environ["POSTGRES_PASSWORD"] = "root"

        try:
            connection = psycopg2.connect(
                host=os.getenv('POSTGRES_HOST'),
                port=os.getenv('POSTGRES_PORT'),
                database=os.getenv('POSTGRES_DB'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD')
            )
            register(connection)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            raise error
       
        return connection
    
    def close_connection(self):
        self.connection.close()
    
    def insert_one_register(self, query: str, vars=...):
        """
        insert one register into database table

        Example usage: 
            insert_one_register(
                'INSERT INTO Table(id, name) VALUES (%s)', 
                (1, 'a'), (2, 'b')
            )
        
        :param str query: SQL INSERT query
        :param tuple vars: tuple of values to insert
        """
        connection = None

        try:
            connection = self.create_connection()
            cursor = connection.cursor()
            cursor.execute(query, vars)
            connection.commit()
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if connection is not None:
                connection.close()

    def insert_multiple_registers(self, query: str, vars_list: List) -> None:
        """
        insert multiple registers into database table

        Example usage: 
            insert_multiple_registers(
                'INSERT INTO Table(id, name) VALUES (%s)', 
                [(1, 'a'), (2, 'b')]
            )
        
        :param str query: SQL INSERT query
        :param list vars_list: list of values to insert
        """

        connection = None

        try:
            connection = self.create_connection()
            cursor = connection.cursor()
            cursor.executemany(query, vars_list)
            connection.commit()
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if connection is not None:
                connection.close()

    def get_registers(self, query: str) -> Tuple[int, List[Tuple]]:
        """
        execute SELECT statement in database
        returns how many registers were found and the registers

        Example usage: 
            get_registers('SELECT id, name FROM table')
        
        :param str query: SQL SELECT query
        """

        connection = None

        number_of_registers = 0
        registers = []

        try:
            connection = self.create_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            
            number_of_registers = cursor.rowcount
            registers = cursor.fetchall()
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if connection is not None:
                connection.close()
        
        return number_of_registers, registers

    def update_one_register(self, query: str, vars=...):
        """
        insert one register into database table

        Example usage: 
            insert_one_register(
                'UPDATE Table SET name = %s WHERE id = %s', 
                ('a', 1)
            )
        
        :param str query: SQL UPDATE query
        :param tuple vars: tuple of values to update - set and where
        """
        connection = None

        try:
            connection = self.create_connection()
            cursor = connection.cursor()
            cursor.execute(query, vars)
            connection.commit()
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if connection is not None:
                connection.close()
