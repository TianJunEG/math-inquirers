// Tutor-guide / console line for the focus habit of a holiday lesson (docs/pedagogy/inquiry_skills_explicit.md).
// All wording comes from levels/habits.json.   const HG = require('../levels/habit_guide.js');  HG.line(level, n)
const fs = require('fs'), path = require('path');
const DATA = JSON.parse(fs.readFileSync(path.join(__dirname, 'habits.json'), 'utf8'));
function info(level, n) {
  const name = DATA.lessons[`${level}.${n}`], h = DATA.habits[name];
  return { name, h, label: DATA.badge_label, rule: DATA.rule };
}
// One line: "Focus habit: Notice - <teaching move> Say: "<prompt>" <rule>"
function line(level, n) {
  const i = info(level, n);
  return `${i.label}: ${i.name} - ${i.h.move} Say: “${i.h.prompt}” ${i.rule}`;
}
module.exports = { info, line, DATA };
