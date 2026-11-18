# Publish the BRK367 resource page

## Required authorization

Publishing requires a GitHub account with permission to create a **public** repository in the chosen user or organization. Registering the `aka.ms` alias requires separate access to the Microsoft short-link administration experience.

## Recommended repository

- Name: `cosmosdb-ignite-2026-brk367`
- Visibility: **Public**
- Pages URL: `https://<owner>.github.io/cosmosdb-ignite-2026-brk367/`

## Publish with GitHub CLI

1. Install and authenticate GitHub CLI:

   ```bash
   gh auth login
   ```

2. From this directory, run:

   ```bash
   ./publish.sh
   ```

   Optional environment variables:

   ```bash
   GH_OWNER=<github-user-or-org> GH_REPO=cosmosdb-ignite-2026-brk367 ./publish.sh
   ```

3. In the new repository, open **Settings → Pages** and confirm the source is **GitHub Actions**. The included workflow deploys the site after a push to `main`.

4. Wait for the Pages workflow to complete, then verify the public page in a signed-out/private browser window.

## Register the umbrella shortcut

After the GitHub Pages URL is live and verified:

- Proposed short name: `CosmosDBIgnite2026`
- Destination: the final GitHub Pages URL
- Intended public URL: `https://aka.ms/CosmosDBIgnite2026`

Do not claim the alias is registered until the administration experience confirms creation and the redirect is verified in a signed-out browser.

## Generate the final slide QR

After the alias redirects successfully:

```bash
python3 scripts/generate-qr.py \
  --url https://aka.ms/CosmosDBIgnite2026 \
  --output slide-assets/qr-cosmosdb-ignite-2026.png
```

The generated PNG uses a high error-correction level and a large quiet zone suitable for a closing slide.
