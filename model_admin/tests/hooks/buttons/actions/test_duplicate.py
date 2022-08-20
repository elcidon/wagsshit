from unittest.mock import patch
from django.test import TestCase
from django.db import models

from model_admin.hooks.buttons.actions.duplicate import DuplicateObject


class MockedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("title", max_length=255)
    slug = models.CharField("slug", max_length=255)
    another_field = models.CharField("Another Field", max_length=255, unique=True)
    max_lgt_field = models.CharField("Max LGT Field", max_length=10, unique=True)


class TestDuplicateUtils(TestCase):

    def setUp(self) -> None:
        self.obj = MockedModel(
            pk="MEU_UUID",
            slug="slug-1",
            title="Titulo do meu objeto",
            another_field="Outro",
            max_lgt_field="max length"
        )

    def test_concatenate_COPY_to_field(self):
        """Should concatenate COPY as prefix of field. If slug passed, must `slugify` the text"""
        title_result = DuplicateObject._set_copy_to_text(self.obj, "title")
        title_expected = "COPY Titulo do meu objeto"

        self.assertEqual(title_result, title_expected)

        slug_result = DuplicateObject._set_copy_to_text(self.obj, "slug")
        slug_expected = "copy-slug-1"

        self.assertEqual(slug_result, slug_expected)

    @patch.object(MockedModel, 'save')
    def test_duplicate_object_without_set_COPY_as_prefix(self, mocked_model_save):
        """Should duplicate the object"""
        DuplicateObject.do(self.obj)
        self.assertTrue(mocked_model_save.called)
        self.assertEqual(self.obj.title, "Titulo do meu objeto")
        self.assertEqual(self.obj.slug, "slug-1")

    @patch.object(MockedModel, 'save')
    def test_check_all_fields_to_duplicate(self, mocked_model_save):
        """should fetch all fields to duplicate and set the prefix copy to each of them."""
        self.obj.UNIQUE_FIELDS_TO_DUPLICATE = ["title", "slug"]
        DuplicateObject.do(self.obj)
        self.assertTrue(mocked_model_save.called)
        self.assertEqual(self.obj.title, "COPY Titulo do meu objeto")
        self.assertEqual(self.obj.slug, "copy-slug-1")

    @patch.object(MockedModel, 'save')
    def test_auto_import_unique_fields(self, mocked_model_save):
        DuplicateObject.do(self.obj)
        self.assertEqual(self.obj.another_field, "COPY Outro")

    @patch.object(MockedModel, 'save')
    def test_field_max_length(self, mocked_model_save):
        """Should return stripped text if limit go over of the maximum length."""
        DuplicateObject.do(self.obj)
        self.assertEqual(self.obj.max_lgt_field, "COPY max l")

