from django.test import TestCase
from .models import SurveyAnswer


class SurveyAnswerCase(TestCase):

    # MEDIAN UNIT TESTS

    def test_count_median_uneven(self):
        """
        This test checks if median is counted correctly when length of array is uneven.
        """
        sorted_list = [0, 1, 2, 5, 6]
        self.assertEqual(SurveyAnswer.count_median(sorted_list, len(sorted_list)), 2)

    def test_count_median_even(self):
        """
        This test checks if median is counted correctly when length of array is uneven.
        """
        sorted_list = [0, 1, 1, 5, 6, 10]
        self.assertEqual(SurveyAnswer.count_median(sorted_list, len(sorted_list)), 3)

    def test_count_median_on_0_elements(self):
        """
        This test checks if median is being returned when database is empty.
        """
        sorted_list = []
        self.assertEqual(SurveyAnswer.count_median(sorted_list, len(sorted_list)), 0)

    # WOMEN IN TECH ATTENDANCE

    def test_get_percentage_of_attendance(self):
        """
        This test checks if Women in Tech presence is counted correctly.
        """
        dict_of_attendance = [{
            'question4': 'Yes',
            'cnt': 70
        },
            {
                'question4': 'No',
                'cnt': 20
            },
            {
                'question4': 'Maybe',
                'cnt': 10
            }]
        count = 70 + 20 + 10
        self.assertEqual(SurveyAnswer.get_percentage_of_attendance(dict_of_attendance, count), '70.0%')

    def test_get_percentage_of_attendance_on_0_elements(self):
        """
        This test checks if Women in Tech presence is counted correctly when database is empty.
        """
        dict_of_attendance = []
        count = 0
        self.assertEqual(SurveyAnswer.get_percentage_of_attendance(dict_of_attendance, count), '0.0%')

    # AVERAGE UNIT TESTS


    # start of the excercise
    # uncomment below

    # def test_average(self):
    #     """
    #     This test checks if average is counted correctly.
    #     """
    #       # TODO: define sum_of_weather_notes as a list and expected_result
    #       self.assertEqual(SurveyAnswer.count_average(sum_of_weather_notes, len(list_of_weather_notes)), expected_result)
    #
    # def test_average_on_0_elements(self):
    #     """
    #     This test checks if average is counted correctly when database is empty.
    #     """
    #     # TODO: define sum_of_weather_notes as an empty list and expected_result as an average result
    #     self.assertEqual(SurveyAnswer.count_average(sum_of_weather_notes, len(list_of_weather_notes)), expected_result)