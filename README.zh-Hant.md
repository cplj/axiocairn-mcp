# Axiocairn MCP

[研究與學習](https://axiocairn.com/zh-hant/research)公開探索性論文與研究筆記的方法和限制；教程預計於 2026 年 11 月 6 日推出。

Axiocairn MCP 讓 AI 助理檢視持倉曝險、跑假設情境、估算交易成本與容量、檢查回測紀律，並讀取已發布的研究報告，附資料日期與限制。

[English](README.md) · [連線指南](https://axiocairn.com/zh-hant/assistant) · [服務狀態](https://axiocairn.com/zh-hant/status)

<img src="docs/media/claude-logo.svg" alt="Claude" width="112" height="24">

相容於 Claude（claude.ai 網頁版）。

存取依方案而定。

## 60 秒試用

1. 在你的 AI 應用新增自訂連接器，名稱填 Axiocairn，網址填下面這行。ChatGPT 請改用下表的 ChatGPT 網址。

   ```text
   https://axiocairn.com/mcp
   ```

2. 依提示用 Google 或 GitHub 登入。
3. 直接問：

   ```text
   Axiocairn 今天有哪些報告？
   ```

   ```text
   你看得到的最新一份 Axiocairn 報告，資料日期是哪天？是今天的版本嗎？
   ```

   ```text
   用幾個簡短重點說明 Axiocairn 報告有哪些限制。
   ```

## For AI agents

透過 Streamable HTTP 與帳號授權流程，連線至 **https://axiocairn.com/mcp**。不需要在本機安裝伺服器。

| 客戶端 | 網址 | 連線狀態 |
| --- | --- | --- |
| Claude（claude.ai 網頁版） | https://axiocairn.com/mcp | 已驗證（2026-10-27） |
| ChatGPT（網頁版） | https://axiocairn.com/mcp/chatgpt | 已驗證（2026-10-27） |
| Grok | https://axiocairn.com/mcp/grok | 待驗證 |
| Muse | https://axiocairn.com/mcp/muse | 待驗證 |
| 其他 MCP 客戶端（Claude Code、Cursor、Gemini CLI） | https://axiocairn.com/mcp | 待驗證 |

「已驗證」表示我們在該客戶端新增連接器、完成帳號授權，並在標示日期問過報告問題、拿到回答。以上為已部署、需要帳號授權的入口。列出網址本身不能證明客戶端相容性。下列內容是設定模板，不代表每個客戶端都已連線成功。

授權後，請呼叫 `tools/list`，取得現行工具名稱、描述與輸入結構。以下最小 `tools/call` 請求查詢報告時程：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_report_schedule",
    "arguments": {"language": "en"}
  }
}
```

回答應保留報告連結、資料日期、缺漏欄位與限制。預定發布時間不能證明報告已經可用。

## 客戶端設定

### Claude

在 claude.ai 開啟 Customize → Connectors → Add custom connector，名稱填 Axiocairn，網址填 `https://axiocairn.com/mcp`。這個做法已於 2026 年 10 月 27 日驗證。Claude Code 尚未驗證。Claude Code 的[官方遠端 HTTP 設定文件](https://code.claude.com/docs/en/mcp)支援下列使用通用入口的模板：

```sh
claude mcp add --transport http axiocairn https://axiocairn.com/mcp
```

若客戶端提供授權流程，請依畫面完成。這個指令說明設定方式，不代表 Axiocairn 相容性已通過驗證。連線指南目前沒有公布已驗證的 Claude Desktop 設定。

### ChatGPT

新增自訂連接器時，填入下列內容。已於 2026 年 10 月 27 日在 ChatGPT 網頁版驗證。

```text
Name: Axiocairn
Connector URL: https://axiocairn.com/mcp/chatgpt
```

