# mongo-migrate

# MongoDB Data Migration Script

This script allows you to migrate data from a live MongoDB database to a local MongoDB database.

## Prerequisites

- Python 3.x installed
- Pip package manager installed

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ennanuel/mongo-migrate.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Set up Environment Variables

Create a `.env` file in the project directory with the following content:

```env
LIVE_MONGO_URI=your_live_mongo_uri
LOCAL_MONGO_URI=your_local_mongo_uri
```

Replace `your_live_mongo_uri` and `your_local_mongo_uri` with your actual MongoDB connection URIs.

### 2. Run the Script

Run the migration script using the following command:

```bash
python mongo_migration.py --live-uri "your_live_mongo_uri" --local-uri "your_local_mongo_uri" --database "your_database_name"
```

Replace placeholders with your actual MongoDB connection URIs and database name.

### Note

- The script will clear existing data in the local database for each collection before migrating data.
- Make sure to have backups of your data before running the migration.
