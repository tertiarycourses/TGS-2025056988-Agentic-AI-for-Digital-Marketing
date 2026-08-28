# SocialPost API contract used in Lab 11

Base URL: `https://socialmediapost.tertiaryinfotech.com`

| Media | Endpoint | Required multipart fields |
|---|---|---|
| Text | `POST /api/upload_text` | `user`, `platform[]`, `title`; optional `caption` |
| Photos | `POST /api/upload_photos` | `photos[]`, `user`, `platform[]`, `title`; optional `description` |
| Video | `POST /api/upload` | `video`, `title`, `user`, `platform[]` |

Authentication header: `Authorization: Apikey <sandbox-key>`. Store the complete header value in an n8n Header Auth credential. Never place the key in workflow JSON, Excel, screenshots or evidence.

The supplied workflow is configured for the text-post fixture. For photo or video work, use the matching endpoint and map the binary property in the HTTP Request node.

Source verified 29 August 2026: https://socialmediapost.tertiaryinfotech.com/
