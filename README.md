
# Selenium Automation Script for Gmail Login

This Python script automates the process of logging into multiple Gmail accounts using Selenium WebDriver. It reads email and password combinations from a CSV file and sequentially logs into each account.

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/prajxwal/Selenium-Automation-Script-for-Gmail-Login.git
    cd Selenium-Automation-Script-for-Gmail-Login
    ```

2. **Prepare CSV file**:
   
   - Add Gmail account credentials to `CSD.csv` in the format:
     ```csv
     Email,Password
     user1@gmail.com,password1
     user2@gmail.com,password2
     ```

## Usage

3. **Run the script**:

    ```bash
    python script.py
    ```

    The script will sequentially open Chrome, log into each Gmail account, and print login status to the console.

## Notes

- Ensure your Chrome browser is up to date.
- Consider the security implications of storing passwords in plaintext.
- Customize timeout settings in the script (`script.py`) as per your network conditions.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.


