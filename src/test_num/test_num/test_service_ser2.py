from test_interfaces.srv import AddThreeInts
from test_interfaces.srv import MinusThreeInts

import rclpy
from rclpy.node import Node

class MService(Node):
  def __init__(self):
    super().__init__('mservice2')
    self.srv = self.create_service(AddThreeInts, 'add_three_ints', self.add_three_ints_callback)
    self.srv = self.create_service(MinusThreeInts, 'minus_three_ints', self.minus_three_ints_callback)
    self.testprint = self.create_timer(1, self.testpp)

  def add_three_ints_callback(self, request, response):
    response.sum = request.a + request.b + request.c
    self.get_logger().info(f'Incoming request add/n a: {request.a}, b: {request.b}, c: {request.c}')
    return response

  def minus_three_ints_callback(self, request, response):
    response.sum = request.a - request.b - request.c
    self.get_logger().info(f'Incoming request minus/n a: {request.a}, b: {request.b}, c: {request.c}')
    return response

  def testpp(self):
    print('aaa')

def main(args=None):
  rclpy.init(args = args)
  mservice = MService()

  rclpy.spin(mservice)
  rclpy.shutdown()

if __name__ == '__main__':
  main()