批准存取前，請先閱讀帳號授權畫面。現行設定狀態以[連線指南](https://axiocairn.com/zh-hant/assistant)為準。

### Cursor

[加入 Cursor（Add to Cursor）](https://cursor.com/en/install-mcp?name=axiocairn&config=eyJ1cmwiOiJodHRwczovL2F4aW9jYWlybi5jb20vbWNwIn0%3D)

安裝前先在 Cursor 確認伺服器設定。出現授權提示時，登入 Axiocairn 並確認 OAuth 授權畫面（批准帳號存取的步驟）。此設定不需要填入 API 金鑰。

[Cursor MCP 文件](https://cursor.com/docs/context/mcp)說明如何在 `mcp.json` 設定遠端伺服器。請將下列項目合併至既有的 `mcpServers`，保留其他伺服器設定：

```json
{
  "mcpServers": {
    "axiocairn": {
      "url": "https://axiocairn.com/mcp"
    }
  }
}
```

Axiocairn 公開指南尚未將 Cursor 列為已驗證。此模板使用通用入口，需要相容的帳號授權流程。

### Gemini CLI

[Gemini CLI MCP 文件](https://geminicli.com/docs/tools/mcp-server/)說明 `settings.json` 中的 `httpUrl`。請將下列項目合併至既有設定：

```json
{
  "mcpServers": {
    "axiocairn": {
      "httpUrl": "https://axiocairn.com/mcp"
    }
  }
}
```

Axiocairn 公開指南尚未將 Gemini CLI 列為已驗證。此模板需要相容的遠端 HTTP 與帳號授權功能。

### Muse

Muse 尚待驗證。新增自訂連接器時，填入下列內容：

```text
Name: Axiocairn
Connector URL: https://axiocairn.com/mcp/muse
```

請依[Muse 指南](https://axiocairn.com/zh-hant/muse)完成帳號授權，再重新整理工具清單。

## 工具參考

工具探索需要帳戶授權。請以授權後伺服器回傳的 `tools/list` 為準；未授權的探索會收到授權錯誤。部分工具依方案限制。

| 工具 | 做什麼 |
| --- | --- |
| `analyze_holdings` | 檢視貼上的持倉：曝險、產業集中度與連動的 SPY 壓力估計。 |
| `check_portfolio` | 一籃部位的集中度、日波動、相關性與 SPY beta。 |
| `what_if` | 對既有持倉結果套用壓力情境、SPY 變動或權重調整。 |
| `estimate_cost_capacity` | 估算假設下單的成本，以及股票或 ETF 能承接的金額。 |
| `calculate_options` | 以有日期的歷史輸入計算描述性的 Black-Scholes-Merton 價格與 Greeks。 |
| `check_backtest_discipline` | 列出使用者提供的試驗次數、多重檢定折減與訓練／測試設定缺口。 |
| `check_idea` | 把代號、方向與期間改寫成可被推翻的陳述，並列出證據缺口。 |
| `get_screen` | 並列同一代號在有日期的模擬持倉清單中的讀數：列入、未列入、缺漏。 |
| `get_bench_result` | 以 job_id 讀取排隊中的計算結果、圖表資料與解讀說明。 |
| `get_data_quality` | 資料集日期、缺漏觀測、重複列與來源版本變動。 |
| `get_alerts` | 讀取依你設定的上限所記錄的比較結果。 |
| `get_alert_conditions` | 讀取你儲存的收盤條件與其版本。 |
| `set_alert_condition` | 儲存或停用一個收盤條件；不發送通知。 |
| `get_todays_reports` | 查今天或指定日期的報告，包括每週觀點。 |
| `get_latest_report_by_type` | 取得指定報告類別中最新的一份。 |
| `search_report_archive` | 依類別、日期、代號或語言找已發布報告；範例會標示。 |
| `search_reports` | 依代號、日期範圍與類別搜尋已有報告。 |
| `get_symbol_reports` | 列出某代號已有的報告，再取得你選的那份。 |
| `get_house_view` | 本週每週觀點，或下一個預計發布日期。 |
| `get_report_schedule` | 預計報告時間、時區與已記錄的生成時間。 |
| `get_usage_guide` | 報告類別、各自用途與新生成所需額度。 |
| `list_guides` | 列出說明中心主題。 |
| `get_guide` | 回傳單一說明項目的完整內容。 |
| `get_plans` | 方案、額度與升級方式，與網站方案設定同源。 |

## 登入一次，從 Reader 開始

連接器提示時登入一次。請使用 Axiocairn 帳號所用的同一個 Google 或 GitHub 帳號。批准前先閱讀存取範圍。授權到期或撤銷後，可能需要重新授權。

Reader 是免費層，提供有限的股票查詢、延遲的市場簡報與有限的歷史範圍；部分深入內容僅提供預覽。範例與報告存取依帳號權限開放。額度與存取條件請見[現行方案說明](https://axiocairn.com/zh-hant/subscribe)。連接客戶端不會擴大帳號權限。

連線失敗時，可以在網站閱讀帳號有權存取的報告。工具清單過期時，請重新連線。不要將帳號憑證貼入提問或共用設定檔。

## 範例提問

1. 今天有哪些報告可用？各自的資料日期是什麼？
2. 請提供最新盤前簡報，並指出缺少的資訊。
3. NVDA 有哪些已發布報告？請先讓我選擇，再開啟其中一份。
4. 當週 House View 是否可用？下一份預定何時發布？
5. 報告時程是什麼？哪些生成紀錄缺漏或延遲？

## 資料時間與休市日

請分別閱讀每份報告的資料截止時間與發布日期。今天讀取舊報告，不會讓內容變成今天的資料。預定時間與已記錄的生成時間描述不同事件，兩者都不能單獨證明已送達。

週末與市場休市日保留最近交易日的資料，因此查詢今天的報告可能沒有當日版本。請改查最新可用報告，並確認日期。時程與已知缺漏請見[服務狀態](https://axiocairn.com/zh-hant/status)與[常見問題](https://axiocairn.com/zh-hant/faq)。

## Registry 中繼資料

[`server.json`](server.json)以 `com.axiocairn/mcp` 描述託管伺服器，Streamable HTTP 遠端網址為 `https://axiocairn.com/mcp`。檔案使用官方 `2025-12-11` schema，查閱日期為 2026 年 10 月 25 日。

參考資料：[官方格式規格](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/generic-server-json.md)、[schema](https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json)與[遠端伺服器發布指南](https://modelcontextprotocol.io/registry/remote-servers)。本目錄含有中繼資料，不代表已列入 Registry。使用此 DNS 命名空間發布，需要驗證網域控制權。

## 限制與免責聲明

本目錄提供託管服務的文件與連線中繼資料，不包含伺服器實作，也不授予受限報告的存取權。MIT 授權適用於本目錄；報告內容另依[服務條款](https://axiocairn.com/zh-hant/terms)。

存取取決於帳號權限、額度、客戶端支援與服務可用性。報告可能不完整或延遲。連線可分析你提供的持倉、儲存你設定的收盤條件，並讀取已有報告；方案允許時，可請求新生成個股模型評估，並扣除生成額度。公司研究與事件研究尚未開放依請求生成。連線不下單，也不管理帳戶。

Axiocairn 提供研究資訊，不構成投資建議（research information, not investment advice）。內容為一般性資訊，並非個人化建議，也不是買賣推薦。模型無法預測未來結果。投資涉及損失風險。請獨立核實資訊，並閱讀[完整揭露](https://axiocairn.com/zh-hant/disclaimer)。

各客戶端名稱歸其權利人所有。Axiocairn 與這些公司沒有隸屬或背書關係。安全問題請依 [SECURITY.md](SECURITY.md) 回報。
