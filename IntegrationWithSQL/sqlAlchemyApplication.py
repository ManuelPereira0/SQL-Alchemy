from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import *

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    #Atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)
    
    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"
    

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address =Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    
    user = relationship(
        "User", back_populates="address"
        )
    
    def __repr__(self):
        return f"Address(id={self.id}, email={self.email_address})"
    

# Conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# inspect, tem a função de investigar o esquema do banco de dados
insp = inspect(engine)

# Printa o nome das tabelas
print(insp.get_table_names())

#Criando sessão com a engine

with Session(engine) as session:
    manuel = User(
        name = 'Manuel',
        fullname = "Manuel Pereira",
        address = [Address(email_address = "manuel.neto@gmail.com"),
                   Address(email_address = "manuel.pereira@gmail.com")]
    )
    
    duda = User(
        name = "Maria",
        fullname = "Maria",
        address = [Address(email_address = "maria123@gmail.com")]
    )
    
    fabiana = User(
        name = "Fabiana",
        fullname = "Fabiana Pereira"
    )
    
    # Enviando para o db (persistência de dados)
    session.add_all([manuel, duda, fabiana])
    
    session.commit()
    
# Realizando um select na tabela User, onde o nome é Manuel, pode colocar mais de um nome no select: ["Manuel", "Duda"] 
stmt = select(User).where(User.name.in_(["Manuel"]))
for user in session.scalars(stmt):
    #print(user)
    pass

# Realizando um select na tabela Address, onde o user_id é 1, pode colocar mais de um nome no select: [1, 2]
stmt_address = select(Address).where(Address.user_id.in_([1]))
for address in session.scalars(stmt_address):
    #print(address)
    pass

# Realizando um select ordenado pelo fullname da tabela User, em ordem decrescente
stmt_order = select(User).order_by(User.fullname.desc())
for result in session.scalars(stmt_order):
    #print(result)
    pass


# Realizando um selct com join nas 2 tabelas
stmt_join = select(User.fullname, Address.email_address).join_from(User, Address)
for result in session.scalars(stmt_join):
    #print(result)
    pass

# Para realizar a busca e trazer todas as informações
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for result in results:
    #print(result)
    pass

# Mostrando o total de instâncias dentro de User
stmt_count = select(func.count("*")).select_from(User)
for result in session.scalars(stmt_count):
    #print(result)
    pass
