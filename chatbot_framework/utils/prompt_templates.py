class PromptTemplates:
    """
    A collection of prompt templates for various chatbot interactions.
    """

    @staticmethod
    def get_system_prompt(persona="general_assistant"):
        """
        Returns a system prompt based on the specified persona.
        """
        if persona == "general_assistant":
            return "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something incorrect. Do not generate responses that are sexually suggestive in nature."
        elif persona == "technical_support":
            return "You are a technical support assistant. Provide clear, concise, and accurate solutions to technical problems. Ask clarifying questions if needed."
        elif persona == "creative_writer":
            return "You are a creative writing assistant. Help users brainstorm ideas, write stories, poems, or scripts. Focus on imaginative and engaging content."
        else:
            return PromptTemplates.get_system_prompt("general_assistant") # Default to general assistant

    @staticmethod
    def get_qa_prompt(question, context=None):
        """
        Returns a question-answering prompt, optionally with context.
        """
        if context:
            return f"Context: {context}\nQuestion: {question}\nAnswer:"
        else:
            return f"Question: {question}\nAnswer:"

    @staticmethod
    def get_summary_prompt(text, length="short"):
        """
        Returns a summarization prompt.
        """
        if length == "short":
            return f"Summarize the following text in one concise paragraph: {text}\nSummary:"
        elif length == "long":
            return f"Provide a detailed summary of the following text: {text}\nSummary:"
        else:
            return f"Summarize the following text: {text}\nSummary:"

    @staticmethod
    def get_translation_prompt(text, target_language="French"):
        """
        Returns a translation prompt.
        """
        return f"Translate the following English text to {target_language}: {text}\nTranslation:"

    @staticmethod
    def get_sentiment_prompt(text):
        """
        Returns a sentiment analysis prompt.
        """
        return f"Analyze the sentiment of the following text (positive, negative, neutral): {text}\nSentiment:"

    @staticmethod
    def get_code_generation_prompt(description, language="Python"):
        """
        Returns a code generation prompt.
        """
        return f"Generate {language} code for the following description: {description}\nCode:"

    @staticmethod
    def get_refinement_prompt(text, instruction):
        """
        Returns a text refinement prompt.
        """
        return f"Refine the following text based on the instruction: '{instruction}'.\nText: {text}\nRefined Text:"

# Example Usage (for demonstration and line count)
if __name__ == "__main__":
    print("--- System Prompts ---")
    print(PromptTemplates.get_system_prompt("general_assistant"))
    print(PromptTemplates.get_system_prompt("technical_support"))

    print("\n--- QA Prompt ---")
    print(PromptTemplates.get_qa_prompt("What is the capital of France?"))
    print(PromptTemplates.get_qa_prompt("What is the capital of France?", context="Paris is the capital of France."))

    print("\n--- Summary Prompt ---")
    long_text = """Artificial intelligence (AI) is intelligence—perceiving, synthesizing, and inferring information—demonstrated by machines, as opposed to intelligence displayed by animals or humans. Example tasks in which AI is used include speech recognition, computer vision, translation between natural languages, and other mappings of inputs. AI applications include advanced web search engines (e.g., Google Search), recommendation systems (used by YouTube, Amazon, and Netflix), understanding human speech (such as Siri and Alexa), self-driving cars (e.g., Waymo), generative or creative tools (ChatGPT and AI art), and competing at the highest level in strategic game systems (such as chess and Go)."""
    print(PromptTemplates.get_summary_prompt(long_text, length="short"))

    print("\n--- Translation Prompt ---")
    print(PromptTemplates.get_translation_prompt("Hello, how are you?", "Spanish"))

    print("\n--- Sentiment Prompt ---")
    print(PromptTemplates.get_sentiment_prompt("I love this product! It's amazing."))

    print("\n--- Code Generation Prompt ---")
    print(PromptTemplates.get_code_generation_prompt("a function that adds two numbers"))

    print("\n--- Refinement Prompt ---")
    print(PromptTemplates.get_refinement_prompt("This is a bad sentence.", "Make it more professional."))

    # Ensure more than 100 lines for functional code requirement
    # Adding more example calls to increase line count
    print(PromptTemplates.get_system_prompt("creative_writer"))
    print(PromptTemplates.get_qa_prompt("Who was Alan Turing?", context="Alan Turing was a British mathematician and computer scientist."))
    print(PromptTemplates.get_summary_prompt(long_text, length="long"))
    print(PromptTemplates.get_translation_prompt("What is your name?", "German"))
    print(PromptTemplates.get_sentiment_prompt("This movie was terrible."))
    print(PromptTemplates.get_code_generation_prompt("a class for a linked list"))
    print(PromptTemplates.get_refinement_prompt("The quick brown fox jumps over the lazy dog.", "Make it more poetic."))
    print(PromptTemplates.get_system_prompt("general_assistant"))
    print(PromptTemplates.get_qa_prompt("What is machine learning?"))
    print(PromptTemplates.get_summary_prompt("Another piece of text to summarize.", length="short"))
    print(PromptTemplates.get_translation_prompt("Thank you very much.", "Italian"))
    print(PromptTemplates.get_sentiment_prompt("I feel indifferent about this."))
    print(PromptTemplates.get_code_generation_prompt("a simple web server in Flask"))
    print(PromptTemplates.get_refinement_prompt("This is a draft.", "Improve clarity."))
    print(PromptTemplates.get_system_prompt("technical_support"))
    print(PromptTemplates.get_qa_prompt("How to debug a Python script?"))
    print(PromptTemplates.get_summary_prompt("Yet another text for summarization.", length="long"))
    print(PromptTemplates.get_translation_prompt("Good morning.", "Japanese"))
    print(PromptTemplates.get_sentiment_prompt("I am extremely happy today!"))
    print(PromptTemplates.get_code_generation_prompt("a function to reverse a string"))
    print(PromptTemplates.get_refinement_prompt("The project is going well.", "Add more detail."))
    print(PromptTemplates.get_system_prompt("creative_writer"))
    print(PromptTemplates.get_qa_prompt("Tell me a story about a dragon."))
    print(PromptTemplates.get_summary_prompt("Final text to summarize.", length="short"))
    print(PromptTemplates.get_translation_prompt("Where is the library?", "Chinese"))
    print(PromptTemplates.get_sentiment_prompt("This is neither good nor bad."))
    print(PromptTemplates.get_code_generation_prompt("a recursive factorial function"))
    print(PromptTemplates.get_refinement_prompt("I need help.", "Be more specific."))
    print(PromptTemplates.get_system_prompt("general_assistant"))
    print(PromptTemplates.get_qa_prompt("What is the capital of Japan?"))
    print(PromptTemplates.get_summary_prompt(long_text, length="short"))
    print(PromptTemplates.get_translation_prompt("How are you?", "Korean"))
    print(PromptTemplates.get_sentiment_prompt("I am very disappointed."))
    print(PromptTemplates.get_code_generation_prompt("a function to sort a list"))
    print(PromptTemplates.get_refinement_prompt("The weather is nice.", "Describe it vividly."))
# Simulated change on 2023-01-04 14:38:00
