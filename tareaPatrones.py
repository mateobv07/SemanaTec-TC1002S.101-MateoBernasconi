import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("peso_estatura_genero.csv")

modelo = LinearRegression()
x = df['Estatura'].to_numpy(dtype='float').reshape(-1, 1)
y = df['Peso'].to_numpy(dtype='float')

modelo.fit(x, y)

print("Score:", modelo.score(x, y))

b0 = modelo.intercept_
print("b0:", b0)
b = modelo.coef_
print("b:", b)

# y_ = b0 + b[0]*x
y_ = modelo.predict(x)
print("y:", y_)

#fig = plt.figure()
# plt.scatter(df['Estatura'], df['Peso'], marker='*')
# plt.plot(x, y_, c='r')
# plt.show()

""" Modelo Cuadratico """
df.Peso = df.Peso**2
# print("df peso^2", df)

transformador = PolynomialFeatures()
transformador.fit(x)

x_ = transformador.transform(x)
# print("x:", x_)

modelo_2 = LinearRegression()
modelo_2.fit(x_, y)
modelo_2.intercept_
modelo_2.coef_

print("Score modelo 2:", modelo_2.score(x_, y))

y_2 = modelo_2.predict(x_)


""" Graficar ambos modelos """
fig = plt.figure()
plt.scatter(df['Estatura'], df['Peso'], marker='*')
plt.plot(x, y_2, c='r')
plt.show()
