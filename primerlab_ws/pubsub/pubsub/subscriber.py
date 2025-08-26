#Creando el nodo SUSCRIPTOR#

import rclpy #importar la libreria de ros
from std_msgs.msg import String #el canal que enviara cadenas de texto esto varia dependiendo que tipo de datos vamos a enviar
from rclpy.node import Node #libreria node

#utilizando herencia (osea clases para el publicador)
class MiSubscriptor(Node):
    def __init__(self):
        super().__init__('subscriptor')
        self.subcriptor =  self.create_subscription(String, 'topic', self.callback, 10)

        self.subcriptor

    def callback(self, msg):
        print("Me llego el dato: ", msg.data)
    
def main(args=None):   #funcion principal
    rclpy.init(args=args)

    subscriptor = MiSubscriptor()

    rclpy.spin(subscriptor ) #se abre el cilco de repeticion

    subscriptor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()