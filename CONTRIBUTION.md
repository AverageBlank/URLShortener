# Contributing to URLShortener

Thank you for your interest in contributing to **URLShortener**! We welcome contributions to help improve this project, whether it’s bug fixes, new features, or documentation improvements. Please review the guidelines below to get started.

## Getting Started

1. **Fork the repository**: Click on the "Fork" button at the top of this repository.
2. **Clone your fork**: Clone the forked repository to your local environment.

```bash
git clone https://github.com/your-username/URLShortener.git
```

## Setting Up Locally

### Prerequisites

Make sure you have Python and MongoDB installed on your system.

- **[Python](https://www.python.org/downloads/)**: Download and install Python.
- **[MongoDB](https://docs.mongodb.com/manual/installation/)**: Follow the installation guide for MongoDB.
- **[MongoDB Compass](https://www.mongodb.com/products/compass)**: Download and install MongoDB Compass for a GUI to interact with MongoDB.

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/AverageBlank/URLShortener.git
   cd URLShortener
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On bash use `source venv/bin/activate`
   ```

3. **Install the required libraries**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   - Create a `.env` file in the root directory of the project.
   - Add your MongoDB URI and a secret key in the `.env` file. For example:
     ```env
     link={your_mongodb_uri}
     SECRET_KEY={your_secret_key}
     ```

5. **Run MongoDB**

   - Start the MongoDB server. If you installed MongoDB locally, you can start it with the following command:
     ```bash
     mongod
     ```

6. **Connect to MongoDB with MongoDB Compass**

   - Open MongoDB Compass.
   - In the "New Connection" window, enter your MongoDB URI in the connection string field (this is the same URI you put in the `.env` file).
   - Click "Connect" to connect to your MongoDB server.
   - You can now view and manage your databases and collections through the Compass GUI.

7. **Run the application**

   ```bash
   flask --app app run
   ```

8. **Open your browser**
   - Navigate to `http://127.0.0.1:5000/` to see the application running locally.

## Making Changes

To ensure a smooth contribution process, please follow these guidelines when making changes to the **URLShortener** project:

- **Align with Project Goals**: Ensure that your changes align with the purpose of a URL shortener. New features should add relevant value and be within the scope of this project.
- **Document Your Code**: Use comments to clarify complex parts of your code. Make sure that any new functions, classes, or modules are well-documented to help future contributors understand their purpose.

### Code Style

- **Python Code**: Adhere to PEP 8 standards. Keep functions and methods concise, modular, and single-purpose.
- **HTML/CSS/JavaScript**: Follow best practices. Use semantic HTML, modular and responsive CSS, and clean, well-structured JavaScript.
- **Naming Conventions**: Choose descriptive, consistent names for variables, functions, and files. Also use camelCase.
- **Comments**: Only add comments where they help explain complex logic. Keep comments clear and concise.

### Commit Messages

- Write clear, concise, and descriptive commit messages.
- Use the present tense (e.g., "Fix broken redirect logic").
- Reference issues using `#issue-number` if your changes are related to an existing issue.
  - Example: `Fix #45 - Add custom validation for URL input`

## Testing Your Changes

Before creating a pull request, please test your changes by:

1. **Running Tests**: Run any existing tests to ensure your changes haven’t broken anything.
   - If the project uses a test framework, ensure that all tests pass.
2. **Browser Testing**: Test the application in different browsers to confirm functionality and layout.
3. **Checking Responsiveness**: Ensure the application works on various screen sizes and devices.
4. **Manual Testing**: Test different scenarios manually, including edge cases (e.g., invalid URLs, duplicate URLs) to confirm your code handles them correctly.

## Submitting a Pull Request

Once you have completed your changes and thoroughly tested them, you can submit a pull request (PR):

1. **Push Your Branch**: Push your branch to your forked repository.
   ```bash
   git push origin feature/your-feature-name
   ```
2. **Open a Pull Request**: Go to the original **URLShortener** repository on GitHub and open a pull request (PR) from your branch. Follow these steps when creating the PR:

   - **Title**: Use a descriptive title that summarizes your changes, such as "Fix redirect issue for invalid URLs" or "Add analytics tracking for URL clicks".
   - **Base and Compare Branches**: Set the base branch to `main` (or whichever branch is specified by the project) and the compare branch to the feature branch you created.
   - **Description**: Provide a detailed description in the PR. This should include:
     - **Summary of Changes**: Explain what changes you’ve made and why.
     - **Issue Link**: Reference any related issues by mentioning `#issue-number` if applicable.
     - **Testing and Verification**: Describe the tests you’ve run to verify the functionality of your code, including specific scenarios or edge cases tested.
     - **Known Issues**: If there are any known limitations or areas needing further work, mention them here.

3. **Label and Assign Reviewers** (optional): If the repository has specific labels or allows contributors to assign reviewers, feel free to add relevant labels (e.g., `enhancement`, `bug`) or request a review from the appropriate maintainers.

4. **Keep Your Branch Updated**: If there are new commits on the `main` branch after you create your PR, update your branch to include these changes:
   ```bash
   git fetch origin
   git checkout feature/your-feature-name
   git merge origin/main
   ```
5. **Respond to Feedback**: After submitting your pull request, maintainers may review it and provide feedback or request changes. Here’s how to handle any feedback you receive:

   - **Make the Changes**: Apply any suggested updates directly on your feature branch.
   - **Commit and Push**: Once you’ve made the requested changes, commit them to your branch and push the updates to your fork.
     ```bash
     git add .
     git commit -m "Address feedback: update URL validation logic"
     git push origin feature/your-feature-name
     ```
   - **Update the PR**: The pull request will automatically update to include your latest commits. Consider adding a comment to the PR to summarize the changes made in response to the feedback, especially if multiple rounds of feedback are provided.

   > **Tip**: Stay engaged and respond promptly to feedback to ensure a smooth review process. If you disagree with any suggestions, feel free to open a respectful discussion within the PR comments.

6. **Merge Approval and Final Steps**: Once all feedback is addressed and maintainers approve your PR, it will be merged into the `main` branch. After merging, you can do a few optional clean-up steps:

   - **Delete Your Branch**: To keep your repository tidy, delete the feature branch from both your local machine and GitHub fork.
     ```bash
     git branch -d feature/your-feature-name
     git push origin --delete feature/your-feature-name
     ```
   - **Sync Your Fork**: To keep your fork up-to-date with the original repository, pull the latest changes from the `main` branch:
     ```bash
     git checkout main
     git pull upstream main
     git push origin main
     ```

7. **Celebrate Your Contribution** 🎉: Congratulations! Your contribution is now part of the **URLShortener** project. Thank you for helping improve the project and making it better for everyone.

## Additional Tips for Contributors

- **Stay Organized**: Keeping your branches organized and regularly updating your fork helps streamline the contribution process and reduces potential conflicts.
- **Be Open to Learning**: Don’t hesitate to ask questions if you’re unsure about any part of the codebase or the contribution process.
- **Document Complex Changes**: For large or complex contributions, consider adding detailed documentation or comments to assist future contributors.

Thank you for contributing to **URLShortener**! Your contributions make this project a valuable tool for all users.
