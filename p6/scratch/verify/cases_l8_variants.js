// Cases for the test-only L8 variants made by make_l8_variants.py (run with ROOT=<that folder> CASES=verify/cases_l8_variants.js node verify/editor_check.js run).
const last=r=>r.said[r.said.length-1];
module.exports=[
 ['L8_shift_16.sb3','flag',['MYNO SC PEX'],r=>last(r)==='CODE IS FUN'],
 ['L8_shift_16.sb3','flag',['PIZZA'],r=>last(r)==='FYPPQ'],
 ['L8_shift_minus4.sb3','flag',['CODE'],r=>last(r)==='YKZA'],
 ['L8_shift_minus4.sb3','flag',['A B'],r=>last(r)==='W X'],
 ['L8_shift_26.sb3','flag',['MATH IS FUN'],r=>last(r)==='MATH IS FUN'],
];
