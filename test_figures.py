import unittest
import math

import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_negative_radius_area(self):
        with self.assertRaises(ValueError):
            circle.area(-5)

    def test_string_radius_area(self):
        with self.assertRaises(TypeError):
            circle.area("5")

    def test_none_radius_area(self):
        with self.assertRaises(TypeError):
            circle.area(None)

    def test_list_radius_area(self):
        with self.assertRaises(TypeError):
            circle.area([5])

    def test_int_radius_area1(self):
        res = circle.area(1)
        self.assertAlmostEqual(res, math.pi * 1**2, 5)

    def test_int_radius_area2(self):
        res = circle.area(58)
        self.assertAlmostEqual(res, math.pi * 58**2, 5)

    def test_int_radius_area3(self):
        res = circle.area(289)
        self.assertAlmostEqual(res, math.pi * 289**2, 5)

    def test_int_radius_area4(self):
        res = circle.area(500)
        self.assertAlmostEqual(res, math.pi * 500**2, 5)

    def test_int_radius_area5(self):
        res = circle.area(1007)
        self.assertAlmostEqual(res, math.pi * 1007**2, 5)

    def test_int_radius_area6(self):
        res = circle.area(2567)
        self.assertAlmostEqual(res, math.pi * 2567**2, 5)

    def test_int_radius_area7(self):
        res = circle.area(4321)
        self.assertAlmostEqual(res, math.pi * 4321**2, 5)

    def test_int_radius_area8(self):
        res = circle.area(6092)
        self.assertAlmostEqual(res, math.pi * 6092**2, 5)

    def test_int_radius_area9(self):
        res = circle.area(8345)
        self.assertAlmostEqual(res, math.pi * 8345**2, 5)

    def test_int_radius_area10(self):
        res = circle.area(10784)
        self.assertAlmostEqual(res, math.pi * 10784**2, 5)

    def test_int_radius_area11(self):
        res = circle.area(14623)
        self.assertAlmostEqual(res, math.pi * 14623**2, 5)

    def test_int_radius_area12(self):
        res = circle.area(18939)
        self.assertAlmostEqual(res, math.pi * 18939**2, 5)

    def test_int_radius_area13(self):
        res = circle.area(35625)
        self.assertAlmostEqual(res, math.pi * 35625**2, 5)

    def test_int_radius_area14(self):
        res = circle.area(43001)
        self.assertAlmostEqual(res, math.pi * 43001**2, 5)

    def test_int_radius_area15(self):
        res = circle.area(58923)
        self.assertAlmostEqual(res, math.pi * 58923**2, 5)

    def test_double_radius_area1(self):
        res = circle.area(12.753246561241234)
        self.assertAlmostEqual(res, math.pi * 12.753246561241234**2, 5)

    def test_double_radius_area2(self):
        res = circle.area(134.562038465925692)
        self.assertAlmostEqual(res, math.pi * 134.562038465925692**2, 5)

    def test_double_radius_area3(self):
        res = circle.area(567.891739416519531)
        self.assertAlmostEqual(res, math.pi * 567.891739416519531**2, 5)

    def test_double_radius_area4(self):
        res = circle.area(1024.35789231542789)
        self.assertAlmostEqual(res, math.pi * 1024.35789231542789**2, 5)

    def test_double_radius_area5(self):
        res = circle.area(1500.78134680414935)
        self.assertAlmostEqual(res, math.pi * 1500.78134680414935**2, 5)

    def test_double_radius_area6(self):
        res = circle.area(2345.67053427841038)
        self.assertAlmostEqual(res, math.pi * 2345.67053427841038**2, 5)

    def test_double_radius_area7(self):
        res = circle.area(3456.91059813042514)
        self.assertAlmostEqual(res, math.pi * 3456.91059813042514**2, 5)

    def test_double_radius_area8(self):
        res = circle.area(4567.23973410489652)
        self.assertAlmostEqual(res, math.pi * 4567.23973410489652**2, 5)

    def test_double_radius_area9(self):
        res = circle.area(5678.45342596725737)
        self.assertAlmostEqual(res, math.pi * 5678.45342596725737**2, 5)

    def test_double_radius_area10(self):
        res = circle.area(6789.12034979652916)
        self.assertAlmostEqual(res, math.pi * 6789.12034979652916**2, 5)

    def test_double_radius_area11(self):
        res = circle.area(7890.56147914145618)
        self.assertAlmostEqual(res, math.pi * 7890.56147914145618**2, 5)

    def test_double_radius_area12(self):
        res = circle.area(8765.43193465651073)
        self.assertAlmostEqual(res, math.pi * 8765.43193465651073**2, 5)

    def test_double_radius_area13(self):
        res = circle.area(11876.54862458205611)
        self.assertAlmostEqual(res, math.pi * 11876.54862458205611**2, 5)

    def test_double_radius_area14(self):
        res = circle.area(22345.6736726898604)
        self.assertAlmostEqual(res, math.pi * 22345.6736726898604**2, 5)

    def test_double_radius_area15(self):
        res = circle.area(53456.7814562352622)
        self.assertAlmostEqual(res, math.pi * 53456.7814562352622**2, 5)

    def test_big_double_radius_area1(self):
        res = circle.area(123456.78901234567)
        self.assertAlmostEqual(res, math.pi * 123456.78901234567**2, 5)

    def test_big_double_radius_area2(self):
        res = circle.area(234567.89012345678)
        self.assertAlmostEqual(res, math.pi * 234567.89012345678**2, 5)

    def test_big_double_radius_area3(self):
        res = circle.area(345678.90123456789)
        self.assertAlmostEqual(res, math.pi * 345678.90123456789**2, 5)

    def test_big_double_radius_area4(self):
        res = circle.area(456789.01234567891)
        self.assertAlmostEqual(res, math.pi * 456789.01234567891**2, 5)

    def test_big_double_radius_area5(self):
        res = circle.area(567890.12345678912)
        self.assertAlmostEqual(res, math.pi * 567890.12345678912**2, 5)

    def test_big_double_radius_area6(self):
        res = circle.area(678901.23456789123)
        self.assertAlmostEqual(res, math.pi * 678901.23456789123**2, 5)

    def test_big_double_radius_area7(self):
        res = circle.area(789012.34567891234)
        self.assertAlmostEqual(res, math.pi * 789012.34567891234**2, 5)

    def test_big_double_radius_area8(self):
        res = circle.area(890123.45678912345)
        self.assertAlmostEqual(res, math.pi * 890123.45678912345**2, 5)

    def test_big_double_radius_area9(self):
        res = circle.area(987654.32109876543)
        self.assertAlmostEqual(res, math.pi * 987654.32109876543**2, 5)

    def test_big_double_radius_area10(self):
        res = circle.area(1234567.89012345678)
        self.assertAlmostEqual(res, math.pi * 1234567.89012345678**2, 5)

    def test_big_double_radius_area11(self):
        res = circle.area(2345678.90123456789)
        self.assertAlmostEqual(res, math.pi * 2345678.90123456789**2, 5)

    def test_big_double_radius_area12(self):
        res = circle.area(3456789.01234567891)
        self.assertAlmostEqual(res, math.pi * 3456789.01234567891**2, 5)

    def test_big_double_radius_area13(self):
        res = circle.area(4567890.12345678912)
        self.assertAlmostEqual(res, math.pi * 4567890.12345678912**2, 5)

    def test_big_double_radius_area14(self):
        res = circle.area(5678901.23456789123)
        self.assertAlmostEqual(res, math.pi * 5678901.23456789123**2, 5)

    def test_big_double_radius_area15(self):
        res = circle.area(9876543.21098765432)
        self.assertAlmostEqual(res, math.pi * 9876543.21098765432**2, 5)

    def test_zero_radius_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_negative_radius_perimeter(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-5)

    def test_string_radius_perimeter(self):
        with self.assertRaises(TypeError):
            circle.perimeter("5")

    def test_none_radius_perimeter(self):
        with self.assertRaises(TypeError):
            circle.perimeter(None)

    def test_list_radius_perimeter(self):
        with self.assertRaises(TypeError):
            circle.perimeter([5])

    def test_int_radius_perimeter1(self):
        res = circle.perimeter(37)
        self.assertAlmostEqual(res, 2 * math.pi * 37, 5)

    def test_int_radius_perimeter2(self):
        res = circle.perimeter(126)
        self.assertAlmostEqual(res, 2 * math.pi * 126, 5)

    def test_int_radius_perimeter3(self):
        res = circle.perimeter(347)
        self.assertAlmostEqual(res, 2 * math.pi * 347, 5)

    def test_int_radius_perimeter4(self):
        res = circle.perimeter(681)
        self.assertAlmostEqual(res, 2 * math.pi * 681, 5)

    def test_int_radius_perimeter5(self):
        res = circle.perimeter(1293)
        self.assertAlmostEqual(res, 2 * math.pi * 1293, 5)

    def test_int_radius_perimeter6(self):
        res = circle.perimeter(2784)
        self.assertAlmostEqual(res, 2 * math.pi * 2784, 5)

    def test_int_radius_perimeter7(self):
        res = circle.perimeter(3956)
        self.assertAlmostEqual(res, 2 * math.pi * 3956, 5)

    def test_int_radius_perimeter8(self):
        res = circle.perimeter(5173)
        self.assertAlmostEqual(res, 2 * math.pi * 5173, 5)

    def test_int_radius_perimeter9(self):
        res = circle.perimeter(7462)
        self.assertAlmostEqual(res, 2 * math.pi * 7462, 5)

    def test_int_radius_perimeter10(self):
        res = circle.perimeter(9281)
        self.assertAlmostEqual(res, 2 * math.pi * 9281, 5)

    def test_int_radius_perimeter11(self):
        res = circle.perimeter(13579)
        self.assertAlmostEqual(res, 2 * math.pi * 13579, 5)

    def test_int_radius_perimeter12(self):
        res = circle.perimeter(21746)
        self.assertAlmostEqual(res, 2 * math.pi * 21746, 5)

    def test_int_radius_perimeter13(self):
        res = circle.perimeter(32489)
        self.assertAlmostEqual(res, 2 * math.pi * 32489, 5)

    def test_int_radius_perimeter14(self):
        res = circle.perimeter(47632)
        self.assertAlmostEqual(res, 2 * math.pi * 47632, 5)

    def test_int_radius_perimeter15(self):
        res = circle.perimeter(62581)
        self.assertAlmostEqual(res, 2 * math.pi * 62581, 5)

    def test_double_radius_perimeter1(self):
        res = circle.perimeter(17.392846152738491)
        self.assertAlmostEqual(res, 2 * math.pi * 17.392846152738491, 5)

    def test_double_radius_perimeter2(self):
        res = circle.perimeter(246.817395620481735)
        self.assertAlmostEqual(res, 2 * math.pi * 246.817395620481735, 5)

    def test_double_radius_perimeter3(self):
        res = circle.perimeter(739.125846293718462)
        self.assertAlmostEqual(res, 2 * math.pi * 739.125846293718462, 5)

    def test_double_radius_perimeter4(self):
        res = circle.perimeter(1183.74629183562749)
        self.assertAlmostEqual(res, 2 * math.pi * 1183.74629183562749, 5)

    def test_double_radius_perimeter5(self):
        res = circle.perimeter(1672.93841572638491)
        self.assertAlmostEqual(res, 2 * math.pi * 1672.93841572638491, 5)

    def test_double_radius_perimeter6(self):
        res = circle.perimeter(2591.48372619584731)
        self.assertAlmostEqual(res, 2 * math.pi * 2591.48372619584731, 5)

    def test_double_radius_perimeter7(self):
        res = circle.perimeter(3674.21958374610285)
        self.assertAlmostEqual(res, 2 * math.pi * 3674.21958374610285, 5)

    def test_double_radius_perimeter8(self):
        res = circle.perimeter(4829.65719382461037)
        self.assertAlmostEqual(res, 2 * math.pi * 4829.65719382461037, 5)

    def test_double_radius_perimeter9(self):
        res = circle.perimeter(5917.38462019573846)
        self.assertAlmostEqual(res, 2 * math.pi * 5917.38462019573846, 5)

    def test_double_radius_perimeter10(self):
        res = circle.perimeter(6842.19375628401953)
        self.assertAlmostEqual(res, 2 * math.pi * 6842.19375628401953, 5)

    def test_double_radius_perimeter11(self):
        res = circle.perimeter(7936.52841963720518)
        self.assertAlmostEqual(res, 2 * math.pi * 7936.52841963720518, 5)

    def test_double_radius_perimeter12(self):
        res = circle.perimeter(9147.36281947510386)
        self.assertAlmostEqual(res, 2 * math.pi * 9147.36281947510386, 5)

    def test_double_radius_perimeter13(self):
        res = circle.perimeter(12753.84619273510842)
        self.assertAlmostEqual(res, 2 * math.pi * 12753.84619273510842, 5)

    def test_double_radius_perimeter14(self):
        res = circle.perimeter(23819.57462819374615)
        self.assertAlmostEqual(res, 2 * math.pi * 23819.57462819374615, 5)

    def test_double_radius_perimeter15(self):
        res = circle.perimeter(54927.18374629105837)
        self.assertAlmostEqual(res, 2 * math.pi * 54927.18374629105837, 5)

    def test_big_double_radius_perimeter1(self):
        res = circle.perimeter(135792.46801357924)
        self.assertAlmostEqual(res, 2 * math.pi * 135792.46801357924, 5)

    def test_big_double_radius_perimeter2(self):
        res = circle.perimeter(246813.57912468035)
        self.assertAlmostEqual(res, 2 * math.pi * 246813.57912468035, 5)

    def test_big_double_radius_perimeter3(self):
        res = circle.perimeter(357924.68123579146)
        self.assertAlmostEqual(res, 2 * math.pi * 357924.68123579146, 5)

    def test_big_double_radius_perimeter4(self):
        res = circle.perimeter(468135.79234681257)
        self.assertAlmostEqual(res, 2 * math.pi * 468135.79234681257, 5)

    def test_big_double_radius_perimeter5(self):
        res = circle.perimeter(579246.81345792368)
        self.assertAlmostEqual(res, 2 * math.pi * 579246.81345792368, 5)

    def test_big_double_radius_perimeter6(self):
        res = circle.perimeter(681357.92456813479)
        self.assertAlmostEqual(res, 2 * math.pi * 681357.92456813479, 5)

    def test_big_double_radius_perimeter7(self):
        res = circle.perimeter(792468.13567924581)
        self.assertAlmostEqual(res, 2 * math.pi * 792468.13567924581, 5)

    def test_big_double_radius_perimeter8(self):
        res = circle.perimeter(813579.24680135792)
        self.assertAlmostEqual(res, 2 * math.pi * 813579.24680135792, 5)

    def test_big_double_radius_perimeter9(self):
        res = circle.perimeter(924681.35791246803)
        self.assertAlmostEqual(res, 2 * math.pi * 924681.35791246803, 5)

    def test_big_double_radius_perimeter10(self):
        res = circle.perimeter(1357924.68135792468)
        self.assertAlmostEqual(res, 2 * math.pi * 1357924.68135792468, 5)

    def test_big_double_radius_perimeter11(self):
        res = circle.perimeter(2468135.79246813579)
        self.assertAlmostEqual(res, 2 * math.pi * 2468135.79246813579, 5)

    def test_big_double_radius_perimeter12(self):
        res = circle.perimeter(3579246.81357924680)
        self.assertAlmostEqual(res, 2 * math.pi * 3579246.81357924680, 5)

    def test_big_double_radius_perimeter13(self):
        res = circle.perimeter(4681357.92468135791)
        self.assertAlmostEqual(res, 2 * math.pi * 4681357.92468135791, 5)

    def test_big_double_radius_perimeter14(self):
        res = circle.perimeter(5792468.13579246802)
        self.assertAlmostEqual(res, 2 * math.pi * 5792468.13579246802, 5)

    def test_big_double_radius_perimeter15(self):
        res = circle.perimeter(8913579.24681357913)
        self.assertAlmostEqual(res, 2 * math.pi * 8913579.24681357913, 5)

class SquareTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            square.area(-5)

    def test_string_side_area(self):
        with self.assertRaises(TypeError):
            square.area("5")

    def test_none_side_area(self):
        with self.assertRaises(TypeError):
            square.area(None)

    def test_list_side_area(self):
        with self.assertRaises(TypeError):
            square.area([5])

    def test_int_square_area1(self):
        res = square.area(7)
        self.assertEqual(res, 7**2)

    def test_int_square_area2(self):
        res = square.area(25)
        self.assertEqual(res, 25**2)

    def test_int_square_area3(self):
        res = square.area(43)
        self.assertEqual(res, 43**2)

    def test_int_square_area4(self):
        res = square.area(86)
        self.assertEqual(res, 86**2)

    def test_int_square_area5(self):
        res = square.area(137)
        self.assertEqual(res, 137**2)

    def test_int_square_area6(self):
        res = square.area(264)
        self.assertEqual(res, 264**2)

    def test_int_square_area7(self):
        res = square.area(391)
        self.assertEqual(res, 391**2)

    def test_int_square_area8(self):
        res = square.area(528)
        self.assertEqual(res, 528**2)

    def test_int_square_area9(self):
        res = square.area(746)
        self.assertEqual(res, 746**2)

    def test_int_square_area10(self):
        res = square.area(913)
        self.assertEqual(res, 913**2)

    def test_int_square_area11(self):
        res = square.area(1247)
        self.assertEqual(res, 1247**2)

    def test_int_square_area12(self):
        res = square.area(2381)
        self.assertEqual(res, 2381**2)

    def test_int_square_area13(self):
        res = square.area(3562)
        self.assertEqual(res, 3562**2)

    def test_int_square_area14(self):
        res = square.area(4729)
        self.assertEqual(res, 4729**2)

    def test_int_square_area15(self):
        res = square.area(6384)
        self.assertEqual(res, 6384**2)

    def test_double_square_area1(self):
        res = square.area(17.392846152738491)
        self.assertAlmostEqual(res, 17.392846152738491**2, 5)

    def test_double_square_area2(self):
        res = square.area(246.817395620481735)
        self.assertAlmostEqual(res, 246.817395620481735**2, 5)

    def test_double_square_area3(self):
        res = square.area(739.125846293718462)
        self.assertAlmostEqual(res, 739.125846293718462**2, 5)

    def test_double_square_area4(self):
        res = square.area(1183.74629183562749)
        self.assertAlmostEqual(res, 1183.74629183562749**2, 5)

    def test_double_square_area5(self):
        res = square.area(1672.93841572638491)
        self.assertAlmostEqual(res, 1672.93841572638491**2, 5)

    def test_double_square_area6(self):
        res = square.area(2591.48372619584731)
        self.assertAlmostEqual(res, 2591.48372619584731**2, 5)

    def test_double_square_area7(self):
        res = square.area(3674.21958374610285)
        self.assertAlmostEqual(res, 3674.21958374610285**2, 5)

    def test_double_square_area8(self):
        res = square.area(4829.65719382461037)
        self.assertAlmostEqual(res, 4829.65719382461037**2, 5)

    def test_double_square_area9(self):
        res = square.area(5917.38462019573846)
        self.assertAlmostEqual(res, 5917.38462019573846**2, 5)

    def test_double_square_area10(self):
        res = square.area(6842.19375628401953)
        self.assertAlmostEqual(res, 6842.19375628401953**2, 5)

    def test_double_square_area11(self):
        res = square.area(7936.52841963720518)
        self.assertAlmostEqual(res, 7936.52841963720518**2, 5)

    def test_double_square_area12(self):
        res = square.area(9147.36281947510386)
        self.assertAlmostEqual(res, 9147.36281947510386**2, 5)

    def test_double_square_area13(self):
        res = square.area(12753.84619273510842)
        self.assertAlmostEqual(res, 12753.84619273510842**2, 5)

    def test_double_square_area14(self):
        res = square.area(23819.57462819374615)
        self.assertAlmostEqual(res, 23819.57462819374615**2, 5)

    def test_double_square_area15(self):
        res = square.area(54927.18374629105837)
        self.assertAlmostEqual(res, 54927.18374629105837**2, 5)

    def test_big_double_square_area1(self):
        res = square.area(135792.46801357924)
        self.assertAlmostEqual(res, 135792.46801357924**2, 5)

    def test_big_double_square_area2(self):
        res = square.area(246813.57912468035)
        self.assertAlmostEqual(res, 246813.57912468035**2, 5)

    def test_big_double_square_area3(self):
        res = square.area(357924.68123579146)
        self.assertAlmostEqual(res, 357924.68123579146**2, 5)

    def test_big_double_square_area4(self):
        res = square.area(468135.79234681257)
        self.assertAlmostEqual(res, 468135.79234681257**2, 5)

    def test_big_double_square_area5(self):
        res = square.area(579246.81345792368)
        self.assertAlmostEqual(res, 579246.81345792368**2, 5)

    def test_big_double_square_area6(self):
        res = square.area(681357.92456813479)
        self.assertAlmostEqual(res, 681357.92456813479**2, 5)

    def test_big_double_square_area7(self):
        res = square.area(792468.13567924581)
        self.assertAlmostEqual(res, 792468.13567924581**2, 5)

    def test_big_double_square_area8(self):
        res = square.area(813579.24680135792)
        self.assertAlmostEqual(res, 813579.24680135792**2, 5)

    def test_big_double_square_area9(self):
        res = square.area(924681.35791246803)
        self.assertAlmostEqual(res, 924681.35791246803**2, 5)

    def test_big_double_square_area10(self):
        res = square.area(1357924.68135792468)
        self.assertAlmostEqual(res, 1357924.68135792468**2, 5)

    def test_big_double_square_area11(self):
        res = square.area(2468135.79246813579)
        self.assertAlmostEqual(res, 2468135.79246813579**2, 5)

    def test_big_double_square_area12(self):
        res = square.area(3579246.81357924680)
        self.assertAlmostEqual(res, 3579246.81357924680**2, 5)

    def test_big_double_square_area13(self):
        res = square.area(4681357.92468135791)
        self.assertAlmostEqual(res, 4681357.92468135791**2, 5)

    def test_big_double_square_area14(self):
        res = square.area(5792468.13579246802)
        self.assertAlmostEqual(res, 5792468.13579246802**2, 5)

    def test_big_double_square_area15(self):
        res = square.area(8913579.24681357913)
        self.assertAlmostEqual(res, 8913579.24681357913**2, 5)

    def test_zero_side_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            square.perimeter(-5)

    def test_string_side_perimeter(self):
        with self.assertRaises(TypeError):
            square.perimeter("5")

    def test_none_side_perimeter(self):
        with self.assertRaises(TypeError):
            square.perimeter(None)

    def test_list_side_perimeter(self):
        with self.assertRaises(TypeError):
            square.perimeter([5])

    def test_int_square_perimeter1(self):
        res = square.perimeter(13)
        self.assertEqual(res, 4 * 13)

    def test_int_square_perimeter2(self):
        res = square.perimeter(29)
        self.assertEqual(res, 4 * 29)

    def test_int_square_perimeter3(self):
        res = square.perimeter(47)
        self.assertEqual(res, 4 * 47)

    def test_int_square_perimeter4(self):
        res = square.perimeter(92)
        self.assertEqual(res, 4 * 92)

    def test_int_square_perimeter5(self):
        res = square.perimeter(158)
        self.assertEqual(res, 4 * 158)

    def test_int_square_perimeter6(self):
        res = square.perimeter(273)
        self.assertEqual(res, 4 * 273)

    def test_int_square_perimeter7(self):
        res = square.perimeter(419)
        self.assertEqual(res, 4 * 419)

    def test_int_square_perimeter8(self):
        res = square.perimeter(536)
        self.assertEqual(res, 4 * 536)

    def test_int_square_perimeter9(self):
        res = square.perimeter(782)
        self.assertEqual(res, 4 * 782)

    def test_int_square_perimeter10(self):
        res = square.perimeter(945)
        self.assertEqual(res, 4 * 945)

    def test_int_square_perimeter11(self):
        res = square.perimeter(1268)
        self.assertEqual(res, 4 * 1268)

    def test_int_square_perimeter12(self):
        res = square.perimeter(2397)
        self.assertEqual(res, 4 * 2397)

    def test_int_square_perimeter13(self):
        res = square.perimeter(3671)
        self.assertEqual(res, 4 * 3671)

    def test_int_square_perimeter14(self):
        res = square.perimeter(4852)
        self.assertEqual(res, 4 * 4852)

    def test_int_square_perimeter15(self):
        res = square.perimeter(6293)
        self.assertEqual(res, 4 * 6293)

    def test_double_square_perimeter1(self):
        res = square.perimeter(19.482736194857321)
        self.assertAlmostEqual(res, 4 * 19.482736194857321, 5)

    def test_double_square_perimeter2(self):
        res = square.perimeter(257.193846205718394)
        self.assertAlmostEqual(res, 4 * 257.193846205718394, 5)

    def test_double_square_perimeter3(self):
        res = square.perimeter(846.291735618492037)
        self.assertAlmostEqual(res, 4 * 846.291735618492037, 5)

    def test_double_square_perimeter4(self):
        res = square.perimeter(1294.837261945028371)
        self.assertAlmostEqual(res, 4 * 1294.837261945028371, 5)

    def test_double_square_perimeter5(self):
        res = square.perimeter(1783.492615837204619)
        self.assertAlmostEqual(res, 4 * 1783.492615837204619, 5)

    def test_double_square_perimeter6(self):
        res = square.perimeter(2694.183726495817302)
        self.assertAlmostEqual(res, 4 * 2694.183726495817302, 5)

    def test_double_square_perimeter7(self):
        res = square.perimeter(3785.629184736102948)
        self.assertAlmostEqual(res, 4 * 3785.629184736102948, 5)

    def test_double_square_perimeter8(self):
        res = square.perimeter(4938.172635849201736)
        self.assertAlmostEqual(res, 4 * 4938.172635849201736, 5)

    def test_double_square_perimeter9(self):
        res = square.perimeter(6027.483916275103849)
        self.assertAlmostEqual(res, 4 * 6027.483916275103849, 5)

    def test_double_square_perimeter10(self):
        res = square.perimeter(7159.284617395028461)
        self.assertAlmostEqual(res, 4 * 7159.284617395028461, 5)

    def test_double_square_perimeter11(self):
        res = square.perimeter(8246.193857264019538)
        self.assertAlmostEqual(res, 4 * 8246.193857264019538, 5)

    def test_double_square_perimeter12(self):
        res = square.perimeter(9361.728495103826174)
        self.assertAlmostEqual(res, 4 * 9361.728495103826174, 5)

    def test_double_square_perimeter13(self):
        res = square.perimeter(13847.291635827401926)
        self.assertAlmostEqual(res, 4 * 13847.291635827401926, 5)

    def test_double_square_perimeter14(self):
        res = square.perimeter(24916.837261945028371)
        self.assertAlmostEqual(res, 4 * 24916.837261945028371, 5)

    def test_double_square_perimeter15(self):
        res = square.perimeter(56283.194726385019472)
        self.assertAlmostEqual(res, 4 * 56283.194726385019472, 5)

    def test_big_double_square_perimeter1(self):
        res = square.perimeter(145827.39162584710)
        self.assertAlmostEqual(res, 4 * 145827.39162584710, 5)

    def test_big_double_square_perimeter2(self):
        res = square.perimeter(258316.49271836502)
        self.assertAlmostEqual(res, 4 * 258316.49271836502, 5)

    def test_big_double_square_perimeter3(self):
        res = square.perimeter(369427.58381947613)
        self.assertAlmostEqual(res, 4 * 369427.58381947613, 5)

    def test_big_double_square_perimeter4(self):
        res = square.perimeter(471538.69492058724)
        self.assertAlmostEqual(res, 4 * 471538.69492058724, 5)

    def test_big_double_square_perimeter5(self):
        res = square.perimeter(582649.71503169835)
        self.assertAlmostEqual(res, 4 * 582649.71503169835, 5)

    def test_big_double_square_perimeter6(self):
        res = square.perimeter(693751.82614270946)
        self.assertAlmostEqual(res, 4 * 693751.82614270946, 5)

    def test_big_double_square_perimeter7(self):
        res = square.perimeter(714862.93725381057)
        self.assertAlmostEqual(res, 4 * 714862.93725381057, 5)

    def test_big_double_square_perimeter8(self):
        res = square.perimeter(825973.14836492168)
        self.assertAlmostEqual(res, 4 * 825973.14836492168, 5)

    def test_big_double_square_perimeter9(self):
        res = square.perimeter(936184.25947503279)
        self.assertAlmostEqual(res, 4 * 936184.25947503279, 5)

    def test_big_double_square_perimeter10(self):
        res = square.perimeter(1462957.31846027185)
        self.assertAlmostEqual(res, 4 * 1462957.31846027185, 5)

    def test_big_double_square_perimeter11(self):
        res = square.perimeter(2573168.42957138296)
        self.assertAlmostEqual(res, 4 * 2573168.42957138296, 5)

    def test_big_double_square_perimeter12(self):
        res = square.perimeter(3684279.53168249307)
        self.assertAlmostEqual(res, 4 * 3684279.53168249307, 5)

    def test_big_double_square_perimeter13(self):
        res = square.perimeter(4795381.64279350418)
        self.assertAlmostEqual(res, 4 * 4795381.64279350418, 5)

    def test_big_double_square_perimeter14(self):
        res = square.perimeter(5816492.75380461529)
        self.assertAlmostEqual(res, 4 * 5816492.75380461529, 5)

    def test_big_double_square_perimeter15(self):
        res = square.perimeter(8927513.86491572630)
        self.assertAlmostEqual(res, 4 * 8927513.86491572630, 5)

