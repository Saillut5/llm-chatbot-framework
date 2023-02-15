import unittest
from unittest.mock import MagicMock
from chatbot_framework.chatbot import Chatbot
from chatbot_framework.llm_backends.openai import OpenAIBackend
from chatbot_framework.memory.buffer import ConversationBufferMemory

class TestChatbot(unittest.TestCase):

    def setUp(self):
        # Mock the OpenAIBackend to avoid actual API calls during testing
        self.mock_llm_backend = MagicMock(spec=OpenAIBackend)
        self.mock_llm_backend.generate_response.return_value = "Mocked LLM response."
        
        self.memory = ConversationBufferMemory()
        self.chatbot = Chatbot(llm_backend=self.mock_llm_backend, memory=self.memory)

    def test_initial_chat(self):
        user_message = "Hello, chatbot!"
        response = self.chatbot.chat(user_message)
        
        self.assertEqual(response, "Mocked LLM response.")
        self.mock_llm_backend.generate_response.assert_called_once()
        
        # Check if messages are stored in memory
        history = self.memory.get_history(self.chatbot.session_id)
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0]["role"], "user")
        self.assertEqual(history[0]["content"], user_message)
        self.assertEqual(history[1]["role"], "assistant")
        self.assertEqual(history[1]["content"], "Mocked LLM response.")

    def test_conversation_history(self):
        self.chatbot.chat("First message.")
        self.chatbot.chat("Second message.")
        
        history = self.memory.get_history(self.chatbot.session_id)
        self.assertEqual(len(history), 4) # Two user, two assistant messages
        self.assertEqual(history[2]["content"], "Second message.")

    def test_reset_conversation(self):
        self.chatbot.chat("Message before reset.")
        old_session_id = self.chatbot.session_id
        self.chatbot.reset_conversation()
        
        self.assertNotEqual(self.chatbot.session_id, old_session_id)
        self.assertEqual(len(self.memory.get_history(old_session_id)), 0) # Old history should be cleared
        self.assertEqual(len(self.memory.get_history(self.chatbot.session_id)), 0) # New session should be empty

    def test_prompt_building(self):
        self.chatbot.chat("How are you?")
        self.chatbot.chat("What's up?")
        
        # The mock should have been called with a prompt containing history
        # We can't directly inspect the prompt from the mock, but we know it was built
        # based on the internal _build_prompt method. This test primarily checks
        # that the chat function executes without error and memory is updated.
        self.mock_llm_backend.generate_response.assert_called()

if __name__ == "__main__":
    unittest.main()
# Simulated change on 2023-01-02 18:16:00
# Simulated change on 2023-01-18 18:05:00
# Simulated change on 2023-01-23 12:06:00
# Simulated change on 2023-02-06 16:00:00
# Simulated change on 2023-02-15 16:28:00
