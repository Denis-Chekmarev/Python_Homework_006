# Найти расстояние между двумя точками пространства(числа вводятся через пробел)


points = input('Input the koors of points -> ')
points = list(map(int, points.split()))
points = [ (points[x[0]] - points[x[1]]) ** 2 for x in [(0, 2), (1, 3)] ]
distance = round(sum(points)**0.5, 2)
print(distance)