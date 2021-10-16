from django.test import TestCase
from .models import Item


class TestViews(TestCase):
    def test_get_todo_list(self):
        """
        Testing the http response with django's built in client and that the
        correct template is used
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        """
        Testing the http response with django's built in client and that the
        correct template is used
        """
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        """
        Testing the http response with django's built in client, test using a
        Item object and creating instance, and that correct template is used.
        """
        item = Item.objects.create(name='Test To Do Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        """
        Testing the http response with django's built in client, test using a
        Item object and creating instance, and that correct template is used.
        """
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        """
        Testing the http response with django's built in client, test create an
        item and deleting it. Also that the correct template is used.
        """
        item = Item.objects.create(name='Test To Do Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)


    def test_can_toggle_item(self):
        """
        Testing the http response with django's built in client, test create an
        item and deleting it. Also that the correct template is used.
        """
        item = Item.objects.create(name='Test To Do Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
