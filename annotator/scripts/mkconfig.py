import srsly
import os
from dotenv import dotenv_values

ENV = {
    **dotenv_values(".env"),
    **os.environ,
}

# Load configuration file
config = srsly.read_json("prodigy.json")

# Ensure postgres variables in `prodigy.json`
config["db_settings"]["postgresql"]["user"] = ENV['POSTGRES_USER']
config["db_settings"]["postgresql"]["password"] = ENV['POSTGRES_PWD']
config["db_settings"]["postgresql"]["host"] = ENV['POSTGRES_HOST']
config["db_settings"]["postgresql"]["port"] = ENV['POSTGRES_PORT']
config["db_settings"]["postgresql"]["dbname"] = ENV['POSTGRES_DB_NAME']

# Write configuration file
config = srsly.write_json("prodigy.json", config)
