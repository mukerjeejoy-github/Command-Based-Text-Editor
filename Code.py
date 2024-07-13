import os

class Node:
    """A node in a doubly linked list."""

    def __init__(self, char):
        """
        Initialize a Node object.

        Args:
            char (str): The character value stored in the node.
        """

        self.char = char
        self.prev = None
        self.next = None


class TextEditor:
    """A text editor that supports basic editing operations."""

    def __init__(self, capacity=None):
        """
        Initializes a TextEditor object.

        Args:
            capacity (int, optional): The maximum capacity of the text editor in bytes. Defaults to None.
            file_size (int, optional): The maximum allowed input file size in bytes. Defaults to None.
        """
        self.head = None
        self.tail = None
        self.cursor_position = 0
        self.capacity = capacity or 40
        self.output_texts = []  # Added output_texts attribute
        self.remaining_capacity = self.capacity

    def __len__(self):
        """Returns the length of the doubly linked list."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def empty_text_editor(self):
        """Empties the entire doubly linked list and resets the cursor position to 0."""
        self.head = None
        self.tail = None
        self.cursor_position = 0
        self.remaining_capacity = self.capacity


    def handle_error(self, error_message):
        """
        Handles and prints the given error message.

        Args:
            error_message (str): The error message to handle.
        """
        print("Error:", error_message)


    def add_text(self, text):
        """
        Adds the text to the doubly linked list.

        Args:
            text (str): The text to add.
        """
        remaining_capacity = self.remaining_capacity
        
        if self.capacity is not None and len(text) >= remaining_capacity :
            self.handle_error("TextEditor is full. Cannot add more text.")
            return
        
        if text == '-':
            text = '-'  # Treat hyphen as normal text

        for char in text:
            new_node = Node(char)

            if self.cursor_position == 0:
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                else:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
            elif self.cursor_position >= len(self):
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                current = self.head
                count = 0

                while count < self.cursor_position:
                    current = current.next
                    count += 1

                new_node.prev = current.prev
                new_node.next = current
                current.prev.next = new_node
                current.prev = new_node

            self.cursor_position += 1
        self.remaining_capacity -= len(text)
           


    def delete_text(self, no_of_backspaces):
        """
        Deletes the character at the specified position before the cursor.

        Args:
            no_of_backspaces (int): The position on which the characters is to be deleted.
        """
        if not no_of_backspaces.isdigit():
            self.handle_error("Invalid number of backspaces. Please enter a positive integer.")
            return
        
        if self.cursor_position == 0:
            self.handle_error("Nothing to delete.")
            return

        count = 0
        current = self.head
        while count < self.cursor_position - int(no_of_backspaces):
            current = current.next
            count += 1

        if current.prev is None:
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
        else:
            current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev

        self.cursor_position -= min(int(no_of_backspaces), self.cursor_position)  # Correction made here
        self.remaining_capacity += 1


    def move_left(self, no_of_arrow_strokes):
        """
        Moves the cursor to the left by the specified number of positions.

        Args:
            no_of_arrow_strokes (int): The number of positions to move the cursor to the left.
        """
       
        if not no_of_arrow_strokes.isdigit():
            self.handle_error("Invalid number of arrow strokes. Please enter a positive integer.")
            return
        
        if self.cursor_position == 0:
            return

        if self.cursor_position - int(no_of_arrow_strokes) <= 0:
            self.cursor_position = 0
        else:
            self.cursor_position -= int(no_of_arrow_strokes)


    def move_right(self, no_of_arrow_strokes):
        """
        Moves the cursor to the right by the specified number of positions.

        Args:
            no_of_arrow_strokes (int): The number of positions to move the cursor to the right.
        """

        if not no_of_arrow_strokes.isdigit():
            self.handle_error("Invalid number of arrow strokes. Please enter a positive integer.")
            return
        
        text_length = len(self)
        if self.cursor_position == text_length:
            return

        if self.cursor_position + int(no_of_arrow_strokes) >= text_length:
            self.cursor_position = text_length
        else:
            self.cursor_position += int(no_of_arrow_strokes)


    def print_text(self):
        """Prints the text stored in the doubly linked list."""
        if self.head is None:
            self.handle_error("No text to print.")
            return
        
        current = self.head
        text = ""

        while current is not None:
            text += current.char
            print(current.char, end='')
            current = current.next

        self.output_texts.append(text)
        print()


    def generate_output_file(self, output_file_path):
        """
        Generates an output file containing all the texts generated in the text editor for each command.

        Args:
            output_file_path (str): The path of the output file to generate.
        """
        with open(output_file_path, 'w') as file:
            for text in self.output_texts:
                file.write(text + '\n')


def process_text_editor(text_editor):
    """
    Process the commands in the interactive mode of the text editor.

    Args:
        text_editor (TextEditor): The TextEditor object to process the commands on.
    """
    
    while True:
        command = input().split(' ', 1)
        if command[0] == 'Exit':
            break
        elif command[0] == 'AddText':
            if len(command) > 1 and len(command[1]) > 0 :
                text_editor.add_text(command[1])
            else:
                text_editor.handle_error("No text provided for AddText command.")
        elif command[0] == 'DeleteText':
            if len(command) > 1 and command[1].strip():
                text_editor.delete_text((command[1]))
            else:
                text_editor.handle_error("No number of backspaces provided for DeleteText command.")
        elif command[0] == 'MoveLeft':
            if len(command) > 1 and command[1].strip():
                text_editor.move_left((command[1]))
            else:
                text_editor.handle_error("No number of arrow strokes provided for MoveLeft command.")
        elif command[0] == 'MoveRight':
            if len(command) > 1 and command[1].strip():
                text_editor.move_right((command[1]))
            else:
                text_editor.handle_error("No number of arrow strokes provided for MoveRight command.")
        elif command[0] == 'PrintText':
            text_editor.print_text()
        elif command[0] == 'EmptyEditor':  # New command
            text_editor.empty_text_editor()
        else:
            text_editor.handle_error("Invalid command.")


def process_input_file(input_file_path, output_file_path, text_editor):
    """
    Processes the commands from an input file and generates an output file.

    Args:
        input_file_path (str): The path of the input file.
        output_file_path (str): The path of the output file to generate.
        text_editor (TextEditor): The TextEditor object to process the commands on.
    """

    # Validate File Path
    validate_file = os.path.isfile(input_file_path)
    if not (validate_file):
        text_editor.handle_error("File name or path does not exist.")
        return

    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace

            # Fetch command and arguments
            command_args = line.split(' ', 1)
            command = command_args[0]
            arguments = command_args[1] if len(command_args) > 1 else ''

            # Perform tasks based on the command
            if command == 'Exit':
                break
            elif command == 'AddText':
                text_editor.add_text(arguments)
            elif command == 'DeleteText':
                text_editor.delete_text((arguments))
            elif command == 'MoveLeft':
                text_editor.move_left((arguments))
            elif command == 'MoveRight':
                text_editor.move_right((arguments))
            elif command == 'PrintText':
                text_editor.print_text()
            else:
                text_editor.handle_error("Invalid command: " + command)
    text_editor.generate_output_file(output_file_path)


def select_capacity():
    """
    Allows the user to select the capacity of the data structure.

    Returns:
        int: The selected capacity in terms of characters.
    """

    capacity_choice = input("The default capacity is 40. Do you want to change it? (yes/no): ").strip()
    if capacity_choice.lower() in ['yes', 'y'] and capacity_choice.lower() not in ['no', 'n']:
        capacity_input = input("Enter the capacity: ").strip()
        if capacity_input and capacity_input.isdigit():
            try:
                capacity = int(capacity_input)
                if capacity <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid capacity. Using the default capacity of 40.")
                capacity = 40
        else:
            print("Invalid capacity. Using the default capacity of 40.")
            capacity = 40
    else:
        print("Using the default capacity of 40.")
        capacity = 40

    return capacity 


# Driver code
def main():
    print("Text Editor Program\n")
    while True:
        option = input("Select an option:\n1. Interactive Mode\n2. Test Mode(using input file)\nEnter your choice (1-2): ")

        if option == '1':
            capacity = select_capacity()
            text_editor = TextEditor(capacity=capacity)
            process_text_editor(text_editor)
        elif option == '2':
            text_editor = TextEditor()
            input_file_path = input("Enter the input file name or path: ")
            output_file_path = "output.txt"
            process_input_file(input_file_path, output_file_path, text_editor)
        else:
            print("Invalid choice.")
        
        run_again = input("Do you want to run another option? (yes/no): ")
        if run_again.lower() != 'yes':
            break

    print("Exiting...")

    
if __name__ == '__main__':
    main()