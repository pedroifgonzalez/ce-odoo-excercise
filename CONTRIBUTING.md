# Contributing Guidelines

This document outlines the best practices for contributing to the CRM Social Networks module.

## Git Workflow

### Branching Strategy

We follow a simplified Git Flow strategy:

- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: Feature branches (e.g., `feature/social-networks`)
- `bugfix/*`: Bug fix branches
- `release/*`: Release preparation branches

### Commit Messages

Follow the conventional commits format:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code refactoring
- `test`: Adding or modifying tests
- `chore`: Maintenance tasks

Examples:
- `feat(social): add LinkedIn field to partner model`
- `fix(validation): correct URL validation for Twitter`
- `test(partner): add tests for profile completion`

### Pull Request Process

1. Create a feature branch from `develop`
2. Implement your changes with appropriate tests
3. Ensure all tests pass
4. Create a pull request to merge into `develop`
5. Request code review
6. Address review comments
7. Merge after approval

## Testing

### Running Tests

To run the tests for this module:

```bash
cd /path/to/odoo
./odoo-bin -d your_database --test-enable --log-level=test --stop-after-init -i ce-odoo-excercise
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files with `test_` prefix
- Use appropriate test classes:
  - `TransactionCase` for model tests
  - `HttpCase` for controller/UI tests
- Test both positive and negative scenarios
- Mock external dependencies when necessary

### Test Coverage

We aim for at least 80% test coverage. To generate a coverage report:

1. Install the coverage package:
   ```bash
   pip install coverage
   ```

2. Run tests with coverage:
   ```bash
   coverage run --source=./odoo-practice-addons/ce-odoo-excercise ./odoo-bin -d your_database --test-enable --stop-after-init -i ce-odoo-excercise
   ```

3. Generate a report:
   ```bash
   coverage report -m
   coverage html  # Creates HTML report in htmlcov/
   ```

## Code Style

- Follow PEP 8 for Python code
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use meaningful variable and function names
- Add docstrings to all classes and methods

## Documentation

- Update README.md with any new features
- Document API changes
- Keep the test coverage report up to date
