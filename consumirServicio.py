from zeep import Client

url = "http://localhost:8000/?wsdl"
cliente = Client(url)

celsius = int(input("Ingrese los Grados Celsius: "))
resultado = cliente.service.celsius_a_fahrenheit(celsius)

# fahrenheit = int(input("Ingrese los Grados Fahrenheit: "))
# resultado = cliente.service.fahrenheit_a_celsius(fahrenheit)

print(f"{celsius} Celsius es igual a {resultado} Fahrenheit")
