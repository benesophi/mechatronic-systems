# @author Lucas Bosso de Mello (lucasbmello@usp.br)
# @brief
# @date 22/04/2026

import numpy as np
import roboticstoolbox as rtb

D2R = np.pi / 180

class Manipulator:
    def __init__(self):
        self.init_manipulator()
        self.qi = [0 * D2R, 0 * D2R, 0 * D2R]
       
    def init_manipulator(self):
        self.robot = rtb.DHRobot([
            rtb.RevoluteDH( d = 0.1, a = 0.0,  alpha = -np.pi / 2),
            rtb.RevoluteDH( d = 0.0, a = 0.1,  alpha =  0.0      ),
            rtb.RevoluteDH( d = 0.0, a = 0.05, alpha =  0.0      )
        ])

def main():
    rb = Manipulator()
    rb.robot.plot(rb.qi, block=True)

if __name__ == '__main__':
    main()