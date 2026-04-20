# base.py
#
# This file defines the `Base` class, which serves as the foundation for all ORM models.
# The `Base` class provides essential methods for interacting with the database, such as:
#   - `save()`: Insert or update the current model instance in the database.
#   - `_insert()`: Insert the current instance into the database (private method).
#   - `_update()`: Update the current instance in the database (private method).
#   - `get()`: Retrieve a record by its ID.
#   - `delete()`: Delete a record by its ID.
#   - `all()`: Retrieve all records of the model from the database.
#   - `query()`: Query records based on filter conditions.
#   - `create_schema()`: Generate the schema (sql code) for the model in the database.
#   - `create()`: Uses the generated schema from the previous function to create a table in the database based on the model's schema.
#   - `join()`: Join multiple models together for data retrieval.
#   - `where()`: Add WHERE conditions to queries.
#   - `having()`: Add HAVING conditions to queries.
#   - `group_by()`: Add GROUP BY clauses to queries.
#
# Connection management is critical. Every method interacting with the database must:
#   - Open a new connection and cursor at the start of the operation.
#   - Close the cursor and connection after the operation is complete,
#     whether the operation is successful or not, to avoid memory leaks.
#   - Transactions must be committed on success, and rolled back on failure.
#
# Students should implement proper connection management in each method, including:
#   - Using `try`, `except`, and `finally` to ensure the connection and cursor are always closed.
#   - Handling potential exceptions during database operations and performing rollbacks if needed.
#
# The `Base` class is meant to be subclassed, and any model that extends `Base` will automatically
# inherit the methods for database interaction.


from api.db_connectors import MySQL
from api.columns import Column


class Base:
    def __init__(self, **kwargs):
        """Initialize model instance with attributes."""
        for key, value in kwargs.items():
            setattr(self, key, value)


    def save(self):
        """Insert or update the record in the database.

        TODO:
            - If the model instance has an `id`, call `_update()` to update the existing record.
            - Otherwise, call `_insert()` to insert the new record.
            - Ensure connection and cursor management is handled properly (open and close as needed).
        """
        pass

    def _insert(self):
        """Insert the current instance into the database.

        TODO:
            - Open a new connection and cursor.
            - Construct the `INSERT` SQL query to add the model instance.
            - Ensure the connection and cursor are properly closed after the operation, even if an error occurs.
            - Commit the transaction if successful; rollback if there's an error.
        """
        pass


    def _update(self):
        """Update the current instance in the database.

        TODO:
            - Open a new connection and cursor.
            - Construct the `UPDATE` SQL query to modify the existing record.
            - Ensure the connection and cursor are properly closed after the operation, even if an error occurs.
            - Commit the transaction if successful; rollback if there's an error.
        """
        pass


    @classmethod
    def get(cls, id):
        """Retrieve a record from the database by its ID.

        TODO:
            - Open a connection and cursor.
            - Construct the `SELECT` SQL query to fetch the record by its primary key (`id`).
            - Ensure the connection and cursor are properly closed after the operation.
            - Handle potential exceptions using `try`, `except`, and `finally` blocks.
        """
        pass





    @classmethod
    def delete(cls, id):
        """Delete a record from the database by its ID.

        TODO:
            - Open a connection and cursor.
            - Construct the `DELETE` SQL query to remove the record by its primary key (`id`).
            - Ensure the connection and cursor are properly closed after the operation.
            - Commit the transaction if successful; rollback if there's an error.
        """
        pass

    @classmethod
    def all(cls):
        """Retrieve all records of this model from the database.

        TODO:
            - Open a connection and cursor.
            - Construct the `SELECT` SQL query to fetch all records.
            - Ensure the connection and cursor are properly closed after the operation.
            - Return the results as instances of the model.
        """
        pass

    @classmethod
    def query(cls, **filters):
        """Query records based on filters.

        TODO:
            - Open a connection and cursor.
            - Construct the `SELECT` SQL query using the provided filters as conditions.
            - Ensure the connection and cursor are properly closed after the operation.
            - Return the results as instances of the model.
        """
        pass

    @classmethod
    def create(cls):
        """Create a table for an existing schema.

        TODO:
            - Open a connection and cursor.
            - Construct the `CREATE TABLE` SQL query using the provided schema.
            - Ensure the connection and cursor are properly closed after the operation.
            - Commit the transaction if successful; rollback if there's an error.
        """
        pass

    @classmethod
    def create_schema(cls):
        """Generate the schema for the model in the database.

        TODO:
            - Open a connection and cursor.
            - Construct the `CREATE SCHEMA` SQL query using the provided descriptor.
            - Ensure the connection and cursor are properly closed after the operation.
            - Commit the transaction if successful; rollback if there's an error.
        """
        pass

    @classmethod
    def join(cls, models):
        """Join multiple models to organize your data.

        TODO:
            - Open a connection and cursor.
            - Construct the appropriate `JOIN` SQL query to combine data from multiple models.
            - Ensure the connection and cursor are properly closed after the operation.
            - Return the joined results.
        """
        pass

    @classmethod
    def where(cls, **conditions):
        """Add WHERE conditions to a query.

        TODO:
            - This method should help in adding WHERE conditions to any SELECT query.
            - Build the WHERE clause dynamically based on the given conditions (e.g., `WHERE column = value`).
            - Return the generated WHERE condition string.
        """
        pass

    @classmethod
    def having(cls, **conditions):
        """Add HAVING conditions to a query.

        TODO:
            - This method should help in adding HAVING conditions to a query.
            - Construct the HAVING clause dynamically (useful when performing aggregate functions).
            - Return the generated HAVING condition string.
        """
        pass

    @classmethod
    def group_by(cls, *columns):
        """Add GROUP BY clauses to a query.

        TODO:
            - This method should help in adding GROUP BY clauses to any SELECT query.
            - Construct the GROUP BY clause dynamically based on the provided columns (e.g., `GROUP BY column1, column2`).
            - Return the generated GROUP BY condition string.
        """
        pass

    @classmethod
    def table_descriptor(cls):
        """
        :return: the name of the table t
        """
        pass


    @classmethod
    def columns(cls):
        """
        :return: the list of column names
        """
        pass


    @classmethod
    def primary_key(cls):
        """
        :return: the primary key attribute name, not the value.
                 for example student_id = 1, will return student_id, not the value 1
        """
        pass


