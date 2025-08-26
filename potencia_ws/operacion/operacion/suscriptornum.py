import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class PotenciaSubscriber(Node):
    def __init__(self):
        super().__init__('potencia_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'numeros',
            self.listener_callback,
            10)
        self.subscription  # evitar advertencia

    def listener_callback(self, msg):
        cuadrado = msg.data ** 2
        self.get_logger().info(f'Recibí {msg.data}, su potencia es {cuadrado}')

def main(args=None):
    rclpy.init(args=args)
    node = PotenciaSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
