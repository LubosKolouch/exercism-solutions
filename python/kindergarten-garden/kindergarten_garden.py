import numpy as np


class Garden:

    def __init__(self, diagram,
                 students=["Alice", "Bob", "Charlie", "David", "Eve",
                           "Fred", "Ginny", "Harriet", "Ileana", "Joseph",
                           "Kincaid", "Larry"]):

        self.diagram = diagram.replace('\n', '')
        m_arr = []
        self.transl = {"V": "Violets", "R": "Radishes",
                       "C": "Clover", "G": "Grass"}

        for fl in self.diagram:
            m_arr.append(self.transl[fl])

        self.arr = np.array(m_arr)

        students = sorted(students)

        self.arr = np.reshape(self.arr, (2, -1))
        self.dictionary = dict()
        pos = pos2 = 0

        while pos < len(self.arr[0]):
            arr_sl = self.arr[:2, pos:pos+2]
            arr_sl = list(np.reshape(arr_sl, (-1)))
            self.dictionary[students[pos2]] = list(arr_sl)
            pos += 2
            pos2 += 1

    def plants(self, student):

        return list(self.dictionary[student])


if __name__ == '__main__':
    # g = Garden("VCRRGVRG\nRVGCCGCV",
    #             students=["Samantha", "Patricia", "Xander", "Roger"])
    g = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
    print(g.diagram)
    print(g.dictionary)
