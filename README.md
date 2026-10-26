# Axiocairn MCP

Axiocairn MCP lets AI agents retrieve published market research reports, their data dates, and their limitations.

[Traditional Chinese](README.zh-Hant.md) · [Connection guide](https://axiocairn.com/en/assistant) · [Service status](https://axiocairn.com/en/status)

## For AI agents

Connect to the hosted server at **https://axiocairn.com/mcp** using Streamable HTTP and the account authorization flow. No local server installation is needed.

| Entry | URL | Published connection status |
| --- | --- | --- |
| General MCP | https://axiocairn.com/mcp | Verification pending |
| ChatGPT | https://axiocairn.com/mcp/chatgpt | Verification pending |
| Grok | https://axiocairn.com/mcp/grok | Verification pending |
| Muse | https://axiocairn.com/mcp/muse | Verified in the connection guide |

These are deployed, account-protected endpoints. A listed URL alone does not establish client compatibility. The [connection guide](https://axiocairn.com/en/assistant) is the current source for connection status. The examples below are configuration templates; they do not establish a successful connection in each client.

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

Claude's connection remains pending in the published guide. For Claude Code, the [official remote HTTP configuration](https://code.claude.com/docs/en/mcp) supports this template using the general endpoint:

```sh
claude mcp add --transport http axiocairn https://axiocairn.com/mcp
```

Complete the client's authorization flow if offered. This command describes configuration, not verified Axiocairn compatibility. A verified Claude Desktop configuration is not currently published in the connection guide.

### ChatGPT

Use these values in a custom connector. Connection verification is pending.

```text
Name: Axiocairn
Connector URL: https://axiocairn.com/mcp/chatgpt
```

Review the account authorization screen before approving access. Follow the [connection guide](https://axiocairn.com/en/assistant) for the current setup status.

### Cursor

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

The published guide marks Muse as verified. Add a custom connector with these values:

```text
Name: Axiocairn
Connector URL: https://axiocairn.com/mcp/muse
```

Follow the [Muse guide](https://axiocairn.com/en/muse), authorize the account, and refresh the tool list.

## Tool reference

Tool discovery requires account authorization. Use the authorized server's `tools/list` response as the authority for the tools available to your connection; unauthenticated discovery returns an authorization error.

| Tool | When to use it |
| --- | --- |
| `get_todays_reports` | Find reports for today or a specified date, including the availability of the weekly House View. |
| `get_latest_report_by_type` | Retrieve the newest available report in a selected report family. |
| `search_report_archive` | Find published reports by type, date, ticker, or language. Use `report_type: "sample"` for sample reports. |
| `get_report_schedule` | Check expected report times, the schedule's time zone, and recorded generation times. |
| `get_symbol_reports` | List existing reports for a ticker, then retrieve the selected report type. If a report is not available yet, the response says so and, where your plan allows, may offer to prepare it. Availability is rolling out. |
| `get_house_view` | Check this week's House View and the next expected publication date; missing editions are identified. |

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

Access depends on account permissions, allowances, client support, and service availability. Reports may be incomplete or delayed. Retrieval covers existing reports; this documentation makes no claim that report generation on request is available. The connection reads research and does not place trades or manage accounts.

Axiocairn provides research information, not investment advice. Content is general, is not personalized, and is not a recommendation to buy or sell. Models cannot predict future outcomes. Investing involves the risk of loss. Verify information independently and read the [full disclosure](https://axiocairn.com/en/disclaimer).

Client names belong to their respective owners. Axiocairn is not affiliated with or endorsed by those companies. Report security concerns using [SECURITY.md](SECURITY.md).
