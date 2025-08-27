import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class ServidorSuma(Node):
    def __init__(self):
        super().__init__('servidor_suma')
        # nombre del servicio: /sumar_dos_ints
        self.srv = self.create_service(AddTwoInts, 'sumar_dos_ints', self.callback)

    def callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Recibí: a={request.a}, b={request.b} -> sum={response.sum}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ServidorSuma()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
