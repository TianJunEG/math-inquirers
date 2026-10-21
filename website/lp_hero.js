function heroArt(){
  var nl='',i;for(i=0;i<=10;i++){var x=20+i*44;nl+='<line x1="'+x+'" y1="0" x2="'+x+'" y2="12" stroke="#1B2A49" stroke-width="3"/><text x="'+x+'" y="38" font-size="20" text-anchor="middle" fill="#1B2A49">'+i+'</text>'}
  var tf='',r,c,fill=[1,1,1,1,1,2,2,0,0,0];for(r=0;r<2;r++)for(c=0;c<5;c++){var k=r*5+c;tf+='<rect x="'+(c*36)+'" y="'+(r*36)+'" width="36" height="36" fill="#fff" stroke="#1B2A49" stroke-width="3"/>'+(fill[k]?'<circle cx="'+(c*36+18)+'" cy="'+(r*36+18)+'" r="12" fill="'+(fill[k]==1?'#D64545':'#FFC93C')+'" stroke="#1B2A49" stroke-width="2"/>':'')}
  return '<svg class="art" viewBox="0 0 520 430" role="img" aria-label="A frog hopping along a number line, a ten-frame with counters, coins and a pattern puzzle">'+
  '<rect x="8" y="16" width="504" height="400" rx="44" fill="#D6E9FB" stroke="#1B2A49" stroke-width="3"/>'+
  '<g transform="translate(48,62) rotate(-5)"><g class="wob">'+tf+'</g></g>'+
  '<g transform="translate(330,52)"><circle cx="40" cy="40" r="36" fill="#C9CED6" stroke="#1B2A49" stroke-width="3"/><circle cx="40" cy="40" r="28" fill="none" stroke="#1B2A49" stroke-width="1.5" stroke-dasharray="4 4"/><text x="40" y="48" font-size="22" text-anchor="middle" fill="#1B2A49">50¢</text>'+
  '<circle cx="118" cy="62" r="28" fill="#E1E4E9" stroke="#1B2A49" stroke-width="3"/><text x="118" y="69" font-size="18" text-anchor="middle" fill="#1B2A49">20¢</text>'+
  '<circle cx="84" cy="112" r="22" fill="#EEF0F3" stroke="#1B2A49" stroke-width="3"/><text x="84" y="118" font-size="15" text-anchor="middle" fill="#1B2A49">10¢</text></g>'+
  '<g transform="translate(60,182) rotate(-3)"><rect width="230" height="64" rx="16" fill="#FFC93C" stroke="#1B2A49" stroke-width="3"/><text x="115" y="43" font-size="30" text-anchor="middle" fill="#1B2A49" letter-spacing="4">2, 4, 6, ?</text></g>'+
  '<g transform="translate(306,196)"><rect width="196" height="56" rx="18" fill="#fff" stroke="#1B2A49" stroke-width="3"/><path d="M30 56 L22 76 L50 56" fill="#fff" stroke="#1B2A49" stroke-width="3" stroke-linejoin="round"/><rect x="24" y="50" width="30" height="8" fill="#fff"/><text x="98" y="36" font-size="19" text-anchor="middle" fill="#1B2A49">Why does it work?</text></g>'+
  '<g transform="translate(20,330)">'+nl+'<line x1="20" y1="0" x2="460" y2="0" stroke="#1B2A49" stroke-width="3"/>'+
  '<path class="hop" d="M20 -4 Q64 -70 108 -4" fill="none" stroke="#FF7A59" stroke-width="4"/><path class="hop" d="M108 -4 Q152 -70 196 -4" fill="none" stroke="#FF7A59" stroke-width="4"/><path class="hop" d="M196 -4 Q240 -70 284 -4" fill="none" stroke="#FF7A59" stroke-width="4"/>'+
  '<g transform="translate(284,-30)"><g class="frog"><ellipse cx="0" cy="8" rx="30" ry="22" fill="#3DBE7A" stroke="#1B2A49" stroke-width="3"/><circle cx="-13" cy="-12" r="10" fill="#fff" stroke="#1B2A49" stroke-width="3"/><circle cx="13" cy="-12" r="10" fill="#fff" stroke="#1B2A49" stroke-width="3"/><circle cx="-11" cy="-11" r="4" fill="#1B2A49"/><circle cx="15" cy="-11" r="4" fill="#1B2A49"/><path d="M-10 12 Q0 20 10 12" fill="none" stroke="#1B2A49" stroke-width="3" stroke-linecap="round"/></g></g></g>'+
  '</svg>';
}
