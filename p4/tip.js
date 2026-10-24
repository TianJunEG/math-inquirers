// A small "Start here" tip box for the printed workbook (low-floor entry to a question: an object, a picture, a table starter or a first try).
// Placed inside the question box (wb_pdf.py keeps 'class="p easy"' inside the box). Plain text in, safe HTML out.
const esc = x => String(x).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
module.exports = (text) => {
  const s = String(text); const t = s.charAt(0).toUpperCase() + s.slice(1);
  return `<div class="p easy" style="margin:1px 4px 3px 4px;padding:2px 9px;border-left:5px solid #FFC93C;background:#FFF9E5;font-size:13px;line-height:1.25;break-after:avoid;break-inside:avoid"><b>Start here.</b> ${esc(t)}</div>`;
};
