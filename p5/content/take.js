// Markers for the workbook: parts that are moved out of class (re-budget, docs/audit/rebudget_p5.md).
//   TKQ   a whole question that is take-home            (class "tkq": p5/data.js does not count it for "After question N you may choose")
//   TKP   a part (a), (b), ... that is take-home
//   LATER a whole question printed on page 1 that is done in the page 2 time (also class "tkq")
const TKQ = '<b class="tkq" style="color:#8A3F10">&#9733; take-home&nbsp; </b>';
const TKP = '<b style="color:#8A3F10">&#9733; take-home&nbsp; </b>';
const LATER = '<b class="tkq" style="color:#1F7A6F">Do this in the page 2 time&nbsp; </b>';
module.exports = { TKQ, TKP, LATER };
