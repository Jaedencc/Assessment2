Feature: Spotify Database Table

"""
make sure that the Spotify table was created successfully 
and if data inserting and querying are working well as expected
"""

Scenario: Insert and get data from the Spotify table
  Given the Spotify table is created
  When I insert a data row into the Spotify table
  Then the data should be queried from the Spotify table