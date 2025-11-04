class Insect():
    insect_num = 0
    def __init__(self, insect_num, sting, cage = 'A'):
        self._insect_num = insect_num
        insect_num += 1
        self._sting = sting
        self._cage = cage

class Spider(Insect):
    def __init__(self, insect_num, cage = 'A'):
        super().__init__(insect_num, True, cage)

class Grasshopper(Insect):
    def __init__(self, region, insect_num, cage = 'A'):
        super().__init__(insect_num, False, cage)
        self._region = region

class Butterfly(Insect):
    def __init__(self, color, insect_num, cage = 'A'):
        super().__init__(insect_num, False, cage)
        self._color = color

