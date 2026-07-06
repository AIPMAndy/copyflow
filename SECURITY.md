# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 3.0.x   | :white_check_mark: |
| < 3.0   | :x:                |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to: [YOUR_SECURITY_EMAIL]

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

Please include the following information:

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

## Security Best Practices

When using CopyFlow:

1. **API Keys**: Never commit API keys to version control
   ```bash
   # Use environment variables
   export OPENAI_API_KEY="your-key"
   export PONYFLASH_API_KEY="your-key"
   ```

2. **Dependencies**: Keep dependencies updated
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Input Validation**: Be cautious with user-provided topics in automated scenarios

4. **Output Review**: Always review generated content before publishing

5. **Rate Limiting**: Use appropriate rate limits to avoid unexpected API costs

## Known Security Considerations

- **API Costs**: Malicious input could trigger excessive API calls. Use rate limiting.
- **Output Content**: AI-generated content should always be reviewed by humans.
- **Prompt Injection**: The system includes safeguards but review outputs carefully.

## Security Updates

Security updates will be released as patch versions and announced:
- GitHub Security Advisories
- Release notes
- Discussions

## Attribution

We appreciate responsible disclosure and will credit reporters (unless anonymity is requested).
