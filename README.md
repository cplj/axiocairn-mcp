# Axiocairn MCP

[Research & Learning](https://axiocairn.com/en/research) publishes exploratory papers and research notes with their methods and limitations; tutorials are coming on November 6, 2026.

Hedge-fund risk checks for your holdings: beta, concentration, scenarios, research.

Review where portfolio risk is concentrated before comparing hypothetical changes. Axiocairn measures holdings concentration, historical volatility and SPY beta, an estimate of sensitivity to SPY. Conditional scenarios show results under stated assumptions; they do not forecast returns. Results depend on the data window, coverage and assumptions, and historical relationships can change. Dated published research is also available within the signed-in account’s access. Some calculations and report generation use account allowance. Confirm the inputs and allowance use before requesting calculations or new reports. Saving, changing or deleting alert conditions, research plans or scenarios requires the applicable access and user agreement. Use synthetic or nonidentifying inputs. No brokerage connection or trade execution is provided. Results are for general research reference. Not personalized, not investment advice, and not a recommendation to buy or sell.

[Traditional Chinese](README.zh-Hant.md) · [Connection guide](https://axiocairn.com/en/assistant) · [Service status](https://axiocairn.com/en/status)

## A real question, a real output

> "I hold 50% NVDA, 30% MSFT, 20% SPY. How exposed am I to the market?"

| Reading | Value |
|---|---|
| Largest position | NVDA, 50% |
| Technology, direct weights (NVDA + MSFT) | 80% |
| Concentration (HHI) | 0.38 |
| Daily volatility | 1.58% |
| Beta to SPY | 1.47 |
| Beta on SPY down days (121 of 252) | 1.58 |
| Correlation with SPY: NVDA / MSFT | 0.66 / 0.39 |

Data date 2026-10-30. Window 2025-10-30 to 2026-10-30, 252 daily returns, licensed market data. This is a simulated holding with fixed weights, not an account and not advice. The readings describe how the three symbols moved together in that window, not a forecast. The 80% counts only the two direct technology positions, not what SPY holds.

<img src="docs/media/claude-logo.svg" alt="Claude" width="112" height="24">

Works with Claude (claude.ai web).

Access follows your plan.

## Try it in 60 seconds

1. In your AI app, add a custom connector named Axiocairn with this address. For ChatGPT, use the ChatGPT address in the table below.

   ```text
   https://axiocairn.com/mcp
   ```

2. Sign in with Google or GitHub when asked.
3. Ask:

   ```text
   What Axiocairn reports are available today?
   ```

   ```text
   What is the data date of the latest Axiocairn report you can see, and is it today's edition?
   ```

   ```text
   In a few short bullets, what are the limits of Axiocairn reports?
   ```

## For AI agents

Connect to the hosted server at **https://axiocairn.com/mcp** using Streamable HTTP and the account authorization flow. No local server installation is needed.

| Client | URL | Connection status |
| --- | --- | --- |
| Claude (claude.ai web) | https://axiocairn.com/mcp | Verified on 2026-10-27 |
| ChatGPT (web) | https://axiocairn.com/mcp/chatgpt | Verified on 2026-10-27 |
| Grok | https://axiocairn.com/mcp/grok | Verification pending |
| Muse | https://axiocairn.com/mcp/muse | Verification pending |
| Other MCP clients (Claude Code, Cursor, Gemini CLI) | https://axiocairn.com/mcp | Verification pending |

"Verified" means we added the connector, authorized an account, and got answers to report questions in that client on the date shown. These are deployed, account-protected endpoints. A listed URL alone does not establish client compatibility. The examples below are configuration templates; they do not establish a successful connection in each client.

After authorization, request `tools/list` for the current tool names, descriptions, and input schemas. This minimal `tools/call` request asks for report timing:

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

Keep the report link, data date, missing fields, and limitations in the answer. An expected publication time is not evidence that a report is available.

## Client configuration

### Claude

On claude.ai, open Customize → Connectors → Add custom connector, name it Axiocairn, and use `https://axiocairn.com/mcp`. This was verified on October 27, 2026. Claude Code has not been verified. For Claude Code, the [official remote HTTP configuration](https://code.claude.com/docs/en/mcp) supports this template using the general endpoint:

```sh
claude mcp add --transport http axiocairn https://axiocairn.com/mcp
```

Complete the client's authorization flow if offered. This command describes configuration, not verified Axiocairn compatibility. A verified Claude Desktop configuration is not currently published in the connection guide.

### ChatGPT

Use these values in a custom connector. This was verified in ChatGPT on the web on October 27, 2026.

```text
Name: Axiocairn
Connector URL: https://axiocairn.com/mcp/chatgpt
```

Review the account authorization screen before approving access. Follow the [connection guide](https://axiocairn.com/en/assistant) for the current setup status.

### Cursor

[Add to Cursor](https://cursor.com/en/install-mcp?name=axiocairn&config=eyJ1cmwiOiJodHRwczovL2F4aW9jYWlybi5jb20vbWNwIn0%3D)

Review the server configuration in Cursor before installing. When prompted, sign in to Axiocairn and review the OAuth authorization screen (the account access approval step). No API key belongs in this configuration.

The [Cursor MCP documentation](https://cursor.com/docs/context/mcp) describes remote server entries in `mcp.json`. Merge this entry into the existing `mcpServers` object without replacing other servers:

```json
{
  "mcpServers": {
    "axiocairn": {
      "url": "https://axiocairn.com/mcp"
    }
  }
}
```

Cursor is not listed as verified in Axiocairn's published guide. This template uses the general endpoint and requires a compatible account authorization flow.

### Gemini CLI

The [Gemini CLI MCP documentation](https://geminicli.com/docs/tools/mcp-server/) describes `httpUrl` in `settings.json`. Merge this entry into the existing settings:

```json
{
  "mcpServers": {
    "axiocairn": {
      "httpUrl": "https://axiocairn.com/mcp"
    }
  }
}
```

Gemini CLI is not listed as verified in Axiocairn's published guide. This template requires compatible remote HTTP and account authorization support.

### Muse

Muse verification is pending. Add a custom connector with these values:

```text
Name: Axiocairn
Connector URL: https://axiocairn.com/mcp/muse
```

Follow the [Muse guide](https://axiocairn.com/en/muse), authorize the account, and refresh the tool list.

## Tool reference

Tool discovery requires account authorization. Use the authorized server's `tools/list` response as the authority for the tools available to your connection; unauthenticated discovery returns an authorization error. Some tools are limited by plan.

| Tool | What it does |
| --- | --- |
| `analyze_holdings` | Review pasted holdings: exposures, sector concentration and a linked SPY stress estimate. |
| `check_portfolio` | Concentration, daily volatility, correlation and SPY beta of a basket. |
| `what_if` | Apply a stress scenario, an SPY move or a weight change to a prior holdings result. |
| `estimate_cost_capacity` | Estimate the cost of a hypothetical order and the size a stock or ETF can absorb. |
| `calculate_options` | Descriptive Black-Scholes-Merton prices and Greeks from dated historical inputs. |
| `check_backtest_discipline` | List supplied trial counts, multiple-testing adjustment and train/test gaps. |
| `check_idea` | Turn a symbol, direction and horizon into a falsifiable statement with its evidence gaps. |
| `get_screen` | Compare one symbol across dated simulated-position lists: listed, not listed, missing. |
| `get_bench_result` | Read a queued calculation by job_id: result, chart data and interpretation guide. |
| `get_data_quality` | Dataset dates, missing observations, duplicate rows and source-version changes. |
| `get_alerts` | Read recorded comparisons against limits you defined. |
| `get_alert_conditions` | Read your saved daily-close conditions and their versions. |
| `set_alert_condition` | Save or disable one daily-close condition; sends no notification. |
| `get_todays_reports` | Find reports for today or a given date, including the weekly House View. |
| `get_latest_report_by_type` | Retrieve the newest available report in a selected report family. |
| `search_report_archive` | Find published reports by type, date, ticker or language; samples are labelled. |
| `search_reports` | Search existing reports by ticker, date range and category. |
| `get_symbol_reports` | List the existing reports for a ticker, then retrieve the one you pick. |
| `get_house_view` | This week’s House View, or the next expected publication date. |
| `get_report_schedule` | Expected report times, time zone and recorded generation times. |
| `get_usage_guide` | Which report categories exist, what each is for and what generation costs in allowance. |
| `list_guides` | List help-center topics. |
| `get_guide` | Return one full help-center entry. |
| `get_plans` | Plans, allowances and how to upgrade, from the website plan settings. |

## Sign in once and start with Reader

Sign in once when the connector prompts you. Use the same Google or GitHub account as your Axiocairn account. Review the requested access before approving it. Reauthorization may be needed after access expires or is revoked.

Reader is the free tier. It includes limited ticker look-ups, delayed market briefs, and a limited history window; some in-depth content is a preview. Samples and report access follow the account's permissions. See the [current plan details](https://axiocairn.com/en/subscribe) for allowances and access conditions. Connecting a client does not expand those permissions.

If a connection fails, use the website to read the reports your account can access. Reconnect to refresh an outdated tool list. Do not paste account credentials into prompts or shared configuration files.

## Example questions

1. What reports are available for today, and what are their data dates?
2. Show the latest pre-market brief and identify any missing information.
3. Which published reports are available for NVDA? Let me choose one before opening it.
4. Is this week's House View available, and when is the next edition expected?
5. What is the report schedule, and which generation records are missing or delayed?

## Data time and market closures

Read each report's data cutoff and publication date separately. An older report does not become current because it is retrieved today. Expected times and recorded generation times describe different events; neither alone confirms delivery.

On weekends and market holidays, the service retains the latest trading day's data. A request for today's reports may therefore return no edition. Ask for the latest available report and check its date. Consult the [service status](https://axiocairn.com/en/status) and [FAQ](https://axiocairn.com/en/faq) for timing and known gaps.

## Registry metadata

[`server.json`](server.json) describes the hosted server as `com.axiocairn/mcp` with a Streamable HTTP remote at `https://axiocairn.com/mcp`. It uses the official `2025-12-11` schema, consulted on October 25, 2026.

References: [official format specification](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/generic-server-json.md), [schema](https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json), and [remote server publishing guide](https://modelcontextprotocol.io/registry/remote-servers). Including metadata here does not establish a Registry listing. Publishing under this DNS namespace requires ownership verification.

## Limits and disclaimer

This repository contains documentation and connection metadata for a hosted service. It does not contain the server implementation or grant access to restricted reports. The MIT license covers this repository; report content remains subject to the [service terms](https://axiocairn.com/en/terms).

Access depends on account permissions, allowances, client support, and service availability. Reports may be incomplete or delayed. The connection analyzes holdings you provide, stores the daily-close conditions you set, and reads existing reports. Where your plan allows, it can request a new stock model assessment, which uses generation allowance. Company research and event research are not generated on request yet. It does not place trades or manage accounts.

Axiocairn provides research information, not investment advice. Content is general, is not personalized, and is not a recommendation to buy or sell. Models cannot predict future outcomes. Investing involves the risk of loss. Verify information independently and read the [full disclosure](https://axiocairn.com/en/disclaimer).

Client names belong to their respective owners. Axiocairn is not affiliated with or endorsed by those companies. Report security concerns using [SECURITY.md](SECURITY.md).
