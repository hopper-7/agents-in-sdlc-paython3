# Using Playwright MCP for GitHub Topic Search

## 快速開始 (Quick Start)

這個實作示範如何使用 Playwright MCP 工具來搜尋 GitHub 相關的演講主題。

### 指令範例

```bash
#playwright 幫我找 有關 github 的演講主題
https://www.digitimes.com.tw/Seminar/DevDaysAsia2025/index.html
```

### 運行範例腳本

```bash
# Python 版本
python scripts/playwright-github-search.py

# Node.js 版本
npm install
node scripts/playwright-github-search.js
```

## 搜尋結果範例

🎯 **找到的 GitHub 相關主題：**

1. **AI-Powered Development with GitHub Copilot**
   - 關鍵字: github copilot
   - 描述: 學習 GitHub Copilot 如何透過 AI 驅動的程式碼建議來轉變開發體驗
   - 相關性評分: 10/10

2. **CI/CD Automation with GitHub Actions**  
   - 關鍵字: github actions
   - 描述: 使用 GitHub Actions 建立強健的 CI/CD 管線
   - 相關性評分: 9/10

3. **Securing Your Codebase with GitHub Advanced Security**
   - 關鍵字: github security  
   - 描述: 探索 GitHub 的安全功能，包括祕密掃描和程式碼掃描
   - 相關性評分: 8/10

## 建議的 GitHub 演講主題

基於 DevDays Asia 2025 主題，以下是相關的 GitHub 主題建議：

1. **GitHub Copilot: 在亞洲市場加速開發**
2. **使用 GitHub Actions 建立彈性 CI/CD 管線**
3. **GitHub 企業安全最佳實務**
4. **全球團隊的協作開發工作流程**
5. **亞洲科技公司的開源策略**
6. **GitHub API 整合與自訂開發工具**
7. **使用 GitHub Actions 和雲服務的行動應用程式 CI/CD**
8. **GitHub 和 Terraform 的基礎架構即程式碼**
9. **使用 GitHub Checks 和 Reviews 的程式碼品質自動化**
10. **使用 GitHub Enterprise 的 DevOps 轉型**

## 設定檔案

`.vscode/mcp.json` 已設定 Playwright MCP 伺服器：

```json
{
  "servers": {
    "playwright": {
      "command": "npx",
      "args": ["--yes", "mcp-playwright"],
      "env": {
        "NODE_ENV": "development"
      }
    }
  }
}
```

## 檔案說明

- `scripts/playwright-github-search.py` - Python 實作範例
- `scripts/playwright-github-search.js` - Node.js 實作範例  
- `docs/playwright-github-search.md` - 詳細技術文件
- `package.json` - Node.js 相依性設定

## 功能特色

✅ **自動內容探索** - 自動找到相關主題，無需手動瀏覽  
✅ **全面搜尋** - 同時搜尋網站的多個區段  
✅ **相關性評分** - 基於關鍵字頻率和上下文優先排序主題  
✅ **節省時間** - 快速識別大型會議網站中的相關內容  
✅ **結構化輸出** - 提供人類可讀和機器可處理的格式結果  

## 技術實作

這個實作展示了如何：
- 使用 Playwright 進行網頁自動化
- 分析網頁內容中的 GitHub 相關關鍵字
- 提供相關性評分和建議
- 處理網站存取限制的備用方案

詳細技術文件請參閱 [docs/playwright-github-search.md](docs/playwright-github-search.md)。