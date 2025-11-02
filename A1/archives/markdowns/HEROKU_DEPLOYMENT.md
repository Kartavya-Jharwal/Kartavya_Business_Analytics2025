# Heroku Deployment Guide for CarbonSeer

## 🚀 Quick Deploy

### Prerequisites
- Git repository initialized
- Heroku CLI installed
- Heroku account created

### Deployment Steps

1. **Ensure all deployment files are in place:**
   ```bash
   ls -la  # Check for these files:
   # - .python-version
   # - Procfile
   # - pyproject.toml
   # - .streamlit/config.toml
   ```

2. **Login to Heroku:**
   ```bash
   heroku login
   ```

3. **Create Heroku app:**
   ```bash
   heroku create carbonseer-analytics
   # Or use your preferred app name
   ```

4. **Set buildpack for UV:**
   ```bash
   heroku buildpacks:set https://github.com/heroku/heroku-buildpack-python
   ```

5. **Commit all changes:**
   ```bash
   git add .
   git commit -m "Add Heroku deployment configuration"
   ```

6. **Deploy to Heroku:**
   ```bash
   git push heroku main
   ```

7. **Open your app:**
   ```bash
   heroku open
   ```

---

## 📁 Required Files

### 1. `.python-version` ✅
```
3.12
```
**Purpose:** Tells Heroku which Python version to use with UV

### 2. `Procfile` ✅
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```
**Purpose:** Tells Heroku how to run your application

### 3. `pyproject.toml` ✅
**Already exists** - Contains all dependencies

### 4. `.streamlit/config.toml` ✅
**Updated** - Configured for Heroku deployment

---

## 🔧 Configuration Details

### Procfile Explained:
- `web:` - Process type for web server
- `streamlit run app.py` - Start command
- `--server.port=$PORT` - Use Heroku's dynamic port
- `--server.address=0.0.0.0` - Bind to all interfaces

### Config.toml for Heroku:
```toml
[server]
headless = true  # No browser auto-open
address = "0.0.0.0"  # Bind to all addresses
enableCORS = false  # Heroku handles CORS
enableXsrfProtection = false  # Disabled for Heroku
```

---

## 🐛 Troubleshooting

### Error: "No Python version was specified"
**Solution:** ✅ Fixed - `.python-version` file created

### Error: "Application Error"
**Check logs:**
```bash
heroku logs --tail
```

### Error: "Port binding failed"
**Verify Procfile:**
- Must include `--server.port=$PORT`
- Must include `--server.address=0.0.0.0`

### Error: "Module not found"
**Check dependencies:**
```bash
# Ensure all imports are in pyproject.toml
# Current dependencies include:
# - streamlit>=1.50.0
# - streamlit-extras>=0.4.0
# - pandas, numpy, scipy, etc.
```

### Error: "Slug size too large"
**Reduce size:**
```bash
# Remove unnecessary files
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".pytest_cache/" >> .gitignore
```

---

## 📊 Environment Variables (Optional)

Set environment variables if needed:

```bash
# Set config vars
heroku config:set STREAMLIT_THEME_PRIMARY_COLOR="#FBA834"

# View current config
heroku config

# Remove config var
heroku config:unset VARIABLE_NAME
```

---

## 🔄 Continuous Deployment

### Option 1: GitHub Integration
1. Go to Heroku Dashboard
2. Select your app
3. Go to "Deploy" tab
4. Connect to GitHub repository
5. Enable automatic deploys from `main` branch

### Option 2: Manual Git Push
```bash
# Make changes
git add .
git commit -m "Update application"
git push heroku main
```

---

## 🎯 Post-Deployment Checklist

After successful deployment:

- [ ] App loads without errors
- [ ] Splash screen displays correctly
- [ ] Logo images render properly
- [ ] PDF viewer works in sidebar
- [ ] Data explorer filters correctly
- [ ] All pages navigate properly
- [ ] Interactive elements function
- [ ] Mobile responsive
- [ ] Performance acceptable

---

## 📈 Scaling (If Needed)

### Upgrade dyno type:
```bash
# Check current dynos
heroku ps

# Scale to hobby dyno ($7/month)
heroku ps:scale web=1:hobby

# Scale to standard ($25-50/month)
heroku ps:scale web=1:standard-1x
```

### Add monitoring:
```bash
# Enable logging add-on (free)
heroku addons:create papertrail:choklad

# View logs
heroku addons:open papertrail
```

---

## 🔐 Security Considerations

### Sensitive Data:
- Don't commit API keys or secrets
- Use environment variables:
  ```bash
  heroku config:set SECRET_KEY="your-secret-here"
  ```

### Access in code:
```python
import os
secret = os.environ.get('SECRET_KEY')
```

---

## 💰 Cost Estimation

### Free Tier:
- ✅ 550-1000 free dyno hours/month
- ✅ Sleeps after 30 min inactivity
- ✅ Wakes on request (cold start ~10s)

### Hobby Tier ($7/month):
- ✅ Never sleeps
- ✅ Custom domain support
- ✅ Better performance

### Production Tier ($25+/month):
- ✅ Horizontal scaling
- ✅ Preboot (zero downtime deploys)
- ✅ Threshold autoscaling

---

## 🌐 Custom Domain (Optional)

Add custom domain:

```bash
# Add domain
heroku domains:add www.carbonseer.com

# Configure DNS
# Add CNAME record:
# www.carbonseer.com -> your-app.herokuapp.com

# Enable SSL (automatic with hobby+ tier)
heroku certs:auto:enable
```

---

## 📦 Alternative Deployment Options

If Heroku doesn't work, consider:

### 1. Streamlit Cloud (Recommended)
- Free hosting for public repos
- Automatic GitHub integration
- Built-in Streamlit optimization
- Deploy: https://streamlit.io/cloud

### 2. Render
```yaml
# render.yaml
services:
  - type: web
    name: carbonseer
    env: python
    buildCommand: uv sync
    startCommand: streamlit run app.py
```

### 3. Railway
```toml
# railway.toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "streamlit run app.py"
```

### 4. Google Cloud Run
```dockerfile
# Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install uv
RUN uv sync
CMD streamlit run app.py --server.port=$PORT
```

---

## 🆘 Support Resources

### Heroku Documentation:
- Python Support: https://devcenter.heroku.com/categories/python-support
- Streamlit on Heroku: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app

### CarbonSeer Issues:
- GitHub Issues: https://github.com/Kartavya-Jharwal/Kartavya_Business_Analytics2025/issues
- Email: (your contact)

---

## ✅ Deployment Checklist

Before deploying:

- [x] `.python-version` file created (3.12)
- [x] `Procfile` created with correct command
- [x] `pyproject.toml` has all dependencies
- [x] `.streamlit/config.toml` configured for production
- [ ] All files committed to Git
- [ ] Git remote set to Heroku
- [ ] Environment variables set (if any)
- [ ] Tested locally with production settings

---

## 🎉 Success!

Once deployed, your CarbonSeer application will be live at:
```
https://your-app-name.herokuapp.com
```

Share with:
- Professors for grading
- Peers for feedback
- Portfolio for showcasing
- LinkedIn for networking

---

**Date:** October 16, 2025  
**Version:** 2.2 - Production Ready  
**Status:** ✅ Deployment Configured

## Quick Commands Reference

```bash
# Deploy
git push heroku main

# View logs
heroku logs --tail

# Open app
heroku open

# Check status
heroku ps

# Restart app
heroku restart

# Run migrations (if needed)
heroku run python migrate.py

# Access bash
heroku run bash
```

Good luck with your deployment! 🚀
