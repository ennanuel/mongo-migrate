import click
from pymongo import MongoClient
import os

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    with open(env_path, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            os.environ[key] = value

@click.command()

def migrate_data():
    try:
        # Alternatively, you can replace these with your actual connection strings
        live_uri = os.environ.get('LIVE_MONGO_URI')
        local_uri = os.environ.get('LOCAL_MONGO_URI')
        database = os.environ.get('DATABASE_NAME')

        click.echo(f'Copying data from {live_uri} to {local_uri} for database {database}')

        # Connect to live and local MongoDB instances
        live_client = MongoClient(live_uri)
        local_client = MongoClient(local_uri)

        # Access the source and destination databases
        live_db = live_client[database]
        local_db = local_client[database]

        # Get a list of collections in the live database
        collections = live_db.list_collection_names()

        for collection_name in collections:
            try:
                click.echo(f'Clearing data in {collection_name} in the local database...')
                local_db[collection_name].delete_many({})

                click.echo(f'Copying data from {collection_name}...')
                collection_data = live_db[collection_name].find()

                # Insert the data into the local collection
                local_db[collection_name].insert_many(collection_data)

                click.echo(f'{collection_name} data copy complete.')

            except Exception as e:
                click.echo(f'Error copying data for {collection_name}: {str(e)}')

        click.echo('Data copy complete.')

    except Exception as e:
        click.echo(f'Error: {str(e)}')

if __name__ == '__main__':
    migrate_data()
