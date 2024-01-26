import numpy as np

NUM2COLOR = {0: "white", 1: "red", 2:"blue", 3:"yellow", 4:"orange", 5:"green"} 

class Rubik:

    def __init__(self) -> None:
        self.faces = np.ones((6, 3, 3), dtype=int) * np.arange(0, 6)[:, None, None]
                             
        self.face_cur = (1, 2)

    def turn(self, dir):

        f,r = self.face_cur

        fu = self.calc_up(f, r)
        fuu = self.calc_up(fu, r)
        fuuu = self.calc_up(fuu, r)
    
        if dir == "u":
            self.faces[f][:,2], self.faces[fu][:,2], self.faces[fuu][:,2], self.faces[fuu][:,2] = self.faces[fu][:,2], self.faces[fuu][:,2], self.faces[fuuu][:,2], self.faces[f][:,2]
        else:
            self.faces[f][:,2], self.faces[fu][:,2], self.faces[fuu][:,2], self.faces[fuu][:,2] = self.faces[fuuu][:,2], self.faces[f][:,2], self.faces[fu][:,2], self.faces[fuu][:,2]


    def set_face(self, face):
        try:
            self.face = face

        except:
            raise NameError
        
    def calc_up(self, f, r):
        if r%3 == f%3:
            raise ValueError
        
        return
    