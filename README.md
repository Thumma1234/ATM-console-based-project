# ATM-console-based-project
# Simple ATM Simulator (Python)

This Python script provides a basic ATM simulator with functionalities for withdrawal, deposit, PIN generation, mini-statement, and balance inquiry.

## Features

* **Withdrawal:** Allows users to withdraw funds after verifying their account number and PIN.
* **Deposit:** Enables users to deposit funds into their accounts.
* **PIN Generation:** Allows users to create or reset their PIN.
* **Mini-Statement:** Displays account details, including name, account number, date of birth, and balance.
* **Balance Inquiry:** Shows the current account balance.
* **Account Data:** Account information is stored in a Python dictionary.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Running the Code

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    ```
2.  **Navigate to the directory containing the Python script.**
3.  **Run the script:**
    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file.)

### Usage

1.  The program will display a welcome message and a menu of options.
2.  Enter the number corresponding to your desired action.
3.  Follow the on-screen prompts to enter your account number and PIN as required.
4.  The program will execute the chosen action and display the result.
5.  Repeat steps 2-4 for other transactions.
6.  To exit, enter `6`.

## Code Explanation

* The `accounts` dictionary stores account data (account number, name, date of birth, balance, and PIN).
* `dobm` dictionary stores the month number to month name mapping.
* The `while True` loop keeps the ATM running until the user chooses to exit.
* `if` and `elif` statements handle the different menu options.
* Input validation checks if the account exists, and if the pin is correct.
* String splitting is used to reformat the date of birth.

## Example Account Data

The script initializes with the following example accounts:

```python
accounts = {
    1111 : ["sowmya","12-12-2002",10000,1234],
    2222 : ["sandhya","30-04-2001",20000,1020],
    3333 : ["rani","01-01-2003",5000,None],
    4444 : ["ram","02-02-2003",15000,2468],
}
