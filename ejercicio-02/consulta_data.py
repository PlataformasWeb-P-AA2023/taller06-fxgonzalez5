from sqlalchemy.orm import sessionmaker
from crear_base import Paises
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

print('Consulta 1: Presentar todos los países del continente americano')
data = session.query(Paises).filter(Paises.continente.in_(['NA','SA']))

for d in data:
    print('País: %s - Continente: %s' % (d.nombre, d.continente))


print('\nConsulta 2: Presentar los países de Asía, ordenados por el atributo Dial')
data1 = session.query(Paises).filter(Paises.continente == 'AS').order_by(Paises.dial)

for d in data1:
    print('País: %s - Continente: %s' % (d.nombre, d.continente))


print('\nConsulta 3: Presentar los lenguajes de cada país')
data2 = session.query(Paises).all()

for d in data2:
    print('País: %s - Lengaujes: %s' % (d.nombre, d.lenguajes))


print('\nConsulta 4: Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa')
data3 = session.query(Paises).filter(Paises.continente == 'EU').order_by(Paises.capital)

for d in data3:
    print('País: %s - Capital: %s - Continente: %s' % (d.nombre, d.capital, d.continente))


print('\nConsulta 5: Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".')
data4 = session.query(Paises).filter((Paises.nombre.like('%uador%')) | (Paises.capital.like('%ito%')))

for d in data4:
    print('País: %s - Capital: %s' % (d.nombre, d.capital))


# se confirman las transacciones
session.commit()
