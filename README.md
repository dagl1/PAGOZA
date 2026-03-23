


________________________________________________
Required installations:

- Node.js (v14 or higher)
  - Download and install from https://nodejs.org/
  - Verify installation by running `node -v` in your terminal.
  - NPM (Node Package Manager) comes bundled with Node.js.
  - Verify installation by running `npm -v` in your terminal.
  - Optional: Install Yarn as an alternative package manager
    - Install via npm: `npm install -g yarn`
    - Verify installation by running `yarn -v` in your terminal.

- Git
  - Download and install from https://git-scm.com/
  - Verify installation by running `git --version` in your terminal.


____________________________________
Required actions:

- Github token setup:
  - Go to your GitHub account settings.
  - Navigate to "Developer settings" > "Personal access tokens".
  - Click on "Generate new token".
  - Select the necessary scopes for your project (read & write access).
    - Contents
    - Issues
    - Pull requests
    - Any additional scopes, eg. workflows
  - Generate the token and copy it securely.
  - Set the token as an environment variable in your terminal:
    - On macOS/Linux: `export GITHUB_TOKEN=your_token_here`
    - On Windows (Command Prompt): `set GITHUB_TOKEN=your_token_here`
    - On Windows (PowerShell): `$env:GITHUB_TOKEN="your_token_here"`


- Clone the repository:
  - Open your terminal.
  - Run the command: `git clone`
  - Navigate into the project directory: `cd your-repo-name`

- Run bootstrap.sh:
  - In the project directory (preferably using git Bash):
`./bootstrap.sh` (macOS/Linux) or `bootstrap.bat` (Windows terminal)
  - This script will install all necessary dependencies and set up the project environment.


________________________________________________

