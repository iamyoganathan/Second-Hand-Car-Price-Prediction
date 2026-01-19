# 🚀 Azure Deployment Guide

## Deploy Second Hand Car Price Prediction to Azure App Service

This guide will walk you through deploying your Streamlit ML application to Microsoft Azure.

---

## 📋 Prerequisites

Before starting, ensure you have:

- ✅ **Azure Account** - [Create free account](https://azure.microsoft.com/free/) ($200 credit)
- ✅ **Azure CLI** - Install from [here](https://docs.microsoft.com/cli/azure/install-azure-cli)
- ✅ **Git** - Already configured in this project
- ✅ **Python 3.8+** - Already installed

---

## 🎯 Deployment Options

### **Option 1: Deploy via Azure Portal (Easiest)** ⭐ Recommended for Beginners

### **Option 2: Deploy via Azure CLI** (More Control)

### **Option 3: Deploy via GitHub Actions** (CI/CD Pipeline)

---

## 📦 Option 1: Deploy via Azure Portal

### **Step 1: Login to Azure Portal**
1. Go to [Azure Portal](https://portal.azure.com)
2. Sign in with your Microsoft account

### **Step 2: Create Resource Group**
1. Click **"Create a resource"**
2. Search for **"Resource Group"**
3. Click **"Create"**
4. Fill in details:
   - **Subscription**: Choose your subscription
   - **Resource Group Name**: `car-price-prediction-rg`
   - **Region**: Choose closest region (e.g., East US)
5. Click **"Review + Create"** → **"Create"**

### **Step 3: Create App Service Plan**
1. In Resource Group, click **"+ Create"**
2. Search for **"App Service"**
3. Click **"Create"** → **"Web App"**
4. Configure:
   - **Subscription**: Your subscription
   - **Resource Group**: `car-price-prediction-rg`
   - **Name**: `car-price-predictor-app` (must be globally unique)
   - **Publish**: **Code**
   - **Runtime Stack**: **Python 3.11**
   - **Region**: Same as Resource Group
   - **Pricing Plan**: 
     - For free: **F1 (Free)** - Limited resources
     - For better performance: **B1 (Basic)** - $13/month
5. Click **"Review + Create"** → **"Create"**
6. Wait for deployment (2-3 minutes)

### **Step 4: Configure Deployment**
1. Go to your App Service
2. In left menu, click **"Deployment Center"**
3. Choose **"GitHub"** as source
4. Click **"Authorize"** and connect GitHub account
5. Select:
   - **Organization**: Your GitHub username
   - **Repository**: `second-hand-car-price-prediction`
   - **Branch**: `main`
6. Click **"Save"**

### **Step 5: Configure Startup Command**
1. In App Service, go to **"Configuration"**
2. Click **"General settings"** tab
3. Set **Startup Command**: 
   ```bash
   python -m streamlit run app.py --server.port=8000 --server.address=0.0.0.0
   ```
4. Click **"Save"**

### **Step 6: Configure Application Settings**
1. Still in **"Configuration"**
2. Click **"Application settings"** tab
3. Add new setting:
   - **Name**: `PORT`
   - **Value**: `8000`
4. Click **"Save"** → **"Continue"**

### **Step 7: Verify Deployment**
1. Go to **"Overview"** page
2. Click the **URL** (e.g., `https://car-price-predictor-app.azurewebsites.net`)
3. Wait 2-3 minutes for first deployment
4. Your app should be live! 🎉

---

## 💻 Option 2: Deploy via Azure CLI

### **Step 1: Install Azure CLI**
```powershell
# Windows
winget install Microsoft.AzureCLI

# Verify installation
az --version
```

### **Step 2: Login to Azure**
```powershell
az login
```

### **Step 3: Create Resource Group**
```powershell
az group create --name car-price-prediction-rg --location eastus
```

### **Step 4: Create App Service Plan**
```powershell
az appservice plan create `
  --name car-price-prediction-plan `
  --resource-group car-price-prediction-rg `
  --sku B1 `
  --is-linux
```

### **Step 5: Create Web App**
```powershell
az webapp create `
  --name car-price-predictor-app `
  --resource-group car-price-prediction-rg `
  --plan car-price-prediction-plan `
  --runtime "PYTHON:3.11"
```

### **Step 6: Configure Startup Command**
```powershell
az webapp config set `
  --resource-group car-price-prediction-rg `
  --name car-price-predictor-app `
  --startup-file "python -m streamlit run app.py --server.port=8000 --server.address=0.0.0.0"
```

### **Step 7: Deploy from Local Git**
```powershell
# Get deployment credentials
az webapp deployment user set --user-name <username> --password <password>

# Configure local git
az webapp deployment source config-local-git `
  --name car-price-predictor-app `
  --resource-group car-price-prediction-rg

# Add Azure remote
git remote add azure <git-url-from-previous-command>

# Push to Azure
git push azure main
```

### **Step 8: Open in Browser**
```powershell
az webapp browse --name car-price-predictor-app --resource-group car-price-prediction-rg
```

---

## 🔧 Option 3: CI/CD with GitHub Actions

This will be automatically set up if you use Option 1 (Azure Portal with GitHub integration).

The workflow file will be created in `.github/workflows/` automatically.

---

## 📊 Add Application Insights (Monitoring)

### **Step 1: Create Application Insights**
```powershell
az monitor app-insights component create `
  --app car-price-predictor-insights `
  --location eastus `
  --resource-group car-price-prediction-rg `
  --application-type web
```

### **Step 2: Get Instrumentation Key**
```powershell
az monitor app-insights component show `
  --app car-price-predictor-insights `
  --resource-group car-price-prediction-rg `
  --query instrumentationKey
```

### **Step 3: Add to App Settings**
```powershell
az webapp config appsettings set `
  --resource-group car-price-prediction-rg `
  --name car-price-predictor-app `
  --settings APPINSIGHTS_INSTRUMENTATIONKEY=<your-instrumentation-key>
```

---

## 💾 Optional: Azure Blob Storage for Model

### **Step 1: Create Storage Account**
```powershell
az storage account create `
  --name carpredictorstorage `
  --resource-group car-price-prediction-rg `
  --location eastus `
  --sku Standard_LRS
```

### **Step 2: Create Container**
```powershell
az storage container create `
  --name models `
  --account-name carpredictorstorage `
  --auth-mode login
```

### **Step 3: Upload Model**
```powershell
az storage blob upload `
  --account-name carpredictorstorage `
  --container-name models `
  --name CarPricePrediction.pickle `
  --file CarPricePrediction.pickle `
  --auth-mode login
```

### **Step 4: Get Connection String**
```powershell
az storage account show-connection-string `
  --name carpredictorstorage `
  --resource-group car-price-prediction-rg
```

### **Step 5: Add to App Settings**
```powershell
az webapp config appsettings set `
  --resource-group car-price-prediction-rg `
  --name car-price-predictor-app `
  --settings AZURE_STORAGE_CONNECTION_STRING=<connection-string>
```

---

## 🔍 Troubleshooting

### **Issue: App not starting**
- Check logs: Go to App Service → **Log stream**
- Or use CLI: `az webapp log tail --name car-price-predictor-app --resource-group car-price-prediction-rg`

### **Issue: Port binding error**
- Ensure startup command uses port 8000
- Check Application Settings has `PORT=8000`

### **Issue: Module not found**
- Verify `requirements.txt` is in root directory
- Check all dependencies are listed

### **Issue: Pickle file too large**
- Consider using Azure Blob Storage (see optional section above)
- Or compress the pickle file

---

## 📈 Monitoring & Scaling

### **View Logs**
```powershell
az webapp log tail --name car-price-predictor-app --resource-group car-price-prediction-rg
```

### **Scale Up (Vertical)**
```powershell
az appservice plan update `
  --name car-price-prediction-plan `
  --resource-group car-price-prediction-rg `
  --sku S1
```

### **Scale Out (Horizontal)**
```powershell
az appservice plan update `
  --name car-price-prediction-plan `
  --resource-group car-price-prediction-rg `
  --number-of-workers 3
```

---

## 💰 Cost Estimation

| Service | Tier | Monthly Cost |
|---------|------|--------------|
| App Service | F1 (Free) | $0 |
| App Service | B1 (Basic) | ~$13 |
| App Service | S1 (Standard) | ~$70 |
| Storage Account | Standard LRS | ~$0.02/GB |
| Application Insights | Basic | Free (5GB/month) |

**Estimated Total for Internship**: $13-15/month (using B1 plan)
**Note**: Azure Free Account includes $200 credit for 30 days

---

## ✅ Verification Checklist

- [ ] App Service created
- [ ] GitHub repository connected
- [ ] Startup command configured
- [ ] Application deployed successfully
- [ ] App accessible via URL
- [ ] All features working (predictions)
- [ ] Application Insights enabled (optional)
- [ ] Logs accessible

---

## 🎓 For Your Internship Report

Include these in your documentation:

1. **Architecture Diagram** - Draw Azure services used
2. **Deployment Screenshots** - Azure Portal, running app
3. **Cost Analysis** - Breakdown of Azure resources
4. **Monitoring Setup** - Application Insights dashboards
5. **CI/CD Pipeline** - GitHub Actions workflow
6. **Security** - Authentication, Key Vault usage
7. **Scalability** - How to scale the application
8. **Challenges & Solutions** - Issues faced and resolved

---

## 📚 Additional Resources

- [Azure App Service Documentation](https://docs.microsoft.com/azure/app-service/)
- [Streamlit Deployment Guide](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app)
- [Azure Python SDK](https://docs.microsoft.com/python/azure/)
- [Azure Free Account](https://azure.microsoft.com/free/)

---

## 🆘 Need Help?

If you encounter any issues:
1. Check Azure Portal logs
2. Review this guide
3. Check Azure documentation
4. Ask your internship mentor

---

**Good luck with your Azure deployment! 🚀**
