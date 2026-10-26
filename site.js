(function(){
  'use strict';
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  var THESES={fiber:{name:'Fiber',color:'#6F7F2E',page:'fiber.html'},nonalc:{name:'Non-alc',color:'#EF5B2B',page:'non-alc.html'},meat:{name:'Meat protein',color:'#7A2E3B',page:'meat-protein.html'},wear:{name:'Wearables',color:'#9B72CF',page:'wearables.html'}};
  window.THESES=THESES;

  /* ---------- navigation ---------- */
  var tog=document.getElementById('navToggle'),mp=document.getElementById('mpanel');
  if(tog&&mp){tog.addEventListener('click',function(){var o=mp.hidden;mp.hidden=!o;tog.setAttribute('aria-expanded',String(o));tog.textContent=o?'Close':'Menu';});
    mp.addEventListener('click',function(e){if(e.target.tagName==='A'){mp.hidden=true;tog.setAttribute('aria-expanded','false');tog.textContent='Menu';}});}
  document.querySelectorAll('.nav .top[data-dd]').forEach(function(b){
    b.addEventListener('click',function(e){var li=b.parentNode;if(matchMedia('(hover:none)').matches&&!li.classList.contains('open')){e.preventDefault();document.querySelectorAll('.nav li.open').forEach(function(x){x.classList.remove('open');});li.classList.add('open');}});
  });
  document.addEventListener('click',function(e){if(!e.target.closest('.nav'))document.querySelectorAll('.nav li.open').forEach(function(x){x.classList.remove('open');});});

  /* ---------- generic row filters (data-g on buttons, data-fg on table) ---------- */
  document.querySelectorAll('.flt[data-g]').forEach(function(b){
    if(b.dataset.g==='db'||b.dataset.g==='th')return;
    b.addEventListener('click',function(){
      var g=b.dataset.g,f=b.dataset.f;
      document.querySelectorAll('.flt[data-g="'+g+'"]').forEach(function(x){x.setAttribute('aria-pressed',String(x===b));});
      document.querySelectorAll('table[data-fg="'+g+'"] tbody tr').forEach(function(tr){tr.hidden=!(f==='all'||(' '+(tr.dataset.tags||'')+' ').indexOf(' '+f+' ')>-1);});
    });
  });

  /* label cells for stacked mobile tables */
  function labelCells(tbl){if(!tbl)return;var hs=[].map.call(tbl.querySelectorAll('thead th'),function(th){return th.textContent.replace(/[↑↓↕]/g,'').trim();});
    [].forEach.call(tbl.querySelectorAll('tbody tr'),function(tr){[].forEach.call(tr.children,function(td,i){if(hs[i])td.setAttribute('data-label',hs[i]);});});}
  document.querySelectorAll('table').forEach(labelCells);

  /* ---------- charts ---------- */
  var C={ink:'#1C1B1F',taupe:'#5B3E86',sand:'#C9B1E8',clay:'#EF5B2B',stone:'#EBDDF8',olive:'#F2A07B',mute:'#BDB6AE',light:'#F4EDFB'};
  window.CC=C;
  function el(t,a,txt){var e=document.createElementNS('http://www.w3.org/2000/svg',t);for(var k in a)e.setAttribute(k,a[k]);if(txt!=null)e.textContent=txt;return e;}
  function hostW(id,d){var h=document.getElementById(id);var w=h&&h.clientWidth;return w&&w>0?Math.round(w):d;}
  function mob(){return window.matchMedia&&window.matchMedia('(max-width:640px)').matches;}
  function svg(id,w,h,label){var host=document.getElementById(id);if(!host)return null;host.innerHTML='';var s=el('svg',{viewBox:'0 0 '+w+' '+h,role:'img','aria-label':label});host.appendChild(s);return s;}
  function tip(n,t){n.appendChild(el('title',{},t));return n;}
  function money(v){if(v>=1000){var b=v/1000;return '$'+(Math.round(b*100)/100)+'B';}return '$'+(v<10?Math.round(v*10)/10:Math.round(v))+'M';}
  function coLink(slug){return 'companies.html#co-'+slug;}
  function decYear(k){var p=String(k).split('-');return +p[0]+(p[1]?(+p[1]-0.5)/12:0.5);}
  var KCOL={r:C.ink,e:C.clay,s:C.sand};

  function timeline(c){
    var D=c.deals,W=hostW(c.id,900);
    if(mob()){var L=118,R=58,rh=30,H=D.length*rh+6,s=svg(c.id,W,H,c.label||'Deal timeline');if(!s)return;var lo=Math.log10(1),hi=Math.log10(Math.max.apply(null,D.map(function(d){return d[2];}))*1.3);
      D.forEach(function(d,i){var y=i*rh+4,w=Math.max(4,(Math.log10(d[2])-lo)/(hi-lo)*(W-L-R));
        s.appendChild(el('text',{x:0,y:y+12,class:'lab'},d[0]));s.appendChild(el('text',{x:0,y:y+24,'font-size':'10'},d[4]||d[1]));
        s.appendChild(el('rect',{x:L,y:y+5,width:w,height:12,rx:3,fill:KCOL[d[3]]}));s.appendChild(el('text',{x:L+w+6,y:y+15,class:'val'},money(d[2])));});return;}
    var H=300,L=56,R=24,T=16,B=36,ys=D.map(function(d){return decYear(d[1]);}),x0=Math.min.apply(null,ys)-0.25,x1=Math.max.apply(null,ys)+0.3;
    var vmax=Math.max.apply(null,D.map(function(d){return d[2];})),lo=Math.log10(0.5),hi=Math.log10(vmax*2.2);
    var s=svg(c.id,W,H,c.label||'Deal timeline');if(!s)return;
    function X(v){return L+(v-x0)/(x1-x0)*(W-L-R);}function Y(v){return T+(1-(Math.log10(v)-lo)/(hi-lo))*(H-T-B);}
    [1,10,100,1000,10000].forEach(function(g){if(Math.log10(g)<lo||Math.log10(g)>hi)return;s.appendChild(el('line',{x1:L,x2:W-R,y1:Y(g),y2:Y(g),class:'grid'}));s.appendChild(el('text',{x:L-8,y:Y(g)+4,'text-anchor':'end'},money(g)));});
    for(var yy=Math.ceil(x0);yy<=Math.floor(x1);yy++){s.appendChild(el('line',{x1:X(yy),x2:X(yy),y1:T,y2:H-B,class:'axis','stroke-dasharray':'3 4'}));s.appendChild(el('text',{x:X(yy)+6,y:H-12},String(yy)));}
    D.forEach(function(d){var cx=X(decYear(d[1])),cy=Y(d[2]),r=5+Math.log10(d[2]+1)*2.2;
      tip(s.appendChild(el('circle',{cx:cx,cy:cy,r:r,fill:KCOL[d[3]],'fill-opacity':.9})),d[0]+': '+money(d[2]));
      var right=cx<W-170;s.appendChild(el('text',{x:right?cx+r+5:cx-r-5,y:cy+4,'text-anchor':right?'start':'end',class:'lab'},d[0]+' '+money(d[2])));});
  }
  function fmtv(v,u){if(u==='$B')return '$'+(Math.round(v*10)/10)+'B';if(u==='$M')return money(v);if(u==='%')return (Math.round(v*10)/10)+'%';return String(v);}
  function pairbars(c){
    var m=mob(),W=hostW(c.id,440),gap=m?60:52,H=c.rows.length*gap+6,L=m?0:Math.min(c.labelW||190,W*.42),R=64;
    var max=c.max||Math.max.apply(null,c.rows.map(function(r){return Math.max(r[1],r[2]);}));var s=svg(c.id,W,H,c.label||'Comparison');if(!s)return;
    var ca=c.colors?c.colors[0]:C.stone,cb=c.colors?c.colors[1]:C.ink;
    c.rows.forEach(function(r,i){var y=4+i*gap,oy=m?16:0,a=(r[1]/max)*(W-L-R),b=(r[2]/max)*(W-L-R);
      s.appendChild(el('text',{x:0,y:m?y+10:y+19,class:m?'lab':''},r[0]));
      s.appendChild(el('rect',{x:L,y:y+4+oy,width:Math.max(a,2),height:12,rx:2,fill:ca}));
      s.appendChild(el('rect',{x:L,y:y+19+oy,width:Math.max(b,2),height:12,rx:2,fill:cb}));
      s.appendChild(el('text',{x:L+Math.max(a,2)+6,y:y+14+oy},(r[3]||'')+fmtv(r[1],c.unit)));
      s.appendChild(el('text',{x:L+Math.max(b,2)+6,y:y+29+oy,class:'val'},(r[4]||'')+fmtv(r[2],c.unit)));});
  }
  function hbars(c){
    var m=mob(),W=hostW(c.id,440),L=m?(c.labelWm||104):(c.labelW||150),R=70,H=c.rows.length*34+6;
    var max=c.max||Math.max.apply(null,c.rows.map(function(r){return Math.abs(r[1]);}))||1;var s=svg(c.id,W,H,c.label||'Bar chart');if(!s)return;
    c.rows.forEach(function(r,i){var y=4+i*34,w=(Math.abs(r[1])/max)*(W-L-R);
      s.appendChild(el('text',{x:0,y:y+15},r[0]));
      tip(s.appendChild(el('rect',{x:L,y:y+3,width:Math.max(w,2),height:16,rx:3,fill:r[3]||(i===0?C.ink:C.sand)})),r[0]+': '+(r[2]||r[1]));
      s.appendChild(el('text',{x:L+Math.max(w,2)+6,y:y+15,class:'val'},r[2]||String(r[1])));});
  }
  function lines(c){
    var m=mob(),W=hostW(c.id,900),H=m?240:290,L=36,R=44,T=12,B=28,y0=c.start,y1=c.end,vals=[];
    c.series.forEach(function(sr){for(var y=y0;y<=y1;y++)vals.push(100*Math.pow(1+sr[1],y-y0));});
    var lo=Math.floor(Math.min.apply(null,vals)/20)*20,hi=Math.ceil(Math.max.apply(null,vals)/20)*20;if(hi-lo<40)hi=lo+40;
    var s=svg(c.id,W,H,c.label||'Indexed growth');if(!s)return;
    function X(v){return L+(v-y0)/(y1-y0)*(W-L-R);}function Y(v){return T+(1-(v-lo)/(hi-lo))*(H-T-B);}
    for(var g=lo;g<=hi;g+=(hi-lo>120?40:20)){s.appendChild(el('line',{x1:L,x2:W-R,y1:Y(g),y2:Y(g),class:g===100?'axis':'grid'}));s.appendChild(el('text',{x:L-6,y:Y(g)+4,'text-anchor':'end'},g));}
    for(var y=y0;y<=y1;y++){if(m&&(y-y0)%2===1&&y!==y1)continue;s.appendChild(el('text',{x:X(y),y:H-8,'text-anchor':'middle'},m?"'"+String(y).slice(2):String(y)));}
    var ends=[];
    c.series.forEach(function(sr){var pts=[];for(var y=y0;y<=y1;y++)pts.push(X(y)+','+Y(100*Math.pow(1+sr[1],y-y0)));
      tip(s.appendChild(el('polyline',{points:pts.join(' '),fill:'none',stroke:sr[2],'stroke-width':2.4,'stroke-linejoin':'round','stroke-dasharray':sr[3]?'5 4':''})),sr[0]);
      var e=100*Math.pow(1+sr[1],y1-y0);s.appendChild(el('circle',{cx:X(y1),cy:Y(e),r:4,fill:sr[2]}));ends.push([Y(e),Math.round(e)]);});
    ends.sort(function(a,b){return a[0]-b[0];});var last=-99;ends.forEach(function(e){var yy=Math.max(e[0]+4,last+12);last=yy;s.appendChild(el('text',{x:X(y1)+8,y:yy,class:'val'},String(e[1])));});
    if(c.legend){var lg=document.getElementById(c.legend);if(lg)lg.innerHTML=c.series.map(function(sr){var r=sr[1]*100;return '<span><i style="background:'+sr[2]+'"></i>'+esc(sr[0])+' &nbsp;<strong>'+(r>0?'+':'')+r.toFixed(1)+'%/yr</strong></span>';}).join('');}
  }
  var GCOL={w:C.ink,a:C.clay,i:C.mute,e:C.stone,d:'#FFFFFF',hot:C.ink,cold:C.mute};
  function quadrant(c){
    var m=mob(),W=hostW(c.id,c.W||900),H=m?Math.round(W*1.08):(c.H||460),L=m?22:40,R=12,T=12,B=m?26:40;var s=svg(c.id,W,H,c.label||'Map');if(!s)return;
    var xa=c.xa||0,xb=c.xb||10,ya=c.ya||0,yb=c.yb||10;
    function X(v){return L+(v-xa)/(xb-xa)*(W-L-R);}function Y(v){return T+(1-(v-ya)/(yb-ya))*(H-T-B);}
    var Q=c.quads||[[0,5,5,10,'Untapped: early, strong signals','#EBDDF8','Untapped'],[5,10,5,10,'Breakout candidates','#E8F6EE','Breakout'],[0,5,0,5,'Early and unproven','#FBF8EF','Unproven'],[5,10,0,5,'Scaled, exited, or incumbent','#FBE7E1','Scaled']];
    Q.forEach(function(q){s.appendChild(el('rect',{x:X(q[0]),y:Y(q[3]),width:X(q[1])-X(q[0]),height:Y(q[2])-Y(q[3]),fill:q[5],rx:Q.length===1?4:0}));
      s.appendChild(el('text',{x:Q.length===1?X(q[1])-8:X(q[0])+10,y:Y(q[3])+18,class:'lab','text-anchor':Q.length===1?'end':'start','font-size':m?'10':'11'},m&&q[6]?q[6]:q[4]));});
    if(Q.length>1){s.appendChild(el('line',{x1:X(5),x2:X(5),y1:T,y2:H-B,stroke:'#FFFFFF','stroke-width':3}));s.appendChild(el('line',{x1:L,x2:W-R,y1:Y(5),y2:Y(5),stroke:'#FFFFFF','stroke-width':3}));}
    s.appendChild(el('line',{x1:L,x2:W-R,y1:H-B,y2:H-B,class:'axis'}));s.appendChild(el('line',{x1:L,x2:L,y1:T,y2:H-B,class:'axis'}));
    s.appendChild(el('text',{x:(L+W-R)/2,y:H-8,'text-anchor':'middle'},(m?c.xs:c.xl)||''));
    s.appendChild(el('text',{x:10,y:(T+H-B)/2,'text-anchor':'middle',transform:'rotate(-90 10 '+((T+H-B)/2)+')'},(m?c.ys:c.yl)||''));
    var keys=[];
    c.points.forEach(function(d,i){
      var grp=d[5]||((d[1]>=5&&d[2]>=5)?'hot':'cold'),fill=GCOL[grp],cx=X(d[1]),cy=Y(d[2]),r=m?9:(d[4]?6+Math.log10(d[4]+1)*3:6);
      var g=c.click?el('a',{href:coLink(d[6]||d[0].toLowerCase().replace(/[^a-z0-9]+/g,'-')),'aria-label':'Open '+d[0]+' in the company database'}):el('g',{});
      var circ=el('circle',{cx:cx,cy:cy,r:r,fill:fill,stroke:(grp==='e'||grp==='d')?C.taupe:'#FFFFFF','stroke-width':1.5,'stroke-dasharray':grp==='d'?'3 2':''});tip(circ,d[0]);g.appendChild(circ);
      var dark=(grp==='w'||grp==='a'||grp==='hot'||grp==='i'||grp==='cold');
      if(m){g.appendChild(el('text',{x:cx,y:cy+3.5,'text-anchor':'middle',style:'font-size:9.5px;font-weight:700;pointer-events:none;fill:'+(dark?'#FFFFFF':'#1C1B1F')},String(i+1)));keys.push({t:d[0],c:fill,dark:dark,href:c.click?coLink(d[6]):null});}
      else{var right=d[3]!=='l';g.appendChild(el('text',{x:right?cx+r+6:cx-r-6,y:cy+4,'text-anchor':right?'start':'end',class:(grp==='w'||grp==='hot')?'lab':''},d[0]));}
      s.appendChild(g);});
    if(m){var host=document.getElementById(c.id),ol=document.createElement('ol');ol.className='chartkey';
      keys.forEach(function(k,i){var li=document.createElement('li');var badge='<span class="kn" style="background:'+k.c+';color:'+(k.dark?'#fff':'#1C1B1F')+';border:1px solid '+C.taupe+'">'+(i+1)+'</span>';li.innerHTML=badge+(k.href?'<a href="'+k.href+'">'+esc(k.t)+'</a>':'<span>'+esc(k.t)+'</span>');ol.appendChild(li);});host.appendChild(ol);}
  }
  function category(c){
    if(!window.COMPANIES)return;var sum={},order=[];
    window.COMPANIES.forEach(function(r){if(r.thesis!==c.thesis||r.raisedM==null||(c.exclude||[]).indexOf(r.name)>-1)return;if(!(r.category in sum)){sum[r.category]=0;order.push(r.category);}sum[r.category]+=r.raisedM;});
    var rows=order.map(function(k){return [k,Math.round(sum[k]*10)/10];}).filter(function(r){return r[1]>0;}).sort(function(a,b){return b[1]-a[1];}).map(function(r,i){return [r[0],r[1],money(r[1]),i===0?C.ink:C.sand];});
    hbars({id:c.id,rows:rows,label:'Disclosed capital by category',labelW:150});
  }
  var DRAW={timeline:timeline,pairbars:pairbars,hbars:hbars,lines:lines,quadrant:quadrant,category:category};
  function drawAll(){(window.CHARTS||[]).forEach(function(c){try{DRAW[c.type](c);}catch(e){if(window.console)console.warn('chart',c.id,e);}});}
  window.drawAllCharts=drawAll;
  var rz,lw=window.innerWidth;window.addEventListener('resize',function(){if(Math.abs(window.innerWidth-lw)<8)return;lw=window.innerWidth;clearTimeout(rz);rz=setTimeout(drawAll,150);});
  drawAll();

  /* ---------- company database page ---------- */
  var dbb=document.querySelector('#dbTbl tbody');
  if(dbb&&window.COMPANIES){
    var rows=window.COMPANIES.slice();
    var lastList=rows;
    var st={th:'all',cat:'all',q:'',status:'all',cap:'all',key:'latest',dir:'desc'};
    var countEl=document.getElementById('count'),catSel=document.getElementById('cat');
    function ini(n){return n.replace(/\(.*?\)/g,'').trim().split(/[\s&,]+/).filter(Boolean).slice(0,2).map(function(w){return w[0];}).join('').toUpperCase();}
    function hue(n){var h=0;for(var k=0;k<n.length;k++)h=(h*31+n.charCodeAt(k))%360;return h;}
    var MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    function fdate(d){if(!d)return '';var p=String(d).split('-');return p[1]?MON[+p[1]-1]+' '+p[0]:p[0];}
    function fraise(r){if(r.raisedM==null)return '<span class="muted">&ndash;</span>';return money(r.raisedM)+(r.raisedPlus?'+':'');}
    function capOk(r){var m=r.raisedM;if(st.cap==='all')return true;if(st.cap==='none')return m==null;if(m==null)return false;if(st.cap==='u10')return m<10;if(st.cap==='10-50')return m>=10&&m<=50;return m>50;}
    function cmp(a,b){var k=st.key,x=a[k],y=b[k],nx=(x==null||x===''),ny=(y==null||y==='');if(nx&&ny)return a.name.localeCompare(b.name);if(nx)return 1;if(ny)return -1;
      var c=(typeof x==='number')?x-y:String(x).localeCompare(String(y));if(k==='latest'&&c===0)c=String(x).length-String(y).length;return st.dir==='asc'?c:-c;}
    function fillCats(){var cats=[];rows.forEach(function(r){if((st.th==='all'||st.th==='watch'||r.thesis===st.th)&&cats.indexOf(r.category)<0)cats.push(r.category);});cats.sort();
      catSel.innerHTML='<option value="all">Any category</option>'+cats.map(function(c){return '<option'+(c===st.cat?' selected':'')+'>'+esc(c)+'</option>';}).join('');if(cats.indexOf(st.cat)<0)st.cat='all';}
    function render(){
      var list=rows.filter(function(r){
        var okT=st.th==='all'||(st.th==='watch'?r.watch:r.thesis===st.th);
        var okC=st.cat==='all'||r.category===st.cat,okS=st.status==='all'||r.status===st.status;
        var hay=[r.name,r.category,r.what,r.investors,r.why,r.latestNote,r.status,THESES[r.thesis].name].join(' ').toLowerCase();
        return okT&&okC&&okS&&capOk(r)&&(!st.q||hay.indexOf(st.q)>-1);}).sort(cmp);
      dbb.innerHTML='';
      lastList=list;
      list.forEach(function(r){var t=THESES[r.thesis];
        var tags=(r.watch?'<span class="pill watch">Watch</span>':'')+(r.status&&r.status!=='Private'?'<span class="pill'+(r.status==='Acquired'?' acq':(r.status==='Declining'?' down':''))+'">'+esc(r.status)+'</span>':'');
        var tr=document.createElement('tr');tr.id='co-'+r.slug;
        tr.innerHTML='<td><div class="co"><span class="logo" aria-hidden="true" style="background:hsl('+hue(r.name)+',38%,46%)">'+esc(ini(r.name))+'</span><div><strong>'+esc(r.name)+'</strong><span class="sub">'+tags+'</span></div></div></td>'+
          '<td><a class="thchip" href="'+t.page+'"><i style="background:'+t.color+'"></i>'+esc(t.name)+'</a><span class="catname">'+esc(r.category)+'</span></td>'+
          '<td>'+esc(r.what||'')+'</td><td class="num">'+fraise(r)+'</td><td>'+esc(r.investors||'')+'</td>'+
          '<td>'+(r.latest?'<strong>'+esc(fdate(r.latest))+'</strong>':'<span class="muted">&ndash;</span>')+'<span class="sub">'+esc(r.latestNote||'')+'</span></td><td>'+esc(r.why||'')+'</td>';
        dbb.appendChild(tr);});
      if(!list.length){var tr=document.createElement('tr');tr.innerHTML='<td colspan="7">No companies match these filters. Clear a filter or try a different search.</td>';dbb.appendChild(tr);}
      countEl.textContent=list.length+' of '+rows.length+' companies';
      document.querySelectorAll('.sorth').forEach(function(b){var on=b.dataset.k===st.key;b.setAttribute('aria-sort',on?(st.dir==='asc'?'ascending':'descending'):'none');b.dataset.dir=on?st.dir:'';});
      document.getElementById('sort').value=st.key+':'+st.dir;labelCells(document.getElementById('dbTbl'));
    }

    /* ---------- export ---------- */
    var COLS=[['Company','name'],['Thesis',function(r){return THESES[r.thesis].name;}],['Category','category'],['What they do','what'],['Raised ($M)',function(r){return r.raisedM==null?'':r.raisedM;}],['Raised is partial',function(r){return r.raisedPlus?'Yes':'';}],['Status','status'],['Watch list',function(r){return r.watch?'Yes':'';}],['Key investors','investors'],['Latest news date','latest'],['Latest news','latestNote'],['Why it matters','why']];
    function cell(r,c){var v=typeof c[1]==='function'?c[1](r):r[c[1]];return v==null?'':String(v);}
    function toCSV(list){var q=function(v){return /[",\n]/.test(v)?'"'+v.replace(/"/g,'""')+'"':v;};
      return '﻿'+[COLS.map(function(c){return q(c[0]);}).join(',')].concat(list.map(function(r){return COLS.map(function(c){return q(cell(r,c));}).join(',');})).join('\r\n');}
    function toTSV(list){return [COLS.map(function(c){return c[0];}).join('\t')].concat(list.map(function(r){return COLS.map(function(c){return cell(r,c).replace(/[\t\n]/g,' ');}).join('\t');})).join('\n');}
    var msg=document.getElementById('xmsg');function say(t){if(msg)msg.textContent=t;}
    function stamp(){var d=new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
    function saveFile(name,data){
      if(window.claude&&window.claude.use){
        window.claude.use('downloads').then(function(dl){
          if(!dl){say('Downloads are not available in this view. Use Copy for Sheets or Excel instead.');return;}
          dl.save({filename:name,data:data}).then(function(){say('Saved '+name+'.');},function(e){var c=e&&e.code;say(c==='declined'?'Download cancelled.':(c==='rate_limited'?'A download prompt is already open.':'Download is not available here. Use Copy for Sheets or Excel instead.'));});
        });
        return;}
      try{var b=new Blob([data],{type:'text/csv;charset=utf-8'}),u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download=name;document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(u);},1500);say('Downloaded '+name+'.');}
      catch(e){say('Download failed. Use Copy for Sheets or Excel instead.');}
    }
    var xv=document.getElementById('xView'),xa=document.getElementById('xAll'),xc=document.getElementById('xCopy');
    if(xv)xv.addEventListener('click',function(){saveFile('venture-thesis-companies-filtered-'+stamp()+'.csv',toCSV(lastList));});
    if(xa)xa.addEventListener('click',function(){saveFile('venture-thesis-companies-all-'+stamp()+'.csv',toCSV(rows));});
    if(xc)xc.addEventListener('click',function(){var t=toTSV(lastList);
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(function(){say('Copied '+lastList.length+' rows. Paste into Google Sheets or Excel.');},function(){say('Copy was blocked here. Select the table and copy it instead.');});}
      else say('Copy is not available here. Select the table and copy it instead.');});
    function setTh(v){st.th=v;document.querySelectorAll('.flt[data-g="th"]').forEach(function(x){x.setAttribute('aria-pressed',String(x.dataset.f===v));});fillCats();}
    document.querySelectorAll('.flt[data-g="th"]').forEach(function(b){b.addEventListener('click',function(){setTh(b.dataset.f);render();});});
    document.getElementById('q').addEventListener('input',function(e){st.q=e.target.value.trim().toLowerCase();render();});
    document.getElementById('sort').addEventListener('change',function(e){var v=e.target.value.split(':');st.key=v[0];st.dir=v[1];render();});
    document.getElementById('status').addEventListener('change',function(e){st.status=e.target.value;render();});
    document.getElementById('cap').addEventListener('change',function(e){st.cap=e.target.value;render();});
    catSel.addEventListener('change',function(e){st.cat=e.target.value;render();});
    document.querySelectorAll('.sorth').forEach(function(b){b.addEventListener('click',function(){var k=b.dataset.k;if(st.key===k)st.dir=st.dir==='asc'?'desc':'asc';else{st.key=k;st.dir=(k==='name'||k==='category')?'asc':'desc';}render();});});
    document.getElementById('reset').addEventListener('click',function(){st.q='';st.status='all';st.cap='all';st.cat='all';document.getElementById('q').value='';document.getElementById('status').value='all';document.getElementById('cap').value='all';setTh('all');render();});
    function fromHash(){var h=(location.hash||'').slice(1);
      if(h.indexOf('co-')===0){var r=rows.filter(function(x){return x.slug===h.slice(3);})[0];if(r){setTh('all');st.q=r.name.toLowerCase();document.getElementById('q').value=r.name;}}
      else if(h.indexOf('t-')===0&&THESES[h.slice(2)]){setTh(h.slice(2));}
      else if(h==='watch')setTh('watch');}
    fillCats();fromHash();render();window.addEventListener('hashchange',function(){fromHash();render();});
    if((location.hash||'').indexOf('#co-')===0){setTimeout(function(){var t=document.getElementById('dbTbl');if(t)t.scrollIntoView({block:'start'});},60);}
  }
})();
