// render coins and frames SVG from kit.js into PNGs for the docx versions
const k=require('./kit.js')();const fs=require('fs');
fs.writeFileSync('kitpng.html','<html><body style="margin:0;background:#fff">'+k.join('\n')+'</body></html>');
