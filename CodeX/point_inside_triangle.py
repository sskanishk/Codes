class Area:

    def Areax(self, x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2.0)

    def isInside(self, x1, y1, x2, y2, x3, y3, p1, p2):
        A = z.Areax(x1, y1, x2, y2, x3, y3)

        A1 = z.Areax(p1, p2, x2, y2, x3, y3)

        A2 = z.Areax(x1, y1, p1, p2, x3, y3)

        A3 = z.Areax(x1, y1, x2, y2, p1, p2)

        if(A == A1 + A2 + A3):
            print("Inside")
        else:
            print("Outside")

        return 0


z = Area()
z.isInside(0, 0, 20, 0, 10, 30, 10, 15)

