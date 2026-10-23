# Daily print and dispatch list (November beta posted workbooks)

Used by the owner's staff. One row per parcel. Template: `docs/printing/dispatch_list_template.csv` (open in Excel or Google Sheets).

## Columns
| Column | What to put |
|---|---|
| date | Date the row is sent to the printer (YYYY-MM-DD). One batch per day, before the printer's cutoff time. |
| child_level | 1 to 6 (ages 6-8 ... 11-13), as registered. |
| workbook_file | `outputs/print/Math_Inquirers_P<level>_Workbook_PRINT.pdf` (P1 = Level 1 ... P6 = Level 6). |
| quantity | Copies in this parcel (1 per child; 2 for siblings only if in one parcel). |
| parcel_name | Recipient name on the parcel (the "Parcel name" field if given, otherwise the parent's name). |
| address | Block/house number, street, unit. Singapore only. |
| postal_code | 6 digits. |
| phone | Phone for the courier. |
| notes | Late registration (PDF sent first), resend, damaged parcel report, tracking number. |

## Daily routine
1. Copy new registrations (WhatsApp messages with consent for delivery details ticked) into the sheet. Check the postal code has 6 digits.
2. Registrations after the register-by date: send the PDF to print at home today, and still list the parcel with note `late: PDF sent`.
3. Group rows by workbook_file, send one batch order to the printer by the cutoff, and record the tracking numbers in notes.
4. Report any late or damaged parcel to the printer for one free reprint (family must report within 7 days).
5. Delete the sheet (and the printer's copy) within 90 days after the program ends. Do not share it for any other purpose.
