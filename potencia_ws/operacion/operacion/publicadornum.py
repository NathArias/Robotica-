import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class NumeroPublisher(Node):
    def __init__(self):
        super().__init__('numero_publisher')
        self.publisher_ = self.create_publisher(Int32, 'numeros', 10)
        timer_period = 1.0  # cada 1 segundo
        self.timer = self.create_timer(timer_period, self.publish_number)
        self.numero = 1

    def publish_number(self):
        msg = Int32()
        msg.data = self.numero
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: {msg.data}')
        self.numero += 1

def main(args=None):
    rclpy.init(args=args)
    node = NumeroPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
