from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, text


class Hero(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] | None = None


hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


engine = create_engine("sqlite:///database.db", echo=True)


SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    # session.add(hero_1)
    # session.add(hero_2)
    # session.add(hero_3)
    
    #Consulta SQL
    statement = text("SELECT * FROM hero;")

    #Execução dos Resultados
    results = session.exec(statement)

    #Fetch dos Resultados
    heroes = results.fetchall()
    
    #Imprimindo os resultados
    for hero in heroes:
       print(hero)
    session.commit()