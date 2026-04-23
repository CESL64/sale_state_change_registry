# Sale State Change Registry

## Overview
`sale_state_change_registry` extends the base module `state_change_registry` to manage **state tracking for sales documents** in Odoo 18.

The module is focused on `sale.order` and provides complete traceability for sales order state transitions, including logs, chatter integration, report visibility, reporting tools, and email notifications.

## Main Features
- 🛒 Inherits `sale.order` and detects changes in the `state` field
- 📝 Creates a `state.change.registry` record for every relevant sales state transition
- 💬 Publishes a message in the sales order chatter when the state changes
- 🔗 Relates each log with its originating sales order through `sale_id`
- 📂 Adds a dedicated notebook page on the sales order form
- 📄 Extends the printed sales document with a state change section
- ✉️ Implements notification sending for sales-related records
- ✅ Updates `mail_sent` when the notification process is completed
- 📅 Includes a wizard to consult records by date range and company

## Notification Logic
This module inherits `send_state_change_notification()` from the base module and applies sales-specific behavior:

- only processes records where `document_type = 'sale'`
- uses `sale_id` to identify the source document
- sends notifications to followers of the sales order
- records the communication in the chatter for traceability

## User Experience
- New **Registro de Cambios de Estado** tab in the sales order form
- Read-only list of related logs
- Per-line action button to trigger notifications manually
- Reporting wizard accessible from the Sales reports menu

## Reports
- 📑 Inherited QWeb section inside the sales order report
- Presents state transition data in a structured table suitable for review and audit

## Dependencies
- `sale`
- `state_change_registry`

## Business Value
This module improves control over the sales process by making status transitions:
- visible
- auditable
- reportable
- communicable

It is particularly useful for organizations that need stronger operational follow-up on quotations, confirmations, and downstream sales document flow.
