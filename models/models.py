# models.py
#
# This file is where you define your ORM models. Models represent tables in the database,
# and each instance of a model corresponds to a row in that table.
#
# Models should inherit from the `Base` class, which provides methods for interacting with the database,
# such as saving records, querying, and deleting.
#
# In this file, you will:
#   - Define your own models, from your database schema in this project, by subclassing the `Base` class.
#   - Use `Column` objects to define columns and their types (e.g., `Integer`, `String`).
#   - Add attributes to each model class to represent columns in the corresponding database table.
#   - Define additional methods in the models as necessary for specific functionality (e.g., custom queries,
#     business logic, etc.).
#
#
# Students should implement their own models, specifying the columns using `Column` and selecting the appropriate
# `types` for each column, such as `Integer`, `String`, `Boolean`, etc.
#

from api.columns import Column
from api.datatypes import Integer, String, Boolean
from api.base import Base




