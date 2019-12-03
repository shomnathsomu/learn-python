# inherit another class
from Chef import Chef


class ChineseChef(Chef):

    def make_special_dish(self):
        print("The chef makes orange chicken")

    @staticmethod
    def make_fried_rice():
        print("The chef makes fried rice")
