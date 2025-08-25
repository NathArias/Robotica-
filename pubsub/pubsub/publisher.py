#Creando el nodo PUBLICADOR#

import rclpy #importar la libreria de ros
from std_msgs.msg import String #el canal que enviara cadenas de texto esto varia dependiendo que tipo de datos vamos a enviar
from rclpy.node import Node #libreria node

#utilizando herencia (osea clases para el publicador)
class MiPublicador(Node):
    def __init__(self):
        super().__init__('mipublicador')
        self.publisher =  self.create_publisher(String, 'topic', 10)
        timer_pub = 0.5 #tiempo de publicacion para el nodo
        self.timer  = self.create_timer(timer_pub, self.timer_callback) #crear un timer, callback se ejecuta cuando se genera una interrupcion, en este caso cada 0.5 se generara la interrupcion
    
    def timer_callback(self):
        msg = String()
        msg.data = "HOli mundo"
        self.publisher.publish(msg)
        print("Enviando Dato: ", msg.data)
    
def main(args=None):   #funcion principal
    rclpy.init(args=args)

    publicador = MiPublicador()

    rclpy.spin(publicador) #se abre el cilco de repeticion

    publicador.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()