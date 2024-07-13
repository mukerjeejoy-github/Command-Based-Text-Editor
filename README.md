# Command-Based-Text-Editor
A command based text-editor using doubly-linked-list

1. Usage of Double-Linked List data structure.
   
2. All data structure insert and delete operations throw appropriate messages when their capacity is empty or full. Basic error handling is implemented.
   
3. For the purposes of testing, we have functions to print the data structures or other test data. But all such functions are commented.
   
4. The input, prompt, and output samples shown here are only a representation of the syntax to be used. Hence, no hard coded values are used in the code.
   
5. Run time analysis is provided in asymptotic notations and not timestamp-based runtimes in seconds or milliseconds.
   
6. Design document includes:
   a. The data structure model chosen with justifications
   b. Details of each operation with the time complexity and reasons why the chosen operations are efficient for the given representation
   c. One alternate way of modeling the problem with the cost implications.

## Operations
### Commands

The following commands are supported by the system:

- **AddText**: Adds the text to the linked-list.
- **DeleteText**: Deletes the text.
- **MoveLeft / MoveRight**: Moves the cursor left or right.
- **PrintText**: Prints the text in the linked-list.

The commands follow a specific format:

- **AddText**:
  ```md
  <command> <space> <string> <newline>
  ```
- **DeleteText**
  ```md
  <command> <space> <no_of_backspace_strokes> <newline>
  ```
- **MoveLeft / MoveRight**
  ```md
  <command> <space> <no_of_arrow_key_strokes> <newline>
  ```
- **PrintText**
  ```md
  <command> <newline>
  ```

### Sample Input

  ```md
  AddText HW
  MoveLeft 2
  AddText -
  PrintText
  MoveRight 1
  AddText ell
  PrintText
  MoveRight 20
  AddText orld
  PrintText
  MoveLeft 30
  MoveRight 1
  DeleteText 4
  PrintText
  MoveLeft 4
  AddText o
  PrintText
  ```

  ### Sample Output

  ```md
  -HW
  -HellW
  -HellWorld
  HellWorld
  HelloWorld
 ```
