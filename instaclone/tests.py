from django.test import TestCase
from .models import User_prof, Image, Comments, User

# Create your tests here.
class User_profTestClass(TestCase):
    """ test that the use_prof is working """
    def setUp(self):
        """setting an instance of the class """
        self.new_user = User_prof(username = 'munga',bio = 'funny thing to say')


    def test_isinstance(self):
        """ checking instance truthyness """
        self.assertTrue(isinstance(self.new_user, User_prof))

    def test_save_user(self):
        """ checking the save function """
        self.new_user.save_prof()
        user2 = User_prof(username = "mbugua", bio = "the world revolves" ) 
        user2.save()

        _all = User_prof.objects.all()
        self.assertEqual(len(_all),2)

    def test_delete_funtction(self):
        """ testing the delete function """ 
        self.new_user.save_prof()
        user2 = User_prof(username = "mbugua", bio = "the world revolves" ) 
        user2.save_prof()
        
        user2.delete_prof()
        all = User_prof.objects.all()
        self.assertEqual(len(all),1)

    # def test_update(self):
    #     """ testing for the update of user """
    #     User_prof = 
        
