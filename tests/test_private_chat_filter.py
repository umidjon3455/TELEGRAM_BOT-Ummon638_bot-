import unittest
from types import SimpleNamespace

from filters.private_chat import ChatPrivateFilter


class ChatPrivateFilterTests(unittest.IsolatedAsyncioTestCase):
    async def test_private_filter_accepts_private_chat(self):
        chat = SimpleNamespace(type="private")
        self.assertTrue(await ChatPrivateFilter(["private"])(SimpleNamespace(chat=chat)))

    async def test_private_filter_rejects_group_chat(self):
        chat = SimpleNamespace(type="group")
        self.assertFalse(await ChatPrivateFilter(["private"])(SimpleNamespace(chat=chat)))

    async def test_filter_accepts_a_single_chat_type(self):
        chat = SimpleNamespace(type="group")
        self.assertTrue(await ChatPrivateFilter("group")(SimpleNamespace(chat=chat)))


if __name__ == "__main__":
    unittest.main()
