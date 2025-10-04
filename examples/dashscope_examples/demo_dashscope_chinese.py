#!/usr/bin/env python3
"""
TradingAgents English Demo Script - Using Alibaba DashScope Models
Stock analysis demo optimized for English-speaking users
"""

import os
import sys
from pathlib import Path

# Import logging module
from tradingagents.utils.logging_manager import get_logger
logger = get_logger('default')

# Add project root directory to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
from tradingagents.llm_adapters import ChatDashScope
from langchain_core.messages import HumanMessage, SystemMessage

# Load .env file
load_dotenv()

def analyze_stock_with_english_output(stock_symbol="AAPL", analysis_date="2024-05-10"):
    """Perform stock analysis using Alibaba DashScope in English"""
    
    logger.info(f"🚀 TradingAgents English Stock Analysis - DashScope Version")
    logger.info(f"=")
    
    # Check API keys
    dashscope_key = os.getenv('DASHSCOPE_API_KEY')
    finnhub_key = os.getenv('FINNHUB_API_KEY')
    
    if not dashscope_key:
        logger.error(f"❌ Error: DASHSCOPE_API_KEY environment variable not found")
        return
    
    if not finnhub_key:
        logger.error(f"❌ Error: FINNHUB_API_KEY environment variable not found")
        return
    
    logger.info(f"✅ DashScope API Key: {dashscope_key[:10]}...")
    logger.info(f"✅ FinnHub API Key: {finnhub_key[:10]}...")
    print()
    
    try:
        logger.info(f"🤖 Initializing DashScope LLM...")
        
        # Create DashScope model instance
        llm = ChatDashScope(
            model="qwen-plus-latest",
            temperature=0.1,
            max_tokens=3000
        )
        
        logger.info(f"✅ Model initialization successful!")
        print()
        
        logger.info(f"📈 Starting stock analysis for: {stock_symbol}")
        logger.info(f"📅 Analysis date: {analysis_date}")
        logger.info(f"⏳ Performing intelligent analysis, please wait...")
        print()
        
        # Build English analysis prompt
        system_prompt = """You are a professional stock analyst with extensive financial market experience. Please conduct analysis in English, ensuring content is professional, objective, and easy to understand.

Your task is to perform comprehensive analysis of the specified stock, including:
1. Technical analysis
2. Fundamental analysis  
3. Market sentiment analysis
4. Risk assessment
5. Investment recommendations

Ensure the analysis results:
- Use clear English expression
- Content is professional and accurate
- Structure is clear
- Include specific data and indicators
- Provide clear investment recommendations"""

        user_prompt = f"""Please conduct a comprehensive stock analysis of Apple Inc. (AAPL).

Analysis requirements:
1. **Technical Analysis**:
   - Price trend analysis
   - Key technical indicators (MA, MACD, RSI, Bollinger Bands, etc.)
   - Support and resistance levels
   - Volume analysis

2. **Fundamental Analysis**:
   - Company financial condition
   - Revenue and profit trends
   - Market position and competitive advantages
   - Future growth prospects

3. **Market Sentiment Analysis**:
   - Investor sentiment
   - Analyst ratings
   - Institutional holdings
   - Market focus and attention

4. **Risk Assessment**:
   - Major risk factors
   - Macroeconomic impact
   - Industry competition risks
   - Regulatory risks

5. **Investment Recommendations**:
   - Clear buy/hold/sell recommendations
   - Target price levels
   - Investment timeframe
   - Risk management suggestions

Please write a detailed analysis report in English, ensuring the content is professional and easy to understand."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        # Generate analysis report
        response = llm.invoke(messages)
        
        logger.info(f"🎯 English Analysis Report:")
        logger.info(f"=")
        print(response.content)
        logger.info(f"=")
        
        print()
        logger.info(f"✅ Analysis completed!")
        print()
        logger.info(f"🌟 DashScope LLM Advantages:")
        logger.info(f"  - Strong language understanding and expression")
        logger.info(f"  - Rich financial professional knowledge")
        logger.info(f"  - Clear and rigorous analysis logic")
        logger.info(f"  - Suitable for international investors")
        
        return response.content
        
    except Exception as e:
        logger.error(f"❌ Error occurred during analysis: {str(e)}")
        import traceback

        logger.error(f"🔍 Detailed error information:")
        traceback.print_exc()
        return None

def compare_models_english():
    """Compare different Qwen models' English expression capabilities"""
    logger.info(f"\n🔄 Comparing different Qwen models' English analysis capabilities")
    logger.info(f"=")
    
    models = [
        ("qwen-turbo", "Qwen Turbo"),
        ("qwen-plus", "Qwen Plus"),
        ("qwen-max", "Qwen Max")
    ]
    
    question = "Please summarize Apple Inc.'s current investment value in one paragraph, including advantages and risks."
    
    for model_id, model_name in models:
        try:
            logger.info(f"\n🧠 {model_name} Analysis:")
            logger.info(f"-")
            
            llm = ChatDashScope(model=model_id, temperature=0.1, max_tokens=500)
            response = llm.invoke([HumanMessage(content=question)])
            
            print(response.content)
            
        except Exception as e:
            logger.error(f"❌ {model_name} analysis failed: {str(e)}")

def main():
    """Main function"""
    # Perform complete stock analysis
    result = analyze_stock_with_english_output("AAPL", "2024-05-10")
    
    # Compare different models
    compare_models_english()
    
    logger.info(f"\n💡 Usage Recommendations:")
    logger.info(f"  1. Qwen Plus suitable for daily analysis, balancing performance and cost")
    logger.info(f"  2. Qwen Max suitable for deep analysis, highest quality")
    logger.info(f"  3. Qwen Turbo suitable for quick queries, fastest response")
    logger.info(f"  4. All models are optimized for multilingual capabilities")

if __name__ == "__main__":
    main()
