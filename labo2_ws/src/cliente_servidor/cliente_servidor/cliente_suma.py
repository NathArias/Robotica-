import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class ClienteSuma(Node):
    def __init__(self):
        super().__init__('cliente_suma')
        # Cliente del servicio
        self.cli = self.create_client(AddTwoInts, 'sumar_dos_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando al servicio sumar_dos_ints...')

    def send_request(self, a: int, b: int):
        req = AddTwoInts.Request()
        req.a = a
        req.b = b
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    rclpy.init(args=args)
    node = ClienteSuma()

    # Toma argumentos desde la línea de comandos o usa valores por defecto
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except (IndexError, ValueError):
        a, b = 7, 5
        node.get_logger().warn(f'Usando valores por defecto: {a}, {b}')

    resp = node.send_request(a, b)
    node.get_logger().info(f'Respuesta: {a} + {b} = {resp.sum}')

    rclpy.shutdown()


if __name__ == '__main__':
    main()
