import argparse
from SetupLogger import setup_logging

class User:

    """
    A class to represent a user in an AI chat application.

    This class provides functionalities for a user to interact with an AI chat system.
    It allows the user to ask questions, view their message history, and receive responses
    from an AI model. The class includes methods to simulate AI interactions and determine
    whether a response is experimental or accepted.

    Attributes:
    - username (str): The username of the user.
    - message_history (list): A list to store the history of messages (questions and responses).

    Methods:
    - view_message_history(): Displays the user's message history.
    - ask_question(question, ai_model): Allows the user to ask a question to an AI model.
    - get_ai_response(question, ai_model): Simulates getting a response from an AI model.
    - is_experimental(question): Determines if a query is experimental.
    """

    def __init__(self, username):

        """
        Constructor for the User class.

        Parameters:
        - username (str): Username of the user.

        Initializes a new user with a username and an empty message history.
        """

        self.username = username
        self.message_history = []

    def view_message_history(self):

        """
        Method to display the user's message history.

        Iterates over the message history and prints each message.
        """

        for message in self.message_history:
            print(message)

    def ask_question(self, question, ai_model):

        """
        Method for the user to ask a question to an AI model.

        Parameters:
        - question (str): The question asked by the user.
        - ai_model (str): The AI model to be used for generating a response.

        The method simulates asking a question to an AI model, receives a response,
        appends the question and response to the message history, and returns the response.

        Returns:
        - str: The response generated by the AI model.
        """

        # Simulate asking a question to an AI model
        response = self.get_ai_response(question, ai_model)
        self.message_history.append((question, response))
        return response

    def get_ai_response(self, question, ai_model):

        """
        Private method to simulate getting a response from an AI model.

        Parameters:
        - question (str): The question asked by the user.
        - ai_model (str): The AI model to be used for generating a response.

        This method simulates an AI response. In a real scenario, this would be replaced
        with actual AI response logic. It also determines if the response is experimental
        based on the question content.

        Returns:
        - str: The simulated AI response.
        """

        # Simulate AI response (this would be replaced with actual AI response logic)
        is_experimental = self.is_experimental(question)
        response_label = "Experimental" if is_experimental else "Accepted"
        return f"AI Response ({response_label}): [Simulated response to '{question}' using {ai_model}]"

    def is_experimental(self, question):

        """
        Private method to check if a query is experimental.

        Parameters:
        - question (str): The question asked by the user.

        This method simulates a check to determine if a query is experimental.
        In a real application, this would involve more complex logic.

        Returns:
        - bool: True if the query is experimental, False otherwise.
        """

        # Simulate check for experimental query
        return "new" in question.lower()

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Interact with an AI chat system as a user.")
    parser.add_argument("username", type=str, help="Username of the user.")
    parser.add_argument("question", type=str, help="Question to ask the AI model.")
    parser.add_argument("ai_model", type=str, help="AI model to use for generating a response.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Create an instance of the User class with the provided username
    user = User(args.username)
    
    # Set up logging and obtain a logger instance
    logger = setup_logging() 

    # Simulate asking a question to the AI model
    response = user.ask_question(args.question, args.ai_model)

    # Log and print the response
    logger.info("AI Response: %s", response)
    print("AI Response:", response)

    # Log and optionally view the entire message history
    logger.info("Complete Message History:")
    print("\nComplete Message History:")
    user.view_message_history()