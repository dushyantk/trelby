import pml

# character widths and general font information for each font. acquired
# from the PDF font metrics. ((width / 1000) * point_size) / 72.0 = how
# many inches wide that character is.
#
# all Courier-* fonts have characters 600 units wide.

# get the FontMetrics object for the given style
def getMetrics(style):
    # the "& 15" gets rid of the underline flag
    return _fontMetrics[style & 15]

class FontMetrics:
    def __init__(self, fontWeight, flags, bbox, italicAngle, ascent, descent,
                 capHeight, stemV, stemH, xHeight, widths):

        # character widths in an array of 256 integers, or None for the
        # Courier fonts.
        self.widths = widths
        
        # see the PDF spec for the details on what these are.
        self.fontWeight = fontWeight
        self.flags = flags
        self.bbox = bbox
        self.italicAngle = italicAngle
        self.ascent = ascent
        self.descent = descent
        self.capHeight = capHeight
        self.stemV = stemV
        self.stemH = stemH
        self.xHeight = xHeight

    # calculate width of 'text' in 'size', and return it in 1/72 inch
    # units.
    def getTextWidth(self, text, size):
        widths = self.widths

        # Courier
        if not widths:
            return 0.6 * (size * len(text))

        total = 0
        for ch in text:
            total += widths[ord(ch)]

        return (total / 1000.0) * size

