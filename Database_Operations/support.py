from sqlalchemy import create_engine, text

# Define the database URL
DATABASE_URL = "sqlite:///./chats.db"
engine = create_engine(DATABASE_URL)

# SQL commands to alter the table
alter_table_sql = """
ALTER TABLE chat_records ADD COLUMN transfer_call_user_message TEXT;
ALTER TABLE chat_records ADD COLUMN transfer_call_response TEXT;
"""

# Execute the commands
with engine.connect() as connection:
    try:
        connection.execute(text(alter_table_sql))
        print("Columns added successfully.")
    except Exception as e:
        print(f"Error updating schema: {e}")
