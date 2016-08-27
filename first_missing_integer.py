"""
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Algorithm: loop through the array. If the ith elem is positive, swap it with the element
in the array thats taking the place of where that particular ith elem should be. For example,
for array [3,4,-1,1], 3 should be in the 2nd place for that array. So, swap 3 with -1. Then, increment i and 
repeat steps for the rest of the list. At the end, loop through 'sorted' array and then return the first
elem that's not 1 greater than its index. E.g. in the example array, in the end it'll look like 
[1,-1,3,4]. 2 will be returned bc -1 != 1.

O(N) time 
O(1) space
"""

import unittest


def first_missing_int(arr):
    i = 0
    while i < len(arr):
        if arr[i] > 0 and arr[i] - 1 < len(arr) and arr[i] != arr[arr[i] - 1]:
            # print "swap"
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
        else:
            # print "increment i"
            i += 1

    for i, integer in enumerate(arr):
        if integer != i + 1:
            return i + 1
    return len(arr) + 1


class TestFirstMissing(unittest.TestCase):

    def test_1(self):
        a = [1, 2, 0]
        result = first_missing_int(a)
        expected = 3
        self.assertEqual(result, expected)

    def test_2(self):
        a = [-1, 1]
        result = first_missing_int(a)
        expected = 2
        self.assertEqual(result, expected)

    def test_3(self):
        a = [3, 4, -1, 1]
        result = first_missing_int(a)
        expected = 2
        self.assertEqual(result, expected)

    def test_4(self):
        a = [-8, -7, -6]
        result = first_missing_int(a)
        expected = 1
        self.assertEqual(result, expected)

    def test_5(self):
        a = [894, 669, 852, 722, 778, 169, 247, 927, 875, 858, 396, 760, 318, 409, 640, 976, 419, 600, 711, 610, 864, 655, 859, 567, 7, 487, 953, 632, 544, 158, 53, 919, 45, 699, 493, 414, 586, 460, 339, 540, 12, 948, 515, 16, 116, 772, 529, 606, 684, 214, 724, 811, 925, 703, 454, 592, 330, 143, 41, 401, 570, 326, 885, 943, 836, 252, 119, 773, 768, 447, 581, 237, 380, 182, 457, 868, 667, 109, 702, 692,
             542, 517, 966, 583, 983, 273, 641, 691, 985, 115, 574, 216, 372, 298, 411, 784, 95, 251, 389, 354, 964, 430, 991, 799, 824, 826, 714, 238, 967, 977, 291, 545, 355, 287, 425, 305, 118, 902, 479, 388, 19, 61, 301, 782, 688, 893, 673, 195, 971, 693, 797, 996, 3, 314, 353, 103, 391, 905, 316, 734, 54, 939, 648, 526, 448, 255, 690, 114, 715, 148, 376, 878, 483, 408, 804, 585, 79, 644, 621, 221, 345]
        result = first_missing_int(a)
        expected = 1
        self.assertEqual(result, expected)

    def test_6(self):
        a = [110, 483, 137, 881, 946, 231, 378, 449, 68, 518, 476, 898, 685, 384, 839, 553, 304, 689, 467, 292, 414, 679, 301, 30, 457, 300, 93, 427, 619, 439, 4, 348, 714, 966, 142, 538, 484, 827, 237, 447, 442, 133, 771, 578, 190, 782, 182, 23, 192, 177, 164, 276, 273, 45, 624, 12, 354, 938, 472, 899, 42, 612, 813, 386, 380, 63, 136, 589, 334, 349, 757, 999, 526, 156, 803, 991, 961, 535, 297, 336, 409, 59, 558, 678, 755, 720, 88, 906, 571, 770, 673, 581, 399, 868, 446, 123, 707, 643, 548, 226, 854, 830, 423, 621, 14, 767, 801, 651, 932, 492, 462, 321, 250, 591, 208, 862, 413, 418, 724, 746, 388, 925, 882, 808, 543, 171, 737, 994, 283, 950, 528, 443, 853, 671, 699, 19, 344, 365, 134, 818, 531, 48, 464, 124, 377, 379, 792, 387, 11, 796, 159, 65, 842, 109, 631, 600, 987, -3, 263, 28, 833, 779, 100, 73, 790, 179, 889, 557, 887, 455, 502, 511, 907, 686, 713, 864, 271, 372, 850, 534, 347, 649, 21, 169, 712, 435, 1, 222, 509, 866, 628, 604, 885, 385, 896, 498, 964, 598, 508,
             575, 893, 294, 520, 918, 729, 789, 772, 660, 87, 569, 677, 602, 962, 217, 69, 648, 72, 331, 749, 637, 180, 489, 733, 481, 393, 40, 274, 320, 113, 930, 633, 516, 878, 835, 754, 126, 15, 593, 338, 494, 972, 603, 34, 739, 947, 592, 886, 583, 127, 172, 675, 975, 232, 394, 763, 92, 512, 616, 983, 856, 955, 166, 157, 608, 218, 56, 66, 696, 310, 933, 185, 563, 647, 960, 323, 727, 471, 397, 367, 582, 223, 369, 759, 706, 35, 588, 478, 317, 564, 768, 904, 149, 202, 165, 695, 985, 731, 486, 312, 561, 466, 197, 245, 980, 979, 620, 774, 438, 193, 146, 653, 468, 963, 485, 178, 29, 434, 272, 296, 700, 549, 181, 586, 595, 410, 108, 91, 640, 175, 750, 490, 20, 101, 879, 74, 798, 910, 611, 187, 286, 997, 138, 488, 901, 154, 267, 403, 122, 572, 787, 942, 391, 525, 176, 383, 1000, 458, 24, 780, 691, 738, 151, 170, 351, 441, 776, 453, 590, 545, 139, 859, 461, 970, 491, 785, 969, 670, 570, 219, 99, 353, 723, 470, 716, 249, 115, 680, 501, 128, 851, 9, 120, 256, 820, 114, 416, 329]
        result = first_missing_int(a)
        expected = 2
        self.assertEqual(result, expected)

    def test_7(self):
        a = [1]
        result = first_missing_int(a)
        expected = 2
        self.assertEqual(result, expected)

    def test_8(self):
        a = [1, 2, 3, 4, 5, 6]
        result = first_missing_int(a)
        expected = 7
        self.assertEqual(result, expected)

    def test_9(self):
        a = [5, 6, 7]
        result = first_missing_int(a)
        expected = 1
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
