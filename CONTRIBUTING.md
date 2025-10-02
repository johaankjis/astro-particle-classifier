# Contributing to Astro Particle Classifier

Thank you for your interest in contributing to the Astro Particle Classifier project! This document provides guidelines and instructions for contributing.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project is committed to providing a welcoming and inclusive experience for everyone. We expect all contributors to:
- Be respectful and considerate
- Welcome newcomers and beginners
- Accept constructive criticism gracefully
- Focus on what is best for the community

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, package versions)
- Any relevant error messages or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Explain why this enhancement would be useful
- List any potential drawbacks or alternatives considered

### Code Contributions

We welcome code contributions in the following areas:

1. **New Models**: Implement additional classification algorithms
2. **Feature Engineering**: Add new feature extraction or transformation methods
3. **Hyperparameter Optimization**: Improve tuning strategies (e.g., Bayesian optimization)
4. **Visualization**: Add new plots or analysis tools
5. **Performance**: Optimize existing code for speed or accuracy
6. **Documentation**: Improve or expand documentation
7. **Testing**: Add unit tests or integration tests
8. **Bug Fixes**: Fix identified issues

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/astro-particle-classifier.git
   cd astro-particle-classifier
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Process

1. Make your changes in your feature branch
2. Test your changes thoroughly
3. Update documentation as needed
4. Ensure your code follows the style guidelines
5. Commit your changes with clear commit messages
6. Push to your fork
7. Submit a pull request

## Style Guidelines

### Python Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Use type hints where appropriate

### Example:

```python
from typing import Tuple
import numpy as np

def scale_dataset(dataframe: pd.DataFrame, 
                  oversample: bool = False) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Scale features and optionally oversample the dataset.
    
    Args:
        dataframe: Input DataFrame with features and target
        oversample: Whether to apply random oversampling
        
    Returns:
        Tuple of (scaled_data, X, y)
    """
    # Implementation here
    pass
```

### Jupyter Notebook Guidelines

- Add markdown cells to explain each section
- Clear output before committing (unless demonstrating results)
- Keep cells reasonably sized
- Use descriptive variable names
- Add comments for complex operations

## Commit Messages

Write clear, concise commit messages:

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests when relevant

### Examples:

```
Add XGBoost classifier implementation

Implement XGBoost model with hyperparameter tuning and cross-validation.
Includes visualization of feature importance.

Fixes #123
```

## Pull Request Process

1. **Before Submitting**:
   - Ensure all tests pass
   - Update README.md if adding new features
   - Update requirements.txt if adding dependencies
   - Add or update docstrings as needed

2. **PR Description**:
   - Clearly describe what changes you made
   - Explain why these changes are necessary
   - Reference related issues
   - Include screenshots for visual changes
   - List any breaking changes

3. **Review Process**:
   - Maintainers will review your PR
   - Address any feedback or requested changes
   - Keep your PR updated with the main branch
   - Be patient and responsive

4. **Merging**:
   - PRs require approval from maintainers
   - Ensure CI checks pass
   - Squash commits if requested
   - Maintainers will merge when approved

## Testing

While the project doesn't currently have extensive test coverage, consider:

- Testing your code with different input scenarios
- Verifying model performance on the test set
- Checking that existing functionality still works
- Adding assertions for critical functions

## Documentation

- Update README.md for significant changes
- Add docstrings to new functions/classes
- Update inline comments as needed
- Consider adding examples for new features

## Questions?

Feel free to open an issue with the "question" label if you need help or clarification.

## Attribution

Contributors will be acknowledged in the project. Thank you for your contributions!