class RectangleTestCase(unittest.TestCase):
    def test_zero_a_area(self):
        res = rectangle.area(0, 15)
        self.assertEqual(res, 0)

    def test_zero_b_area(self):
        res = rectangle.area(15, 0)
        self.assertEqual(res, 0)

    def test_negative_a_area(self):
        with self.assertRaises(ValueError):
            rectangle.area(-5, 10)

    def test_negative_b_area(self):
        with self.assertRaises(ValueError):
            rectangle.area(10, -5)

    def test_string_a_area(self):
        with self.assertRaises(TypeError):
            rectangle.area("5", 10)

    def test_string_b_area(self):
        with self.assertRaises(TypeError):
            rectangle.area(5, "10")

    def test_none_a_area(self):
        with self.assertRaises(TypeError):
            rectangle.area(None, 10)

    def test_none_b_area(self):
        with self.assertRaises(TypeError):
            rectangle.area(5, None)

    def test_list_a_area(self):
        with self.assertRaises(TypeError):
            rectangle.area([5], 10)

    def test_list_b_area(self):
        with self.assertRaises(TypeError):
            rectangle.area(5, [10])

    def test_int_rectangle_area1(self):
        res = rectangle.area(7, 12)
        self.assertEqual(res, 7 * 12)

    def test_int_rectangle_area2(self):
        res = rectangle.area(25, 18)
        self.assertEqual(res, 25 * 18)

    def test_int_rectangle_area3(self):
        res = rectangle.area(43, 29)
        self.assertEqual(res, 43 * 29)

    def test_int_rectangle_area4(self):
        res = rectangle.area(86, 54)
        self.assertEqual(res, 86 * 54)

    def test_int_rectangle_area5(self):
        res = rectangle.area(137, 92)
        self.assertEqual(res, 137 * 92)

    def test_int_rectangle_area6(self):
        res = rectangle.area(264, 153)
        self.assertEqual(res, 264 * 153)

    def test_int_rectangle_area7(self):
        res = rectangle.area(391, 247)
        self.assertEqual(res, 391 * 247)

    def test_int_rectangle_area8(self):
        res = rectangle.area(528, 316)
        self.assertEqual(res, 528 * 316)

    def test_int_rectangle_area9(self):
        res = rectangle.area(746, 429)
        self.assertEqual(res, 746 * 429)

    def test_int_rectangle_area10(self):
        res = rectangle.area(913, 587)
        self.assertEqual(res, 913 * 587)

    def test_int_rectangle_area11(self):
        res = rectangle.area(1247, 836)
        self.assertEqual(res, 1247 * 836)

    def test_int_rectangle_area12(self):
        res = rectangle.area(2381, 1459)
        self.assertEqual(res, 2381 * 1459)

    def test_int_rectangle_area13(self):
        res = rectangle.area(3562, 2187)
        self.assertEqual(res, 3562 * 2187)

    def test_int_rectangle_area14(self):
        res = rectangle.area(4729, 3196)
        self.assertEqual(res, 4729 * 3196)

    def test_int_rectangle_area15(self):
        res = rectangle.area(6384, 5271)
        self.assertEqual(res, 6384 * 5271)

    def test_double_rectangle_area1(self):
        a, b = 17.392846152738491, 23.748192635184726
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area2(self):
        a, b = 246.817395620481735, 135.629481736205194
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area3(self):
        a, b = 739.125846293718462, 528.374619283746105
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area4(self):
        a, b = 1183.74629183562749, 947.285163829471625
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area5(self):
        a, b = 1672.93841572638491, 1258.473619284756193
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area6(self):
        a, b = 2591.48372619584731, 1837.294615827364918
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area7(self):
        a, b = 3674.21958374610285, 2948.617352819463027
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area8(self):
        a, b = 4829.65719382461037, 3761.928453617204859
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area9(self):
        a, b = 5917.38462019573846, 4286.193754628193746
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area10(self):
        a, b = 6842.19375628401953, 5193.827461928374615
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area11(self):
        a, b = 7936.52841963720518, 6382.194756281937461
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area12(self):
        a, b = 9147.36281947510386, 7259.483617294856103
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area13(self):
        a, b = 12753.84619273510842, 9836.271945628193746
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area14(self):
        a, b = 23819.57462819374615, 17642.839517263948105
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_double_rectangle_area15(self):
        a, b = 54927.18374629105837, 43816.295173846201957
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area1(self):
        a, b = 135792.46801357924, 246813.57912468035
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area2(self):
        a, b = 357924.68123579146, 468135.79234681257
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area3(self):
        a, b = 579246.81345792368, 681357.92456813479
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area4(self):
        a, b = 792468.13567924581, 813579.24680135792
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area5(self):
        a, b = 924681.35791246803, 1357924.68135792468
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area6(self):
        a, b = 2468135.79246813579, 3579246.81357924680
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area7(self):
        a, b = 4681357.92468135791, 5792468.13579246802
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area8(self):
        a, b = 6813579.24681357913, 7924681.35792468024
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area9(self):
        a, b = 8135792.46813579135, 9246813.57924680146
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area10(self):
        a, b = 13579246.8135792468, 24681357.9246813579
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area11(self):
        a, b = 35792468.1357924680, 46813579.2468135791
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area12(self):
        a, b = 57924681.3579246802, 68135792.4681357913
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area13(self):
        a, b = 79246813.5792468014, 81357924.6813579125
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area14(self):
        a, b = 92468135.7913579246, 135792468.0135792468
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_big_double_rectangle_area15(self):
        a, b = 246813579.12468035, 357924681.23579146
        res = rectangle.area(a, b)
        self.assertAlmostEqual(res, a * b, 5)

    def test_zero_a_perimeter(self):
        res = rectangle.perimeter(0, 15)
        self.assertEqual(res, 30)

    def test_zero_b_perimeter(self):
        res = rectangle.perimeter(15, 0)
        self.assertEqual(res, 30)

    def test_negative_a_perimeter(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, 10)

    def test_negative_b_perimeter(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(10, -5)

    def test_string_a_perimeter(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("5", 10)

    def test_string_b_perimeter(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(5, "10")

    def test_none_a_perimeter(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(None, 10)

    def test_none_b_perimeter(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(5, None)

    def test_list_a_perimeter(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter([5], 10)

    def test_list_b_perimeter(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(5, [10])

    def test_int_rectangle_perimeter1(self):
        res = rectangle.perimeter(13, 27)
        self.assertEqual(res, 2 * (13 + 27))

    def test_int_rectangle_perimeter2(self):
        res = rectangle.perimeter(36, 19)
        self.assertEqual(res, 2 * (36 + 19))

    def test_int_rectangle_perimeter3(self):
        res = rectangle.perimeter(48, 32)
        self.assertEqual(res, 2 * (48 + 32))

    def test_int_rectangle_perimeter4(self):
        res = rectangle.perimeter(91, 57)
        self.assertEqual(res, 2 * (91 + 57))

    def test_int_rectangle_perimeter5(self):
        res = rectangle.perimeter(143, 86)
        self.assertEqual(res, 2 * (143 + 86))

    def test_int_rectangle_perimeter6(self):
        res = rectangle.perimeter(275, 164)
        self.assertEqual(res, 2 * (275 + 164))

    def test_int_rectangle_perimeter7(self):
        res = rectangle.perimeter(428, 239)
        self.assertEqual(res, 2 * (428 + 239))

    def test_int_rectangle_perimeter8(self):
        res = rectangle.perimeter(547, 328)
        self.assertEqual(res, 2 * (547 + 328))

    def test_int_rectangle_perimeter9(self):
        res = rectangle.perimeter(793, 416)
        self.assertEqual(res, 2 * (793 + 416))

    def test_int_rectangle_perimeter10(self):
        res = rectangle.perimeter(956, 638)
        self.assertEqual(res, 2 * (956 + 638))

    def test_int_rectangle_perimeter11(self):
        res = rectangle.perimeter(1274, 859)
        self.assertEqual(res, 2 * (1274 + 859))

    def test_int_rectangle_perimeter12(self):
        res = rectangle.perimeter(2416, 1537)
        self.assertEqual(res, 2 * (2416 + 1537))

    def test_int_rectangle_perimeter13(self):
        res = rectangle.perimeter(3682, 2194)
        self.assertEqual(res, 2 * (3682 + 2194))

    def test_int_rectangle_perimeter14(self):
        res = rectangle.perimeter(4893, 3271)
        self.assertEqual(res, 2 * (4893 + 3271))

    def test_int_rectangle_perimeter15(self):
        res = rectangle.perimeter(6417, 5382)
        self.assertEqual(res, 2 * (6417 + 5382))

    def test_double_rectangle_perimeter1(self):
        a, b = 19.482736194857321, 27.391846205718394
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter2(self):
        a, b = 257.193846205718394, 146.582937164820573
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter3(self):
        a, b = 846.291735618492037, 529.183746205819374
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter4(self):
        a, b = 1294.837261945028371, 958.472619384756102
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter5(self):
        a, b = 1783.492615837204619, 1269.384716205938471
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter6(self):
        a, b = 2694.183726495817302, 1847.592638174205936
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter7(self):
        a, b = 3785.629184736102948, 2958.173624819405726
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter8(self):
        a, b = 4938.172635849201736, 3872.649183726405918
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter9(self):
        a, b = 6027.483916275103849, 4397.261835729401826
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter10(self):
        a, b = 7159.284617395028461, 5284.193726485017392
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter11(self):
        a, b = 8246.193857264019538, 6473.825194736102849
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter12(self):
        a, b = 9361.728495103826174, 7368.194725836102947
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter13(self):
        a, b = 13847.291635827401926, 9947.382615294817306
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter14(self):
        a, b = 24916.837261945028371, 17853.492617384756102
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_double_rectangle_perimeter15(self):
        a, b = 56283.194726385019472, 44927.381645209837164
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter1(self):
        a, b = 145827.39162584710, 256938.47273695821
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter2(self):
        a, b = 258316.49271836502, 369427.58381947613
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter3(self):
        a, b = 369427.58381947613, 471538.69492058724
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter4(self):
        a, b = 471538.69492058724, 582649.71503169835
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter5(self):
        a, b = 582649.71503169835, 693751.82614270946
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter6(self):
        a, b = 693751.82614270946, 714862.93725381057
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter7(self):
        a, b = 714862.93725381057, 825973.14836492168
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter8(self):
        a, b = 825973.14836492168, 936184.25947503279
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter9(self):
        a, b = 936184.25947503279, 1462957.31846027185
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter10(self):
        a, b = 1462957.31846027185, 2573168.42957138296
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter11(self):
        a, b = 2573168.42957138296, 3684279.53168249307
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter12(self):
        a, b = 3684279.53168249307, 4795381.64279350418
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter13(self):
        a, b = 4795381.64279350418, 5816492.75380461529
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter14(self):
        a, b = 5816492.75380461529, 6937513.86491572630
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

    def test_big_double_rectangle_perimeter15(self):
        a, b = 8927513.86491572630, 7938624.97502683741
        res = rectangle.perimeter(a, b)
        self.assertAlmostEqual(res, 2 * (a + b), 5)

class TriangleTestCase(unittest.TestCase):
    def test_zero_base_area(self):
        res = triangle.area(0, 15)
        self.assertEqual(res, 0)

    def test_zero_height_area(self):
        res = triangle.area(15, 0)
        self.assertEqual(res, 0)

    def test_negative_base_area(self):
        with self.assertRaises(ValueError):
            triangle.area(-5, 10)

    def test_negative_height_area(self):
        with self.assertRaises(ValueError):
            triangle.area(10, -5)

    def test_string_base_area(self):
        with self.assertRaises(TypeError):
            triangle.area("5", 10)

    def test_string_height_area(self):
        with self.assertRaises(TypeError):
            triangle.area(10, "5")

    def test_none_base_area(self):
        with self.assertRaises(TypeError):
            triangle.area(None, 10)

    def test_none_height_area(self):
        with self.assertRaises(TypeError):
            triangle.area(10, None)

    def test_list_base_area(self):
        with self.assertRaises(TypeError):
            triangle.area([5], 10)

    def test_list_height_area(self):
        with self.assertRaises(TypeError):
            triangle.area(10, [5])

    def test_int_triangle_area1(self):
        res = triangle.area(7, 12)
        self.assertEqual(res, 7 * 12 / 2)

    def test_int_triangle_area2(self):
        res = triangle.area(25, 18)
        self.assertEqual(res, 25 * 18 / 2)

    def test_int_triangle_area3(self):
        res = triangle.area(43, 29)
        self.assertEqual(res, 43 * 29 / 2)

    def test_int_triangle_area4(self):
        res = triangle.area(86, 54)
        self.assertEqual(res, 86 * 54 / 2)

    def test_int_triangle_area5(self):
        res = triangle.area(137, 92)
        self.assertEqual(res, 137 * 92 / 2)

    def test_int_triangle_area6(self):
        res = triangle.area(264, 153)
        self.assertEqual(res, 264 * 153 / 2)

    def test_int_triangle_area7(self):
        res = triangle.area(391, 247)
        self.assertEqual(res, 391 * 247 / 2)

    def test_int_triangle_area8(self):
        res = triangle.area(528, 316)
        self.assertEqual(res, 528 * 316 / 2)

    def test_int_triangle_area9(self):
        res = triangle.area(746, 429)
        self.assertEqual(res, 746 * 429 / 2)

    def test_int_triangle_area10(self):
        res = triangle.area(913, 587)
        self.assertEqual(res, 913 * 587 / 2)

    def test_int_triangle_area11(self):
        res = triangle.area(1247, 836)
        self.assertEqual(res, 1247 * 836 / 2)

    def test_int_triangle_area12(self):
        res = triangle.area(2381, 1459)
        self.assertEqual(res, 2381 * 1459 / 2)

    def test_int_triangle_area13(self):
        res = triangle.area(3562, 2187)
        self.assertEqual(res, 3562 * 2187 / 2)

    def test_int_triangle_area14(self):
        res = triangle.area(4729, 3196)
        self.assertEqual(res, 4729 * 3196 / 2)

    def test_int_triangle_area15(self):
        res = triangle.area(6384, 5271)
        self.assertEqual(res, 6384 * 5271 / 2)

    def test_double_triangle_area1(self):
        res = triangle.area(17.392846152738491, 23.748192635184726)
        self.assertAlmostEqual(res, 17.392846152738491 * 23.748192635184726 / 2, 5)

    def test_double_triangle_area2(self):
        res = triangle.area(246.817395620481735, 135.629481736205194)
        self.assertAlmostEqual(res, 246.817395620481735 * 135.629481736205194 / 2, 5)

    def test_double_triangle_area3(self):
        res = triangle.area(739.125846293718462, 528.374619283746105)
        self.assertAlmostEqual(res, 739.125846293718462 * 528.374619283746105 / 2, 5)

    def test_double_triangle_area4(self):
        res = triangle.area(1183.74629183562749, 947.285163829471625)
        self.assertAlmostEqual(res, 1183.74629183562749 * 947.285163829471625 / 2, 5)

    def test_double_triangle_area5(self):
        res = triangle.area(1672.93841572638491, 1258.473619284756193)
        self.assertAlmostEqual(res, 1672.93841572638491 * 1258.473619284756193 / 2, 5)

    def test_double_triangle_area6(self):
        res = triangle.area(2591.48372619584731, 1837.294615827364918)
        self.assertAlmostEqual(res, 2591.48372619584731 * 1837.294615827364918 / 2, 5)

    def test_double_triangle_area7(self):
        res = triangle.area(3674.21958374610285, 2948.617352819463027)
        self.assertAlmostEqual(res, 3674.21958374610285 * 2948.617352819463027 / 2, 5)

    def test_double_triangle_area8(self):
        res = triangle.area(4829.65719382461037, 3761.928453617204859)
        self.assertAlmostEqual(res, 4829.65719382461037 * 3761.928453617204859 / 2, 5)

    def test_double_triangle_area9(self):
        res = triangle.area(5917.38462019573846, 4286.193754628193746)
        self.assertAlmostEqual(res, 5917.38462019573846 * 4286.193754628193746 / 2, 5)

    def test_double_triangle_area10(self):
        res = triangle.area(6842.19375628401953, 5193.827461928374615)
        self.assertAlmostEqual(res, 6842.19375628401953 * 5193.827461928374615 / 2, 5)

    def test_double_triangle_area11(self):
        res = triangle.area(7936.52841963720518, 6382.194756281937461)
        self.assertAlmostEqual(res, 7936.52841963720518 * 6382.194756281937461 / 2, 5)

    def test_double_triangle_area12(self):
        res = triangle.area(9147.36281947510386, 7259.483617294856103)
        self.assertAlmostEqual(res, 9147.36281947510386 * 7259.483617294856103 / 2, 5)

    def test_double_triangle_area13(self):
        res = triangle.area(12753.84619273510842, 9836.271945628193746)
        self.assertAlmostEqual(res, 12753.84619273510842 * 9836.271945628193746 / 2, 5)

    def test_double_triangle_area14(self):
        res = triangle.area(23819.57462819374615, 17642.839517263948105)
        self.assertAlmostEqual(res, 23819.57462819374615 * 17642.839517263948105 / 2, 5)

    def test_double_triangle_area15(self):
        res = triangle.area(54927.18374629105837, 43816.295173846201957)
        self.assertAlmostEqual(res, 54927.18374629105837 * 43816.295173846201957 / 2, 5)

    def test_big_double_triangle_area1(self):
        res = triangle.area(135792.46801357924, 246813.57912468035)
        self.assertAlmostEqual(res, 135792.46801357924 * 246813.57912468035 / 2, 5)

    def test_big_double_triangle_area2(self):
        res = triangle.area(357924.68123579146, 468135.79234681257)
        self.assertAlmostEqual(res, 357924.68123579146 * 468135.79234681257 / 2, 5)

    def test_big_double_triangle_area3(self):
        res = triangle.area(579246.81345792368, 681357.92456813479)
        self.assertAlmostEqual(res, 579246.81345792368 * 681357.92456813479 / 2, 5)

    def test_big_double_triangle_area4(self):
        res = triangle.area(792468.13567924581, 813579.24680135792)
        self.assertAlmostEqual(res, 792468.13567924581 * 813579.24680135792 / 2, 5)

    def test_big_double_triangle_area5(self):
        res = triangle.area(924681.35791246803, 1357924.68135792468)
        self.assertAlmostEqual(res, 924681.35791246803 * 1357924.68135792468 / 2, 5)

    def test_big_double_triangle_area6(self):
        res = triangle.area(2468135.79246813579, 3579246.81357924680)
        self.assertAlmostEqual(res, 2468135.79246813579 * 3579246.81357924680 / 2, 5)

    def test_big_double_triangle_area7(self):
        res = triangle.area(4681357.92468135791, 5792468.13579246802)
        self.assertAlmostEqual(res, 4681357.92468135791 * 5792468.13579246802 / 2, 5)

    def test_big_double_triangle_area8(self):
        res = triangle.area(6813579.24681357913, 7924681.35792468024)
        self.assertAlmostEqual(res, 6813579.24681357913 * 7924681.35792468024 / 2, 5)

    def test_big_double_triangle_area9(self):
        res = triangle.area(8135792.46813579135, 9246813.57924680146)
        self.assertAlmostEqual(res, 8135792.46813579135 * 9246813.57924680146 / 2, 5)

    def test_big_double_triangle_area10(self):
        res = triangle.area(13579246.8135792468, 24681357.9246813579)
        self.assertAlmostEqual(res, 13579246.8135792468 * 24681357.9246813579 / 2, 5)

    def test_big_double_triangle_area11(self):
        res = triangle.area(35792468.1357924680, 46813579.2468135791)
        self.assertAlmostEqual(res, 35792468.1357924680 * 46813579.2468135791 / 2, 5)

    def test_big_double_triangle_area12(self):
        res = triangle.area(57924681.3579246802, 68135792.4681357913)
        self.assertAlmostEqual(res, 57924681.3579246802 * 68135792.4681357913 / 2, 5)

    def test_big_double_triangle_area13(self):
        res = triangle.area(79246813.5792468014, 81357924.6813579125)
        self.assertAlmostEqual(res, 79246813.5792468014 * 81357924.6813579125 / 2, 5)

    def test_big_double_triangle_area14(self):
        res = triangle.area(92468135.7913579246, 135792468.0135792468)
        self.assertAlmostEqual(res, 92468135.7913579246 * 135792468.0135792468 / 2, 5)

    def test_big_double_triangle_area15(self):
        res = triangle.area(246813579.12468035, 357924681.23579146)
        self.assertAlmostEqual(res, 246813579.12468035 * 357924681.23579146 / 2, 5)

    def test_zero_a_perimeter(self):
        res = triangle.perimeter(0, 10, 15)
        self.assertEqual(res, 25)

    def test_zero_b_perimeter(self):
        res = triangle.perimeter(10, 0, 15)
        self.assertEqual(res, 25)

    def test_zero_c_perimeter(self):
        res = triangle.perimeter(10, 15, 0)
        self.assertEqual(res, 25)

    def test_negative_a_perimeter(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-5, 10, 10)

    def test_negative_b_perimeter(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(10, -5, 10)

    def test_negative_c_perimeter(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(10, 10, -5)

    def test_string_a_perimeter(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("5", 10, 15)

    def test_string_b_perimeter(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(5, "10", 15)

    def test_string_c_perimeter(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(5, 10, "15")

    def test_none_a_perimeter(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(None, 10, 15)

    def test_none_b_perimeter(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(5, None, 15)

    def test_none_c_perimeter(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(5, 10, None)

    def test_list_a_perimeter(self):
        with self.assertRaises(TypeError):
            triangle.perimeter([5], 10, 15)

    def test_list_b_perimeter(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(5, [10], 15)

    def test_list_c_perimeter(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(5, 10, [15])

    def test_int_triangle_perimeter1(self):
        res = triangle.perimeter(7, 12, 15)
        self.assertEqual(res, 7 + 12 + 15)

    def test_int_triangle_perimeter2(self):
        res = triangle.perimeter(25, 18, 21)
        self.assertEqual(res, 25 + 18 + 21)

    def test_int_triangle_perimeter3(self):
        res = triangle.perimeter(43, 29, 36)
        self.assertEqual(res, 43 + 29 + 36)

    def test_int_triangle_perimeter4(self):
        res = triangle.perimeter(86, 54, 72)
        self.assertEqual(res, 86 + 54 + 72)

    def test_int_triangle_perimeter5(self):
        res = triangle.perimeter(137, 92, 115)
        self.assertEqual(res, 137 + 92 + 115)

    def test_int_triangle_perimeter6(self):
        res = triangle.perimeter(264, 153, 198)
        self.assertEqual(res, 264 + 153 + 198)

    def test_int_triangle_perimeter7(self):
        res = triangle.perimeter(391, 247, 318)
        self.assertEqual(res, 391 + 247 + 318)

    def test_int_triangle_perimeter8(self):
        res = triangle.perimeter(528, 316, 427)
        self.assertEqual(res, 528 + 316 + 427)

    def test_int_triangle_perimeter9(self):
        res = triangle.perimeter(746, 429, 583)
        self.assertEqual(res, 746 + 429 + 583)

    def test_int_triangle_perimeter10(self):
        res = triangle.perimeter(913, 587, 724)
        self.assertEqual(res, 913 + 587 + 724)

    def test_int_triangle_perimeter11(self):
        res = triangle.perimeter(1247, 836, 951)
        self.assertEqual(res, 1247 + 836 + 951)

    def test_int_triangle_perimeter12(self):
        res = triangle.perimeter(2381, 1459, 1872)
        self.assertEqual(res, 2381 + 1459 + 1872)

    def test_int_triangle_perimeter13(self):
        res = triangle.perimeter(3562, 2187, 2941)
        self.assertEqual(res, 3562 + 2187 + 2941)

    def test_int_triangle_perimeter14(self):
        res = triangle.perimeter(4729, 3196, 3854)
        self.assertEqual(res, 4729 + 3196 + 3854)

    def test_int_triangle_perimeter15(self):
        res = triangle.perimeter(6384, 5271, 4916)
        self.assertEqual(res, 6384 + 5271 + 4916)

    def test_double_triangle_perimeter1(self):
        a, b, c = 17.392846152738491, 23.748192635184726, 19.583726194857321
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter2(self):
        a, b, c = 246.817395620481735, 135.629481736205194, 198.472619384756102
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter3(self):
        a, b, c = 739.125846293718462, 528.374619283746105, 614.829375192846301
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter4(self):
        a, b, c = 1183.74629183562749, 947.285163829471625, 1056.384729183652741
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter5(self):
        a, b, c = 1672.93841572638491, 1258.473619284756193, 1437.629184756203918
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter6(self):
        a, b, c = 2591.48372619584731, 1837.294615827364918, 2146.837192846501273
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter7(self):
        a, b, c = 3674.21958374610285, 2948.617352819463027, 3157.482619384756201
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter8(self):
        a, b, c = 4829.65719382461037, 3761.928453617204859, 4182.735619284756103
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter9(self):
        a, b, c = 5917.38462019573846, 4286.193754628193746, 5173.829461928374615
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter10(self):
        a, b, c = 6842.19375628401953, 5193.827461928374615, 5937.184629375102846
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter11(self):
        a, b, c = 7936.52841963720518, 6382.194756281937461, 7148.392617485203916
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter12(self):
        a, b, c = 9147.36281947510386, 7259.483617294856103, 8163.294718562039471
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter13(self):
        a, b, c = 12753.84619273510842, 9836.271945628193746, 11372.584619273840516
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter14(self):
        a, b, c = 23819.57462819374615, 17642.839517263948105, 19573.482619384756201
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_double_triangle_perimeter15(self):
        a, b, c = 54927.18374629105837, 43816.295173846201957, 49271.638194726350819
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter1(self):
        a, b, c = 135792.46801357924, 246813.57912468035, 198765.43210987654
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter2(self):
        a, b, c = 357924.68123579146, 468135.79234681257, 392846.13579246801
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter3(self):
        a, b, c = 579246.81345792368, 681357.92456813479, 623819.47562019384
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter4(self):
        a, b, c = 792468.13567924581, 813579.24680135792, 756192.48376102948
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter5(self):
        a, b, c = 924681.35791246803, 1357924.68135792468, 1124681.35792468013
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter6(self):
        a, b, c = 2468135.79246813579, 3579246.81357924680, 2981357.92468135791
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter7(self):
        a, b, c = 4681357.92468135791, 5792468.13579246802, 5124681.35792468024
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter8(self):
        a, b, c = 6813579.24681357913, 7924681.35792468024, 7357924.68135791246
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter9(self):
        a, b, c = 8135792.46813579135, 9246813.57924680146, 8671357.92468135791
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter10(self):
        a, b, c = 13579246.8135792468, 24681357.9246813579, 19813579.2468135791
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter11(self):
        a, b, c = 35792468.1357924680, 46813579.2468135791, 41246813.5792468013
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter12(self):
        a, b, c = 57924681.3579246802, 68135792.4681357913, 62357924.6813579124
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter13(self):
        a, b, c = 79246813.5792468014, 81357924.6813579125, 75681357.9246813579
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter14(self):
        a, b, c = 92468135.7913579246, 135792468.0135792468, 112468135.7913579246
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

    def test_big_double_triangle_perimeter15(self):
        a, b, c = 246813579.12468035, 357924681.23579146, 298135792.46801357
        res = triangle.perimeter(a, b, c)
        self.assertAlmostEqual(res, a + b + c, 5)

