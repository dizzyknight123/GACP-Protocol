# Contribution Guide

Welcome to the GACP Protocol community! We greatly appreciate your contributions to the project. This guide will help you understand how to participate in the development and improvement of the GACP Protocol.

## Table of Contents

- [Contribution Guide](#contribution-guide)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [Ways to Contribute](#ways-to-contribute)
  - [Development Environment Setup](#development-environment-setup)
  - [Code Commit Guidelines](#code-commit-guidelines)
  - [Branch Management Strategy](#branch-management-strategy)
  - [Pull Request Process](#pull-request-process)
  - [Code Review Standards](#code-review-standards)
  - [Testing Guide](#testing-guide)
  - [Documentation Contributions](#documentation-contributions)
  - [Issue Reporting](#issue-reporting)
  - [Feature Requests](#feature-requests)
  - [GIP Proposals](#gip-proposals)
  - [Community Communication](#community-communication)

## Code of Conduct

To maintain a friendly and inclusive community environment, we expect all contributors to adhere to the following code of conduct:

- **Respect others**: Be polite and respectful to other contributors and users
- **Embrace diversity**: Welcome contributors from different backgrounds and experience levels
- **Constructive communication**: Provide constructive feedback and suggestions
- **Focus on issues**: Keep discussions focused on technical issues and solutions
- **Avoid personal attacks**: No personal attacks, insults, or discriminatory remarks

## Copyright Attribution

- The copyright of code you contribute belongs to you
- The copyright of community-contributed code belongs to the contributors
- The overall project is licensed under the Apache 2.0 license

## Contribution Process

1. **Fork the repository**
   Fork the GACP Protocol repository on GitHub to your own account.

2. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/GACP-Protocol.git
   cd GACP-Protocol
   ```

3. **Create a branch**
   Create a new feature branch or fix branch from the `develop` branch.

4. **Develop and test**
   Develop on the new branch and ensure all tests pass.

5. **Commit code**
   Follow the code commit guidelines and include copyright information in the commit message.

6. **Push to remote**
   ```bash
   git push origin feature/feature-name
   ```

7. **Create a Pull Request**
   Create a Pull Request on GitHub from your branch to the `develop` branch.

8. **Code review**
   The core team will review your code and may request some modifications.

9. **Merge**
   After review is complete, your code will be merged into the `develop` branch.

## Ways to Contribute

You can contribute to the GACP Protocol in many ways:

1. **Code contributions**: Submit bug fixes, new features, or performance optimizations
2. **Documentation contributions**: Improve documentation, add examples, or translations
3. **Testing contributions**: Write test cases, report bugs, or improve test coverage
4. **Community support**: Answer questions, participate in discussions, or help other users
5. **GIP proposals**: Submit protocol improvement suggestions

## Development Environment Setup

### Prerequisites

- Python 3.10 or higher
- Git
- Text editor or IDE (VS Code, PyCharm, etc. recommended)

### Steps

1. **Fork the repository**
   Fork the GACP Protocol repository on GitHub to your own account.

2. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/GACP-Protocol.git
   cd GACP-Protocol
   ```

3. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   Copy the `.env.example` file to `.env` and fill in the corresponding API Key if needed.

6. **Run tests**
   ```bash
   python -m pytest 03-Test/
   ```

## Code Commit Guidelines

To maintain consistency and maintainability of the codebase, we follow the following code commit guidelines:

### Commit Message Format

```
<type>(<scope>): <description>

<detailed description>

<optional footer information>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation update
- **style**: Code style adjustment (no functional impact)
- **refactor**: Code refactoring (no new features or bug fixes)
- **test**: Test-related modifications
- **chore**: Build process or auxiliary tool modifications

### Scope

The scope can be a module name, file path, or functional area, for example:
- `requirement_parser`
- `contract_generator`
- `docs`
- `test`

### Example

```
feat(requirement_parser): Add natural language parsing enhancement

- Added parsing capability for complex requirements
- Optimized parsing algorithm performance
- Added more test cases

Closes #123
```

## Branch Management Strategy

We adopt the following branch management strategy:

- **main**: Main branch, contains stable production code
- **develop**: Development branch, contains the latest development code
- **feature/**: Feature branches, used for developing new features
- **fix/**: Fix branches, used for bug fixes
- **docs/**: Documentation branches, used for updating documentation

### Branch Naming Guidelines

- Feature branches: `feature/feature-name`
- Fix branches: `fix/issue-description`
- Documentation branches: `docs/document-name`

## Pull Request Process

1. **Describe the Pull Request**
   - Clearly describe your changes
   - Explain the purpose and impact of the changes
   - Link to related Issues or GIP proposals
   - Provide test results or examples

2. **Code review**
   The core team will review your code and may request some modifications.

3. **Merge**
   After review is complete, your code will be merged into the `develop` branch.

## Code Review Standards

Code review will be based on the following standards:

1. **Functional correctness**: Does the code implement the expected functionality
2. **Code quality**: Is the code clear, concise, and easy to understand
3. **Test coverage**: Is there sufficient test coverage
4. **Performance impact**: Will it affect system performance
5. **Security**: Are there any security concerns
6. **Compatibility**: Is it backward compatible
7. **Documentation completeness**: Are there corresponding documentation updates

## Testing Guide

### Running Tests

```bash
# Run all tests
python -m pytest 03-Test/

# Run specific test files
python -m pytest 03-Test/test_unit.py

# Run specific test cases
python -m pytest 03-Test/test_unit.py::test_requirement_parser
```

### Testing Standards

- All new features should have corresponding unit tests
- All bug fixes should have corresponding test cases
- Tests should cover normal cases and edge cases
- Tests should be repeatable and not dependent on external environment

## Documentation Contributions

### Documentation Structure

- **README.md**: Project overview
- **docs/quickstart/**: Quick start guide
- **docs/agents/**: Agent integration guide
- **docs/api/**: API documentation
- **docs/faq/**: Frequently asked questions

### Documentation Standards

- Use Markdown format
- Maintain documentation accuracy and timeliness
- Provide clear steps and examples
- Use consistent terminology and formatting

## Issue Reporting

If you find a bug or issue, please submit a report in GitHub Issues with the following information:

1. **Issue description**: Clearly describe the issue
2. **Reproduction steps**: Detailed instructions on how to reproduce the issue
3. **Expected behavior**: Describe the expected correct behavior
4. **Actual behavior**: Describe the actual observed behavior
5. **Environment information**: Operating system, Python version, dependency versions, etc.
6. **Related logs**: Provide relevant error messages or logs
7. **Possible solutions**: If you have ideas for solutions, please share

## Feature Requests

If you want to add a new feature, please submit a feature request in GitHub Issues with the following information:

1. **Feature description**: Clearly describe the feature you want to add
2. **Feature motivation**: Explain why this feature is needed
3. **Implementation ideas**: If you have implementation ideas, please share
4. **Related resources**: Provide relevant reference materials or examples

## GIP Proposals

GIP (GACP Improvement Proposal) is the mechanism for submitting protocol improvement suggestions. If you want to make major improvements to the GACP Protocol, please create a GIP proposal, see the `GIP.md` file for details.

## Community Communication

- **GitHub Issues**: Submit issues and feature requests
- **GitHub Discussions**: Participate in community discussions
- **GIP Proposals**: Submit protocol improvement proposals
- **Mailing list**: Subscribe to the project mailing list for latest updates

---

Thank you for your contributions to the GACP Protocol! We look forward to building a better AI agent collaboration ecosystem with you.