_fontMetrics = {

    pml.COURIER : FontMetrics(
    fontWeight = 400, flags = 35, bbox = (-23, -250, 715, 805),
    italicAngle = 0, ascent = 629, descent = -157, capHeight = 562,
    stemV = 51, stemH = 51, xHeight = 426, widths = None),
                              
    pml.COURIER | pml.BOLD : FontMetrics(
    fontWeight = 700, flags = 35, bbox = (-113, -250, 749, 801),
    italicAngle = 0, ascent = 629, descent = -157, capHeight = 562,
    stemV = 106, stemH = 84, xHeight = 439, widths = None),
    
    pml.COURIER | pml.ITALIC : FontMetrics(
    fontWeight = 400, flags = 99, bbox = (-27, -250, 849, 805),
    italicAngle = -12, ascent = 629, descent = -157, capHeight = 562,
    stemV = 51, stemH = 51, xHeight = 426, widths = None),
    
    pml.COURIER | pml.BOLD | pml.ITALIC : FontMetrics(
    fontWeight = 700, flags = 99, bbox = (-57, -250, 869, 801),
    italicAngle = -12, ascent = 629, descent = -157, capHeight = 562,
    stemV = 106, stemH = 84, xHeight = 439, widths = None),


    pml.HELVETICA : FontMetrics(
    fontWeight = 400, flags = 32, bbox = (-166, -225, 1000, 931),
    italicAngle = 0, ascent = 718, descent = -207, capHeight = 718,
    stemV = 88, stemH = 76, xHeight = 523, widths = [
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    278, 278, 355, 556, 556, 889, 667, 191,
    333, 333, 389, 584, 278, 333, 278, 278,
    556, 556, 556, 556, 556, 556, 556, 556,
    556, 556, 278, 278, 584, 584, 584, 556,
    1015, 667, 667, 722, 722, 667, 611, 778,
    722, 278, 500, 667, 556, 833, 722, 778,
    667, 778, 722, 667, 611, 722, 667, 944,
    667, 667, 611, 278, 278, 278, 469, 556,
    333, 556, 556, 500, 556, 556, 278, 556,
    556, 222, 222, 500, 222, 833, 556, 556,
    556, 556, 333, 500, 278, 556, 500, 722,
    500, 500, 500, 334, 260, 334, 584, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 333, 556, 556, 556, 556, 260, 556,
    333, 737, 370, 556, 584, 545, 737, 333,
    400, 584, 333, 333, 333, 556, 537, 278,
    333, 333, 365, 556, 834, 834, 834, 611,
    667, 667, 667, 667, 667, 667, 1000, 722,
    667, 667, 667, 667, 278, 278, 278, 278,
    722, 722, 778, 778, 778, 778, 778, 584,
    778, 722, 722, 722, 722, 667, 667, 611,
    556, 556, 556, 556, 556, 556, 889, 500,
    556, 556, 556, 556, 278, 278, 278, 278,
    556, 556, 556, 556, 556, 556, 556, 584,
    611, 556, 556, 556, 556, 500, 556, 500
    ]),
    
    pml.HELVETICA | pml.BOLD : FontMetrics(
    fontWeight = 700, flags = 32, bbox = (-170, -228, 1003, 962),
    italicAngle = 0, ascent = 718, descent = -207, capHeight = 718,
    stemV = 140, stemH = 118, xHeight = 532, widths = [
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    278, 333, 474, 556, 556, 889, 722, 238,
    333, 333, 389, 584, 278, 333, 278, 278,
    556, 556, 556, 556, 556, 556, 556, 556,
    556, 556, 333, 333, 584, 584, 584, 611,
    975, 722, 722, 722, 722, 667, 611, 778,
    722, 278, 556, 722, 611, 833, 722, 778,
    667, 778, 722, 667, 611, 722, 667, 944,
    667, 667, 611, 333, 278, 333, 584, 556,
    333, 556, 611, 556, 611, 556, 333, 611,
    611, 278, 278, 556, 278, 889, 611, 611,
    611, 611, 389, 556, 333, 611, 556, 778,
    556, 556, 500, 389, 280, 389, 584, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 333, 556, 556, 556, 556, 280, 556,
    333, 737, 370, 556, 584, 564, 737, 333,
    400, 584, 333, 333, 333, 611, 556, 278,
    333, 333, 365, 556, 834, 834, 834, 611,
    722, 722, 722, 722, 722, 722, 1000, 722,
    667, 667, 667, 667, 278, 278, 278, 278,
    722, 722, 778, 778, 778, 778, 778, 584,
    778, 722, 722, 722, 722, 667, 667, 611,
    556, 556, 556, 556, 556, 556, 889, 556,
    556, 556, 556, 556, 278, 278, 278, 278,
    611, 611, 611, 611, 611, 611, 611, 584,
    611, 611, 611, 611, 611, 556, 611, 556,
    ]),
    
    pml.HELVETICA | pml.ITALIC : FontMetrics(
    fontWeight = 400, flags = 96, bbox = (-170, -225, 1116, 931),
    italicAngle = -12, ascent = 718, descent = -207, capHeight = 718,
    stemV = 88, stemH = 76, xHeight = 523, widths = [
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    278, 278, 355, 556, 556, 889, 667, 191,
    333, 333, 389, 584, 278, 333, 278, 278,
    556, 556, 556, 556, 556, 556, 556, 556,
    556, 556, 278, 278, 584, 584, 584, 556,
    1015, 667, 667, 722, 722, 667, 611, 778,
    722, 278, 500, 667, 556, 833, 722, 778,
    667, 778, 722, 667, 611, 722, 667, 944,
    667, 667, 611, 278, 278, 278, 469, 556,
    333, 556, 556, 500, 556, 556, 278, 556,
    556, 222, 222, 500, 222, 833, 556, 556,
    556, 556, 333, 500, 278, 556, 500, 722,
    500, 500, 500, 334, 260, 334, 584, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 545, 545, 545, 545, 545, 545, 545,
    545, 333, 556, 556, 556, 556, 260, 556,
    333, 737, 370, 556, 584, 545, 737, 333,
    400, 584, 333, 333, 333, 556, 537, 278,
    333, 333, 365, 556, 834, 834, 834, 611,
    667, 667, 667, 667, 667, 667, 1000, 722,
    667, 667, 667, 667, 278, 278, 278, 278,
    722, 722, 778, 778, 778, 778, 778, 584,
    778, 722, 722, 722, 722, 667, 667, 611,
    556, 556, 556, 556, 556, 556, 889, 500,
    556, 556, 556, 556, 278, 278, 278, 278,
    556, 556, 556, 556, 556, 556, 556, 584,
    611, 556, 556, 556, 556, 500, 556, 500,
    ]),
    
    pml.HELVETICA | pml.BOLD | pml.ITALIC : FontMetrics(
    fontWeight = 700, flags = 96, bbox = (-174, -228, 1114, 962),
    italicAngle = -12, ascent = 718, descent = -207, capHeight = 718,
    stemV = 140, stemH = 118, xHeight = 532, widths = [
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    278, 333, 474, 556, 556, 889, 722, 238,
    333, 333, 389, 584, 278, 333, 278, 278,
    556, 556, 556, 556, 556, 556, 556, 556,
    556, 556, 333, 333, 584, 584, 584, 611,
    975, 722, 722, 722, 722, 667, 611, 778,
    722, 278, 556, 722, 611, 833, 722, 778,
    667, 778, 722, 667, 611, 722, 667, 944,
    667, 667, 611, 333, 278, 333, 584, 556,
    333, 556, 611, 556, 611, 556, 333, 611,
    611, 278, 278, 556, 278, 889, 611, 611,
    611, 611, 389, 556, 333, 611, 556, 778,
    556, 556, 500, 389, 280, 389, 584, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 564, 564, 564, 564, 564, 564, 564,
    564, 333, 556, 556, 556, 556, 280, 556,
    333, 737, 370, 556, 584, 564, 737, 333,
    400, 584, 333, 333, 333, 611, 556, 278,
    333, 333, 365, 556, 834, 834, 834, 611,
    722, 722, 722, 722, 722, 722, 1000, 722,
    667, 667, 667, 667, 278, 278, 278, 278,
    722, 722, 778, 778, 778, 778, 778, 584,
    778, 722, 722, 722, 722, 667, 667, 611,
    556, 556, 556, 556, 556, 556, 889, 556,
    556, 556, 556, 556, 278, 278, 278, 278,
    611, 611, 611, 611, 611, 611, 611, 584,
    611, 611, 611, 611, 611, 556, 611, 556,
    ]),


    pml.TIMES_ROMAN : FontMetrics(
    fontWeight = 400, flags = 34, bbox = (-168, -218, 1000, 898),
    italicAngle = 0, ascent = 683, descent = -217, capHeight = 662,
    stemV = 84, stemH = 28, xHeight = 450, widths = [
    516, 516, 516, 516, 516, 516, 516, 516,
    516, 516, 516, 516, 516, 516, 516, 516,
    516, 516, 516, 516, 516, 516, 516, 516,
    516, 516, 516, 516, 516, 516, 516, 516,
    250, 333, 408, 500, 500, 833, 778, 180,
    333, 333, 500, 564, 250, 333, 250, 278,
    500, 500, 500, 500, 500, 500, 500, 500,
    500, 500, 278, 278, 564, 564, 564, 444,
    921, 722, 667, 667, 722, 611, 556, 722,
    722, 333, 389, 722, 611, 889, 722, 722,
    556, 722, 667, 556, 611, 722, 722, 944,
    722, 722, 611, 333, 278, 333, 469, 500,
    333, 444, 500, 444, 500, 444, 333, 500,
    500, 278, 278, 500, 278, 778, 500, 500,
    500, 500, 333, 389, 278, 500, 500, 722,
    500, 500, 444, 480, 200, 480, 541, 516,
    516, 516, 516, 516, 516, 516, 516, 516,
    516, 516, 516, 516, 516, 516, 516, 516,
    516, 516, 516, 516, 516, 516, 516, 516,
    516, 516, 516, 516, 516, 516, 516, 516,
    516, 333, 500, 500, 500, 500, 200, 500,
    333, 760, 276, 500, 564, 516, 760, 333,
    400, 564, 300, 300, 333, 500, 453, 250,
    333, 300, 310, 500, 750, 750, 750, 444,
    722, 722, 722, 722, 722, 722, 889, 667,
    611, 611, 611, 611, 333, 333, 333, 333,
    722, 722, 722, 722, 722, 722, 722, 564,
    722, 722, 722, 722, 722, 722, 556, 500,
    444, 444, 444, 444, 444, 444, 667, 444,
    444, 444, 444, 444, 278, 278, 278, 278,
    500, 500, 500, 500, 500, 500, 500, 564,
    500, 500, 500, 500, 500, 500, 500, 500,
    ]),

    pml.TIMES_ROMAN | pml.BOLD : FontMetrics(
    fontWeight = 700, flags = 34, bbox = (-168, -218, 1000, 935),
    italicAngle = 0, ascent = 683, descent = -217, capHeight = 676,
    stemV = 139, stemH = 44, xHeight = 461, widths = [
    540, 540, 540, 540, 540, 540, 540, 540,
    540, 540, 540, 540, 540, 540, 540, 540,
    540, 540, 540, 540, 540, 540, 540, 540,
    540, 540, 540, 540, 540, 540, 540, 540,
    250, 333, 555, 500, 500, 1000, 833, 278,
    333, 333, 500, 570, 250, 333, 250, 278,
    500, 500, 500, 500, 500, 500, 500, 500,
    500, 500, 333, 333, 570, 570, 570, 500,
    930, 722, 667, 722, 722, 667, 611, 778,
    778, 389, 500, 778, 667, 944, 722, 778,
    611, 778, 722, 556, 667, 722, 722, 1000,
    722, 722, 667, 333, 278, 333, 581, 500,
    333, 500, 556, 444, 556, 444, 333, 500,
    556, 278, 333, 556, 278, 833, 556, 500,
    556, 556, 444, 389, 333, 556, 500, 722,
    500, 500, 444, 394, 220, 394, 520, 540,
    540, 540, 540, 540, 540, 540, 540, 540,
    540, 540, 540, 540, 540, 540, 540, 540,
    540, 540, 540, 540, 540, 540, 540, 540,
    540, 540, 540, 540, 540, 540, 540, 540,
    540, 333, 500, 500, 500, 500, 220, 500,
    333, 747, 300, 500, 570, 540, 747, 333,
    400, 570, 300, 300, 333, 556, 540, 250,
    333, 300, 330, 500, 750, 750, 750, 500,
    722, 722, 722, 722, 722, 722, 1000, 722,
    667, 667, 667, 667, 389, 389, 389, 389,
    722, 722, 778, 778, 778, 778, 778, 570,
    778, 722, 722, 722, 722, 722, 611, 556,
    500, 500, 500, 500, 500, 500, 722, 444,
    444, 444, 444, 444, 278, 278, 278, 278,
    500, 556, 500, 500, 500, 500, 500, 570,
    500, 556, 556, 556, 556, 500, 556, 500,
    ]),

    pml.TIMES_ROMAN | pml.ITALIC : FontMetrics(
    fontWeight = 400, flags = 98, bbox = (-169, -217, 1010, 883),
    italicAngle = -15.5, ascent = 683, descent = -217, capHeight = 653,
    stemV = 76, stemH = 32, xHeight = 441, widths = [
    513, 513, 513, 513, 513, 513, 513, 513,
    513, 513, 513, 513, 513, 513, 513, 513,
    513, 513, 513, 513, 513, 513, 513, 513,
    513, 513, 513, 513, 513, 513, 513, 513,
    250, 333, 420, 500, 500, 833, 778, 214,
    333, 333, 500, 675, 250, 333, 250, 278,
    500, 500, 500, 500, 500, 500, 500, 500,
    500, 500, 333, 333, 675, 675, 675, 500,
    920, 611, 611, 667, 722, 611, 611, 722,
    722, 333, 444, 667, 556, 833, 667, 722,
    611, 722, 611, 500, 556, 722, 611, 833,
    611, 556, 556, 389, 278, 389, 422, 500,
    333, 500, 500, 444, 500, 444, 278, 500,
    500, 278, 278, 444, 278, 722, 500, 500,
    500, 500, 389, 389, 278, 500, 444, 667,
    444, 444, 389, 400, 275, 400, 541, 513,
    513, 513, 513, 513, 513, 513, 513, 513,
    513, 513, 513, 513, 513, 513, 513, 513,
    513, 513, 513, 513, 513, 513, 513, 513,
    513, 513, 513, 513, 513, 513, 513, 513,
    513, 389, 500, 500, 500, 500, 275, 500,
    333, 760, 276, 500, 675, 513, 760, 333,
    400, 675, 300, 300, 333, 500, 523, 250,
    333, 300, 310, 500, 750, 750, 750, 500,
    611, 611, 611, 611, 611, 611, 889, 667,
    611, 611, 611, 611, 333, 333, 333, 333,
    722, 667, 722, 722, 722, 722, 722, 675,
    722, 722, 722, 722, 722, 556, 611, 500,
    500, 500, 500, 500, 500, 500, 667, 444,
    444, 444, 444, 444, 278, 278, 278, 278,
    500, 500, 500, 500, 500, 500, 500, 675,
    500, 500, 500, 500, 500, 444, 500, 444,
    ]),

    pml.TIMES_ROMAN | pml.BOLD | pml.ITALIC : FontMetrics(
    fontWeight = 700, flags = 98, bbox = (-200, -218, 996, 921),
    italicAngle = -15, ascent = 683, descent = -217, capHeight = 669,
    stemV = 121, stemH = 42, xHeight = 462, widths = [
    523, 523, 523, 523, 523, 523, 523, 523,
    523, 523, 523, 523, 523, 523, 523, 523,
    523, 523, 523, 523, 523, 523, 523, 523,
    523, 523, 523, 523, 523, 523, 523, 523,
    250, 389, 555, 500, 500, 833, 778, 278,
    333, 333, 500, 570, 250, 333, 250, 278,
    500, 500, 500, 500, 500, 500, 500, 500,
    500, 500, 333, 333, 570, 570, 570, 500,
    832, 667, 667, 667, 722, 667, 667, 722,
    778, 389, 500, 667, 611, 889, 722, 722,
    611, 722, 667, 556, 611, 722, 667, 889,
    667, 611, 611, 333, 278, 333, 570, 500,
    333, 500, 500, 444, 500, 444, 333, 500,
    556, 278, 278, 500, 278, 778, 556, 500,
    500, 500, 389, 389, 278, 556, 444, 667,
    500, 444, 389, 348, 220, 348, 570, 523,
    523, 523, 523, 523, 523, 523, 523, 523,
    523, 523, 523, 523, 523, 523, 523, 523,
    523, 523, 523, 523, 523, 523, 523, 523,
    523, 523, 523, 523, 523, 523, 523, 523,
    523, 389, 500, 500, 500, 500, 220, 500,
    333, 747, 266, 500, 606, 523, 747, 333,
    400, 570, 300, 300, 333, 576, 500, 250,
    333, 300, 300, 500, 750, 750, 750, 500,
    667, 667, 667, 667, 667, 667, 944, 667,
    667, 667, 667, 667, 389, 389, 389, 389,
    722, 722, 722, 722, 722, 722, 722, 570,
    722, 722, 722, 722, 722, 611, 611, 500,
    500, 500, 500, 500, 500, 500, 722, 444,
    444, 444, 444, 444, 278, 278, 278, 278,
    500, 556, 500, 500, 500, 500, 500, 570,
    500, 556, 556, 556, 556, 444, 500, 444,
    ])
    }
