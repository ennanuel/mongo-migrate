from pymongo import MongoClient
import os

env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    with open(env_path, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            os.environ[key] = value

def migrate_data():
    try:
        live_uri = os.environ.get('LIVE_MONGO_URI')
        local_uri = os.environ.get('LOCAL_MONGO_URI')
        database = os.environ.get('DATABASE_NAME')

        print(f'Copying data from {live_uri} to {local_uri} for database {database}')

        live_client = MongoClient(live_uri)
        local_client = MongoClient(local_uri)

        live_db = live_client[database]
        local_db = local_client[database]

        collections = live_db.list_collection_names()

        for collection_name in collections:
            try:
                print(f'Clearing data in {collection_name} in the local database...')
                local_db[collection_name].delete_many({})

                print(f'Copying data from {collection_name}...')
                collection_data = live_db[collection_name].find()
                
                local_db[collection_name].insert_many(collection_data)

                print(f'{collection_name} data copy complete.')

            except Exception as e:
                print(f'Error copying data for {collection_name}: {str(e)}')

        print('Data copy complete.')

    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == '__main__':
    migrate_data()
