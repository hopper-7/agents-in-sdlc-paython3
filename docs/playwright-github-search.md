# Playwright MCP Tools for GitHub Topic Search

This document demonstrates how to use Playwright MCP tools with GitHub Copilot Agent mode to search for GitHub-related presentation topics on seminar websites.

## Overview

The Playwright MCP (Model Context Protocol) server allows GitHub Copilot to perform browser automation tasks, including web scraping and content analysis. This is particularly useful for finding relevant presentation topics on conference websites.

## Setup

The Playwright MCP server is already configured in `.vscode/mcp.json`:

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "playwright": {
      "command": "npx",
      "args": ["--yes", "mcp-playwright"],
      "env": {
        "NODE_ENV": "development"
      }
    }
  }
}
```

## Usage with GitHub Copilot Agent Mode

### Example 1: Search for GitHub Topics on DevDays Asia 2025

```bash
#playwright 幫我找 有關 github 的演講主題
https://www.digitimes.com.tw/Seminar/DevDaysAsia2025/index.html
```

This command instructs the Playwright MCP server to:
1. Navigate to the DevDays Asia 2025 seminar website
2. Search for GitHub-related keywords in session titles, descriptions, and speaker information
3. Extract relevant presentation topics
4. Provide suggestions for GitHub-related presentations

### Example 2: Automated Testing with Playwright

```bash
#playwright to test games.spec.ts and home.spec.ts
```

This command uses Playwright to run automated tests for the application.

## GitHub-Related Keywords

The search looks for the following GitHub-related terms:
- `github`
- `git`
- `copilot`
- `actions`
- `ci/cd`
- `devops`
- `repository`
- `version control`
- `pull request`
- `merge`
- `branch`
- `commit`
- `code review`
- `collaboration`
- `open source`
- `enterprise`
- `security`
- `automation`

## Example Output

When the Playwright MCP server finds GitHub-related content, it provides:

### Found Topics
1. **AI-Powered Development with GitHub Copilot**
   - Keywords: github copilot
   - Description: Learn how GitHub Copilot transforms development experience
   - Relevance Score: 10/10

2. **CI/CD Automation with GitHub Actions**
   - Keywords: github actions
   - Description: Build robust CI/CD pipelines using GitHub Actions
   - Relevance Score: 9/10

3. **Securing Your Codebase with GitHub Advanced Security**
   - Keywords: github security
   - Description: Explore GitHub's security features
   - Relevance Score: 8/10

### Suggested Topics
Based on DevDays Asia 2025 themes:
1. GitHub Copilot: Accelerating Development in Asian Markets
2. Building Resilient CI/CD Pipelines with GitHub Actions
3. Enterprise Security Best Practices with GitHub
4. Collaborative Development Workflows for Global Teams
5. Open Source Strategy for Asian Technology Companies
6. GitHub API Integration for Custom Development Tools
7. Mobile App CI/CD with GitHub Actions and Cloud Services
8. Infrastructure as Code with GitHub and Terraform
9. Code Quality Automation with GitHub Checks and Reviews
10. DevOps Transformation with GitHub Enterprise

## Implementation Details

### Playwright Actions Performed
1. **Navigate** to the target website
2. **Search** for session titles and descriptions
3. **Extract** speaker information and schedules
4. **Analyze** content for GitHub-related keywords
5. **Score** relevance based on keyword frequency and context
6. **Generate** additional topic suggestions

### Content Analysis
The Playwright MCP server analyzes:
- Session titles and subtitles
- Speaker biographies and descriptions
- Session abstracts and summaries
- Schedule and agenda sections
- Workshop and tutorial descriptions

### Output Format
Results are provided in both:
- **Human-readable format** for immediate review
- **JSON format** for further processing and integration

## Demo Scripts

Two demonstration scripts are provided:

### 1. Node.js Script (`scripts/playwright-github-search.js`)
A complete implementation showing how Playwright would search the website and extract GitHub-related topics.

### 2. Python Script (`scripts/playwright-github-search.py`)
A Python implementation demonstrating the search logic and output formatting.

## Running the Demo

```bash
# Run the Python demo script
python scripts/playwright-github-search.py

# Install Node.js dependencies and run the Node.js script
npm install playwright
node scripts/playwright-github-search.js
```

## Benefits of Using Playwright MCP

1. **Automated Content Discovery**: Automatically find relevant topics without manual browsing
2. **Comprehensive Search**: Search multiple sections of websites simultaneously
3. **Relevance Scoring**: Prioritize topics based on keyword frequency and context
4. **Time Savings**: Quickly identify relevant content across large conference websites
5. **Structured Output**: Get results in both human-readable and machine-processable formats

## Troubleshooting

### Website Access Issues
If the target website is blocked or inaccessible:
- The scripts provide fallback suggestions based on common DevDays Asia themes
- Alternative conference websites can be used as examples
- Local HTML files can be used for testing

### MCP Server Configuration
Ensure the Playwright MCP server is properly configured in `.vscode/mcp.json` and that VS Code can access the necessary browser automation tools.

## Next Steps

1. **Customize Keywords**: Modify the GitHub-related keywords list based on specific interests
2. **Add More Websites**: Extend the search to other developer conferences and seminars
3. **Integrate with Issues**: Use the results to create GitHub issues for presentation planning
4. **Automate Scheduling**: Connect with calendar systems to track presentation opportunities

## Related Documentation

- [Exercise 2 - MCP Setup](../docs/2-mcp.zh-TW.md)
- [Playwright MCP Server Repository](https://github.com/microsoft/playwright-mcp)
- [GitHub MCP Server Documentation](https://github.com/github/github-mcp-server)