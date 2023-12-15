from spyne import Application, rpc, ServiceBase, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class ServicioConvertidorTemperatura(ServiceBase):
    @rpc(Float, _returns=Float)
    def celsius_a_fahrenheit(ctx, celsius):
        return (celsius * 9 / 5) + 32

    @rpc(Float, _returns=Float)
    def fahrenheit_a_celsius(ctx, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

aplicacion = Application([ServicioConvertidorTemperatura],
                         tns='convertidor_temperatura',
                         in_protocol=Soap11(validator='lxml'),
                         out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    aplicacion_wsgi = WsgiApplication(aplicacion)
    servidor = make_server('localhost', 8000, aplicacion_wsgi)
    print("Servicio escuchando en http://localhost:8000/")
    servidor.serve_forever()
