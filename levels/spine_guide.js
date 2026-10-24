// Tutor-guide lines for the strategy card and common look-back (docs/pedagogy/spine_routine_spec.md sections 2, 3).
// All wording comes from levels/spine.json.   const SG = require('../levels/spine_guide.js');
const fs = require('fs'), path = require('path');
const DATA = JSON.parse(fs.readFileSync(path.join(__dirname, 'spine.json'), 'utf8'));
const tool = id => DATA.tools.find(t => t.id === id);
const fill = (s, t, band) => s.replace('{name}', t ? t.name : '').replace('{def}', t ? t.def[band] : '');
function info(level, n) {
  const row = DATA.lessons[`${level}.${n}`], band = DATA.bands[String(level)], S = DATA.script;
  const choose = row.main === 'choose', t = choose ? null : tool(row.main);
  return {
    row, band, choose, tool: t,
    openSay: choose ? S.choose_say : fill(S.opening_say, t, band),
    openDo: choose ? S.choose_do : S.opening_do,
    talkAsk: choose ? S.choose_ask : fill(S.talk_ask, t, band),
    talkListen: choose ? 'Listen for a tool being named and a reason for choosing it.' : S.talk_listen,
    lookSay: S.lookback_say, lookDo: S.lookback_do, checkTogether: S.check_together,
    timer: (DATA.lookback.timer_by_level || {})[String(level)] || DATA.lookback.timer_seconds[band],
    kitLine: n === 1 ? DATA.kit_line : ''
  };
}
module.exports = { info, DATA, tool };
