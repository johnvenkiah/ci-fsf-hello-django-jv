from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test To Do Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test To Do Item')
        # confirm that the name is returned when rendering the item as string
        self.assertEqual(str(item), 'Test To Do Item')
