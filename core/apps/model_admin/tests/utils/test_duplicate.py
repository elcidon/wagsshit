from unittest.mock import patch, Mock
from django.test import TestCase
from apps.model_admin.utils.duplicate import DuplicateObject


class TestDuplicateUtils(TestCase):

    def setUp(self) -> None:
        self.obj = Mock(pk="MEU_UUID", slug="slug-1", title="Titulo do meu objeto", save=Mock(return_value=True))

    def test_concatenate_COPY_to_field(self):
        """Should concatenate COPY as prefix of field. If slug passed, must `slugify` the text"""
        title_result = DuplicateObject._set_copy_to_text(self.obj, "title")
        title_expected = "COPY Titulo do meu objeto"

        self.assertEqual(title_result, title_expected)

        slug_result = DuplicateObject._set_copy_to_text(self.obj, "slug")
        slug_expected = "copy-slug-1"

        self.assertEqual(slug_result, slug_expected)

    def test_duplicate_object_without_set_COPY_as_prefix(self):
        """Should duplicate the object """
        DuplicateObject.do(self.obj)
        self.obj.save.assert_called_with()
        self.assertEqual(self.obj.title, "Titulo do meu objeto")
        self.assertEqual(self.obj.slug, "slug-1")

    def test_check_all_fields_to_duplicate(self):
        """should fetch all fields to duplicate and set the prefix copy to each of them."""
        self.obj.UNIQUE_FIELDS_TO_DUPLICATE = ["title", "slug"]
        DuplicateObject.do(self.obj)
        self.obj.save.assert_called_with()
        self.assertEqual(self.obj.title, "COPY Titulo do meu objeto")
        self.assertEqual(self.obj.slug, "copy-slug-1")
