# TradingAgents Enhanced Edition

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/Version-en--0.1.15-green.svg)](./VERSION)
[![Documentation](https://img.shields.io/badge/docs-Documentation-green.svg)](./docs/)
[![Original](https://img.shields.io/badge/Based%20on-TauricResearch/TradingAgents-orange.svg)](https://github.com/TauricResearch/TradingAgents)

> 🚀 **Latest Version en-0.1.15**: Major upgrade to developer experience and LLM ecosystem! New Qianfan model support, complete development toolchain, academic research materials, enterprise-grade workflow standards!
>
> 🎯 **Core Features**: Native OpenAI Support | Full Google AI Integration | Custom Endpoint Configuration | Smart Model Selection | Multi-LLM Provider Support | Model Selection Persistence | Docker Containerized Deployment | Professional Report Export | Complete Global Stock Market Support | Multi-language Support

A **Multi-Agent Large Language Model Financial Trading Decision Framework**. Optimized for global users, providing comprehensive analysis capabilities for A-shares, Hong Kong stocks, US stocks, and international markets.

## 🙏 Tribute to the Original Project

Thanks to the [Tauric Research](https://github.com/TauricResearch) team for creating the revolutionary multi-agent trading framework [TradingAgents](https://github.com/TauricResearch/TradingAgents)!

**🎯 Our Mission**: To provide a complete experience for global users, support A-share/Hong Kong stock markets, integrate leading large models, and promote the popularization of AI financial technology in the community.

## 🆕 v0.1.15 Major Updates

### 🤖 LLM Ecosystem Major Upgrade

- **Qianfan Model Support**: New Baidu Qianfan (ERNIE) large model complete integration
- **LLM Adapter Refactoring**: Unified OpenAI-compatible adapter architecture
- **Multi-Vendor Support**: Support for more leading large model providers
- **Integration Guide**: Complete LLM integration development documentation and testing tools

### 📚 Academic Research Support

- **TradingAgents Paper**: Complete translation and in-depth interpretation
- **Technical Blog**: Detailed technical analysis and implementation principle interpretation
- **Academic Materials**: PDF papers and related research materials
- **Citation Support**: Standard academic citation format and references

### 🛠️ Developer Experience Upgrade

- **Development Workflow**: Standardized development process and branch management standards
- **Installation Verification**: Complete installation testing and verification scripts
- **Documentation Refactoring**: Structured documentation system and quick start guide
- **PR Templates**: Standardized Pull Request templates and code review process

### 🔧 Enterprise-Grade Toolchain

- **Branch Protection**: GitHub branch protection strategies and security rules
- **Emergency Procedures**: Complete emergency handling and fault recovery procedures
- **Testing Framework**: Enhanced test coverage and verification tools
- **Deployment Guide**: Enterprise-grade deployment and configuration management

## 📋 v0.1.14 Feature Review

### 👥 User Permission Management System

- **Complete User Management**: New user registration, login, permission control features
- **Role Permissions**: Support for multi-level user roles and permission management
- **Session Management**: Secure user session and state management
- **User Activity Log**: Complete user operation recording and audit functionality

### 🔐 Web User Authentication System

- **Login Component**: Modern user login interface
- **Authentication Manager**: Unified user authentication and authorization management
- **Security Enhancement**: Password encryption, session security and other security mechanisms
- **User Dashboard**: Personalized user activity dashboard

### 🗄️ Data Management Optimization

- **MongoDB Integration Enhancement**: Improved MongoDB connection and data management
- **Data Directory Reorganization**: Optimized data storage structure and management
- **Data Migration Scripts**: Complete data migration and backup tools
- **Cache Optimization**: Improved data loading and analysis result cache performance

### 🧪 Test Coverage Enhancement

- **Functional Test Scripts**: Added 6 specialized functional test scripts
- **Tool Handler Testing**: Google tool handler fix verification
- **Auto-hide Guidance Testing**: UI interaction functionality testing
- **Online Tool Configuration Testing**: Tool configuration and selection logic testing
- **Real Scenario Testing**: End-to-end testing of actual use scenarios
- **US Stock Independence Testing**: US stock analysis functionality independence verification

---

## 🆕 v0.1.13 Major Updates

### 🤖 Native OpenAI Endpoint Support

- **Custom OpenAI Endpoint**: Support for configuring any OpenAI-compatible API endpoint
- **Flexible Model Selection**: Can use any OpenAI format model, not limited to official models
- **Smart Adapter**: New native OpenAI adapter, providing better compatibility and performance
- **Configuration Management**: Unified endpoint and model configuration management system

### 🧠 Google AI Ecosystem Full Integration

- **Three Major Google AI Packages Support**: langchain-google-genai, google-generativeai, google-genai
- **9 Verified Models**: gemini-2.5-pro, gemini-2.5-flash, gemini-2.0-flash and other latest models
- **Google Tool Handler**: Dedicated Google AI tool invocation handler
- **Smart Degradation Mechanism**: Automatic degradation to basic features when advanced features fail

### 🔧 LLM Adapter Architecture Optimization

- **GoogleOpenAIAdapter**: New Google AI OpenAI-compatible adapter
- **Unified Interface**: All LLM providers use a unified invocation interface
- **Error Handling Enhancement**: Improved exception handling and automatic retry mechanism
- **Performance Monitoring**: Added LLM invocation performance monitoring and statistics

### 🎨 Web Interface Smart Optimization

- **Smart Model Selection**: Automatically select the best model based on availability
- **KeyError Fix**: Completely solve KeyError issues in model selection
- **UI Response Optimization**: Improved model switching response speed and user experience
- **Error Prompts**: More friendly error prompts and solution suggestions

## 🆕 v0.1.12 Major Updates

### 🧠 Smart News Analysis Module

- **Smart News Filter**: AI-based news relevance scoring and quality assessment
- **Multi-level Filtering Mechanism**: Three-tier processing with basic, enhanced, and integrated filtering
- **News Quality Assessment**: Automatic identification and filtering of low-quality, duplicate, and irrelevant news
- **Unified News Tool**: Integrate multiple news sources, providing a unified news acquisition interface

### 🔧 Technical Fixes and Optimizations

- **DashScope Adapter Fix**: Resolve tool invocation compatibility issues
- **DeepSeek Infinite Loop Fix**: Fix infinite loop problem in news analyst
- **LLM Tool Invocation Enhancement**: Improve tool invocation reliability and stability
- **News Retriever Optimization**: Enhanced news data acquisition and processing capabilities

### 📚 Improved Testing and Documentation

- **Comprehensive Test Coverage**: Added 15+ test files covering all new features
- **Detailed Technical Documentation**: Added 8 technical analysis reports and fix documentation
- **User Guide Improvement**: Added news filtering usage guide and best practices
- **Demo Scripts**: Provide complete news filtering feature demonstrations

### 🗂️ Project Structure Optimization

- **Documentation Organization**: Organize documents by function into docs subdirectory
- **Example Code Organization**: Unified demo scripts to examples directory
- **Clean Root Directory**: Keep root directory clean, enhance project professionalism

## 🎯 Core Features

### 🤖 Multi-Agent Collaborative Architecture

- **Professional Division**: Four major analysts - fundamental, technical, news, and social media
- **Structured Debate**: Bullish/bearish researchers conduct in-depth analysis
- **Smart Decision Making**: Traders make final investment recommendations based on all inputs
- **Risk Management**: Multi-level risk assessment and management mechanisms

## 🖥️ Web Interface Showcase

### 📸 Interface Screenshots

> 🎨 **Modern Web Interface**: Responsive web application built on Streamlit, providing intuitive stock analysis experience

#### 🏠 Main Interface - Analysis Configuration

![1755003162925](images/README/1755003162925.png)

![1755002619976](images/README/1755002619976.png)

*Smart configuration panel, supports multi-market stock analysis, 5-level research depth selection*

#### 📊 Real-time Analysis Progress

![1755002731483](images/README/1755002731483.png)

*Real-time progress tracking, visualized analysis process, smart time estimation*

#### 📈 Analysis Results Display

![1755002901204](images/README/1755002901204.png)

![1755002924844](images/README/1755002924844.png)

![1755002939905](images/README/1755002939905.png)

![1755002968608](images/README/1755002968608.png)

![1755002985903](images/README/1755002985903.png)

![1755003004403](images/README/1755003004403.png)

![1755003019759](images/README/1755003019759.png)

![1755003033939](images/README/1755003033939.png)

![1755003048242](images/README/1755003048242.png)

![1755003064598](images/README/1755003064598.png)

![1755003090603](images/README/1755003090603.png)

*Professional investment reports, multi-dimensional analysis results, one-click export functionality*

### 🎯 Core Feature Highlights

#### 📋 **Smart Analysis Configuration**

- **🌍 Multi-Market Support**: One-stop analysis for US stocks, A-shares, and Hong Kong stocks
- **🎯 5-Level Research Depth**: From 2-minute quick analysis to 25-minute comprehensive research
- **🤖 Agent Selection**: Market technical, fundamental, news, and social media analysts
- **📅 Flexible Time Settings**: Support analysis at any historical time point

#### 🚀 **Real-time Progress Tracking**

- **📊 Visualized Progress**: Real-time display of analysis progress and remaining time
- **🔄 Smart Step Recognition**: Automatically identify current analysis stage
- **⏱️ Accurate Time Estimation**: Smart time calculation based on historical data
- **💾 State Persistence**: Analysis progress not lost on page refresh

#### 📈 **Professional Results Display**

- **🎯 Investment Decisions**: Clear buy/hold/sell recommendations
- **📊 Multi-dimensional Analysis**: Comprehensive evaluation of technical, fundamental, and news aspects
- **🔢 Quantitative Indicators**: Confidence level, risk score, target price
- **📄 Professional Reports**: Support Markdown/Word/PDF format export

#### 🤖 **Multi-LLM Model Management**

- **🌐 4 Major Providers**: DashScope, DeepSeek, Google AI, OpenRouter
- **🎯 60+ Model Selection**: Full coverage from economy to flagship models
- **💾 Configuration Persistence**: URL parameter storage, settings maintained on refresh
- **⚡ Quick Switch**: 5 popular model one-click selection buttons

### 🎮 Web Interface User Guide

#### 🚀 **Quick Start Process**

1. **Launch Application**: `python start_web.py` or `docker-compose up -d`
2. **Access Interface**: Open browser to `http://localhost:8501`
3. **Configure Model**: Select LLM provider and model in sidebar
4. **Input Stock**: Enter stock symbol (e.g., AAPL, 000001, 0700.HK)
5. **Select Depth**: Choose 1-5 level research depth based on needs
6. **Start Analysis**: Click "🚀 Start Analysis" button
7. **View Results**: Track real-time progress and view analysis report
8. **Export Report**: One-click export professional format reports

#### 📊 **Supported Stock Symbol Formats**

- **🇺🇸 US Stocks**: `AAPL`, `TSLA`, `MSFT`, `NVDA`, `GOOGL`
- **🇨🇳 A-Shares**: `000001`, `600519`, `300750`, `002415`
- **🇭🇰 Hong Kong Stocks**: `0700.HK`, `9988.HK`, `3690.HK`, `1810.HK`

#### 🎯 **Research Depth Explanation**

- **Level 1 (2-4 minutes)**: Quick overview, basic technical indicators
- **Level 2 (4-6 minutes)**: Standard analysis, technical + fundamental
- **Level 3 (6-10 minutes)**: Deep analysis, includes news sentiment ⭐ **Recommended**
- **Level 4 (10-15 minutes)**: Comprehensive analysis, multi-round agent debate
- **Level 5 (15-25 minutes)**: Deepest analysis, complete research report

#### 💡 **Usage Tips**

- **🔄 Real-time Refresh**: Can refresh page anytime during analysis, progress not lost
- **📱 Mobile Compatibility**: Supports mobile phone and tablet access
- **🎨 Dark Mode**: Automatically adapts to system theme settings
- **⌨️ Keyboard Shortcuts**: Support Enter key for quick analysis submission
- **📋 History**: Automatically saves recent analysis configurations

> 📖 **Detailed Guide**: For complete web interface usage instructions, refer to [🖥️ Web Interface Detailed User Guide](docs/usage/web-interface-detailed-guide.md)

## 🎯 Features

### 🚀 Smart News Analysis✨ **v0.1.12 Major Upgrade**


| Feature               | Status        | Detailed Description                                 |
| ---------------------- | ----------- | ---------------------------------------- |
| **🧠 Smart News Analysis**    | 🆕 v0.1.12  | AI news filtering, quality assessment, relevance analysis         |
| **🔧 News Filter**      | 🆕 v0.1.12  | Multi-level filtering, basic/enhanced/integrated three-tier processing       |
| **📰 Unified News Tool**    | 🆕 v0.1.12  | Integrate multi-source news, unified interface, smart retrieval         |
| **🤖 Multi-LLM Providers**     | 🆕 v0.1.11  | 4 major providers, 60+ models, smart classification management         |
| **💾 Model Selection Persistence**  | 🆕 v0.1.11  | URL parameter storage, refresh retention, configuration sharing          |
| **🎯 Quick Selection Buttons**    | 🆕 v0.1.11  | One-click switch popular models, improve operation efficiency           |
| **📊 Real-time Progress Display**    | ✅ v0.1.10  | Async progress tracking, smart step recognition, accurate time calculation |
| **💾 Smart Session Management**    | ✅ v0.1.10  | State persistence, automatic degradation, cross-page recovery         |
| **🎯 One-click View Report**    | ✅ v0.1.10  | One-click view after analysis completion, smart result recovery         |
| **🖥️ Streamlit Interface** | ✅ Full Support | Modern responsive interface, real-time interaction and data visualization   |
| **⚙️ Configuration Management**      | ✅ Full Support | Web-based API key management, model selection, parameter configuration     |

### 🎨 CLI User Experience ✨ **v0.1.9 Optimization**


| Feature                | Status        | Detailed Description                             |
| ----------------------- | ----------- | ------------------------------------ |
| **🖥️ Interface and Log Separation** | ✅ Full Support | Clean and beautiful user interface, independent technical log management   |
| **🔄 Smart Progress Display**     | ✅ Full Support | Multi-stage progress tracking, prevent duplicate prompts         |
| **⏱️ Time Estimation Function**   | ✅ Full Support | Smart analysis stage display estimated time             |
| **🌈 Rich Color Output**     | ✅ Full Support | Color progress indicators, status icons, visual effect enhancement |

### 🧠 LLM Model Support ✨ **v0.1.13 Comprehensive Upgrade**


| Model Provider        | Supported Models                     | Featured Functions                | New Features |
| ----------------- | ---------------------------- | ----------------------- | -------- |
| **🇨🇳 Alibaba Qwen** | qwen-turbo/plus/max          | Leading optimization, cost-effective    | ✅ Integrated  |
| **🇨🇳 DeepSeek** | deepseek-chat                | Tool invocation, extremely cost-effective    | ✅ Integrated  |
| **🌍 Google AI**  | **9 Verified Models**              | Latest Gemini 2.5 series      | 🆕 Upgraded  |
| ├─**Latest Flagship**  | gemini-2.5-pro/flash         | Latest flagship, ultra-fast response      | 🆕 New  |
| ├─**Stable Recommended**  | gemini-2.0-flash             | Recommended, balanced performance      | 🆕 New  |
| ├─**Classic Powerful**  | gemini-1.5-pro/flash         | Classic stable, high-quality analysis    | ✅ Integrated  |
| └─**Lightweight Fast**  | gemini-2.5-flash-lite        | Lightweight tasks, fast response    | 🆕 New  |
| **🌐 Native OpenAI** | **Custom Endpoint Support**           | Any OpenAI-compatible endpoint      | 🆕 New  |
| **🌐 OpenRouter** | **60+ Model Aggregation Platform**          | Access all mainstream models with one API | ✅ Integrated  |
| ├─**OpenAI**    | o4-mini-high, o3-pro, GPT-4o | Latest o-series, reasoning professional version   | ✅ Integrated  |
| ├─**Anthropic** | Claude 4 Opus/Sonnet/Haiku   | Top performance, balanced version      | ✅ Integrated  |
| ├─**Meta**      | Llama 4 Maverick/Scout       | Latest Llama 4 series         | ✅ Integrated  |
| └─**Custom**    | Any OpenRouter model ID         | Unlimited expansion, personalized selection    | ✅ Integrated  |

**🎯 Quick Selection**: 5 popular model quick buttons | **💾 Persistence**: URL parameter storage, refresh retention | **🔄 Smart Switch**: One-click switch between different providers

### 📊 Data Sources and Markets


| Market Type      | Data Source                   | Coverage                     |
| ------------- | ------------------------ | ---------------------------- |
| **🇨🇳 A-Shares**  | Tushare, AkShare, TDX | Shanghai and Shenzhen markets, real-time quotes, financial data |
| **🇭🇰 Hong Kong Stocks** | AkShare, Yahoo Finance   | HKEX, real-time quotes, fundamentals     |
| **🇺🇸 US Stocks** | FinnHub, Yahoo Finance   | NYSE, NASDAQ, real-time data       |
| **📰 News**   | Google News              | Real-time news, multi-language support         |

### 🤖 Agent Team

**Analyst Team**: 📈Market Analysis | 💰Fundamental Analysis | 📰News Analysis | 💬Sentiment Analysis
**Research Team**: 🐂Bullish Researcher | 🐻Bearish Researcher | 🎯Trading Decision Maker
**Management**: 🛡️Risk Manager | 👔Research Director

## 🚀 Quick Start

### 🐳 Docker Deployment (Recommended)

```bash
# 1. Clone the project
git clone https://github.com/hsliuping/TradingAgents-CN.git
cd TradingAgents-CN

# 2. Configure environment variables
cp .env.example .env
# Edit .env file, fill in API keys

# 3. Start services
# First startup or code changes (need to build image)
docker-compose up -d --build

# Daily startup (image exists, no code changes)
docker-compose up -d

# Smart startup (automatically determine if build is needed)
# Windows environment
powershell -ExecutionPolicy Bypass -File scripts\smart_start.ps1

# Linux/Mac environment
chmod +x scripts/smart_start.sh && ./scripts/smart_start.sh

# 4. Access application
# Web interface: http://localhost:8501
```

### 💻 Local Deployment

```bash
# 1. Upgrade pip (Important! Avoid installation errors)
python -m pip install --upgrade pip

# 2. Install dependencies
pip install -e .

# 3. Start application
python start_web.py

# 4. Access http://localhost:8501
```

### 📊 Start Analysis

1. **Select Model**: DeepSeek V3 / Qwen / Gemini
2. **Input Stock**: `000001` (A-Share) / `AAPL` (US Stock) / `0700.HK` (HK Stock)
3. **Start Analysis**: Click "🚀 Start Analysis" button
4. **Real-time Tracking**: Observe real-time progress and analysis steps
5. **View Report**: Click "📊 View Analysis Report" button
6. **Export Report**: Support Word/PDF/Markdown formats

## 🔐 User Permission Management

### 🔑 Default Account Information

The system provides the following default accounts, automatically created on first startup:

| Username | Password | Role | Permission Description |
|--------|------|------|----------|
| **admin** | **admin123** | Administrator | Full system permissions, user management, system configuration |
| **user** | **user123** | Regular User | Stock analysis, report viewing, basic functions |

> ⚠️ **Security Reminder**: Please change the default password immediately after first login!

### 🛡️ Permission Control System

- **🔐 Login Authentication**: Secure authentication based on username and password
- **👥 Role Management**: Multi-level permissions including administrators and regular users
- **⏰ Session Management**: Automatic timeout protection, secure logout
- **📊 Operation Log**: Complete user activity records

### 🛠️ User Management Tools

The system provides complete command-line user management tools:

#### Windows Users
```powershell
# Using PowerShell script
.\scripts\user_manager.ps1 list                    # List all users
.\scripts\user_manager.ps1 change-password admin   # Change password
.\scripts\user_manager.ps1 create newuser trader  # Create new user
.\scripts\user_manager.ps1 delete olduser         # Delete user

# Or use batch file
.\scripts\user_manager.bat list
```

#### Python Script (Cross-platform)
```bash
# Use Python script directly
python scripts/user_password_manager.py list
python scripts/user_password_manager.py change-password admin
python scripts/user_password_manager.py create newuser --role trader
python scripts/user_password_manager.py delete olduser
python scripts/user_password_manager.py reset  # Reset to default configuration
```

### 📋 Supported User Operations

- **📝 List Users**: View all users and their role permissions
- **🔑 Change Password**: Secure password update mechanism
- **👤 Create User**: Support custom roles and permissions
- **🗑️ Delete User**: Secure user deletion function
- **🔄 Reset Configuration**: Restore default user settings

### 📁 Configuration File Location

User configuration stored in: `web/config/users.json`

> 📚 **Detailed Documentation**: For complete user management guide, refer to [scripts/USER_MANAGEMENT.md](scripts/USER_MANAGEMENT.md)

### 🚧 Current Version Limitations

- ❌ Online user registration not yet supported
- ❌ Web interface role management not yet supported
- ✅ Full command-line user management supported
- ✅ Complete permission control framework supported

---

## 🎯 Core Advantages

- **🧠 Smart News Analysis**: v0.1.12 added AI-driven news filtering and quality assessment system
- **🔧 Multi-level Filtering**: Three-tier news filtering mechanism with basic, enhanced, and integrated levels
- **📰 Unified News Tool**: Integrate multi-source news, providing unified smart retrieval interface
- **🆕 Multi-LLM Integration**: v0.1.11 added 4 major providers, 60+ models, one-stop AI experience
- **💾 Configuration Persistence**: True model selection persistence, URL parameter storage, refresh retention
- **🎯 Quick Switch**: 5 popular model quick buttons, one-click switch between different AIs
- **🆕 Real-time Progress**: v0.1.10 async progress tracking, goodbye to black-box waiting
- **💾 Smart Session**: State persistence, analysis results not lost on page refresh
- **🔐 User Permissions**: v0.1.14 added complete user authentication and permission management system
- **🌍 Global Optimization**: A-share/Hong Kong stock data + leading LLM + multilingual interface
- **🐳 Containerization**: Docker one-click deployment, environment isolation, rapid scaling
- **📄 Professional Reports**: Multi-format export, automatic investment recommendation generation
- **🛡️ Stable and Reliable**: Multi-layer data sources, smart degradation, error recovery

## 🔧 Technical Architecture

**Core Technologies**: Python 3.10+ | LangChain | Streamlit | MongoDB | Redis
**AI Models**: DeepSeek V3 | Alibaba Qwen | Google AI | OpenRouter (60+ models) | OpenAI
**Data Sources**: Tushare | AkShare | FinnHub | Yahoo Finance
**Deployment**: Docker | Docker Compose | Local Deployment

## 📚 Documentation and Support

- **📖 Complete Documentation**: [docs/](./docs/) - Installation guide, usage tutorials, API documentation
- **🚨 Troubleshooting**: [troubleshooting/](./docs/troubleshooting/) - Common problem solutions
- **🔄 Changelog**: [CHANGELOG.md](./docs/releases/CHANGELOG.md) - Detailed version history
- **🚀 Quick Start**: [QUICKSTART.md](./QUICKSTART.md) - 5-minute quick deployment guide

## 🆚 Enhanced Features

**New additions compared to original**: Smart News Analysis | Multi-level News Filtering | News Quality Assessment | Unified News Tool | Multi-LLM Provider Integration | Model Selection Persistence | Quick Switch Buttons | Real-time Progress Display | Smart Session Management | International Interface | A-Share Data | Leading LLM | Docker Deployment | Professional Report Export | Unified Log Management | Web Configuration Interface | Cost Optimization

**Services included in Docker deployment**:

- 🌐 **Web Application**: TradingAgents-CN main program
- 🗄️ **MongoDB**: Data persistence storage
- ⚡ **Redis**: High-speed cache
- 📊 **MongoDB Express**: Database management interface
- 🎛️ **Redis Commander**: Cache management interface

#### 💻 Option 2: Local Deployment

**Applicable Scenarios**: Development environment, custom configuration, offline use

### Environment Requirements

- Python 3.10+ (Recommended 3.11)
- 4GB+ RAM (Recommended 8GB+)
- Stable network connection

### Installation Steps

```bash
# 1. Clone the project
git clone https://github.com/hsliuping/TradingAgents-CN.git
cd TradingAgents-CN

# 2. Create virtual environment
python -m venv env
# Windows
env\Scripts\activate
# Linux/macOS
source env/bin/activate

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. Install all dependencies
pip install -r requirements.txt
# Or use pip install -e .
pip install -e .

# Note: requirements.txt includes all necessary dependencies:
# - Database support (MongoDB + Redis)
# - Multi-market data sources (Tushare, AKShare, FinnHub, etc.)
# - Web interface and report export functionality
```

### Configure API Keys

#### 🇨🇳 Recommended: Use Alibaba Qwen (Leading Large Model)

```bash
# Copy configuration template
cp .env.example .env

# Edit .env file, configure the following required API keys:
DASHSCOPE_API_KEY=your_dashscope_api_key_here
FINNHUB_API_KEY=your_finnhub_api_key_here

# Recommended: Tushare API (Professional A-share data)
TUSHARE_TOKEN=your_tushare_token_here
TUSHARE_ENABLED=true

# Optional: Other AI model APIs
GOOGLE_API_KEY=your_google_api_key_here
DEEPSEEK_API_KEY=your_deepseek_api_key_here

# Database configuration (optional, improves performance)
# Local deployment uses standard ports
MONGODB_ENABLED=false  # Set to true to enable MongoDB
REDIS_ENABLED=false    # Set to true to enable Redis
MONGODB_HOST=localhost
MONGODB_PORT=27017     # Standard MongoDB port
REDIS_HOST=localhost
REDIS_PORT=6379        # Standard Redis port

# Docker deployment requires modifying hostname
# MONGODB_HOST=mongodb
# REDIS_HOST=redis
```

#### 📋 Deployment Mode Configuration Instructions

**Local Deployment Mode**:

```bash
# Database configuration (local deployment)
MONGODB_ENABLED=true
REDIS_ENABLED=true
MONGODB_HOST=localhost      # Local host
MONGODB_PORT=27017         # Standard port
REDIS_HOST=localhost       # Local host
REDIS_PORT=6379           # Standard port
```

**Docker Deployment Mode**:

```bash
# Database configuration (Docker deployment)
MONGODB_ENABLED=true
REDIS_ENABLED=true
MONGODB_HOST=mongodb       # Docker container service name
MONGODB_PORT=27017        # Standard port
REDIS_HOST=redis          # Docker container service name
REDIS_PORT=6379          # Standard port
```

> 💡 **Configuration Tips**:
>
> - Local deployment: Need to manually start MongoDB and Redis services
> - Docker deployment: Database services automatically started through docker-compose
> - Port conflicts: If local database services already exist, modify port mapping in docker-compose.yml

#### 🌍 Optional: Use International Models

```bash
# OpenAI (requires VPN)
OPENAI_API_KEY=your_openai_api_key

# Anthropic (requires VPN)
ANTHROPIC_API_KEY=your_anthropic_api_key
```

### 🗄️ Database Configuration (MongoDB + Redis)

#### High-Performance Data Storage Support

This project supports **MongoDB** and **Redis** databases, providing:

- **📊 Stock Data Caching**: Reduce API calls, improve response speed
- **🔄 Smart Degradation Mechanism**: Multi-layer data sources: MongoDB → API → Local cache
- **⚡ High-Performance Caching**: Redis caches hot data, millisecond-level response
- **🛡️ Data Persistence**: MongoDB stores historical data, supports offline analysis

#### Database Deployment Methods

**🐳 Docker Deployment (Recommended)**

If you use Docker deployment, the database is automatically included:

```bash
# Docker deployment automatically starts all services, including:
docker-compose up -d --build
# - Web application (port 8501)
# - MongoDB (port 27017)
# - Redis (port 6379)
# - Database management interface (ports 8081, 8082)
```

**💻 Local Deployment - Database Configuration**

If you use local deployment, you can choose the following methods:

**Method 1: Start Database Services Only**

```bash
# Start MongoDB + Redis services only (without Web application)
docker-compose up -d mongodb redis mongo-express redis-commander

# Check service status
docker-compose ps

# Stop services
docker-compose down
```

**Method 2: Complete Local Installation**

```bash
# Database dependencies are included in requirements.txt, no additional installation needed

# Start MongoDB (default port 27017)
mongod --dbpath ./data/mongodb

# Start Redis (default port 6379)
redis-server
```

> ⚠️ **Important Notes**:
>
> - **🐳 Docker Deployment**: Database automatically included, no additional configuration needed
> - **💻 Local Deployment**: Can choose to start database services only or complete local installation
> - **📋 Recommended**: Use Docker deployment for best experience and consistency

#### Database Configuration Options

**Environment Variable Configuration** (Recommended):

```bash
# MongoDB Configuration
MONGODB_HOST=localhost
MONGODB_PORT=27017
MONGODB_DATABASE=trading_agents
MONGODB_USERNAME=admin
MONGODB_PASSWORD=your_password

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=your_redis_password
REDIS_DB=0
```

**Configuration File Method**:

```python
# config/database_config.py
DATABASE_CONFIG = {
    'mongodb': {
        'host': 'localhost',
        'port': 27017,
        'database': 'trading_agents',
        'username': 'admin',
        'password': 'your_password'
    },
    'redis': {
        'host': 'localhost',
        'port': 6379,
        'password': 'your_redis_password',
        'db': 0
    }
}
```

#### Database Features

**MongoDB Features**:

- ✅ Stock basic information storage
- ✅ Historical price data caching
- ✅ Analysis result persistence
- ✅ User configuration management
- ✅ Automatic data synchronization

**Redis Features**:

- ⚡ Real-time price data caching
- ⚡ API response result caching
- ⚡ Session state management
- ⚡ Hot data preloading
- ⚡ Distributed lock support

#### Smart Degradation Mechanism

The system adopts a multi-layer data source degradation strategy to ensure high availability:

```
📊 Data Acquisition Process:
1. 🔍 Check Redis cache (millisecond-level)
2. 📚 Query MongoDB storage (second-level)
3. 🌐 Call TDX API (second-level)
4. 💾 Local file cache (backup)
5. ❌ Return error message
```

**Configure Degradation Strategy**:

```python
# Configure in .env file
ENABLE_MONGODB=true
ENABLE_REDIS=true
ENABLE_FALLBACK=true

# Cache expiration time (seconds)
REDIS_CACHE_TTL=300
MONGODB_CACHE_TTL=3600
```

#### Performance Optimization Recommendations

**Production Environment Configuration**:

```bash
# MongoDB Optimization
MONGODB_MAX_POOL_SIZE=50
MONGODB_MIN_POOL_SIZE=5
MONGODB_MAX_IDLE_TIME=30000

# Redis Optimization
REDIS_MAX_CONNECTIONS=20
REDIS_CONNECTION_POOL_SIZE=10
REDIS_SOCKET_TIMEOUT=5
```

#### Database Management Tools

```bash
# Initialize database
python scripts/setup/init_database.py

# System status check
python scripts/validation/check_system_status.py

# Cache cleanup tool
python scripts/maintenance/cleanup_cache.py --days 7
```

#### Troubleshooting

**Common Problem Solutions**:

1. **🪟 Windows 10 ChromaDB Compatibility Issue**

   **Problem Description**: On Windows 10, the error `Configuration error: An instance of Chroma already exists for ephemeral with different settings` appears, while Windows 11 works normally.

   **Quick Solutions**:

   ```bash
   # Solution 1: Disable memory feature (Recommended)
   # Add to .env file:
   MEMORY_ENABLED=false

   # Solution 2: Use dedicated fix script
   powershell -ExecutionPolicy Bypass -File scripts\fix_chromadb_win10.ps1

   # Solution 3: Run with administrator privileges
   # Right-click PowerShell -> "Run as administrator"
   ```

   **Detailed Solution**: Refer to [Windows 10 Compatibility Guide](docs/troubleshooting/windows10-chromadb-fix.md)
2. **MongoDB Connection Failed**

   **Docker Deployment**:

   ```bash
   # Check service status
   docker-compose logs mongodb

   # Restart service
   docker-compose restart mongodb
   ```

   **Local Deployment**:

   ```bash
   # Check MongoDB process
   ps aux | grep mongod

   # Restart MongoDB
   sudo systemctl restart mongod  # Linux
   brew services restart mongodb  # macOS
   ```
3. **Redis Connection Timeout**

   ```bash
   # Check Redis status
   redis-cli ping

   # Clear Redis cache
   redis-cli flushdb
   ```
4. **Cache Issues**

   ```bash
   # Check system status and cache
   python scripts/validation/check_system_status.py

   # Clean expired cache
   python scripts/maintenance/cleanup_cache.py --days 7
   ```

> 💡 **Tip**: Even without database configuration, the system can still run normally and will automatically degrade to direct API call mode. Database configuration is an optional performance optimization feature.

> 📚 **Detailed Documentation**: For more database configuration information, refer to [Database Architecture Documentation](docs/architecture/database-architecture.md)

### 📤 Report Export Functionality

#### New Feature: Professional Analysis Report Export

This project now supports exporting stock analysis results to multiple professional formats:

**Supported Export Formats**:

- **📄 Markdown (.md)** - Lightweight markup language, suitable for technical users and version control
- **📝 Word (.docx)** - Microsoft Word document, suitable for business reports and further editing
- **📊 PDF (.pdf)** - Portable document format, suitable for formal sharing and printing

**Report Content Structure**:

- 🎯 **Investment Decision Summary** - Buy/Hold/Sell recommendations, confidence level, risk score
- 📊 **Detailed Analysis Report** - Technical analysis, fundamental analysis, market sentiment, news events
- ⚠️ **Risk Disclaimer** - Complete investment risk statement and disclaimer clauses
- 📋 **Configuration Information** - Analysis parameters, model information, generation time

**Usage Instructions**:

1. After completing stock analysis, find the "📤 Export Report" section at the bottom of the results page
2. Select the desired format: Markdown, Word, or PDF
3. Click the export button, the system will automatically generate and provide download

**Install Export Dependencies**:

```bash
# Install Python dependencies
pip install markdown pypandoc

# Install system tools (for PDF export)
# Windows: choco install pandoc wkhtmltopdf
# macOS: brew install pandoc wkhtmltopdf
# Linux: sudo apt-get install pandoc wkhtmltopdf
```

> 📚 **Detailed Documentation**: For complete export functionality usage guide, refer to [Export Functionality Guide](docs/EXPORT_GUIDE.md)

### 🚀 Start Application

#### 🐳 Docker Startup (Recommended)

If you use Docker deployment, the application is already automatically started:

```bash
# Application is running in Docker, access directly:
# Web interface: http://localhost:8501
# Database management: http://localhost:8081
# Cache management: http://localhost:8082

# Check running status
docker-compose ps

# View logs
docker-compose logs -f web
```

#### 💻 Local Startup

If you use local deployment:

```bash
# 1. Activate virtual environment
# Windows
.\env\Scripts\activate
# Linux/macOS
source env/bin/activate

# 2. Install project to virtual environment (Important!)
pip install -e .

# 3. Start Web management interface
# Method 1: Use project startup script (Recommended)
python start_web.py

# Method 2: Use original startup script
python web/run_web.py

# Method 3: Use streamlit directly (need to install project first)
streamlit run web/app.py
```

Then access `http://localhost:8501` in your browser

**Web Interface Featured Functions**:

- 🇺🇸 **US Stock Analysis**: Support AAPL, TSLA, NVDA and other US stock codes
- 🇨🇳 **A-Share Analysis**: Support 000001, 600519, 300750 and other A-share codes
- 📊 **Real-time Data**: TDX API provides A-share real-time market data
- 🤖 **Agent Selection**: Choose different analyst combinations
- 📤 **Report Export**: One-click export professional analysis reports in Markdown/Word/PDF format
- 🎯 **5-Level Research Depth**: From quick analysis (2-4 minutes) to comprehensive analysis (15-25 minutes)
- 📊 **Smart Analyst Selection**: Market technical, fundamental, news, social media analysts
- 🔄 **Real-time Progress Display**: Visualize analysis process, avoid waiting anxiety
- 📈 **Structured Results**: Investment recommendations, target price, confidence level, risk assessment
- 🌍 **Fully International**: Interface and analysis results optimized for international users

**Research Depth Level Description**:

- **Level 1 - Quick Analysis** (2-4 minutes): Daily monitoring, basic decisions
- **Level 2 - Basic Analysis** (4-6 minutes): Regular investment, balanced speed
- **Level 3 - Standard Analysis** (6-10 minutes): Important decisions, recommended default
- **Level 4 - In-depth Analysis** (10-15 minutes): Major investment, detailed research
- **Level 5 - Comprehensive Analysis** (15-25 minutes): Most important decisions, most comprehensive analysis

#### 💻 Code Invocation (For Developers)

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Configure Alibaba Qwen
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "dashscope"
config["deep_think_llm"] = "qwen-plus"      # Deep analysis
config["quick_think_llm"] = "qwen-turbo"    # Quick tasks

# Create trading agent
ta = TradingAgentsGraph(debug=True, config=config)

# Analyze stock (using Apple as example)
state, decision = ta.propagate("AAPL", "2024-01-15")

# Output analysis results
print(f"Recommended Action: {decision['action']}")
print(f"Confidence: {decision['confidence']:.1%}")
print(f"Risk Score: {decision['risk_score']:.1%}")
print(f"Reasoning: {decision['reasoning']}")
```

#### Quick Start Scripts

```bash
# Alibaba Qwen demo (Recommended for international users)
python examples/dashscope/demo_dashscope_chinese.py

# Alibaba Qwen complete demo
python examples/dashscope/demo_dashscope.py

# Alibaba Qwen simplified test
python examples/dashscope/demo_dashscope_simple.py

# OpenAI demo (Requires API access)
python examples/openai/demo_openai.py

# Integration test
python tests/integration/test_dashscope_integration.py
```

#### 📁 Data Directory Configuration

**New Feature**: Flexible data storage path configuration with multiple configuration methods:

```bash
# View current data directory configuration
python -m cli.main data-config --show

# Set custom data directory
python -m cli.main data-config --set /path/to/your/data

# Reset to default configuration
python -m cli.main data-config --reset
```

**Environment Variable Configuration**:

```bash
# Windows
set TRADING_AGENTS_DATA_DIR=C:\MyTradingData

# Linux/macOS
export TRADING_AGENTS_DATA_DIR=/home/user/trading_data
```

**Programmatic Configuration**:

```python
from tradingagents.config_manager import ConfigManager

# Set data directory
config_manager = ConfigManager()
config_manager.set_data_directory("/path/to/data")

# Get configuration
data_dir = config_manager.get_data_directory()
print(f"Data Directory: {data_dir}")
```

**Configuration Priority**: Program Settings > Environment Variables > Configuration File > Default Values

For detailed instructions, refer to: [📁 Data Directory Configuration Guide](docs/configuration/data-directory-configuration.md)

### Interactive Analysis

```bash
# Launch interactive command line interface
python -m cli.main
```

## 🎯 **Quick Navigation** - Find What You Need


| 🎯**I Want to...** | 📖**Recommended Documentation**                            | ⏱️**Reading Time** |
| ------------------- | ----------------------------------------------------------- | ------------------- |
| **Get Started**     | [🚀 Quick Start](docs/overview/quick-start.md)             | 10 minutes          |
| **Understand Architecture** | [🏛️ System Architecture](docs/architecture/system-architecture.md) | 15 minutes          |
| **See Code Examples** | [📚 Basic Examples](docs/examples/basic-examples.md)      | 20 minutes          |
| **Solve Problems**  | [🆘 FAQ](docs/faq/faq.md)                                  | 5 minutes           |
| **Deep Learning**   | [📁 Complete Documentation Directory](#-detailed-documentation-directory) | 2+ hours            |

> 💡 **Tip**: Our `docs/` directory contains **50,000+ words** of detailed documentation, this is the biggest difference from the original version!

## 📚 Complete Documentation System - Core Highlights

> **🌟 This is the biggest difference from the original project!** We've built the industry's most comprehensive documentation system for financial AI frameworks, containing over **50,000 words** of detailed technical documentation, **20+** professional document files, and **100+** code examples.

### 🎯 Why Choose Our Documentation?


| Comparison Dimension | Original TradingAgents | 🚀**Enhanced Version**        |
| -------------------- | ---------------------- | ------------------------------ |
| **Documentation Language** | Basic English description | **Complete international system** |
| **Documentation Depth** | Simple introduction    | **Deep technical analysis**    |
| **Architecture Description** | Conceptual description | **Detailed design docs + architecture diagrams** |
| **Usage Guide**      | Basic examples         | **Complete path from beginner to expert** |
| **Troubleshooting**  | None                   | **Detailed FAQ + solutions**   |
| **Code Examples**    | Few examples           | **100+ practical examples**    |

### 📖 Documentation Navigation - Organized by Learning Path

#### 🚀 **Beginner Path** (Recommended starting point)

1. [📋 Project Overview](docs/overview/project-overview.md) - **Understand project background and core value**
2. [⚙️ Detailed Installation](docs/overview/installation.md) - **Detailed installation guide for all platforms**
3. [🚀 Quick Start](docs/overview/quick-start.md) - **10-minute getting started guide**
4. [📚 Basic Examples](docs/examples/basic-examples.md) - **8 practical beginner examples**

#### 🏗️ **Architecture Understanding Path** (Deep dive into system design)

1. [🏛️ System Architecture](docs/architecture/system-architecture.md) - **Complete system architecture design**
2. [🤖 Agent Architecture](docs/architecture/agent-architecture.md) - **Multi-agent collaboration mechanisms**
3. [📊 Data Flow Architecture](docs/architecture/data-flow-architecture.md) - **Complete data processing pipeline**
4. [🔄 Graph Structure Design](docs/architecture/graph-structure.md) - **LangGraph workflow processes**

#### 🤖 **Agent Deep Dive** (Understanding each agent's design)

1. [📈 Analyst Team](docs/agents/analysts.md) - **Four types of professional analysts explained**
2. [🔬 Researcher Team](docs/agents/researchers.md) - **Bull/bear debate mechanisms**
3. [💼 Trader Agent](docs/agents/trader.md) - **Trading decision-making process**
4. [🛡️ Risk Management](docs/agents/risk-management.md) - **Multi-level risk assessment**
5. [👔 Management Agents](docs/agents/managers.md) - **Coordination and decision management**

#### 📊 **Data Processing Focus** (Master data processing techniques)

1. [🔌 Data Source Integration](docs/data/data-sources.md) - **Multi-data source API integration**
2. [⚙️ Data Processing Pipeline](docs/data/data-processing.md) - **Data cleaning and transformation**
3. [💾 Caching Strategy](docs/data/caching.md) - **Multi-layer cache performance optimization**

#### ⚙️ **Configuration and Optimization** (Performance tuning and customization)

1. [📝 Configuration Guide](docs/configuration/config-guide.md) - **Detailed configuration options**
2. [🧠 LLM Configuration](docs/configuration/llm-config.md) - **Large language model optimization**

#### 💡 **Advanced Applications** (Extended development and practical use)

1. [📚 Basic Examples](docs/examples/basic-examples.md) - **8 practical basic examples**
2. [🚀 Advanced Examples](docs/examples/advanced-examples.md) - **Complex scenarios and extended development**

#### ❓ **Problem Solving** (When you encounter issues)

1. [🆘 FAQ](docs/faq/faq.md) - **Detailed FAQ and solutions**

### 📊 Documentation Statistics

- 📄 **Document Files**: 20+ professional documents
- 📝 **Total Words**: 50,000+ words of detailed content
- 💻 **Code Examples**: 100+ practical examples
- 📈 **Architecture Diagrams**: 10+ professional charts
- 🎯 **Coverage**: Complete path from beginner to expert

### 🎨 Documentation Features

- **🌍 Fully International**: Expression optimized for international users
- **📊 Rich Visual Content**: Abundant architecture diagrams and flowcharts
- **💻 Code-Rich**: Every concept has corresponding code examples
- **🔍 Deep Analysis**: Not just how to do it, but why to do it this way
- **🛠️ Practical Oriented**: All documentation is oriented towards real application scenarios

---

## 📚 Detailed Documentation Directory

### 📁 **docs/ Directory Structure** - Complete Knowledge System

```
docs/
├── 📖 overview/              # Project Overview - Must-read for beginners
│   ├── project-overview.md   # 📋 Detailed project introduction
│   ├── quick-start.md        # 🚀 10-minute quick start
│   └── installation.md       # ⚙️ Detailed installation guide
│
├── 🏗️ architecture/          # System Architecture - Deep understanding
│   ├── system-architecture.md    # 🏛️ Overall architecture design
│   ├── agent-architecture.md     # 🤖 Agent collaboration mechanisms
│   ├── data-flow-architecture.md # 📊 Data flow processing architecture
│   └── graph-structure.md        # 🔄 LangGraph workflow
│
├── 🤖 agents/               # Agent Details - Core components
│   ├── analysts.md          # 📈 Four types of professional analysts
│   ├── researchers.md       # 🔬 Bull/bear debate mechanisms
│   ├── trader.md           # 💼 Trading decision making
│   ├── risk-management.md  # 🛡️ Multi-level risk assessment
│   └── managers.md         # 👔 Management coordination
│
├── 📊 data/                 # Data Processing - Technical core
│   ├── data-sources.md      # 🔌 Multi-data source integration
│   ├── data-processing.md   # ⚙️ Data processing pipeline
│   └── caching.md          # 💾 Cache optimization strategy
│
├── ⚙️ configuration/        # Configuration Optimization - Performance tuning
│   ├── config-guide.md      # 📝 Detailed configuration explanation
│   └── llm-config.md       # 🧠 LLM model optimization
│
├── 💡 examples/             # Example Tutorials - Practical applications
│   ├── basic-examples.md    # 📚 8 basic examples
│   └── advanced-examples.md # 🚀 Advanced development examples
│
└── ❓ faq/                  # Problem Solving - Troubleshooting
    └── faq.md              # 🆘 FAQ
```

### 🎯 **Highly Recommended Documents** (Must-read selections)

#### 🔥 **Most Popular Documents**

1. **[📋 Project Overview](docs/overview/project-overview.md)** - ⭐⭐⭐⭐⭐

   > Understand the core value and technical features of the project, understand the entire framework in 5 minutes
   >
2. **[🏛️ System Architecture](docs/architecture/system-architecture.md)** - ⭐⭐⭐⭐⭐

   > Deep analysis of multi-agent collaboration mechanisms, including detailed architecture diagrams
   >
3. **[📚 Basic Examples](docs/examples/basic-examples.md)** - ⭐⭐⭐⭐⭐

   > 8 practical examples, from stock analysis to portfolio optimization
   >

#### 🚀 **Technical Deep Dive Documents**

1. **[🤖 Agent Architecture](docs/architecture/agent-architecture.md)**

   > Multi-agent design patterns and collaboration mechanisms explained
   >
2. **[📊 Data Flow Architecture](docs/architecture/data-flow-architecture.md)**

   > Complete process of data acquisition, processing, and caching
   >
3. **[🔬 Researcher Team](docs/agents/researchers.md)**

   > Innovative design of bull/bear researcher debate mechanisms
   >

#### 💼 **Practical Tool Documents**

1. **[🌐 Web Interface Guide](docs/usage/web-interface-guide.md)** - ⭐⭐⭐⭐⭐

   > Complete web interface usage tutorial, including detailed explanation of 5-level research depth
   >
2. **[💰 Investment Analysis Guide](docs/usage/investment_analysis_guide.md)**

   > Complete investment analysis tutorial from basic to advanced
   >
3. **[🧠 LLM Configuration](docs/configuration/llm-config.md)**

   > Multi-LLM model configuration and cost optimization strategies
   >
4. **[💾 Caching Strategy](docs/data/caching.md)**

   > Multi-layer cache design, significantly reducing API call costs
   >
5. **[🆘 FAQ](docs/faq/faq.md)**

   > Detailed FAQ and troubleshooting guide
   >

### 📖 **Browse Documents by Module**

<details>
<summary><strong>📖 Overview Documents</strong> - Essential reading for project entry</summary>

- [📋 Project Overview](docs/overview/project-overview.md) - Detailed project background and feature introduction
- [🚀 Quick Start](docs/overview/quick-start.md) - Complete guide from installation to first run
- [⚙️ Detailed Installation](docs/overview/installation.md) - Detailed installation instructions for all platforms

</details>

<details>
<summary><strong>🏗️ Architecture Documents</strong> - Deep understanding of system design</summary>

- [🏛️ System Architecture](docs/architecture/system-architecture.md) - Complete system architecture design
- [🤖 Agent Architecture](docs/architecture/agent-architecture.md) - Agent design patterns and collaboration mechanisms
- [📊 Data Flow Architecture](docs/architecture/data-flow-architecture.md) - Data acquisition, processing, and distribution pipeline
- [🔄 Graph Structure Design](docs/architecture/graph-structure.md) - LangGraph workflow process design

</details>

<details>
<summary><strong>🤖 Agent Documents</strong> - Core component details</summary>

- [📈 Analyst Team](docs/agents/analysts.md) - Four types of professional analysts explained
- [🔬 Researcher Team](docs/agents/researchers.md) - Bull/bear researchers and debate mechanisms
- [💼 Trader Agent](docs/agents/trader.md) - Trading decision-making process
- [🛡️ Risk Management](docs/agents/risk-management.md) - Multi-level risk assessment system
- [👔 Management Agents](docs/agents/managers.md) - Coordination and decision management

</details>

<details>
<summary><strong>📊 Data Processing</strong> - Technical core implementation</summary>

- [🔌 Data Source Integration](docs/data/data-sources.md) - Supported data sources and API integration
- [⚙️ Data Processing Pipeline](docs/data/data-processing.md) - Data cleaning, transformation, and validation
- [💾 Caching Strategy](docs/data/caching.md) - Multi-layer cache performance optimization

</details>

<details>
<summary><strong>⚙️ Configuration and Deployment</strong> - Performance tuning guide</summary>

- [📝 Configuration Guide](docs/configuration/config-guide.md) - Detailed configuration options explanation
- [🧠 LLM Configuration](docs/configuration/llm-config.md) - Large language model configuration optimization

</details>

<details>
<summary><strong>💡 Examples and Tutorials</strong> - Practical application guide</summary>

- [📚 Basic Examples](docs/examples/basic-examples.md) - 8 practical basic examples
- [🚀 Advanced Examples](docs/examples/advanced-examples.md) - Complex scenarios and extended development

</details>

<details>
<summary><strong>❓ Help Documents</strong> - Problem solutions</summary>

- [🆘 FAQ](docs/faq/faq.md) - Detailed FAQ and solutions

</details>

## 💰 Cost Control

### Typical Usage Costs

- **Economy Mode**: $0.01-0.05/analysis (using gpt-4o-mini)
- **Standard Mode**: $0.05-0.15/analysis (using gpt-4o)
- **High Precision Mode**: $0.10-0.30/analysis (using gpt-4o + multi-round debate)

### Cost Optimization Recommendations

```python
# Low-cost configuration example
cost_optimized_config = {
    "deep_think_llm": "gpt-4o-mini",
    "quick_think_llm": "gpt-4o-mini", 
    "max_debate_rounds": 1,
    "online_tools": False  # Use cached data
}
```

## 🤝 Contribution Guidelines

We welcome all forms of contributions:

### Contribution Types

- 🐛 **Bug Fixes** - Discover and fix issues
- ✨ **New Features** - Add new functionality
- 📚 **Documentation Improvements** - Enhance documentation and tutorials
- 🌐 **Localization** - Translation and localization work
- 🎨 **Code Optimization** - Performance optimization and code refactoring

### Contribution Process

1. Fork this repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Create Pull Request

### 📋 View Contributors

View all contributors and detailed contributions: **[🤝 Contributors List](CONTRIBUTORS.md)**

## 📄 License

This project is open source under the Apache 2.0 license. See [LICENSE](LICENSE) file for details.

### License Description

- ✅ Commercial use
- ✅ Modification and distribution
- ✅ Private use
- ✅ Patent use
- ❗ Must retain copyright notice
- ❗ Must include license copy

## 🙏 Acknowledgments and Gratitude

### 🌟 Tribute to Original Project Developers

We express our deepest respect and gratitude to the [Tauric Research](https://github.com/TauricResearch) team:

- **🎯 Visionary Leaders**: Thank you for your forward-thinking and innovative practices in the AI finance field
- **💎 Precious Source Code**: Thank you for every line of open source code, which embodies countless wisdom and effort
- **🏗️ Architecture Masters**: Thank you for designing such an elegant and scalable multi-agent framework
- **💡 Technology Pioneers**: Thank you for perfectly combining cutting-edge AI technology with financial practice
- **🔄 Continuous Contribution**: Thank you for your ongoing maintenance, updates, and improvements

### 🤝 Community Contributors Acknowledgment

Thank you to all developers and users who have contributed to the TradingAgents-CN project!

For detailed contributor list and contributions, see: **[📋 Contributors List](CONTRIBUTORS.md)**

Including but not limited to:

- 🐳 **Docker Containerization** - Deployment solution optimization
- 📄 **Report Export Functionality** - Multi-format output support
- 🐛 **Bug Fixes** - System stability improvements
- 🔧 **Code Optimization** - User experience improvements
- 📝 **Documentation Enhancement** - Usage guides and tutorials
- 🌍 **Community Building** - Issue feedback and promotion
- **🌍 Open Source Contribution**: Thank you for choosing the Apache 2.0 license, giving developers maximum freedom
- **📚 Knowledge Sharing**: Thank you for providing detailed documentation and best practice guidance

**Special Thanks**: The [TradingAgents](https://github.com/TauricResearch/TradingAgents) project provided us with a solid technical foundation. Although the Apache 2.0 license grants us the right to use the source code, we deeply understand the precious value of every line of code and will always remember and appreciate your selfless contributions.

### 🌍 Mission and Vision

Creating this enhanced version, we are driven by the following mission:

- **🌉 Technology Dissemination**: Enable excellent TradingAgents technology to gain wider application globally
- **🎓 Educational Outreach**: Provide better tools and resources for AI finance education worldwide
- **🤝 Cultural Bridge**: Build bridges for exchange and cooperation between international technology communities
- **🚀 Innovation Driver**: Promote AI technology innovation and application in the fintech field globally

### 🌍 Open Source Community

Thanks to all developers and users who have contributed code, documentation, suggestions, and feedback to this project. It is because of everyone's support that we can better serve the international user community.

### 🤝 Collaboration and Win-Win

We commit to:

- **Respect for Originality**: Always respect the intellectual property and open source agreements of the source project
- **Feedback Contribution**: Provide valuable improvements and innovations back to the source project and open source community
- **Continuous Improvement**: Continuously improve the enhanced version to provide better user experience
- **Open Collaboration**: Welcome technical exchange and cooperation with the source project team and global developers

## 📈 Version History

- **v0.1.15** (2025-10-04): 🤖 Major LLM ecosystem upgrade with Qianfan support, academic research materials, enterprise toolchain ✨ **Latest Version**
- **v0.1.14** (2025-09-15): 👥 Complete user permission management system and web authentication
- **v0.1.13** (2025-08-02): 🤖 Native OpenAI support and comprehensive Google AI ecosystem integration
- **v0.1.12** (2025-07-29): 🧠 Smart news analysis module and project structure optimization
- **v0.1.11** (2025-07-27): 🤖 Multi-LLM provider integration and model selection persistence
- **v0.1.10** (2025-07-18): 🚀 Web interface real-time progress display and smart session management
- **v0.1.9** (2025-07-16): 🎯 Major CLI user experience optimization and unified log management
- **v0.1.8** (2025-07-15): 🎨 Comprehensive web interface optimization and user experience enhancement
- **v0.1.7** (2025-07-13): 🐳 Containerized deployment and professional report export
- **v0.1.6** (2025-07-11): 🔧 Alibaba Qianfan fixes and data source upgrades
- **v0.1.5** (2025-07-08): 📊 Added DeepSeek model support
- **v0.1.4** (2025-07-05): 🏗️ Architecture optimization and configuration management refactoring
- **v0.1.3** (2025-06-28): 🇨🇳 Complete A-share market support
- **v0.1.2** (2025-06-15): 🌐 Web interface and configuration management
- **v0.1.1** (2025-06-01): 🧠 Leading LLM integration

📋 **Detailed Changelog**: [CHANGELOG.md](./docs/releases/CHANGELOG.md)

## 📞 Contact Information

- **GitHub Issues**: [Submit Issues and Suggestions](https://github.com/hsliuping/TradingAgents-CN/issues)
- **Email**: hsliup@163.com
- Project QQ Group: 782124367
- **Original Project**: [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- **Documentation**: [Complete Documentation Directory](docs/)

## ⚠️ Risk Disclaimer

**Important Statement**: This framework is for research and educational purposes only and does not constitute investment advice.

- 📊 Trading performance may vary due to multiple factors
- 🤖 AI model predictions have uncertainty
- 💰 Investment involves risks, decisions require caution
- 👨‍💼 Recommend consulting professional financial advisors

---

<div align="center">

**🌟 If this project helps you, please give us a Star!**

[⭐ Star this repo](https://github.com/hsliuping/TradingAgents-CN) | [🍴 Fork this repo](https://github.com/hsliuping/TradingAgents-CN/fork) | [📖 Read the docs](./docs/)

</div>
