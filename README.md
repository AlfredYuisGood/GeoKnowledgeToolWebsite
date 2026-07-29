# Geo-KTF Knowledge Explorer

Static GitHub Pages site for browsing Geo-KTF knowledge sections, categories, and representative tools.

## Live site

After Pages is enabled:

`https://<your-username>.github.io/<repo-name>/`

## Deploy (GitHub Pages)

1. Push this repo to GitHub.
2. Open **Settings → Pages**.
3. Under **Build and deployment**:
   - Source: **Deploy from a branch**
   - Branch: `main` / `/ (root)`
4. Save. The site is usually live within a minute.

## Regenerate the site

```bash
python3 generate_geo_ktf_site.py
```

Commit and push `index.html` / `data/` to update the live Pages site.
