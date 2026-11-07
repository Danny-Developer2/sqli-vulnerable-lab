# Security Policy

## Scope

This repository contains an **intentionally vulnerable** educational laboratory
designed to demonstrate SQL injection. It is **not** a production system and
must never be treated as one.

| Item | Detail |
| --- | --- |
| Purpose | Teaching SQL injection and parameterized queries |
| Intended environment | Local machine or isolated lab network only |
| Production use | **Strictly forbidden** |
| Real data | None. Every user, product, customer and log is fictitious |

The intentionally vulnerable code paths are:

| Scenario | Route | Technique |
| --- | --- | --- |
| Login bypass | `/login` | String concatenation in the SQL query |
| Error-based | `/search?q=` | Raw SQL error returned in the HTTP response |
| Boolean-based | `/product?id=` | Response difference between true and false conditions |
| Time-based | `/product?id=` | `SLEEP(5)` measured response delay |
| Secure login (defense) | `/secure-login` | Parameterized query with `%s` placeholders |

The secure implementation at `/secure-login` is the **reference defense** and is
not meant to be attacked. It exists to demonstrate that the same payloads fail
when parameters are bound instead of concatenated.

## Reporting a Vulnerability

This project is a lab: the vulnerabilities above are **by design** and are not
reportable findings. Do not open a security issue for them.

Report only:

- Unintended weaknesses in the lab itself (e.g. an accidentally exposed port or
  a dependency with a known CVE).
- Documentation or setup errors that could lead a user to expose the lab.
- Any real secret found in the repository or its history.

**Responsible disclosure contact:** Danny-Developer2 (repository maintainer).

Please describe the issue with enough detail to reproduce it and avoid publishing
it publicly before a fix or acknowledgement. Expect a response within a
reasonable time; if you do not receive one, assume no commitment has been made.

## Good Practices for Users

1. Run the lab only on `127.0.0.1` or in an isolated network.
2. Never expose port `8080` to the public Internet.
3. Never point any payload at a third-party system or service.
4. Do not replace the fictitious seed data with real credentials.
5. Rotate any credentials you copy into `.env` and never commit that file.
6. Review `docs/seguridad.md` before starting.

## Repository Hygiene

- `.env` is ignored by `.gitignore`; only `.env.example` (with fictitious
  placeholders) is versioned.
- All credentials shipped in `database/seed.sql`, `docker-compose.yml` and
  `app/db.py` are **fictitious demo values** meant for local reproducibility.
