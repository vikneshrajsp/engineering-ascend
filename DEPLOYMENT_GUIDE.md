# Deployment Guide - Engineering Ascend

## 🚀 **GitHub Actions Deployment**

This project uses GitHub Actions for building and deploying the Jekyll site to GitHub Pages, providing full control over the build environment and dependencies.

## 📋 **Setup Instructions**

### **1. Enable GitHub Actions**

1. Go to your repository's **Settings** tab
2. Click **Pages** under **Code and automation**
3. Change **Source** under **Build and deployment** from **Deploy from a branch** to **GitHub Actions**

### **2. Workflow Configuration**

The project includes a pre-configured workflow file:
- **Location**: `.github/workflows/jekyll.yml`
- **Trigger**: Push to `main` branch or pull requests
- **Build**: Jekyll 4.4.1 with custom plugins
- **Deploy**: Automatic deployment to GitHub Pages

### **3. Theme Configuration**

The site uses the [Architect theme](https://pages-themes.github.io/architect/) via remote theme:
- **Theme**: `pages-themes/architect`
- **Plugin**: `jekyll-remote-theme`
- **Custom CSS**: Enhanced styling in `assets/css/style.scss`

## 🛠️ **Build Process**

### **Dependencies**
- **Ruby**: 3.2
- **Jekyll**: 4.4.1
- **Plugins**: 
  - `jekyll-remote-theme`
  - `jekyll-seo-tag`
  - `jekyll-sitemap`

### **Build Steps**
1. **Checkout**: Clone repository with full history
2. **Setup Ruby**: Install Ruby 3.2 with bundler caching
3. **Setup Pages**: Configure GitHub Pages environment
4. **Build Jekyll**: Generate static site with `bundle exec jekyll build`
5. **Upload Artifacts**: Upload built site to GitHub Pages
6. **Deploy**: Deploy to live site

## 📁 **File Structure**

```
├── _config.yml              # Jekyll configuration
├── Gemfile                  # Ruby dependencies
├── index.md                 # Homepage
├── README.md                # Repository documentation
├── .github/workflows/       # GitHub Actions workflows
├── assets/css/style.scss    # Custom styling
├── building-blocks/         # System design fundamentals
├── system-design-challenges/ # Practice problems
└── *.md                     # Additional documentation
```

## 🔧 **Configuration**

### **Jekyll Configuration** (`_config.yml`)
```yaml
# Site settings
title: Engineering Ascend
description: Comprehensive system design learning resource
url: https://vikneshrajsp.github.io
baseurl: /software-engineering-guide

# Theme settings
remote_theme: pages-themes/architect

# Build settings
markdown: kramdown
highlighter: rouge

# Plugins
plugins:
  - jekyll-remote-theme
  - jekyll-seo-tag
  - jekyll-sitemap
```

### **Dependencies** (`Gemfile`)
```ruby
source "https://rubygems.org"

gem "jekyll", "~> 4.4.1"
gem "jekyll-remote-theme", group: :jekyll_plugins
gem "jekyll-seo-tag", group: :jekyll_plugins
gem "jekyll-sitemap", group: :jekyll_plugins
```

## 🚀 **Deployment Process**

### **Automatic Deployment**
1. **Push to main branch** - Triggers build automatically
2. **Build validation** - Jekyll builds the site
3. **Artifact upload** - Built files uploaded to GitHub
4. **Live deployment** - Site goes live at configured URL

### **Manual Deployment**
1. Go to **Actions** tab in repository
2. Select **Jekyll site CI** workflow
3. Click **Run workflow**
4. Select branch and click **Run workflow**

## 📊 **Monitoring**

### **Build Status**
- **Repository view**: Status indicator next to commits
- **Actions tab**: Detailed build logs and history
- **Deployments tab**: Live site URL and deployment history

### **Troubleshooting**
- **Build failures**: Check Actions tab for detailed error logs
- **Theme issues**: Verify `remote_theme` configuration
- **Plugin errors**: Check Gemfile and plugin compatibility

## 🔄 **Local Development**

### **Setup Local Environment**
```bash
# Install Ruby 3.2+
# Install Bundler
gem install bundler

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve
```

### **Local Testing**
- **URL**: `http://localhost:4000/software-engineering-guide/`
- **Live reload**: Automatic page refresh on changes
- **Build testing**: `bundle exec jekyll build`

## 📈 **Performance**

### **Optimizations**
- **Bundler caching**: Automatic gem caching in CI
- **Concurrent builds**: Limited to prevent conflicts
- **Artifact compression**: Optimized file uploads

### **Build Time**
- **Typical build**: 2-3 minutes
- **Cache hits**: Faster subsequent builds
- **Dependency updates**: May increase build time

## 🔒 **Security**

### **Permissions**
- **Contents**: Read access to repository
- **Pages**: Write access for deployment
- **ID Token**: Required for secure deployment

### **Dependencies**
- **Whitelisted gems**: Only approved dependencies
- **Version pinning**: Specific versions for stability
- **Security updates**: Regular dependency updates

## 📞 **Support**

### **Issues**
- **Build problems**: Check Actions tab for logs
- **Configuration**: Review `_config.yml` and `Gemfile`
- **Theme issues**: Verify Architect theme compatibility

### **Resources**
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Actions Guide](https://jekyllrb.com/docs/continuous-integration/github-actions/)
- [Architect Theme](https://pages-themes.github.io/architect/)

---

**The GitHub Actions deployment provides reliable, fast, and secure deployment with full control over the build environment!** 🚀
