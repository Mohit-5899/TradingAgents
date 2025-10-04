#!/usr/bin/env python3
"""
Translation Script for TradingAgents Codebase
Translates Chinese strings to English in user-facing components
"""

import os
import re
import glob
from pathlib import Path

# Translation mappings for common strings
TRANSLATIONS = {
    # Common UI elements
    "股票分析": "Stock Analysis",
    "股票代码": "Stock Code",
    "分析配置": "Analysis Configuration", 
    "分析结果": "Analysis Results",
    "分析日期": "Analysis Date",
    "开始分析": "Start Analysis",
    "分析报告": "Analysis Report",
    "市场分析": "Market Analysis",
    "基本面分析": "Fundamentals Analysis",
    "技术分析": "Technical Analysis",
    "新闻分析": "News Analysis",
    "情感分析": "Sentiment Analysis",
    "风险评估": "Risk Assessment",
    
    # Market types
    "美股": "US Stock",
    "A股": "A-Share", 
    "港股": "HK Stock",
    "选择市场": "Select Market",
    "市场类型": "Market Type",
    
    # User actions
    "请输入": "Please enter",
    "请选择": "Please select",
    "确认": "Confirm",
    "取消": "Cancel",
    "提交": "Submit",
    "重置": "Reset",
    "保存": "Save",
    "加载": "Load",
    "导出": "Export",
    "导入": "Import",
    
    # Status messages
    "成功": "Success",
    "失败": "Failed", 
    "错误": "Error",
    "警告": "Warning",
    "信息": "Info",
    "完成": "Completed",
    "进行中": "In Progress",
    "等待中": "Waiting",
    "已取消": "Cancelled",
    
    # Analysis depth
    "研究深度": "Research Depth",
    "快速分析": "Quick Analysis",
    "基础分析": "Basic Analysis", 
    "标准分析": "Standard Analysis",
    "深度分析": "Deep Analysis",
    "全面分析": "Comprehensive Analysis",
    
    # Analyst types
    "市场分析师": "Market Analyst",
    "基本面分析师": "Fundamentals Analyst",
    "新闻分析师": "News Analyst",
    "社交媒体分析师": "Social Media Analyst",
    "风险管理师": "Risk Manager",
    "投资顾问": "Investment Advisor",
    
    # Common phrases
    "用户登录": "User Login",
    "用户名": "Username",
    "密码": "Password",
    "登录": "Login",
    "退出": "Logout",
    "注册": "Register",
    "忘记密码": "Forgot Password",
    
    # Configuration
    "配置管理": "Configuration",
    "API密钥": "API Key",
    "系统设置": "System Settings",
    "用户设置": "User Settings",
    
    # File operations
    "文件上传": "File Upload",
    "文件下载": "File Download",
    "文件删除": "File Delete",
    
    # Time related
    "今天": "Today",
    "昨天": "Yesterday", 
    "明天": "Tomorrow",
    "本周": "This Week",
    "本月": "This Month",
    "本年": "This Year",
    
    # Data operations
    "数据加载": "Data Loading",
    "数据更新": "Data Update", 
    "数据同步": "Data Sync",
    "数据备份": "Data Backup",
    "数据恢复": "Data Recovery",
    
    # Navigation
    "首页": "Home",
    "返回": "Back",
    "下一步": "Next",
    "上一步": "Previous",
    "跳转": "Navigate",
    
    # Common buttons
    "立即登录": "Login Now",
    "开始分析": "Start Analysis",
    "查看报告": "View Report",
    "下载报告": "Download Report",
    "清除缓存": "Clear Cache",
    "刷新数据": "Refresh Data"
}

def translate_file(file_path):
    """Translate Chinese strings in a file to English"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = False
        
        # Apply translations
        for chinese, english in TRANSLATIONS.items():
            # Replace exact matches in quotes
            patterns = [
                f'"{chinese}"',
                f"'{chinese}'",
                f'f"{chinese}"',
                f"f'{chinese}'",
                f'"{chinese}:',
                f"'{chinese}:",
            ]
            
            replacements = [
                f'"{english}"',
                f"'{english}'",
                f'f"{english}"',
                f"f'{english}'",
                f'"{english}:',
                f"'{english}:",
            ]
            
            for pattern, replacement in zip(patterns, replacements):
                if pattern in content:
                    content = content.replace(pattern, replacement)
                    changes_made = True
        
        # Write back if changes were made
        if changes_made:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Translated: {file_path}")
            return True
        else:
            print(f"ℹ️  No changes: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error translating {file_path}: {e}")
        return False

def get_files_to_translate():
    """Get list of files that need translation"""
    base_path = Path(__file__).parent
    
    # Key directories to focus on
    patterns = [
        "web/**/*.py",
        "cli/**/*.py", 
        "tradingagents/agents/**/*.py",
        "examples/**/*.py"
    ]
    
    files = []
    for pattern in patterns:
        files.extend(glob.glob(str(base_path / pattern), recursive=True))
    
    # Filter out __pycache__ and other non-essential files
    filtered_files = []
    for file in files:
        if not any(exclude in file for exclude in ['__pycache__', '.pyc', 'test_', 'temp_']):
            filtered_files.append(file)
    
    return filtered_files

def main():
    """Main translation function"""
    print("🌍 Starting TradingAgents Translation to English")
    print("=" * 60)
    
    files = get_files_to_translate()
    print(f"📁 Found {len(files)} files to process")
    
    translated_count = 0
    for file_path in files:
        if translate_file(file_path):
            translated_count += 1
    
    print("=" * 60)
    print(f"✅ Translation completed!")
    print(f"📊 Files processed: {len(files)}")
    print(f"📝 Files translated: {translated_count}")
    print(f"📋 Files unchanged: {len(files) - translated_count}")

if __name__ == "__main__":
    main()