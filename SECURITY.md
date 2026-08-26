# Security Policy

## Public Repository Security Boundary

This is a public repository. Never commit or paste:

- API keys, access tokens, passwords, credentials, private keys or signing material;
- private customer, user or personal data;
- private production infrastructure topology;
- confidential runtime evidence or operational logs;
- production configuration containing sensitive endpoints or secrets.

If sensitive information is accidentally exposed, stop propagation, preserve evidence, revoke/rotate affected credentials through the appropriate authority, and follow the applicable incident process. Do not copy the secret into Issues or PR comments.

## Vulnerability Reporting

Do not publish sensitive exploit details or active credentials in public Issues. Use GitHub private vulnerability/security reporting when available. If a private reporting channel is unavailable, open a minimal public security-triage Issue without sensitive exploit material so maintainers can establish a private channel.

## Upstream / Supply Chain

No upstream code, dependency, Action, binary, model provider, plugin, or package is trusted merely because it is popular or official. Review provenance, license, security, integrity and compatibility before adoption.

GitHub Actions should be pinned to immutable commit SHAs where practical and must use minimum permissions. Checkout credentials must not persist unless explicitly required and authorized.

## Authority

Security review does not authorize production changes, secret access, network mutation, signing, publication, or other high-risk actions.
