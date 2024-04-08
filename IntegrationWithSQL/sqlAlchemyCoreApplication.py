from sqlalchemy import *

engine = create_engine("sqlite://")

metadata_obj = MetaData()

user = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key=True, autoincrement=True),
    Column("user_name", String(40), nullable=False),
    Column("email_address", String(60)),
    Column("nickname", String(50), nullable=False)  
)

user_prefs = Table(
    "user_prefs",
    metadata_obj,
    Column("pref_id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False),
    Column("pref_name", String(40), nullable=False),
    Column("pref_value", String(100)) 
)

for table in metadata_obj.sorted_tables:
    print(table)
    
metadata_obj.create_all(engine)
    
metadatadb_obj = MetaData()
financial_info = Table(
    "financial_info",
    metadatadb_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("value", String(100), nullable=False)
)

with engine.connect() as conn:
    conn.execute(user.insert().values(
        user_name = 'Manuel',
        email_address = 'manuel.neto@gmail.com',
        nickname = 'Manuel'
        ))

    result = conn.execute(text("select * from user"))
    for row in result:
        print(row)