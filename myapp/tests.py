from django.test import TestCase
from .models import MyModel  # Assure-toi d'importer le modèle si ce n'est pas déjà fait

class MyModelTest(TestCase):
    def test_model_creation(self):
        # Créer un objet MyModel
        obj = MyModel.objects.create(name="Test Object")
        
        # Vérifier que l'objet a été créé et que son nom est correct
        self.assertEqual(obj.name, "Test Object")
        self.assertTrue(MyModel.objects.exists())
