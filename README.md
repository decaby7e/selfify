
# Selfify - A self-hosted alternative to Netlify

## Getting Started

> Work in progress...

## To-Do

### Roadmap

#### Server Workflow

1. Install Selfify
2. Create wildcard DNS under any domain/subdomain (e.g. dev.example.com)
3. Configure webserver (like Caddy 2) to proxy all requests from chosen domain to Selfify
  - OPTIONAL: Let Selfify listen on 80/443 to handle ALL requests destined for the server
4. Run selfify with CLI config OR file-based config:
```bash
selfify \
  --domain dev.example.com
  --secret $SECRET_SAUCE
  --port 8080
  --tls  # Optional (Default: False)
  --tls_port 8443
  --config selfify.yaml  # Optional (Default: None)
  --data /home/admin/selfify/data  # Optional (Default: ./data)
```

#### Client Workflow
1. Add server domain (e.g. dev.example.com) to webhooks w/ secret
2. Create file in project repository named `selfify.yaml` (OPTIONAL)
```yaml
subdomain: my_app_subdomain  # Will expand to my_app_subdomain.dev.example.com on server
site_dir: /public/           # Relative to repository root (/public/ -> /.../REPOSITORY_DIRECTORY/public/)
```

NOTE: In the future, a web interface on the server may be an option to replace configuration stored in the repository, but for now this seems to be the ideal approach.
